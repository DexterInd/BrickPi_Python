# Karan Nayan
# Initial Date: June 24, 2013
# Last Updated: July 11, 2013
# http://www.dexterindustries.com/
# This code is for rotating a motor by a particular angle

from BrickPi import *   #import BrickPi.py file to use BrickPi operations

BrickPiSetup()  # setup the serial port for sudo su communication

BrickPiSetupSensors()       #Send the properties of sensors to BrickPi
BrickPiUpdateValues()

print motorRotateDegree(100,180,PORT_A,.01)

