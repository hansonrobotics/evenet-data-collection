# Data collection app with faceware

This repository contains scripts for evenet dataset colletion. 
## Getting Started
There rep contains the following scripts.
1. Teleprompter server - This script provides server for web based teleprompter 
2. Faceware live server client - A client which subscribes for live server blendkeys
3. Interface server - A server which listens from teleprompter and commincates with the client
to save transcriptions from teleprompter and blendkeys from client. 

### Prerequisites

* python 2
* config.json - A configuration file for

### Configuration 
Before running the data-collector scripts one should configure for required options of config.json file inside Teleprompter folder
**Config options** *
*   LiveIP                  : IP address of faceware live server
*   LivePORT                : Port number of faceware live server,
*   collector_server_ip     : IP address of collector server,
*   collector_server_port	: IP address of collector client

### Running the datacollector script
All scripts can be run using the following script command

```python data_collector.py```

