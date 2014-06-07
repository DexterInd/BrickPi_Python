# Karan Nayan
# Initial Date: July 11, 2013
# Last Updated: July 11, 2013
# http://www.dexterindustries.com/
#
# These files have been made available online through a Creative Commons Attribution-ShareAlike 3.0  license.
# (http://creativecommons.org/licenses/by-sa/3.0/)
#
# This is an example of controlling the rotation of motors using encoders
from BrickPi import *   #import BrickPi.py file to use BrickPi operations

BrickPiSetup()  # setup the serial port for sudo su communication
BrickPiSetupSensors()       #Send the properties of sensors to BrickPi
BrickPiUpdateValues()

"""
Pass the arguments in a list. 
If a single motor has to be controlled then the arguments should be passed like 
elements of an array,e.g, motorRotateDegree([255],[360],[PORT_A]) where power=255 and
angle=360 for the motor connected at Port A
"""
power=[255]
deg=[360]
port=[PORT_A]
motorRotateDegree(power,deg,port)

"""
If multiple motors have to be controlled then the parameters for running each motor must be passed
as the elements of an array,e.g, motorRotateDegree([255,100],[360,30],[PORT_A,PORT_B]) where 
power=255 and angle=30 are for motor at PORT_A and power=100 and angle=30 are for motor at PORT_B.
It can be used similarly for any number of motors.
"""
time.sleep(1)
power=[255,30]
deg=[360,-180]
port=[PORT_A,PORT_B]
motorRotateDegree(power,deg,port)
