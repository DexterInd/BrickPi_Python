import BrickPi
import socket
import time





# GYROSCOPE CONSTANTS AND VARIABLES ARE DEFINED

def main():

	# WIFI stuff.  Setup a TCP socket.

	motor_speed_1 = -25
	motor_speed_2 = -50
	motor_speed_3 = -75
	BrickPi.SetMotor(motor_speed_1, motor_speed_2, motor_speed_3)
	starting_encoder_value = BrickPi.ReadEncoder(1)

	condition = True

	while condition:
		encoder_val = BrickPi.ReadEncoder(1)-starting_encoder_value
		print encoder_val
		if encoder_val > 50:
			condition = False
		#BrickPi.test_LED()
		time.sleep(0.1)
		print "###"
	
	BrickPi.SetMotor(0,0,0)

#if __name__=='__main__':

main()
