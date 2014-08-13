# Dexter Industries
# Initial Date: June 24, 2013
# Last Updated: August 13, 2014
#
# These files have been made available online through a Creative Commons Attribution-ShareAlike 3.0  license.
# (http://creativecommons.org/licenses/by-sa/3.0/)
#
# http://www.dexterindustries.com/BrickPi
# This code is for testing the BrickPi with a Lego Motor.

from BrickPi import *   #import BrickPi.py file to use BrickPi operations

BrickPiSetup()  # setup the serial port for communication

BrickPi.MotorEnable[PORT_A] = 1 #Enable the Motor A
BrickPi.MotorEnable[PORT_B] = 1 #Enable the Motor B
BrickPi.MotorEnable[PORT_C] = 1 #Enable the Motor A
BrickPi.MotorEnable[PORT_D] = 1 #Enable the Motor B

BrickPiSetupSensors()   #Send the properties of sensors to BrickPi

power = 0

while True:
    print "Running Forward"
    power = 200
    BrickPi.MotorSpeed[PORT_A] = power  #Set the speed of MotorA (-255 to 255)
    BrickPi.MotorSpeed[PORT_B] = power  #Set the speed of MotorB (-255 to 255)
    BrickPi.MotorSpeed[PORT_C] = power  #Set the speed of MotorA (-255 to 255)
    BrickPi.MotorSpeed[PORT_D] = power  #Set the speed of MotorB (-255 to 255)

    ot = time.time()
    while(time.time() - ot < 3):    #running while loop for 3 seconds
        BrickPiUpdateValues()       # Ask BrickPi to update values for sensors/motors
	time.sleep(.1)

    print "Running Backward"
    power = -200
    BrickPi.MotorSpeed[PORT_A] = power  #Set the speed of MotorA (-255 to 255)
    BrickPi.MotorSpeed[PORT_B] = power  #Set the speed of MotorB (-255 to 255)
    BrickPi.MotorSpeed[PORT_C] = power  #Set the speed of MotorA (-255 to 255)
    BrickPi.MotorSpeed[PORT_D] = power  #Set the speed of MotorB (-255 to 255)

    ot = time.time()
    while(time.time() - ot < 3):    #running while loop for 3 seconds
        BrickPiUpdateValues()       # Ask BrickPi to update values for sensors/motors
        time.sleep(.1)              # sleep for 100 ms
