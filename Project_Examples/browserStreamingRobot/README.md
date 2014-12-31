## Browser streaming bot
### This example is for streaming video and controlling the GoPiGo from a web browser


![Mobile control of the GoPiGo Raspberry Pi Robot](https://raw.githubusercontent.com/DexterInd/GoPiGo/master/Software/Python/Examples/Browser%20Streaming%20Robot/Raspberry_Pi_Camera_controlled-by-mobile-browser.jpg "Control of the GoPiGo Raspberry Pi Robot with a mobile phone.")

![Robot Control and streaming through the browser](https://raw.githubusercontent.com/DexterInd/GoPiGo/master/Software/Python/Examples/Browser%20Streaming%20Robot/Raspberry_Pi_Camera_streaming-to-computer-browser.jpg "Streaming video through the browser of the GoPiGo")

![Controlling the GoPiGo robot with a mobile phone](https://raw.githubusercontent.com/DexterInd/GoPiGo/master/Software/Python/Examples/Browser%20Streaming%20Robot/Raspberry_Pi_Camera_controlled-by-mobile-browser.jpg "Streaming video from your Raspberry Pi Robot to your mobile phone.")



**Usage:**
- Make robot_web_server.py executable

 >      chmod +x brickpi_web_server.py

- Run brickpi_web_server.py
- Open a web browser on any computer or mobile device and enter the following in the address bar:

 >      raspberrypi.local/
 
- The video stream would load up and you can use the joystick on the screen to control the robot
- Note: if you want to change the resolution edit camera_streamer.py so that it has the width height like this self.cameraStreamerProcess = subprocess.Popen( [ "/usr/local/bin/raspberry_pi_camera_streamer","-w 320","-h 240" ] )
