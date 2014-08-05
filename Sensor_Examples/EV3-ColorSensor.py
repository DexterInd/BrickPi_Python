# BRICKPI LEGO EV3 Color SENSOR EXAMPLE.
############################################
#
# NOTE: This program is in BETA now
#
# This example will show you how to use the LEGO EV3 Gyro sensor with the BrickPi.  
# Note you must have the latest firmware installed on the BrickPi or this example to work.  
# Gyro sensor is attached to Port 4.
##
# TYPE_SENSOR_EV3_COLOR_M0     = 50	# Reflected Light.  Shine against a surface to see the effect.
# TYPE_SENSOR_EV3_COLOR_M1     = 51	# Ambient.  Detects ambient light, hold up to a bright light to see the effect, dark area to see the effect.
# TYPE_SENSOR_EV3_COLOR_M2     = 52	# Color  // Min is 0, max is 7 (brown).  Returns a value for each color it sees.
									# 1 - Black
									# 2 - Blue?
									# 3	- 	
									# 4	-
									# 5	-
									# 6	- Green?
									# 7	- Brown?									
# TYPE_SENSOR_EV3_COLOR_M3     = 53	# Raw reflected
# TYPE_SENSOR_EV3_COLOR_M4     = 54	# Raw Color Components
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

########################################################################################################################
# ! CHANGE THE VARIABLE BELOW TO TEST DIFFERENT MODES
BrickPi.SensorType[PORT_4] = TYPE_SENSOR_EV3_COLOR_M2   #Set the type of sensor at PORT_4.  M0 is reflected light.
BrickPiSetupSensors()   								#Send the properties of sensors to BrickPi.  Set up the BrickPi.
# There's often a long wait for setup with the EV3 sensors.
# EV3 gyro works best (less drift and less error results) if you hold it still in setup.

while True:
	result = BrickPiUpdateValues()  # Ask BrickPi to update values for sensors/motors 
	if not result :
		gyro = BrickPi.Sensor[PORT_4]
		print str(gyro)
		
	time.sleep(.01)     # sleep for 10 ms

