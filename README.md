# iot-based-smart-bin
This is basically a smart dustbin which notifies its user when its half and full by sending an email on registered user email id and also gives hands free experience by automatic opeming system.
## contributors
* Harsh Verma 
* Sagar Garg
## Idea for the project
As we all have seen large mettalic dustbins of municipal corporation in different parts of a city, people after collecting their waste from their houses collectively dumped that waste in these dustbin ** BUT ** after some time when these dustbins reached to their full capacity and there is no space left for more trash people started to their their waste region around the dustbins and due to this a huge pile of waste having foul smell is created around that area. So for this we have created this smart dustbin system , after installing this system in those dustbins it can notify the municipal corporation about the particular dustbin which is fulled on timely basis and then they can easily free the dustbin by taking out the waste.
## modifications for future
* we are thinking to upload all the data to the cloud platforms like thingspeak so that we can monitor the waste productions in different parts of cities and can monitor easily the waste production rate and can increase the frequency of dumping trucks in those regions so that they can clean those areas more frequently
## Challenges
Opting for sensors that can also work in wet waste. Presently we are using infrared sensors to detect whether the dustbin is full or not but they can work good for dry waste only so opting sensors working for both wet and dry waste will be a task.
## sensors and board used for the projects
* Raspberry pi 3B+
* ultrasonic sensor
* infrared sensors
* servo motor
* bin body


## Code

### block of code for sending mail
'''
