#!/usr/bin/python
import time
import sys
#import Pyro.core
#import controller
#import rockets
import serial

cmd = "Pz"

PORT = serial.Serial("/dev/arduino1",baudrate=57600,bytesize=serial.EIGHTBITS)
while True:
	PORT.write(cmd)
#	print("wheelchair power ON")
        sys.stdout.write(PORT.readline())
	time.sleep(1)
