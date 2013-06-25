# This document Move everything over to serial line

import time
import BrickPi2

# Remove sudo nano /boot/cmdline.txt
# console=ttyAMA0,115200 kgdboc=ttyAMA0,115200
# in nano /etc/inittab comment out the last line.

time.sleep(0.1)

while True:

	# Set Motor Power
	x = 100
	BrickPi2.SetMotor(0,0,0)
	BrickPi2.SetLED(False, False)
	time.sleep(0.1)
	BrickPi2.SetLED(True, True)
	print (BrickPi2.ReadEncoder(1))
	print (BrickPi2.ReadEncoder(2))
	print (BrickPi2.ReadEncoder(3))
	print str((BrickPi2.ReadAnalog()))
	BrickPi2.SetLED(False, False)
	time.sleep(0.1)
