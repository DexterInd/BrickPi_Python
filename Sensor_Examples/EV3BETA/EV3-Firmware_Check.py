# FIRMWARE CHECK.
############################################
# This program will check for the correct firmware version.
# The Touch sensor is attached to Port 4.
# When the touch sensor is pressed, the output should read "1"
#
# Original Author: Jaikrishna
# Initial Date: June 24, 2013
# Last Updated: June 24, 2013
# http://www.dexterindustries.com/BrickPi
#
# These files have been made available online through a Creative Commons Attribution-ShareAlike 3.0  license.
# (http://creativecommons.org/licenses/by-sa/3.0/)

from BrickPi import *   #import BrickPi.py file to use BrickPi operations

print "Trying to communicate with firmware."
result = BrickPiSetup()  # setup the serial port for communication
if result == 0:
	print "PASS: Successfully connected to BrickPi."
	print "PASS: Hardware seems to be running normally."
elif result == -1:
	print "FAIL:  Failed to communicate with BrickPi."
	print "FAIL:  Please check hardware setup and power."
else:
	print "FAIL:  Result is: " + str(result)
	print "FAIL:  We don't have a set answer for what's going on!  Tell us on the forum!"


BrickPi.SensorType[PORT_4] = RETURN_VERSION	  # Software hack: sets a sensor as the Firmware Version
print " "
BrickPiSetupSensors()   #Send the properties of sensors to BrickPi

print "Checking Firmware Version of BrickPi."
result = BrickPiUpdateValues()  # Ask BrickPi to update values for sensors/motors 
version = BrickPi.Sensor[PORT_4]
print "Firmware version is: " + str(version)
if(version == 2):
	print "GREAT!  Firmware is up to date!"
	print "You should be able to run EV3 sensors!"
else:
	print "DOH!  Please update your firmware to run EV3 sensors!"
	print "You should be able to run NXT sensors, but not EV3 sensors."
	
