# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 16:23:17 2018

@author: cap
"""
n = 400
r.PD(n,+4.6,+169.9,+371.4,-88.9,+93.6)   #descanso en espera de ordenes
time.sleep(0.5)
r.PD(n+1,424.4,2.3,358.9,+1.2,183.4)  #antes de agarrar pieza del pallet
time.sleep(0.5)
r.PD(n+2,526.7,0.1,227.4,1.2,183.1)  #posicion de agarrar la pieza en el palet
time.sleep(0.5)
r.PD(n+3,526.7,0.1,325.0,1.2,183.1)  #posicion despues de agarrar la pieza en el palet
time.sleep(0.5)
r.PD(n+4,-218.9,264.6,541.5,-1.1,184.7) #antes de entrar al cm
time.sleep(0.5)
r.PD(n+5,-505.3,-50.8,+510.3,-1.1,+184.7) #dentro del cm
time.sleep(0.5)
r.PD(n+6,-503.7,-52.5,471.7,-1.3,183.3)  #prensa