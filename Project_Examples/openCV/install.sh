#! /bin/bash

sudo apt-get install build-essential
sudo apt-get install python-dev python-numpy
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev
sudo apt-get install libjpeg-dev libpng-dev libtiff-dev libjasper-dev
sudo apt-get install python-scipy python-matplotlib libgtk2.0-dev
sudo git clone git://github.com/Itseez/opencv.git

cd opencv
sudo mkdir release
cd release
cmake -D CMAKE_BUILD_TYPE=RELEASE -D WITH_OPENCL=OFF -D CMAKE_INSTALL_PREFIX=/usr/local ..
sudo make
sudo make install

