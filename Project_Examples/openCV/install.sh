#! /bin/bash
# note you need to manually download opencv 2.4.10 from sourceforge here http://sourceforge.net/projects/opencvlibrary/files/opencv-unix/2.4.10/opencv-2.4.10.zip/download

sudo apt-get install build-essential
sudo apt-get install python-dev python-numpy
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev
sudo apt-get install libjpeg-dev libpng-dev libtiff-dev libjasper-dev
sudo apt-get install python-scipy python-matplotlib libgtk2.0-dev

sudo unzip opencv*
sudo cd opencv*
sudo mkdir release
cd release
cmake -D CMAKE_BUILD_TYPE=RELEASE -D WITH_OPENCL=OFF -D BUILD_PERF_TESTS=OFF -D CMAKE_INSTALL_PREFIX=/usr/local ..
sudo make
sudo make install

