# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 07:40:02 2018

@author: cap
"""

#posicion 1 -297.7,+427.8,+207.3,+.2,+185.5
#sudo chmod 666 /dev/ttyS0 

import RVM1

import time


e = RVM1.execute(port="/dev/ttyS0")
p = RVM1.program(port="/dev/ttyS0")


