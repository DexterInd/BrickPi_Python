This project is an implementation of web socket connection for controlling a robot from a web page

Data is sent from the web page using buttons and Keyboard presses.

The RPi_Server_Code runs on python using tornado, so first install tornado using python package manager pip.

For the sample code and instructions for installing and using tornado on raspberry pi see : http://www.remwebdevelopment.com/blog/python/simple-websocket-server-in-python-144.html

Instructions for running the programs:
	1. Run the server code on raspberry pi
		-->Type "sudo python RPi_Server_Code.py" without quotes.

	2. Open the Browser_Client_Code (on the client compluter, the one from which you want to control the robot) and enter the hostname/ip address(of the Raspberry Pi) on the webpage to set up the socket connection.

	3. Now the  socket connection will set up and a message will be displayed on the terminal "connection opened", which means you are ready to control your robot.

	4. Now you are ready to use the arrow keys and buttons on the web page to control the robot..

	For motors' connection in robot and setup of BrickPi and RaspberryPi open and see the comments in the RPi_Server_Code

Errors and Troubleshooting:
	Don't use Ctrl+Z to stop the program, use Ctrl+c.
	If you use Ctrl+Z, it will not close the socket and you won't be able to run the program the next time.
	If you get the following error:
		"socket.error: [Errno 98] Address already in use "
	Run this on the terminal:
		"sudo netstat -ap |grep :9093"
	Note down the PID of the process running it
	And kill that process using:
		"kill pid"
	If it does not work use:
		"kill -9 pid"
	If the error does not go away, try changin the port number '9093' both in the client and server code