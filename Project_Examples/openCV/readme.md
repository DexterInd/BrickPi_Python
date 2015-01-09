Open Computer Vision
======

This project uses OpenCV to process video and images from the Raspberry Pi camera. You can do things like face recognition, object detection and motion tracking. OpenCV was originally created for Stanford's Darpa autonomous vehicle Stanley. It won the grand challenge by completing the course in the shortest time.

Installation
------
Follow these instructions to install OpenCV.
![OpenCV source code](http://sourceforge.net/projects/opencvlibrary/files/opencv-unix/ "")

1. download the source code from sourceforge and save it to your home folder. If you're using the default Raspbian user it will be /home/pi/
2. run install.sh script

This will take 5-6 hours to complete. The script starts by using apt-get to install the required libraries. When prompted by the installer, answer yes. When all the required libraries are done, it will run cmake to configure unix make. Make will compile the code, which takes the bulk of the time. Once make is done, make install will copy the binaries to /usr/local directory. 

How it works
------
To test the installation works correctly, run one of the examples like this:

sudo python opencv_example.py

