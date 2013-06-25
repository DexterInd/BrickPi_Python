import smbus
import time
import struct
import socket

bus = smbus.SMBus(1)

# GYROSCOPE CONSTANTS AND VARIABLES ARE DEFINED
address = 0x06

addr_Motor = 0x01
addr_Enc_1 = 0x04
addr_Enc_2 = 0x05
addr_Enc_3 = 0x06

motor_speed_1 = 0;
motor_speed_2 = 0;
motor_speed_3 = 0; 

motor_1_encoder = 0;
motor_2_encoder = 0;
motor_3_encoder = 0;



def SetMotor(Motor1, Motor2, Motor3):

	motor_power = [Motor1, Motor2, Motor3]
	try:
		bus.write_i2c_block_data(address, addr_Motor, motor_power)
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

	encoder_number = encoder_number+0x03
	try:
		encoder_value = bus.read_i2c_block_data(address, encoder_number, 4)
	except IOError:
		print "Failed Encoder Reading.  Check BrickPi."
		return 0
	
	retVal = ""
	for x in range(0,4):

		if encoder_value[x] < 0x0F:
			retVal = retVal+"0"
		if encoder_value[x] == 0:
			retVal = retVal+"0"
		retVal = retVal+''.join(hex(encoder_value[x]).lstrip("0x")) 
	retVal = long(("0x" + retVal),16)
	if retVal > 2147483648:
		retVal = signed(retVal)
	time.sleep(0.01)
	return retVal

def ReadAnalog():
	analog_value = bus.read_i2c_block_data(address, 0x0D, 4)
	#retVal = ""
	#for x in range(0,4):
	#
	#	if encoder_value[x] < 0x0F:
	#		retVal = retVal+"0"
	#	if encoder_value[x] == 0:
	#		retVal = retVal+"0"
	#	retVal = retVal+''.join(hex(encoder_value[x]).lstrip("0x")) 
	#retVal = long(("0x" + retVal),16)
	#if retVal > 2147483648:
	#	retVal = signed(retVal)
	retVal = analog_value
	time.sleep(0.01)
	return retVal

def SetLED(LED1, LED2):
	LEDs = [LED1, LED2]
	try:
		bus.write_i2c_block_data(address, 0x0C, LEDs)
	except IOError:
		print "Failed LED write.  Check BrickPi."
		return 0
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

def arm_turn_base(angle):
	# This definition will turn the base to a defined angle, between -90 and 90
	# Read encoder value
	base_enc = ReadEncoder(1)
	print "Base Encoder: "
	print base_enc
	# Compare encoder value to desired encoder position
	if base_enc > angle:
		motor_power = -25
		while(ReadEncoder(3) > angle):
			time.sleep(1)
			print ReadEncoder(3)
			SetMotor(motor_power, 0,0)
			time.sleep(0.1)
	if base_enc < angle:
		motor_power = 25
		while(ReadEncoder(3) < angle):
			time.sleep(0.1)
			print ReadEncoder(3)
			SetMotor(motor_power, 0,0)
			time.sleep(0.01)
	# Turn in a direction, until the encoder value is on position.

	
	return 0	

def arm_raise(angle):
	#nothing
	return 0

def claw(close):
	#nothing
	return 0

def main():

	# WIFI stuff.  Setup a TCP socket.

	motor_speed_1 = -25
	motor_speed_2 = -50
	motor_speed_3 = -75
	SetMotor(motor_speed_1, motor_speed_2, motor_speed_3)
	starting_encoder_value = ReadEncoder(1)

	condition = True

	while condition:
		encoder_val = ReadEncoder(1)-starting_encoder_value
		print encoder_val
		if encoder_val > 50:
			condition = False
		test_LED()
		time.sleep(0.1)
		print "###"
	
	SetMotor(0,0,0)

#if __name__=='__main__':

main()
