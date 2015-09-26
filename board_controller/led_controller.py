# Relays the state of the LED control to the Arduino Board
#
# Setup:
# Run the board program (in board/arduino_led/arduino_led_d3)
# Make sure the remote server is running
#
# Description:
# Communicates with the rails server using REST API.
# Sends an http GET to the rest endpoint. Checks the json response.
# If is_active is True, sends '1' to the board. LED should be switched ON after blinking.
# If is_active is False, sends '0' to the board. LED should be switched OFF after blinking.
#
# TODO: Graceful degradation when the remote server is offline
# TODO: 

import serial
import requests
import time
import glob, os

# Arduino is typically connected to serial port something like /dev/cu.usbmodemxxxx
os.chdir("/dev");
arduino_port = ""
arduino_port_prefix = "cu.usbmodem*"

# Address of the led control on the Rails server
rest_endpoint = 'http://arduino-shoaibkhan.c9.io/sensors/1.json'
waiting_delay = 2

# Detect the Arduino port. We are assuming the host computer to be a Mac OSX
# For Windows, please update the prefix accordingly
for file in glob.glob(arduino_port_prefix):
    arduino_port = file

print "Detected Arduino Port: " + arduino_port

arduino = serial.Serial(arduino_port, 9600)

# We mush wait a bit, since Arduino resets on the first serial com setup
time.sleep(waiting_delay)

led_is_on = False

print "Starting to check the remote server: " + rest_endpoint
print "---------------------------------------------"

while True:
    # Call the remote server 
    # Check if the active field of the json response is set
    # If set, turn on the LED by sending '1' to the board
    # If unset, turn off the LED by sending '0' to the board
    led_control = requests.get(rest_endpoint)
    response = led_control.json()

    if led_is_on != response['is_active']:   
        led_is_on = response['is_active']
        if led_is_on:
            arduino.write('1')
            print "Turning ON"
        else:
            arduino.write('0')
            print "Turning OFF"

    time.sleep(waiting_delay)
