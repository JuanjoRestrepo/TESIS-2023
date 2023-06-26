# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import Robot
import time
import API_CNC

r = Robot.execute(port ='/dev/ttyUSB0')
rn = Robot.program(port="/dev/ttyUSB0")
lathe = API_CNC.cnc(port="/dev/ttyS0")   #el control de flujo por software no esta funcionando para el ttyUSB0