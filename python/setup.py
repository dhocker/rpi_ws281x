# Python wrapper for the rpi_ws281x library.
# Author: Tony DiCola (tony@tonydicola.com)
from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages, Extension

setup(name              = 'rpi_ws281x',
      version           = '1.1.0',
      author            = 'Jeremy Garff',
      author_email      = 'jer@jers.net',
      maintainer        = 'Dave Hocker',
      maintainer_email  = 'athomex10@gmail.com',
      description       = 'Userspace Raspberry Pi PWM library for WS281X LEDs.',
      long_description  = 'This is a fork of the original rpi_ws281x repo',
      license           = 'MIT',
      url               = 'https://github.com/dhocker/rpi_ws281x/',
      py_modules        = ['neopixel'],
      ext_modules       = [Extension('_rpi_ws281x', 
                                     sources=['rpi_ws281x.i'],
                                     library_dirs=['../.'],
                                     libraries=['ws2811', 'rt'])])
