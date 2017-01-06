BrickPi Python Code
===================

This repository contains drivers and examples for using the BrickPi in Python.

These files have been made available online through a [Creative Commons Attribution-ShareAlike 3.0](http://creativecommons.org/licenses/by-sa/3.0/) license.

Installation
============

First, open a terminal program on the Raspberry Pi, and change directories to the location (directory) where you wish to clone the BrickPi_Python.
Follow the following steps to install the BrickPi_Python Module on a Raspbian Jessie Image.
 
1. Run `sudo apt-get update`
2. Run `sudo apt-get upgrade -y`
3. Edit the boot config with
  * `sudo nano /boot/config.txt`
  * Add "dtoverlay=pi3-disable-bt" to the end of the file
  * Save the file
  * Run `sudo systemctl disable hciuart` to prevent BT modem from attempting to use UART
  * Reboot raspberry pi `sudo reboot`
4. Run `sudo git clone http://www.github.com/DexterInd/BrickPi.git`
5. Run `cd BrickPi/Setup\ Files`
6. Run `sudo bash install.sh`
7. Reboot raspberry pi `sudo reboot`
8. `cd Sensor Examples`
and try running an example.

To use the module in your own Python scripts, just import it:

    `import BrickPi`

Sensor Examples
===============

Before trying to run any of the scripts in the `Sensor Examples` directory,
make sure you have installed the `BrickPi` module.  In general, you
will need to be `root` to run these scripts.  The easiest way to do
this on most systems is to use the `sudo` command, like this:

    sudo python "Sensor_Examples/LEGO-Motor Test.py"

If you want to run the examples without installing the module you can
set your `PYTHONPATH` environment variable like this:

    sudo env PYTHONPATH=$PWD python "Sensor_Examples/LEGO-Motor Test.py"

Reinstall or Uninstall BrickPi.py
========

To update or Reinstall BrickPi.py, you must uninstall the BrickPi module first, then reinstall the BrickPi module.

To uninstall the BrickPi module, open a terminal in the BrickPi_Python directory and run the following:

	sudo python setup.py install --record files.txt
	cat files.txt | xargs sudo rm -rf

This should uninstall the BrickPi modules from Python.  To install an updated BrickPi.py module, see "Installation" above.
		
	
See Also
========

More information on BrickPi and Python is found on our website:
<http://www.dexterindustries.com/BrickPi/program-it/python/>

BrickPi is a Raspberry Pi Board that connects [LEGO MINDSTORMS][]
motors and sensors to the [Raspberry Pi][].

More information on hardware, firmware, and software can be found
here:  <http://www.dexterindustries.com/BrickPi>

[lego mindstorms]: http://mindstorms.lego.com/
[raspberry pi]: http://www.raspberrypi.org/
