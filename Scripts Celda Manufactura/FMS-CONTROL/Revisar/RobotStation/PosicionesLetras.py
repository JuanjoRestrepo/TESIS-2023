#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 16:24:21 2017

@author: cap
"""
import RVM1

#sudo chmod 666 /dev/ttyS0 
rvi = RVM1.execute(port="/dev/ttyS0")
import time

x1=-250.0
x2 = x1+50
x3 = x2+50
x4 = x3+50
x5 = x4+50
x6 = x5+50
x7 = x6+50
x8 = x7+50
x9 = x8+50
x10 = x9+50
y1=505.0
z=185.0 +15 #-250.0,+505.0,+195.0,.0,.0'
def Points(x,y,z,Pos):
    rvi.PD(Pos,x,y,z,0,0)
    time.sleep(1)
    rvi.PD(Pos+1,x+20.0,y,z,0,0)
    time.sleep(1)
    rvi.PD(Pos+2,x+40.0,y,z,0,0)
    time.sleep(1)
    rvi.PD(Pos+3,x+40.0,y-20.0,z,0,0)
    time.sleep(1)
    rvi.PD(Pos+4,x,y-40.0,z,0,0)
    time.sleep(1)
    rvi.PD(Pos+5,x+10.0,y-40.0,z,0,0)
    time.sleep(1)
    rvi.PD(Pos+6,x+20.0,y-40.0,z,0,0)
    time.sleep(1)
    rvi.PD(Pos+7,x+30.0,y-40.0,z,0,0)
    time.sleep(1)
    rvi.PD(Pos+8,x+40.0,y-40.0,z,0,0)
    time.sleep(1)
    rvi.PD(Pos+9,x+40.0,y-60.0,z,0,0)
    time.sleep(1)
    rvi.PD(Pos+10,x,y-80.0,z,0,0)
    time.sleep(1)
    rvi.PD(Pos+11,x+20.0,y-80.0,z,0,0)
    time.sleep(1)
    rvi.PD(Pos+12,x+40.0,y-80.0,z,0,0)
    time.sleep(1)
rvi.PD(263,0,0,20.0,0,0)
time.sleep(1)
rvi.PD(260,-230.0,410.0,400.0,0,179.9)
time.sleep(1)
rvi.PD(261,-230.0,410.0,137.0,0,179.9) #-230.0,+410.0,+137.0,.0,+179.9'
time.sleep(1)
rvi.PD(262,-230.0,410.0,400.0,0,0)
time.sleep(1)
Points(x1,y1,z,301)
Points(x2,y1,z,321)
Points(x3,y1,z,341)
Points(x4,y1,z,361)
Points(x5,y1,z,381)
Points(x6,y1,z,401)
Points(x7,y1,z,421)
Points(x8,y1,z,441)
Points(x9,y1,z,461)
Points(x10,y1,z,481)
