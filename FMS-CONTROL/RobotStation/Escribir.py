#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 15:16:36 2017

@author: cap
"""
#sudo chmod 666 /dev/ttyS0 
import RVM1
import time


e = RVM1.execute(port="/dev/ttyUSB0")
p = RVM1.program(port="/dev/ttyUSB0")

n = 10
rvi.SP(9,"H")
rvi.MO(100,"O")
time.sleep(1)
#rv.NT(n)
n=n+1
rv.MO(n,260,"O")
n=n+1
rv.MO(n,261,"O") 
n=n+1
rv.GC(n)
n=n+1
rv.TI(n,10)
n=n+1
rv.MO(n,260,"C")
n=n+1
rv.MO(n,262,"C")
n=n+1
m=0
    
rv.MO(n,260,"C")
n=n+1
rv.MO(n,261,"C")
n=n+1
rv.GO(n)
n=n+1
rv.TI(n,10)
n=n+1
rv.MO(n,260,"O")
n=n+1
rv.MO(n,100,"O")

rvi.RN(11,n+1)

"""
rv.PD(260,-230.0,410.0,400.0,0,179.9)
rv.PD(261,-230.0,410.0,150.0,0,179.9)
rv.PD(262,-230.0,410.0,400.0,0,0)
rv.RS()
"""
