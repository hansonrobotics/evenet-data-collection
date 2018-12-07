import os
import webbrowser

import threading
import sys
print(os.getcwd())


def start_local_server():
	version = sys.version
	os.chdir(os.path.abspath("Teleprompter"))
	if (version.startswith("3")):
		os.system("python3 -m http.server")
	elif (version.startswith("2")):
		os.system("python -m SimpleHTTPServer")
	print("Python local server has started...\n")
def start_python_server():
	print("Python data collector server has started...\n")
	os.system("python collector.py")
	print(os.getcwd())


def open_chrome():
	url = 'localhost:8000'
	chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
	# Linux
	# chrome_path = '/usr/bin/google-chrome %s'
	webbrowser.get(chrome_path).open("localhost:8000")

threading.Thread(target=start_local_server).start()
threading.Thread(target=start_python_server).start()
# open_chrome()

