#!/usr/bin/env python
# All credit to Antonvh:  https://gist.github.com/antonvh/c81c247fc03029a1ba6a
# View his work here:  https://github.com/antonvh
##
#
# See more about the BrickPi here:  http://www.dexterindustries.com/BrickPi
#
# These files have been made available online through a Creative Commons Attribution-ShareAlike 3.0  license.
# (http://creativecommons.org/licenses/by-sa/3.0/)

import smbus

def get_voltage():
    """
    Reads the digital output code of the MCP3021 chip on the BrickPi+ over i2c.
    Some bit operation magic to get a voltage floating number.

    If this doesnt work try this on the command line: i2cdetect -y 1
    The 1 in there is the bus number, same as in bus = smbus.SMBus(1)
    Google the resulting error.

    :return: voltage (float)
    """

    # time.sleep(0.1) # Necessary?
    try:
            bus = smbus.SMBus(1)            # SMBUS 1 because we're using greater than V1.
            address = 0x48
            # read data from i2c bus. the 0 command is mandatory for the protocol but not used in this chip.
            data = bus.read_word_data(address, 0)

            # invert first and last bytes to obtain tension
            last_byte = data & 0xFF
            first_byte = data >> 8
            tension = (last_byte << 8) | first_byte

            # convert tension (units seems te be in 0.025/5.5 V or 1/220 V) into Volts
            units_per_volt = 220.0
            voltage = tension / units_per_volt

            return voltage

    except:
            return False
            
if __name__ == "__main__":
    print get_voltage()
