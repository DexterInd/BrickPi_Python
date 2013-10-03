# Jaikrishna
# Initial Date: June 28, 2013
# Last Updated: June 28, 2013
#
# These files have been made available online through a Creative Commons Attribution-ShareAlike 3.0  license.
# (http://creativecommons.org/licenses/by-sa/3.0/)
#
# http://www.dexterindustries.com/
# This code is for testing the BrickPi LEDs with GPIO library
# If GPIO library isn't installed enter: sudo apt-get install python-rpi.gpio

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print 'Error importing RPi.GPIO. You need to run this with superuser privileges. Try sudo python "LED PWM.py" or sudo idle'
import time

delay = 0.05

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)    #GPIO 18
GPIO.setup(13, GPIO.OUT)    #GPIO 27

p1 = GPIO.PWM(12, 50)
p2 = GPIO.PWM(13, 50)
p1.start(0)
p2.start(100)

print "Press Ctrl+C to exit"

while True:
    try:
        for dc in range (0, 101, 5):
            p1.ChangeDutyCycle(dc)
            p2.ChangeDutyCycle(100 - dc)
            time.sleep(delay)
        for dc in range(100, -1 , -5):
            p1.ChangeDutyCycle(dc)
            p2.ChangeDutyCycle(100 - dc)
            time.sleep(delay)
    except KeyboardInterrupt:
        p1.stop()
        p2.stop()
        GPIO.cleanup()
        break
