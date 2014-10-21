# Jaikrishna
# Initial Date: June 24, 2013
# Last Updated: Oct 21, 2014 by John
#
# These files have been made available online through a Creative Commons Attribution-ShareAlike 3.0  license.
# (http://creativecommons.org/licenses/by-sa/3.0/)
#
# http://www.dexterindustries.com/BrickPi
# This code is for testing the BrickPi with a Lego Color Sensor
# This code will turn a LEGO color sensor on Port 1 to red.  It will output a red LED.
# You can also have the LED emit a Red, Green, or Blue light.

from BrickPi import *   #import BrickPi.py file to use BrickPi operations

BrickPiSetup()  # setup the serial port for communication

Color_Sensor_Port = PORT_1										# Setup the sensor on Port 1.
BrickPi.SensorType[Color_Sensor_Port] = TYPE_SENSOR_COLOR_RED   #Set the type of sensor, set it to function as a Red LED.
																# Change this value to change the LED Color: 
																# TYPE_SENSOR_COLOR_RED
																# TYPE_SENSOR_COLOR_GREEN
																# TYPE_SENSOR_COLOR_BLUE

BrickPiSetupSensors()   #Send the properties of sensors to BrickPi

while True:
    result = BrickPiUpdateValues()  # Ask BrickPi to update values for sensors/motors 
    time.sleep(.1)     # sleep for 100 ms

