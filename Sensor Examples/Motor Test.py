# Jaikrishna
# Initial Date: June 24, 2013
# Last Updated: June 24, 2013
# http://www.dexterindustries.com/
# This code is for testing the BrickPi with a Lego Motor 

from BrickPi import *   #import BrickPi.py file to use BrickPi operations

BrickPiSetup()  # setup the serial port for communication

BrickPi.MotorEnable[PORT_A] = 1 #Enable the Motor A
BrickPi.MotorEnable[PORT_B] = 1 #Enable the Motor B

BrickPiSetupSensors()   #Send the properties of sensors to BrickPi

while True:
    print "Running Forward"
    BrickPi.MotorSpeed[PORT_A] = 200  #Set the speed of MotorA (-255 to 255)
    BrickPi.MotorSpeed[PORT_B] = 200  #Set the speed of MotorA (-255 to 255)
    ot = time.time()
    while(time.time() - ot < 3):    #running while loop for 3 seconds
        BrickPiUpdateValues()       # Ask BrickPi to update values for sensors/motors
        time.sleep(.1)              # sleep for 100 ms
    print "Running Reverse"
    BrickPi.MotorSpeed[PORT_A] = -200  #Set the speed of MotorA (-255 to 255)
    BrickPi.MotorSpeed[PORT_B] = -200  #Set the speed of MotorA (-255 to 255)
    ot = time.time()
    while(time.time() - ot < 3):    #running while loop for 3 seconds
        BrickPiUpdateValues()       # Ask BrickPi to update values for sensors/motors
        time.sleep(.1)              # sleep for 100 ms