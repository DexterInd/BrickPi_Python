#Joshwa
#Ball Shooter Robot controlled by a  mouse.
#Ball Shooter Robot is a stationery robot with two motors - one to rotate and fix a position and another for shooting the ball which is controlled by a mouse
#Make the connections with Shooter Motor at Port A, and the other Motor at Port D 
#Setup battery power source for the RPi & BrickPi and boot.
#Connect the mouse to one of the usb ports of the RaspberryPi
# Mouse Controls #
#Move the mouse right to rotate the motor in right direction
#Move the mouse left to rotate the bot in the left direction
#Click the left button on the mouse to shoot the ball
#Click the right button on the mouse to stop both the motors instantly

from BrickPi import *   #import BrickPi.py file to use Brici operations
import threading
import struct

file = open( "/dev/input/mice", "rb" );      # reads the /dev/input/mice and converts the hex-input into integers
def getMouseEvent():                         # function to get the inputs from the mouse and control motors
  buf = file.read(3);                        
  button = ord( buf[0] );
  bLeft = button & 0x1;                      # assigns the state of left button to bLeft
  bRight = ( button & 0x2 ) > 0;             # assigns the state of right button to bRight
  x,y = struct.unpack( "bb", buf[1:] );      # assigns the speed of mouse in x and y direction to variables x and y.
  global cr               # variable for keeping track whether the mouse has moved right
  global cl               # variable for keeping track whether the mouse has moved left
  if bRight == 1 :        #If right button is clicked all the motors will stop instantly
    bLeft = 0             
    x = 0                 #All the other variables are set to 0 since we want only one motor to be running at a time 
    print "Stop everything"
    BrickPi.MotorSpeed[PORT_A] = 0       #Sets the speed of MotorA (-255 to 255)
    BrickPi.MotorSpeed[PORT_D] = 0       #Sets the speed of MotorA (-255 to 255)
  elif bLeft == 1 :
    bRight = 0
    x = 0
    print "Shoot"
    BrickPi.MotorSpeed[PORT_A] = 200      #Sets the speed of MotorA (-255 to 255)
    BrickPi.MotorSpeed[PORT_D] = 0        #Sets the speed of MotorA (-255 to 255)
  elif x > 100:           #when speed of mouse is greater than 100 the motor rotates right 
    bLeft = 0
    bRight = 0
    print "Turn Right"
    BrickPi.MotorSpeed[PORT_A] = 0        #Sets the speed of MotorA (-255 to 255)
    BrickPi.MotorSpeed[PORT_D] = -200     #Sets the speed of MotorA (-255 to 255)
  elif x < -100 :
    bLeft = 0
    bRight = 0
    print "Turn Left"
    BrickPi.MotorSpeed[PORT_A] = 0         #Sets the speed of MotorA (-255 to 255)
    BrickPi.MotorSpeed[PORT_D] = 200       #Sets the speed of MotorA (-255 to 255)
  BrickPiUpdateValues();                   # BrickPi updates the values for the motors
  print "Values Updated"

BrickPiSetup()                          # setup the serial port for communication
BrickPi.MotorEnable[PORT_A] = 1         #Enable the Motor A
BrickPi.MotorEnable[PORT_D] = 1         #Enable the Motor D
BrickPiSetupSensors()                   #Send the properties of sensors to BrickPi

while( 1 ):
  running = True
  getMouseEvent();       # Calls the function which gets all the inputs from mouse
  
file.close();
