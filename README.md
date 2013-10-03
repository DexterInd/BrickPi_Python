BrickPi Python Code
===================

This repository contains drivers and examples for using the BrickPi in Python.

Installation
============

The `BrickPi` module can be installed using the `setup.py` script included in
this repository:

    sudo python setup.py install

This will install the `BrickPi` module globally.  To use the module in your own
Python scripts, just import it:

    import BrickPi

Sensor Examples
===============

Before trying to run any of the scripts in the `Sensor Examples` directory,
make sure you have installed the `BrickPi` module.  In general, you
will need to be `root` to run these scripts.  The easiest way to do
this on most systems is to use the `sudo` command, like this:

    sudo python "Sensor Examples/LEGO-Motor Test.py"

If you want to run the examples without installing the module you can
set your `PYTHONPATH` environment variable like this:

    sudo env PYTHONPATH=$PWD python "Sensor Examples/LEGO-Motor Test.py"

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
