# BRICKPI LEGO EV3 GYRO SENSOR EXAMPLE.
############################################
#
# NOTE: This program is in BETA now
#
# This example will show you how to use the LEGO EV3 Gyro sensor with the BrickPi.  
# Note you must have the latest firmware installed on the BrickPi or this example to work.  
# Gyro sensor is attached to Port 4.
##
# Select the mode of operation below.  These are the modes of operation for the gyro.
# TYPE_SENSOR_EV3_GYRO_M0 - Returns absolute angle turned from startup.
# TYPE_SENSOR_EV3_GYRO_M1 -  Rotational Speed
# TYPE_SENSOR_EV3_GYRO_M2 -  Raw sensor value ???
# TYPE_SENSOR_EV3_GYRO_M3 -  Angle and Rotational Speed?
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
BrickPi.SensorType[PORT_4] = TYPE_SENSOR_EV3_GYRO_M0   	#Set the type of sensor at PORT_4.  M0 is angle. 
BrickPiSetupSensors()   								#Send the properties of sensors to BrickPi.  Set up the BrickPi.
# There's often a long wait for setup with the EV3 sensors.
# EV3 gyro works best (less drift and less error results) if you hold it still in setup.

while True:
	result = BrickPiUpdateValues()  # Ask BrickPi to update values for sensors/motors 
	if not result :
		gyro = BrickPi.Sensor[PORT_4]
		print str(gyro)
		
	time.sleep(.01)     # sleep for 10 ms

