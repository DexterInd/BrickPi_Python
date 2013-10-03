#!/usr/bin/python

import setuptools

setuptools.setup(
	name="BrickPi",
	description="Drivers and examples for using the BrickPi in Python",
	author="Dexter Industries",
	url="http://www.dexterindustries.com/BrickPi/",
	py_modules=['BrickPi'],
	install_requires=open('requirements.txt').readlines(),
)
