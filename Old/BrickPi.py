import smbus
import time

bus = smbus.SMBus(1)

# GYROSCOPE CONSTANTS AND VARIABLES ARE DEFINED
address = 0x06

addr_Motor = 0x01

def SetMotor(Motor1, Motor2, Motor3):

	motor_power = [Motor1, Motor2, Motor3]
	bus.write_i2c_block_data(address, addr_Motor, motor_power)
	time.sleep(0.1)

def main():
	while True:	
		SetMotor(100, 50, -50)
		time.sleep(0.1)

#if __name__=='__main__':

main()
