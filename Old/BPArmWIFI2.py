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
	bus.write_i2c_block_data(address, addr_Motor, motor_power)
	time.sleep(0.01)

def signed(n):
	return n if n < 0 else n-[i for i in (2**j if n/(2**(j-1)) else iter(()).next() for j in xrange(2**31-1))][-1]

def ReadRaw():
	print bus.read_i2c_block_data(address, 0x04, 4)
	time.sleep(1)
	print bus.read_i2c_block_data(address, 0x05, 4)
	time.sleep(1)
	print bus.read_i2c_block_data(address, 0x06, 4)
	time.sleep(1)
	print " - - - - "


def ReadEncoder(encoder_number):
	encoder_number = encoder_number+0x03
	print "Encoder Number:"
	print encoder_number
	encoder_value = bus.read_i2c_block_data(address, encoder_number, 4)
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
	bus.write_i2c_block_data(address, 0x0C, LEDs)
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

	motor_speed_1 = 0
	motor_speed_2 = 0
	motor_speed_3 = 0

	while True:
		'''SetMotor(0,-60,75)	# Close claw
		time.sleep(2)
		test_LED()
		test_LED()
		SetMotor(0,68,-40)	# Rotate arm
		time.sleep(2)
		test_LED()
		test_LED()

		#SetMotor(100,0,0)	# Raise arm
		#time.sleep(4)
	
		#SetMotor(0,0,0)		# Stop all motors
		#time.sleep(2)
		

		#SetMotor(0,75,0)	# Close claw
		#time.sleep(0.25)
	
		#SetMotor(0,0,-75)	# Rotate arm
		#time.sleep(4)
	
		#SetMotor(-75,0,0)	# Raise arm
		#time.sleep(0.5)
	
		SetMotor(0,0,0)		# Stop all motors
		'''
		'''print ReadEncoder(0x01)
		print ReadEncoder(0x02)
		print ReadEncoder(0x03)
		'''
		ReadRaw()
		time.sleep(2)
		print "###"


#if __name__=='__main__':

main()
