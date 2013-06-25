import smbus
import time
import struct

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

def SetMotor(Motor1, Motor2, Motor3):

	motor_power = [Motor1, Motor2, Motor3]
	bus.write_i2c_block_data(address, addr_Motor, motor_power)
	time.sleep(0.01)

def signed(n):
	return n if n < 0 else n-[i for i in (2**j if n/(2**(j-1)) else iter(()).next() for j in xrange(2**31-1))][-1]

def ReadEncoder(encoder_number):
	encoder_number = encoder_number+0x03
	# error handling needs to go here: if you're not an encoder number.
	# retVal = bus.read_word_data(address, encoder_number)
	# retVal = bus.read_byte_data(address, 0x04)
	encoder_value = bus.read_i2c_block_data(address, encoder_number, 4)
	#print " . . . . "
	#print encoder_value
	retVal = ""
	for x in range(0,4):

		if encoder_value[x] < 0x0F:
			retVal = retVal+"0"
		if encoder_value[x] == 0:
			retVal = retVal+"0"
		retVal = retVal+''.join(hex(encoder_value[x]).lstrip("0x")) 
		#print retVal
	retVal = long(("0x" + retVal),16)
	#print retVal
	if retVal > 2147483648:
		retVal = signed(retVal)
	time.sleep(0.01)
	return retVal

def main():
	motor_speed_1 = 0
	while True:
		if raw_input() == '9':
			motor_speed_1 += 5
		if raw_input() == '3':
			motor_speed_1 -= 5
		print motor_speed_1
		SetMotor(motor_speed_1, motor_speed_1, motor_speed_1)
		print ReadEncoder(1)
		time.sleep(0.1)

#if __name__=='__main__':

main()
