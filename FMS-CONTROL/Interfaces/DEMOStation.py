#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 17:44:46 2018

@author: cap
"""

from RobotDemo import _DEMO



class FUNCIONS:
    
    def __init__(self, SerialPort):
        self.SerialPort= SerialPort
        self.R = _DEMO(self.SerialPort)
        
    def ESCRIBIR(self,P):
        R = self.R
        R.ESCRIBIR(P)
        R.rESCRIBIR()
        print("FIN")
        
    def PLAY(self):
        R = self.R
        R.PLAY()
        R.rPLAY()
        print("FIN")
    
    def PICK(self):
        R = self.R
        R.PICK()
        R.rPICK()
        print("FIN")  
#ESCRIBIR()
#PLAY()    