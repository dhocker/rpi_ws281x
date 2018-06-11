#!/bin/bash

echo This script is designed to be run sudo.

# Designed to be run sudo
source /home/pi/Virtualenvs/rpi_ws281x/bin/activate
python strandtest2.py

