'''
########################################################################
#                                                                      #
# Program Name: MINDSENSORS_PSP.py                                     #
# ===========================                                          #
#                                                                      #
# Copyright (c) 2013 by dexterindustries.com                           #
#                                                                      #
# This program is free software. You can redistribute it and/or modify #
# it under the terms of the GNU General Public License as published by #
# the Free Software Foundation; version 3 of the License.              #
# Read the license at: http://www.gnu.org/licenses/gpl.txt             #
#                                                                      #
########################################################################
# History
# ------------------------------------------------
# Author     Date      Comments
# Karan      04/11/13  Initial Authoring
#
# Ported from the C Library Provided by mindsensors.com: 
# Email: info (<at>) mindsensors (<dot>) com 
# History
# ------------------------------------------------
# Author     Date      Comments
# Deepak     04/08/09  Initial Authoring.
#
#--------------------------------------
  Controller button layout:
----------------------------------------

      L1                R1
      L2                R2

      d                 triang
   a     c         square     circle
      b                  cross

     l_j_b              r_j_b
     l_j_x              r_j_x
     l_j_y              r_j_y

-------------------------------------- #
#
  bits as follows:
	b1:   a b c d x r_j_b l_j_b x
	b2:   square cross circle triang R1 L1 R2 L2
'''
from BrickPi import *   #import BrickPi.py file to use BrickPi operations

#All the definitions and function for the buttons pressed on the controller
class button:
	#Initialize all the buttons to 0
	def init(self):
		self.l1=0
		self.l2=0
		self.r1=0
		self.r2=0
		self.a=0
		self.b=0
		self.c=0
		self.d=0
		self.tri=0
		self.sqr=0
		self.cir=0
		self.cro=0
		self.ljb=0
		self.ljx=0
		self.ljy=0
		self.rjx=0
		rjy=0
		
	#Update all the buttons
	def upd(self):
		#For all buttons:
		#0:	Unpressed
		#1:	Pressed
		#
		#Left and right joystick: -127 to 127
		self.ljb=~(BrickPi.SensorI2CIn[I2C_PORT][0][0]>>1)&1
		self.rjb=~(BrickPi.SensorI2CIn[I2C_PORT][0][0]>>2)&1
		
		#For buttons a,b,c,d
		self.d=~(BrickPi.SensorI2CIn[I2C_PORT][0][0]>>4)&1
		self.c=~(BrickPi.SensorI2CIn[I2C_PORT][0][0]>>5)&1
		self.b=~(BrickPi.SensorI2CIn[I2C_PORT][0][0]>>6)&1
		self.a=~(BrickPi.SensorI2CIn[I2C_PORT][0][0]>>7)&1
		
		#For buttons l1,l2,r1,r2
		self.l2=~(BrickPi.SensorI2CIn[I2C_PORT][0][1])&1
		self.r2=~(BrickPi.SensorI2CIn[I2C_PORT][0][1]>>1)&1
		self.l1=~(BrickPi.SensorI2CIn[I2C_PORT][0][1]>>2)&1
		self.r1=~(BrickPi.SensorI2CIn[I2C_PORT][0][1]>>3)&1
		
		#For buttons square,triangle,cross,circle
		self.tri=~(BrickPi.SensorI2CIn[I2C_PORT][0][1]>>4)&1
		self.cir=~(BrickPi.SensorI2CIn[I2C_PORT][0][1]>>5)&1
		self.cro=~(BrickPi.SensorI2CIn[I2C_PORT][0][1]>>6)&1
		self.sqr=~(BrickPi.SensorI2CIn[I2C_PORT][0][1]>>7)&1
		
		#Left joystick x and y , -127 to 127
		self.ljx=BrickPi.SensorI2CIn[I2C_PORT][0][2]-128
		self.ljy=~BrickPi.SensorI2CIn[I2C_PORT][0][3]+129
	
		#Right joystick x and y , -127 to 127
		self.rjx=BrickPi.SensorI2CIn[I2C_PORT][0][4]-128
		self.rjy=~BrickPi.SensorI2CIn[I2C_PORT][0][5]+129
	
	#Show button values
	def show_val(self):
		print "ljb","rjb","d","c","b","a","l2","r2","l1","r1","tri","cir","cro","sqr","ljx","ljy","rjx","rjy"
		print self.ljb," ",self.rjb," ",self.d,self.c,self.b,self.a,self.l2,"",self.r2,"",self.l1,"",self.r1,"",self.tri," ",self.cir," ",self.cro," ",self.sqr," ",self.ljx," ",self.ljy," ",self.rjx," ",self.rjy
		print ""

print "This program is free software. You can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; version 3 of the License. Read the license at: http://www.gnu.org/licenses/gpl.txt\n\n"
b=button()		#Object of button class
I2C_PORT  = PORT_1     # I2C port for the PSP controller
I2C_SPEED = 1         

BrickPi.SensorType       [I2C_PORT]    = TYPE_SENSOR_I2C#Set the type of sensor at PORT_1
BrickPi.SensorI2CSpeed   [I2C_PORT]    = I2C_SPEED      #Set the speed of communication
BrickPi.SensorI2CDevices [I2C_PORT]    = 1              #number of devices in the I2C bus

BrickPiSetup() 

BrickPi.SensorSettings   [I2C_PORT][0] = 0
BrickPi.SensorI2CAddr    [I2C_PORT][0] = 0x02     #address for writing

BrickPiSetupSensors() 

while True:
	#Send 0x42 to get a response back
	BrickPi.SensorI2CWrite [I2C_PORT][0]    = 1				#number of bytes to write
	BrickPi.SensorI2CRead  [I2C_PORT][0]    = 6				#number of bytes to read
	BrickPi.SensorI2COut   [I2C_PORT][0][0] = 0x42			#byte to write
	BrickPiUpdateValues()               					#writing
	
	b.upd()				#Update the button values
	b.show_val()		#Show the values 
						#To use the button values in you own program just call it, 
						#eg x=b.ljx will fetch and store the value of the Left Joystick position in the X-axis in the variable x
	b.init()			#Initialize all buttons to 0
	time.sleep(.05)		#//Give a delay of 50ms