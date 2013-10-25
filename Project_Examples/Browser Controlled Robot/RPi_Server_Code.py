#Joshwa
# http://www.dexterindustries.com/
# This code is for testing the BrickPi with Lego Motors & Lego Ultrasonic Sensor
# Make the connections with Left Motor at Port A, Right Motor at Port D and Sensor at Port 4
# Setup battery power source for the RPi & BrickPi and boot. 
# To control the program, connection must be made though SSH though PuTTY or similar software
# Open up PuTTY and enter UserName:pi Password:raspberry (Default values)
# Navigate to the directory containing this code and enter 'python Car.py'
# The user needs to enter one of the following keys:
# 8 - Forward
# 4 - Left
# 6 - Right
# 2 - Reverse
# 5 - Stop
# Also, The motors automatically stop when any nearby object is detected using the Ultrasonic Sensor


from BrickPi import *   #import BrickPi.py file to use BrickPi operations
import threading
import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.template
class MainHandler(tornado.web.RequestHandler):
  def get(self):
    loader = tornado.template.Loader(".")
    self.write(loader.load("index.html").generate())
c=0
class WSHandler(tornado.websocket.WebSocketHandler):
  def open(self):
    print 'connection opened...'
  def on_message(self, message):      # receives the data from the webpage and is stored in the variabe message
    global c
    print 'received:', message        # prints the recived from the webpage 
    if message == "u":                # checks for the received data and assigns different values to c whicch controls the movement of robot.
      c = "8";
    if message == "d":
      c = "2"
    if message == "l":
      c = "6"
    if message == "r":
      c = "4"
    if message == "b":
      c = "5"
    print c
    if c == '8' :
      print "Running Forward"
      BrickPi.MotorSpeed[PORT_A] = -200  #Set the speed of MotorA (-255 to 255)
      BrickPi.MotorSpeed[PORT_D] = -200  #Set the speed of MotorA (-255 to 255)
    elif c == '2' :
      print "Running Reverse"
      BrickPi.MotorSpeed[PORT_A] = 200  #Set the speed of MotorA (-255 to 255)
      BrickPi.MotorSpeed[PORT_D] = 200  #Set the speed of MotorA (-255 to 255)
    elif c == '4' :
      print "Turning Right"
      BrickPi.MotorSpeed[PORT_A] = -200  #Set the speed of MotorA (-255 to 255)
      BrickPi.MotorSpeed[PORT_D] = 0  #Set the speed of MotorA (-255 to 255)
    elif c == '6' :
      print "Turning Left"
      BrickPi.MotorSpeed[PORT_A] = 0  #Set the speed of MotorA (-255 to 255)
      BrickPi.MotorSpeed[PORT_D] = -200  #Set the speed of MotorA (-255 to 255)
    elif c == '5' :
      print "Stopped"
      BrickPi.MotorSpeed[PORT_A] = 0
      BrickPi.MotorSpeed[PORT_D] = 0
    BrickPiUpdateValues();                # BrickPi updates the values for the motors
    print "Values Updated"
  def on_close(self):
    print 'connection closed...'
    
application = tornado.web.Application([
  (r'/ws', WSHandler),
  (r'/', MainHandler),
  (r"/(.*)", tornado.web.StaticFileHandler, {"path": "./resources"}),
])


class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print "thread"
        while running:
            BrickPiUpdateValues()       # Ask BrickPi to update values for sensors/motors
            time.sleep(.2)              # sleep for 200 ms

if __name__ == "__main__":
  BrickPiSetup()  # setup the serial port for communication
  BrickPi.MotorEnable[PORT_A] = 1 #Enable the Motor A
  BrickPi.MotorEnable[PORT_D] = 1 #Enable the Motor D
  BrickPiSetupSensors()   #Send the properties of sensors to BrickPi
  running = True
  thread1 = myThread(1, "Thread-1", 1)
  thread1.setDaemon(True)
  thread1.start()  
  application.listen(9093)          #starts the websockets connection
  tornado.ioloop.IOLoop.instance().start()
  

