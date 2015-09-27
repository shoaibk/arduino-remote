### Arduino Remote

Monitor and control a sensor connected to Arduino using a REST client. 

![Diagram](arduino-project-overview.png)

#### Arduino
The Arduino programs (sketch) are in folder ```board/arduino_led/```. They should be uploaded to the Arduino board using the [Arduino GUI](https://www.arduino.cc/en/Main/Software). 

The LED program responds to serial input of '1' and '0' by turning the LED on and off, respectively. Once the program is uploaded to the board, test it by connecting from the host computer.

1. Open the terminal
2. Type in ```cat > /dev/[arduino-port]``` where the exact name of the arduino port might differ from system to system and also from session to session. This will connect the Standard Input of your computer (which is usually the keyboard) to the serial port of the Arduino.
3. On the prompt, type ```1 (enter)```. This should turn the LED on the Arduino ON.
4. Next, type ```0 (enter)```. This should turn the LED on the Arduino OFF.

#### Computer
This can be a Mac, PC, or a Raspberry Pi. The folder ```board_controller``` contains the python program that connects to the remote Rails server and sends control signal to the Arduino through serial interface.

To connect to the server using the REST API, we use ```requests``` [library](http://www.python-requests.org/en/latest/). It has a great [tutorial](http://docs.python-requests.org/en/latest/user/quickstart/) to get you started in less than a minute!
To connect to the Arduino using the serial interface, we use ```pySerial``` [library] (https://github.com/pyserial/pyserial). 

##### Setup

1. Run the board program (in board/arduino_led/arduino_led_d3)
2. Make sure the remote server is running
3. Install packages 'pySerial', and 'requests' if necessary, using either pip or easy_install

##### Description

1. Communicates with the rails server using REST API.
2. Sends an http GET to the rest endpoint. Checks the json response.
3. If is_active is True, sends '1' to the board. LED should be switched ON after blinking.
4. If is_active is False, sends '0' to the board. LED should be switched OFF after blinking.


#### Server
The server is a Ruby on Rails server hosted on [Cloud9](http://c9.io). The source code of this project is [here](https://github.com/shoaibk/arduino-server).

The server has two responsibilities:

1. Host the sensor data and states
2. Serve the sensor data through a REST API

An alternative is using [Parse](http://parse.com), which comes with the added benefit of push notifications. 

#### App
This app is a GUI for the REST client to communicate with the Server.  It can be implemented as an Android, an iOS or a web app.

The rails server provides a GUI to access the sensor data and manipulate them. For starter, we can use this as the App. The url for the LED sensor is [here](http://arduino-shoaibkhan.c9.io/sensors/1).