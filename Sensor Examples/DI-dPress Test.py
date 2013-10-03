# Jaikrishna
# Initial Date: June 24, 2013
# Last Updated: June 24, 2013
#
# These files have been made available online through a Creative Commons Attribution-ShareAlike 3.0  license.
# (http://creativecommons.org/licenses/by-sa/3.0/)
#
# http://www.dexterindustries.com/
# This code is for testing the BrickPi with a Pressure sensor from Dexter Industries
# Product webpage: http://www.dexterindustries.com/Products-dPressure.html

from BrickPi import *   #import BrickPi.py file to use BrickPi operations

DPRESS_VREF = 4.85

BrickPiSetup()  # setup the serial port for communication

BrickPi.SensorType[PORT_3] = TYPE_SENSOR_RAW

if not BrickPiSetupSensors() :
	while True :
		if not BrickPiUpdateValues() :
			# Pressure is calculated using Vout = VS x (0.00369 x P + 0.04)
			# Where Vs is assumed to be equal to around 4.85 on the NXT
			
			# Get raw sensor value
			val = BrickPi.Sensor[PORT_3]
			
			# Calculate Vout
			Vout = ((val * DPRESS_VREF) / 1023)
			
			pressure = ((Vout / DPRESS_VREF) - 0.04) / 0.00369      #divide by 0018 for dPress500
			
			print "Pressure:", pressure
	time.sleep(.1)
	
