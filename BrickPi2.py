import smbus
import time

bus = smbus.SMBus(1)

# GYROSCOPE CONSTANTS AND VARIABLES ARE DEFINED
address = 0x06

addr_Motor = 0x01
addr_Enc_1 = 0x04
addr_Enc_2 = 0x05
addr_Enc_3 = 0x06

def SetMotor(Motor1, Motor2, Motor3):

	motor_power = [Motor1, Motor2, Motor3]
	bus.write_i2c_block_data(address, addr_Motor, motor_power)
	time.sleep(0.01)

def ReadEncoder(encoder_number):
	encoder_number = encoder_number+0x04
	# error handling needs to go here: if you're not an encoder number.
	# retVal = bus.read_word_data(address, encoder_number)
	# retVal = bus.read_byte_data(address, 0x04)
	encoder_value = bus.read_i2c_block_data(address, encoder_number, 4)
	retVal = python
	time.sleep(0.01)
	return retVal

def main():
	while True:	
		SetMotor(100, 50, -50)
		print ReadEncoder(1)
		#time.sleep(0.1)

#if __name__=='__main__':

main()
