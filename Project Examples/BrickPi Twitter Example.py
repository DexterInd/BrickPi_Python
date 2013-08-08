# Jaikrishna
# Initial Date: July 10, 2013
# Last Updated: July 10, 2013
# http://www.dexterindustries.com/
# This code is for setting up the BrickPi & Raspberry Pi as a Tweet bot

# Enter these commands to setup twython library to support twitter:
# sudo wget https://bitbucket.org/pypa/setuptools/raw/0.7.4/ez_setup.py -O - | sudo python
# git clone git://github.com/ryanmcgrath/twython.git
# cd twython
# python setup.py install

from BrickPi import *   #import BrickPi.py file to use BrickPi operations
import time
from twython import Twython, TwythonError

BrickPiSetup()  # setup the serial port for communication

# Setup keys for Twitter
APP_KEY = "1234567890"
APP_SECRET = "1234567890"
OAUTH_TOKEN = "1234567890" #
OAUTH_TOKEN_SECRET = "1234567890" #

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET) # Setup a Twython object

BrickPi.SensorType[PORT_1] = TYPE_SENSOR_RAW   #Set the type of sensor at PORT_1

BrickPiSetupSensors()   #Send the properties of sensors to BrickPi

while True:
    result = BrickPiUpdateValues()  # Ask BrickPi to update values for sensors/motors 
    if not result :
            s = 'Time: ' + time.strftime('%X') + '  Sensor: ' + str(BrickPi.Sensor[PORT_1])    #BrickPi.Sensor[PORT] stores the value obtained from sensor
            try:
                twitter.update_status(status=s) # Make a tweet 
                print "Tweeted:",s
            except TwythonError as e:   # Handles exception if Error is thrown 
                print "Error occured:", e.message
    time.sleep(5*60)     # sleep for 5 minutes













