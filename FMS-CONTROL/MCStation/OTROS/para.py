# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 08:57:07 2018

@author: cap
"""

import parallel


"""
para abrir y dar aceso al puerto
sudo chmod 666 /dev/parport0
sudo modprobe parport
sudo modprobe parport_pc
"""
#p = parallel.Parallel()

b1= p.getInBusy()#Assembly
b2= p.getInAcknowledge() #lathe
b3 = p.getInPaperOut() #Camera
b4 = p.getInSelected() #MC
b5 = p.getInError() #Fin
print(b1,b2,b3,b4,b5)
inp = p.getData()
print(bin(inp))