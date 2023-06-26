# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 16:59:14 2017

@author: cap
"""

import Robot
import Robot2
import time
import API_CNC

#r = Robot.robot(port ='/dev/ttyS0')
#rn = Robot2.robot2(port="/dev/ttyS0")
lathe = API_CNC.cnc(port="/dev/ttyS0")
lathe.dnc.reset_input_buffer()
lathe.dnc.reset_output_buffer()
lathe.nc("O0020.NC")

"""
import serial
import time
#sudo chmod 666 /dev/ttyUSB0 

c = serial.Serial('/dev/ttyUSB0', baudrate=2400,xonxoff=1, rtscts=0,stopbits=2,dsrdtr=0,parity="E",bytesize=7,timeout=1) 

f = open('O0020.NC', 'rb')


for i in f:
    c.write(i)
    print(c.readline())

c.close()
"""