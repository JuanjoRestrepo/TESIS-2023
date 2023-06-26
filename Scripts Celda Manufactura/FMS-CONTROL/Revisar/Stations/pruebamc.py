# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 14:45:10 2018

@author: cap
"""

import Robot
import time
import API_CNC

r = Robot.execute(port ='/dev/ttyUSB0')
rn = Robot.program(port="/dev/ttyUSB0")
lathe = API_CNC.cnc(port="/dev/ttyS0")   #el control de flujo por software no esta funcionando para el ttyUSB0
lathe.nc("COLA.NC")

def m():
    #montar pieza al torno
    n = 160
    r.RN(n,n+14)
        
def w():
    #dejar pieza y esperar 
    m = 180
    r.RN(m,m+6)
        
def u():
    #ir por la pieza al torno
    p = 200
    r.RN(p,p+5)
        
def p():
    #llevar la pieza del torno al pallet
    q = 220
    r.RN(q,q+9) 