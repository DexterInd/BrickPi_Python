# BRICKPI LEGO TOUCH SENSOR EXAMPLE.
############################################
# This example will show you how to use the LEGO touch sensor with the BrickPi.  
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

BrickPiSetup()  # setup the serial port for communication

BrickPi.SensorType[PORT_4] = TYPE_SENSOR_TOUCH   #Set the type of sensor at PORT_1

BrickPiSetupSensors()   #Send the properties of sensors to BrickPi

while True:
    result = BrickPiUpdateValues()  # Ask BrickPi to update values for sensors/motors 
    if not result :
        print BrickPi.Sensor[PORT_4]     #BrickPi.Sensor[PORT] stores the value obtained from sensor
    time.sleep(.01)     # sleep for 10 ms

