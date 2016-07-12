#!/usr/bin/env python
# Dexter Industries
# Initial Date: June 24, 2013	Jaikrishna
# Last Updated: July 12, 2016	John
#
# These files have been made available online through a Creative Commons Attribution-ShareAlike 3.0  license.
# (http://creativecommons.org/licenses/by-sa/3.0/)
#
# http://www.dexterindustries.com/
# This code is for testing the BrickPi with a Lego Ultrasonic Sensor.  Simply 
# define the port number "port_number" and place the Lego Ultrasonic Sensor 
# in the designated port.

from BrickPi import *   #import BrickPi.py file to use BrickPi operations

BrickPiSetup()  # setup the serial port for communication

port_number = PORT_1	# Define the port number here.  

BrickPi.SensorType[port_number] = TYPE_SENSOR_ULTRASONIC_CONT   #Set the type of sensor at PORT_1

BrickPiSetupSensors()   #Send the properties of sensors to BrickPi

while True:
    result = BrickPiUpdateValues()  # Ask BrickPi to update values for sensors/motors 
    if not result :
        print BrickPi.Sensor[port_number]     #BrickPi.Sensor[PORT] stores the value obtained from sensor
    time.sleep(.01)     # sleep for 10 ms

