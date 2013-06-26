This project is an implementation of web socket connection for controlling a robot from a web page

Data is sent from the web page using buttons and Keyboard presses.

The RPi_Server_Code runs on python and tornado, so first install tornado using python package manager pip.

For the sample code and insructions for installing tornado on raspberry pi see : http://www.remwebdevelopment.com/blog/python/simple-websocket-server-in-python-144.html


Instructions for running the programs:

1.)Open the LX Terminal on your RaspberryPi and run the server_code code(python).For instructions on how to run the code see below.

2.)Type the following commands on LX Terminal.

3.)    -->Type "cd Desktop" without quotes   (If your RPi_Server_Code code is not saved in Desktop, type the name of the folder in which it is saved instead of           Desktop).
       -->Type "ls" without quotes to check for the files in Desktop(or the corresponding folder)
       -->Type "sudo python RPi_Server_Code.py" without quotes.

4.)Open the Browser_Client_Code and enter the hostname/ip address on the webpage to set up the web socket connection .

5.)Now the web socket connection will be set up and a message will be displayed on the LX terminal saying "connection opened".

6.)Now you are ready to use the arrow keys and buttons on the web page to control the robot..

For motors' connection in robot and setup of BrickPi and RaspberryPi open and see the comments in the RPi_Server_Code

Errors and Troubleshooting:

" socket.error: [Errno 98] Address already in use "

In case this error appears open both the codes and look for the port numbers in both of them. 
It will be 9093, now change both of them to something else(eg:9094)