#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 10:58:43 2018

@author: root
"""

"""
from osbrain import run_agent
from osbrain import run_nameserver
from osbrain import AgentAddress
"""
import serial
import RobotT
import API_CNC

"""
###############################################################################
instancia de modulo
###############################################################################
"""
t = API_CNC.cnc(port="/dev/ttyS0")
R = RobotT._RobotT(SerialPort = "/dev/ttyUSB0")