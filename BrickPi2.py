# Last modified 2013.04.29
# This is a first attempt at a module for BrickPi

import serial
import time
import struct

ser = serial.Serial("/dev/ttyAMA0", 115200, timeout=0.5)
address = 0x06
addr_Motor = 0x01

motor_speed_1 = 0;
motor_speed_2 = 0;
motor_speed_3 = 0; 

motor_1_encoder = 0;
motor_2_encoder = 0;
motor_3_encoder = 0;


def SetMotor(Motor1, Motor2, Motor3):
	try:
		# bus.write_i2c_block_data(address, addr_Motor, motor_power)
		##############################
		if Motor1 < -100:
			Motor1 = -100
		if Motor2 < -100:
			Motor2 = -100
		if Motor3 < -100:
			Motor3 = -100
		##############################
		if Motor1 > 100:
			Motor1 = 100
		if Motor2 > 100:
			Motor2 = 100
		if Motor3 > 100:
			Motor3 = 100
		##############################
		if Motor1 < 0:
			Motor1 = Motor1+256
		if Motor2 < 0:
			Motor2 = Motor2+256
		if Motor3 < 0:
			Motor3 = Motor3+256
		##############################
		out_string = "1" + chr(int(Motor1))+chr(int(Motor2))+chr(int(Motor3))+"\n"
		ser.write(out_string)
	except IOError:
		print "Failed motor write.  Check BrickPi"
	time.sleep(0.01)

def signed(n):
	return n if n < 0 else n-[i for i in (2**j if n/(2**(j-1)) else iter(()).next() for j in xrange(2**31-1))][-1]

def ReadEncoder(encoder_number):
	if encoder_number > 3:
		encoder_number = 3

	if encoder_number < 1:
		encoder_number = 1

	encoder_number = encoder_number+51
	try:
		out_string = chr(encoder_number)+"\n"
		ser.write(out_string)
		time.sleep(0.1)
		encoder_value = ser.read(200)
	except IOError:
		print "Failed Encoder Reading.  Check BrickPi."
		return 0

	# Find the beginning and ending of the number in the string on the way back.
	begin = 1 + encoder_value.find(chr(encoder_number))
	end = encoder_value.find("\n")-1
	string_val = encoder_value[begin:end]
	retVal = int(string_val)
	return retVal

def ReadAnalog():
	out_string = "8\n"
	ser.write(out_string)
	time.sleep(0.001)
	retVal = ser.read(5)
	retVal = (retVal)
	return retVal

def SetLED(LED1, LED2):
	iLED1 = 0x00
	iLED2 = 0x00
	if LED1:
		iLED1 = 0x01
	if LED2:
		iLED2 = 0x01

	out_string = "7" + chr(iLED1) + chr(iLED2) + "\n"
	ser.write(out_string)
	time.sleep(0.01)

def test_LED():
	SetLED(1,0)
	time.sleep(0.1)
	SetLED(0,1)
	time.sleep(0.1)
	SetLED(0,0)
	time.sleep(0.1)
	SetLED(1,1)
	time.sleep(0.1)

if __name__ == "__main__":
	import sys
	
