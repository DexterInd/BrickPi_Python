# Last modified 2013.06.11
# Edited BrickPi Python library for Tufts CEEO BlockyTalky project

import serial
import time
import struct

ser = serial.Serial("/dev/ttyAMA0", 115200, timeout=0.5)
address = 0x06
addr_Motor = 0x01


def WaitForSerial():
	x= ' '
	while(x==' '):
		x=ser.read(1)

def SetAllMotors(motor_power):
	try:
		if motor_power < -100:
			motor_power= -100
		if motor_power > 100:
			motor_power= 100
		if motor_power < 0:
			motor_power= motor_power+256

		out_string= "9"+chr(int(motor_power))+"\n"
		ser.write(out_string)

	except IOError:
		print "Failed Motor Write. Check BrickPi"
	WaitForSerial()

def SetMotor(motor_num, motor_power):
	try:
		if motor_power < -100:
			motor_power= -100
		if motor_power > 100:
			motor_power= 100
		if motor_num < 1:
			motor_num= 1
		if motor_num > 3:
			motor_num= 3
		if motor_power < 0:
			motor_power= motor_power+256		

		motor_num= motor_num-1
		out_string= "1"+chr(int(motor_num))+chr(int(motor_power))+"\n"
        	ser.write(out_string)

	except IOError:
		print "Failed Motor Write.  Check BrickPi"
	WaitForSerial()

#remnant of original version.... not used
def signed(n):
	return n if n < 0 else n-[i for i in (2**j if n/(2**(j-1)) 
		else iter(()).next() for j in xrange(2**31-1))][-1]

def ReadEncoder(encoder_number):
	if encoder_number > 3:
		encoder_number = 3

	if encoder_number < 1:
		encoder_number = 1

	encoder_number = encoder_number+51
	try:
		out_string = chr(encoder_number)+"\n"
		ser.write(out_string)
		WaitForSerial()
		encoder_value= ser.read(1)
		temp= ' '
		while(temp != '\n'):
			temp= ser.read(1)
			encoder_value+= temp
	except IOError:
		print "Failed Encoder Reading.  Check BrickPi."
		return 0
	retVal= encoder_value[:-2]
	retVal= int(retVal)
	retVal= retVal*-1      #fixes issue of encoders being backwards
	return retVal

def ReadAnalog(port_num):
	if port_num < 1:
		port_num= 1
	if port_num > 4:
		port_num= 4
	port_num= port_num -1
	out_string = "8\n"
	ser.write(out_string)
	WaitForSerial()
	retVal = ser.read(4)
	retVal = (retVal)
	a= retVal[port_num]
	return int(a.encode('hex'),16)

def SetLED(LED1, LED2):
	iLED1 = 0x00
	iLED2 = 0x00
	if LED1:
		iLED1 = 0x01
	if LED2:
		iLED2 = 0x01

	out_string = "7" + chr(iLED1) + chr(iLED2) + "\n"
	ser.write(out_string)
	WaitForSerial()

def test_LED():
	SetLED(1,0)
	time.sleep(0.1)
	SetLED(0,1)
	time.sleep(0.1)
	SetLED(0,0)
	time.sleep(0.1)
	SetLED(1,1)
	time.sleep(0.1)
	SetLED(0,0)
	time.sleep(0.1)
	
if __name__ == "__main__":
	import sys
	
