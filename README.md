# Scripts for data collection with faceware live-server
For compiled binary files and scripts please visit the [release page](https://github.com/hansonrobotics/evenet-data-collection/releases)

## Getting Started
The rep contains the following scripts.
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
<img src="https://github.com/hansonrobotics/evenet-data-collection/blob/master/images/image8.png" width = 50%/> 
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
Faceware analyzer provides functionalities to track landmark position inside videos from file and from webcams. There are two options to track faces inside videos. The first is auto track and uses faceware default models to track face. The second options is to train tracking models for each subject. The following images show two frames selected to train models for this video from youtube(https://www.youtube.com/watch?v=S4roaqfyU2A). 
<img src="https://github.com/hansonrobotics/evenet-data-collection/blob/master/images/image6.PNG" width = 50%/>
<img src="https://github.com/hansonrobotics/evenet-data-collection/blob/master/images/image7.PNG" width = 50%/>

### Adding your own custom emotion script to the Teleprompter
Prepare the data with the following csv format 

<img src="https://github.com/hansonrobotics/evenet-data-collection/blob/master/images/sample.png" width = 50%/>
Go to Teleprompter/assets and replace text_emotion.csv with your script data

### Running the data collector script
All scripts can be run using the following script command

```python2 data_collector.py```

### Runing the Teleprompter
In order to read the  text_emotion.csv file and display it to the Teleprompter, first we should create a local http server  

The above command  ```python data_collector.py``` also creates a local http server

To open the teleprompter, open your browser to  ```localhost:8000```

### How to use the Teleprompter
After you open the teleprompter with your browser 

Press SPACE bar from your keybord to enter server address and port 
<img src="https://github.com/hansonrobotics/evenet-data-collection/blob/master/images/server_addr.png" width = 50%/>
And press ENTER to save the address and port

Press S to start recording

Press D to discard the current recording

Press RIGHT ARROW to save the current recording and go to the next script

Press UP/DOWN ARROW to change the scripts font size on the teleprompter

The collected dataset will be saved inside `Teleprompter/data` folder.


### Dataset(Script) used for Teleprompter
The script text_emotion.csv is orinally taken from text emotion classification project https://github.com/tlkh/text-emotion-classification/tree/master/dataset

This dataset is twitter users tweet, expressing their feeling on different circumstance.
It is scraped from twitter using twitter developer [API](https://developer.twitter.com/en.html)

## Preprocessing of text_emotion.csv for teleprompter
- Some characters and numbers are replace by thier corresponding text word

   '@' is replace by "At"

   '=' is replaceb y "equals"

   '+' is replace by "plus"

   '$' is replaced by "dollar"

   '*' is replaced by "star"

   '&' is replaced by "and"

   '#' is replaced by "Hashtag"

And  numbers replaced by thier coresponding word

eg. 0 ---> zero, 1 --> one,.....etc 

Sample preprocessing

"@jhon_1234" is replaced by  "At jhon underscore one two three four"

## License of dataset(twitter tweets)
- [Twitter agreement and Policy](https://developer.twitter.com/en/developer-terms/agreement-and-policy.html)

### Screenshot's of Teleprompter demo

## Surprise emotion
<img src="https://github.com/hansonrobotics/evenet-data-collection/blob/master/images/surprise.png" width = 50%/>

## Happy emotion
<img src="https://github.com/hansonrobotics/evenet-data-collection/blob/master/images/happy.png" width = 50%/>

## Angry emotion
<img src="https://github.com/hansonrobotics/evenet-data-collection/blob/master/images/angry.png" width = 50%/>

## Sad emotion
<img src="https://github.com/hansonrobotics/evenet-data-collection/blob/master/images/sad.png" width = 50%/>



# Teleprompter

## Preprocessing

- To replace the caracter

go to ```app.component.ts``` file

find ```replace_char(char)``` function and add the caracter you want to add   
```
    
    replace_char(c){
            var value = "";
		    if (c == "0"){
		       value = " zero ";
		    }
		    else if(c == "1"){
		      value = " one ";
		    }
		    else if(c == "2"){
		      value = " two ";
		    }

         return value

       }
       
       
```  
- To do your own preprocessing 

Go to ``` do_other_preprocessing(text)```  function, this function accepts the script text and you can do your own preprocessing inside this function
 

 ``` 

 do_other_preprocessing(text){
     
      Do your preprocessing here.
      
      return text
  }

  ```

# Running Teleprompter 

Install Angular 6

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 6.0.8.

## Development server

- First open faceware 

- Then   

```
	cd Teleprompter 

	npm install 

	npm start
```
 
 The ``` npm start ``` command concurrently runs the angular code and ``` collector.py ``` python script. The python script is a server that save the data and  communicates with angular while collecting the dataset.


Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The app will automatically reload if you change any of the source files.

## Code scaffolding

Run `ng generate component component-name` to generate a new component. You can also use `ng generate directive|pipe|service|class|guard|interface|enum|module`.

## Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory. Use the `--prod` flag for a production build.



## Further help

To get more help on the Angular CLI use `ng help` or go check out the [Angular CLI README](https://github.com/angular/angular-cli/blob/master/README.md).
