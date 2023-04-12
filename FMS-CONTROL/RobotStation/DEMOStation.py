#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 17:44:46 2018

@author: cap
"""

from RobotDemo import _DEMO

R = _DEMO()

def ESCRIBIR():
    R.ESCRIBIR()
    R.rESCRIBIR()
    print("FIN")
    
def PLAY():
    R.PLAY()
    R.rPLAY()
    print("FIN")

def PICK():
    R.PICK()
    R.rPICK()
    print("FIN") 

def Ogripper():
    R.ogripper()

def Cgripper():
    R.cgripper()
    
def Mover(pos):
    R.mover(pos)
    
def NT():
    R.Nest()

def RS():
    R.reset()
   