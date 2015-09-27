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



#### Server
The server is a Ruby on Rails server hosted on [Cloud9](http://c9.io). The server part of this project is [here](https://github.com/shoaibk/arduino-server).

