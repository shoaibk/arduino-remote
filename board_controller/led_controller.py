import serial
import requests
import time
import glob, os

os.chdir("/dev");
arduino_port = ""
arduino_port_prefix = "cu.usbmodem*"
url = 'http://arduino-shoaibkhan.c9.io/sensors/1.json'
waiting_delay = 2


for file in glob.glob(arduino_port_prefix):
    arduino_port = file

print "Detected Arduino Port: " + arduino_port

arduino = serial.Serial(arduino_port, 9600)
time.sleep(waiting_delay)

led_is_on = False

print "Starting to check the remote server"
print "---------------------------------------------"

while True:
    led_control = requests.get(url)
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
