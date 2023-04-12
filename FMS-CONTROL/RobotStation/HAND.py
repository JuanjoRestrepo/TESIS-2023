# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 16:34:29 2018

@author: cap
"""

import RVM1
import time
from POS import pos
import numpy as np 

rvi = RVM1.execute(port="/dev/ttyUSB0")
rv = RVM1.program(port="/dev/ttyUSB0")
rv.WH(351)
time.sleep(0.5)
rvi.SP(8,"H")
def calc(x,y):
    R = np.sqrt(x**2 + y**2)
    ff = 100
    d1 = 425+ff
    d2 = 589 + ff
    an = np.arctan(y/x)
    if R > d1 and R < d2 :
        xr= (R-100)*np.cos(an)
        yr = (R-100)*np.sin(an)
    elif R > d2:
        xr = (580)*np.cos(an)
        yr = (580)*np.sin(an)
    else:
        xr = (430)*np.cos(an)
        yr = (430)*np.sin(an)
    return int(xr),int(yr)
def mov(xr,yr):
    rvi.PD(110,xr,yr,300,0,0)
    time.sleep(0.2)
    rv.MO(350,110,"O")
    time.sleep(0.2)
    rvi.RN(350,351)

   
#(xm,ym) = pos()

xm= 0.1
ym= 500
(xr,yr) = calc(xm,ym)
mov(xr,yr)
#rvi.read()

    
