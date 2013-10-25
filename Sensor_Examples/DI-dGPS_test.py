# Jaikrishna
# Initial Date: June 24, 2013
# Last Updated: June 24, 2013
#
# These files have been made available online through a Creative Commons Attribution-ShareAlike 3.0  license.
# (http://creativecommons.org/licenses/by-sa/3.0/)
#
# http://www.dexterindustries.com/
# This code is for testing the BrickPi with a GPS sensor from Dexter Industries
# Product webpage: http://www.dexterindustries.com/dGPS.html

from BrickPi import *   #import BrickPi.py file to use BrickPi operations

I2C_PORT  = PORT_3                            # I2C port for the dGPS
I2C_SPEED = 0                                 # delay for as little time as possible. Usually about 100k baud
I2C_DEVICE_DGPS = 0                        	# dGPS is device 0 on this I2C bus

DGPS_I2C_ADDR   = 0x06      # Barometric sensor device address 
DGPS_CMD_UTC    = 0x00      # Fetch UTC 
DGPS_CMD_STATUS = 0x01      # Status of satellite link: 0 no link, 1 link 
DGPS_CMD_LAT    = 0x02      # Fetch Latitude 
DGPS_CMD_LONG   = 0x04      # Fetch Longitude 
DGPS_CMD_VELO   = 0x06      # Fetch velocity in cm/s 
DGPS_CMD_HEAD   = 0x07      # Fetch heading in degrees 



BrickPiSetup()  # setup the serial port for communication

BrickPi.SensorType[I2C_PORT] = TYPE_SENSOR_I2C 	#Set the type of sensor at PORT_3
BrickPi.SensorI2CSpeed[I2C_PORT] = I2C_SPEED   #Set the speed of communication
BrickPi.SensorI2CDevices [I2C_PORT] = 1        #number of devices in the I2C bus
BrickPi.SensorI2CAddr  [I2C_PORT][I2C_DEVICE_DGPS]    = DGPS_I2C_ADDR	#address for writing
BrickPi.SensorSettings [I2C_PORT][I2C_DEVICE_DGPS]    = BIT_I2C_MID	# the dGPS device requires a clock change between reading and writing
BrickPi.SensorI2CWrite [I2C_PORT][I2C_DEVICE_DGPS]    = 1				#number of bytes to write


while True:
	#UTC
	BrickPi.SensorI2CRead  [I2C_PORT][I2C_DEVICE_DGPS]    = 4
	BrickPi.SensorI2COut   [I2C_PORT][I2C_DEVICE_DGPS][0] = DGPS_CMD_UTC	#byte to write
	BrickPiSetupSensors()
	result = BrickPiUpdateValues() #write and read
	if not result :
		if (BrickPi.Sensor[I2C_PORT] & (0x01 << I2C_DEVICE_DGPS)) :
			UTC = ((long)(BrickPi.SensorI2CIn[I2C_PORT][I2C_DEVICE_DGPS][0]<<24)) + ((long)(BrickPi.SensorI2CIn[I2C_PORT][I2C_DEVICE_DGPS][1]<<16)) + ((long)(BrickPi.SensorI2CIn[I2C_PORT][I2C_DEVICE_DGPS][2]<<8)) + (long)(BrickPi.SensorI2CIn[I2C_PORT][I2C_DEVICE_DGPS][3])
	
	#Longitude
	BrickPi.SensorI2COut   [I2C_PORT][I2C_DEVICE_DGPS][0] = DGPS_CMD_LONG	#byte to write
	BrickPiSetupSensors()
	result = BrickPiUpdateValues() #write and read
	if not result :
		if (BrickPi.Sensor[I2C_PORT] & (0x01 << I2C_DEVICE_DGPS)) :
			lon = ((long)(BrickPi.SensorI2CIn[I2C_PORT][I2C_DEVICE_DGPS][0]<<24)) + ((long)(BrickPi.SensorI2CIn[I2C_PORT][I2C_DEVICE_DGPS][1]<<16)) + ((long)(BrickPi.SensorI2CIn[I2C_PORT][I2C_DEVICE_DGPS][2]<<8)) + (long)(BrickPi.SensorI2CIn[I2C_PORT][I2C_DEVICE_DGPS][3])

	#Latitude
	BrickPi.SensorI2COut   [I2C_PORT][I2C_DEVICE_DGPS][0] = DGPS_CMD_LAT	#byte to write
	BrickPiSetupSensors()
	result = BrickPiUpdateValues() #write and read
	if not result :
		if (BrickPi.Sensor[I2C_PORT] & (0x01 << I2C_DEVICE_DGPS)) :
			lat = ((long)(BrickPi.SensorI2CIn[I2C_PORT][I2C_DEVICE_DGPS][0]<<24)) + ((long)(BrickPi.SensorI2CIn[I2C_PORT][I2C_DEVICE_DGPS][1]<<16)) + ((long)(BrickPi.SensorI2CIn[I2C_PORT][I2C_DEVICE_DGPS][2]<<8)) + (long)(BrickPi.SensorI2CIn[I2C_PORT][I2C_DEVICE_DGPS][3])

	#Heading
	BrickPi.SensorI2CRead  [I2C_PORT][I2C_DEVICE_DGPS]    = 2
	BrickPi.SensorI2COut   [I2C_PORT][I2C_DEVICE_DGPS][0] = DGPS_CMD_HEAD	#byte to write
	BrickPiSetupSensors()
	result = BrickPiUpdateValues() #write and read
	if not result :
		if (BrickPi.Sensor[I2C_PORT] & (0x01 << I2C_DEVICE_DGPS)) :
			head = ((long)(BrickPi.SensorI2CIn[I2C_PORT][I2C_DEVICE_DGPS][0]<<8)) + ((long)(BrickPi.SensorI2CIn[I2C_PORT][I2C_DEVICE_DGPS][1]))
	
	#Status
	BrickPi.SensorI2CRead  [I2C_PORT][I2C_DEVICE_DGPS]    = 1
	BrickPi.SensorI2COut   [I2C_PORT][I2C_DEVICE_DGPS][0] = DGPS_CMD_STATUS	#byte to write
	BrickPiSetupSensors()
	result = BrickPiUpdateValues() #write and read
	if not result :
		if (BrickPi.Sensor[I2C_PORT] & (0x01 << I2C_DEVICE_DGPS)) :
			status = ((long)(BrickPi.SensorI2CIn[I2C_PORT][I2C_DEVICE_DGPS][0]))

	#Velocity
	BrickPi.SensorI2CRead  [I2C_PORT][I2C_DEVICE_DGPS]    = 3
	BrickPi.SensorI2COut   [I2C_PORT][I2C_DEVICE_DGPS][0] = DGPS_CMD_VELO	#byte to write
	BrickPiSetupSensors()
	result = BrickPiUpdateValues() #write and read
	if not result :
		if (BrickPi.Sensor[I2C_PORT] & (0x01 << I2C_DEVICE_DGPS)) :
			velo = ((long)(BrickPi.SensorI2CIn[I2C_PORT][I2C_DEVICE_DGPS][0]<<16)) + ((long)(BrickPi.SensorI2CIn[I2C_PORT][I2C_DEVICE_DGPS][1]<<8)) + ((long)(BrickPi.SensorI2CIn[I2C_PORT][I2C_DEVICE_DGPS][2]))
	
	print 'Status',status,'UTC',UTC,'Latitude',lat,'Longitude',lon,'Heading',head,'Velocity',velo
	time.sleep(0.50000);   #giving some delay before acquiring next set of data
