import os
import webbrowser
os.chdir(os.path.abspath("Teleprompter"))
import threading

print(os.getcwd())


def start_local_server():
	print("Python local server has started...\n")
	os.system("python -m SimpleHTTPServer")
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
open_chrome()

