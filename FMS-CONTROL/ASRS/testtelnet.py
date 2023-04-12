# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 17:17:27 2019

@author: Portatil
"""

import telnetlib
import time

IP = '192.168.16.254'
PORT = 8080
s = telnetlib.Telnet(IP, PORT)

MESSAGE1 = "GG\n"
s.write(MESSAGE1.encode())