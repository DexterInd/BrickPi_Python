# BRICKPI LEGO EV3 Ultrasonic SENSOR EXAMPLE.
############################################
#
# NOTE: This program is in BETA now
# 
# This example will show you how to use the LEGO EV3 Ultrasonic sensor with the BrickPi.  
# Note you must have the latest firmware installed on the BrickPi or this example to work.  
# Sensor is attached to Port 4.
##
# Select the mode of operation below.  These are the modes of operation for the gyro.
# TYPE_SENSOR_EV3_US_M0 - Continuous measurement, distance, cm
# TYPE_SENSOR_EV3_US_M1 - Continuous measurement, distance, in
# TYPE_SENSOR_EV3_US_M2 - Listen // 0 r 1 depending on presence of another US sensor.
##
#
# Original Author: John
# Initial Date: June 13, 2014
# http://www.dexterindustries.com/BrickPi
#
# These files have been made available online through a Creative Commons Attribution-ShareAlike 3.0  license.
# (http://creativecommons.org/licenses/by-sa/3.0/)

from BrickPi import *   								#import BrickPi.py file to use BrickPi operations
BrickPiSetup()  										# setup the serial port for communication
############################################
# !  Set the sensor type on the line below.  
BrickPi.SensorType[PORT_4] = TYPE_SENSOR_EV3_US_M0   	#Set the type of sensor at PORT_4.  M0 is continuous measurement in cm. 
BrickPiSetupSensors()   								#Send the properties of sensors to BrickPi.  Set up the BrickPi.
# There's often a long wait for setup with the EV3 sensors.  Up to 5 seconds.

while True:
	result = BrickPiUpdateValues()  # Ask BrickPi to update values for sensors/motors 
	if not result :
		gyro = BrickPi.Sensor[PORT_4]
		print str(gyro)
		
	time.sleep(.01)     # sleep for 10 ms

