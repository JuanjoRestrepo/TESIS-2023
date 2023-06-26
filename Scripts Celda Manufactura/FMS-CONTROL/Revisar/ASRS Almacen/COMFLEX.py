# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 15:20:04 2019

@author: Portatil
"""

import time

import serial


c = serial.Serial(port = "COM3", baudrate=9600, parity="N", bytesize=8, stopbits=1,xonxoff = False, timeout=0.5)

def hello():
    c.write(b"A0\r\n")
    r = c.readlines()

    for i in r:
        r1 = r[1].decode('ascii')
        print(r1)
def tx(s):
    #codificar string y mandar por puerto serial
    data = str.encode(s)+b"\r\n"
    c.write(data)
    #print(data)
    time.sleep(0.2)
    r = c.readlines()

    for i in r:
        r1 = r[1].decode('ascii')
        print(r1)
