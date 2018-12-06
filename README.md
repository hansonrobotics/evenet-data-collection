# Scripts for data collection with faceware live-server

This repository contains scripts for evenet dataset collection. 
## Getting Started
The repo contains the following scripts.
1. Teleprompter server - This script provides server for web based teleprompter 
2. Faceware live server client - A client which subscribes for live server blendkeys
3. Interface server - A server which listens from teleprompter and communicates with the client
to save transcriptions from teleprompter and blendkeys from client. 

### Prerequisites

* python 2

### Configuration 
Before running the data-collector scripts one should configure for required options of config.json file inside Teleprompter folder
**Config options** 
*   LiveIP                  : IP address of Faceware live server
*   LivePORT                : Port number of Faceware live server,
*   collector_server_ip     : IP address of collector server,
*   collector_server_port	: IP address of collector client
The following diagram depicts the interaction between the scripts, live server and web app.
<img src="https://github.com/hansonrobotics/evenet-data-collection/blob/master/images/image8.PNG" width = 50%/> 
#### Configuring Faceware live server streaming.
Faceware Live automatically tracks video of a performer’s face to stream realtime animation shape keys using tcp protocol. To record this streaming live server allows to set port number to subscribe. Enabling streaming is done by clicking streaming icon found on top center if live server window.  
<img src="https://github.com/hansonrobotics/evenet-data-collection/blob/master/images/image1.PNG" width = 50%/>  
When the streaming is enabled the icon changes to the following icon  
<img src="https://github.com/hansonrobotics/evenet-data-collection/blob/master/images/image4.PNG" width = 50%/>   
and "Streaming!" message appears on bottom left corner of the window.  
<img src="https://github.com/hansonrobotics/evenet-data-collection/blob/master/images/image2.PNG" width = 50%/>
Values of the animation shape keys can be view using "Animation Tuning" menu of menubar.
<img src="https://github.com/hansonrobotics/evenet-data-collection/blob/master/images/image5.PNG" width = 50%/>
<img src="https://github.com/hansonrobotics/evenet-data-collection/blob/master/images/image3.png" width = 50%/>
Faceware analyzer provides functionalities to track landmark position inside videos from file and from webcams. There are two options to track faces inside videos. The first is auto track and uses faceware default models to track face. The second options is to train tracking models for each subject. The following images show two frames selected to train models for [video from youtube](https://www.youtube.com/watch?v=S4roaqfyU2A)
<img src="https://github.com/hansonrobotics/evenet-data-collection/blob/master/images/image6.PNG" width = 50%/>
<img src="https://github.com/hansonrobotics/evenet-data-collection/blob/master/images/image7.PNG" width = 50%/>
### Running the data collector script
All scripts can be run using the following script command

```python2 data_collector.py```

The collected dataset will be saved inside `Teleprompter/data` folder.