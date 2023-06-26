#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 17:44:04 2018

@author: controlcap2
"""

import telnetlib
 
TCP_IP = '192.168.200.12'
TCP_PORT = 4000
BUFFER_SIZE = 1024
MESSAGE = "c2p11"+"\n"

s = telnetlib.Telnet(TCP_IP, TCP_PORT)
s.write(MESSAGE.encode())