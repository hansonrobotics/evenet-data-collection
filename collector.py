from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import os
from io import BytesIO
from datetime import datetime
import json
import socket
import argparse
import sys
import threading


class BooleanObject(object):
    def __init__(self, value=False):
        self.value = value


class CollectorServer(BaseHTTPRequestHandler):
    """Evenet Dataset collector server class. The server listens http post request
    from angular js. 
    """
    data_dict  = None
    record = None
    save_dir = "data"
    

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Get is not implemented yet!')
    def get_filename(self):
        now = datetime.now()
        filename = now.strftime("%Y-%m-%d-%H-%M-%S")+".json"
        return os.path.join(CollectorServer.save_dir, filename)
    def _save(self):
        # print("dict", CollectorServer.data_dict)
        if CollectorServer.data_dict["frame_length"] == 0:
            print("No values to save")
            return False
        elif CollectorServer.data_dict["transcription"]["ts"] is None or CollectorServer.data_dict["transcription"]["ts"] =="":
            print("No transcription is given to save")
            return False
        filename = self.get_filename()
        if not os.path.exists(CollectorServer.save_dir):
            os.mkdir(CollectorServer.save_dir)
        with open(filename, "w+") as json_file:
            transcription = CollectorServer.data_dict["transcription"]
            shape_keys = CollectorServer.data_dict["shape_keys"]
            new_dict = {"transcription":transcription,"shape_keys":shape_keys}
            json.dump(new_dict,json_file)
            CollectorServer.data_dict["transcription"] = {"ts":None,"emotion":None}
            CollectorServer.data_dict["shape_keys"] = []
            CollectorServer.data_dict["frame_length"] = 0
            return True
        
    
    def do_POST(self):
        """Handles post requests. This method assumes two post variables(case and data).
            case - could be one of 'command' and 'ts' for transcription
            if case is 'command' then data should of one of 'start', 'discard' or 'save'
        Raises:
            Exception -- [description]
        """

        data_length = int(self.headers["Content-Length"])
        data = self.rfile.read(data_length)
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        response = BytesIO()
        response.write("Received:%s" %data)
        self.wfile.write(response.getvalue())
        data = json.loads(data)
        data= data["data"]
        print("data", data)
        if self.data_dict is None:
            raise Exception("Please set data_dict before serving!")
        if data["case"].lower() =="command":
            if data["data"].lower() == "start":
                if not CollectorServer.record.value:
                    self.data_dict["transcription"] = {"ts":None,"emotion":None}
                    self.data_dict["shape_keys"] = []
                    self.data_dict["frame_length"] = 0
                    CollectorServer.record.value = True
                    self.send_response(200)
                    self.send_header("Access-Control-Allow-Origin", "*")
                    response = BytesIO()
                    response.write("Started!")
                    self.wfile.write(response.getvalue())
                else:
                    print("start command sent while recording is on")
                    self.send_response(200)
                    self.send_header("Access-Control-Allow-Origin", "*")
                    response = BytesIO()
                    response.write("Start after started!")
                    self.wfile.write(response.getvalue())
            else:
                self.send_response(200)
                self.send_header("Access-Control-Allow-Origin", "*")
                response = BytesIO()
                response.write("Unrecognized command:%s" %data["data"])
                self.wfile.write(response.getvalue())
        elif data["case"].lower()=="ts":
            current_ts = {"ts":data["data"]["ts"], "emotion":data["data"]["emotion"]}
            print("Current transcription: %s . Emotion: %s" %(current_ts["ts"], current_ts["emotion"]))
            self.data_dict["transcription"] = current_ts
            self._save()
            self.send_response(200)
            self.send_header("Access-Control-Allow-Origin", "*")
            response = BytesIO()
            response.write("Saved!")
            self.wfile.write(response.getvalue())
        else:
            self.send_response(200)
            self.send_header("Access-Control-Allow-Origin", "*")
            response = BytesIO()
            response.write("Unrecognized case:%s" %data["case"])
            self.wfile.write(response.getvalue())


class CollectorClient(object):
    def __init__(self, data_dict, record, IP="localhost", port=9999):
        self._data_dict = data_dict
        self._record = record
        self.IP = IP
        self.port = port
    @property
    def data_dict(self):
        """A dictionary which contains current transcription and list for each time shape key values.
        It contains three keys:- transcription, shape_keys, frame_length
        Returns:
            [type] -- [description]
        """
        return self._data_dict
    @property
    def record(self):
        """BooleanObject Variable to store record flag.
        
        Returns:
            bool -- true if the recording flag is on.
        """
        return self._record
    def do_request(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.IP, self.port))
        while True:
            try:
                
                original = sock.recv(4096)
                data_length = ord(original[0])+1280
                status = original[1:4]
                data = original[4:4+data_length]
                animation_values = eval(data)["animationValues"]
                self.data_dict["shape_keys"].append(animation_values)
                self.data_dict["frame_length"] +=1
            except KeyboardInterrupt:
                break
        sock.close()
def main(args):
    with open(args.config) as config_file:
        config = json.load(config_file)
    collector_server = HTTPServer((config["collector_server_ip"], config["collector_server_port"]), CollectorServer)
    data_dict = {"transcription":  {"ts":None,"emotion":None}, "shape_keys":[],"frame_length":0}
    record = BooleanObject(False)
    CollectorServer.data_dict = data_dict
    CollectorServer.record = record

    
    collector_client = CollectorClient(data_dict,record, config["LiveIP"],config["LivePORT"])

    server_thread = threading.Thread(target=collector_server.serve_forever)
    client_thread = threading.Thread(target=collector_client.do_request)

    server_thread.daemon = True
    client_thread.daemon = True

    server_thread.start()
    client_thread.start()

    server_thread.join()
    client_thread.join()



if __name__=='__main__':
   parser = argparse.ArgumentParser()
   parser.add_argument('-c', '--config',default='config.json')
   args = parser.parse_args()
   main(args)