# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 16:56:19 2019

@author: Portatil
"""

import RobotMC_KEYS
import time
import serial

"""
###############################################################################
instancia de modulo
###############################################################################
"""

port = serial.Serial(port = "COM3", baudrate=9600, parity="O", bytesize=7, stopbits=2,xonxoff = False)

R = RobotMC_KEYS._RobotMC(port)