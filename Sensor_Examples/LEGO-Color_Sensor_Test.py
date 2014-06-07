# Jaikrishna
# Initial Date: June 24, 2013
# Last Updated: June 24, 2013
#
# These files have been made available online through a Creative Commons Attribution-ShareAlike 3.0  license.
# (http://creativecommons.org/licenses/by-sa/3.0/)
#
# http://www.dexterindustries.com/
# This code is for testing the BrickPi with a Lego Color Sensor

from BrickPi import *   #import BrickPi.py file to use BrickPi operations

BrickPiSetup()  # setup the serial port for communication

col = [ None , "Black","Blue","Green","Yellow","Red","White" ]   #used for converting the color index to name
BrickPi.SensorType[PORT_1] = TYPE_SENSOR_COLOR_FULL   #Set the type of sensor at PORT_1


BrickPiSetupSensors()   #Send the properties of sensors to BrickPi

while True:
    result = BrickPiUpdateValues()  # Ask BrickPi to update values for sensors/motors 
    if not result :
        print col[BrickPi.Sensor[PORT_1]]     #BrickPi.Sensor[PORT] stores the value obtained from sensor
    time.sleep(.1)     # sleep for 100 ms

