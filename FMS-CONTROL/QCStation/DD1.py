# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 10:54:56 2018

@author: cap
"""

import serial
import RobotMC
import time
import API_CNC


"""
###############################################################################
instancia de modulo
###############################################################################
"""
mc = API_CNC.cnc(port="/dev/ttyS0")   #el control de flujo por software no esta funcionando para el ttyUSB0
R = RobotMC._RobotMC(SerialPort = '/dev/ttyUSB0')