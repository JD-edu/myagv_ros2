'''
Please run this script as sudo just like:
$sudo python3 lidar_off.py

'''
 
import time 
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
time.sleep(1)
GPIO.setup(20,GPIO.OUT)
GPIO.output(20, GPIO.LOW)