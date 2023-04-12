# -*- coding: utf-8 -*-

"""
Created on Wed Mar  7 22:46:40 2018
@author: cap
"""
from CVDimension import InspectionModule
from opcua import ua
from SaveData import SaveData

import time

IM = InspectionModule()
SD = SaveData()

def QCM(QCEvent):
    time.sleep(1)
    print("Midiendo")
    M2 = 0
    M3 = 0
    m2, m3 = IM.measurePic(m1=22,fm2=1.0067,fm3=1.020,h1=1,g1=0.25,h2=0.65,g2=0.40,h3=0.27,g3=0.32,h4=0.01,g4=0.17)
        
    M3 = round(m3,1)
    M2 = round(m2,1)
    print(M2,M3)
    print("guardando medidas")
    SD.RecordData(M2,M3)
    SD.SaveFile()

    print("evento: ", QCEvent)
    QCEvent.event.Message = ua.LocalizedText("OK")
    QCEvent.event.State = 3
    QCEvent.trigger()
    print("Trigget")

def QCM2(f2,f3,N):
    time.sleep(1)
    print("Midiendo")
    #N = 40
    M2 = 0
    M3 = 0
    for i in range(N):
        m2, m3 = IM.measurePic(m1=22,fm2=f2,fm3=f3,h1=1,g1=0.25,h2=0.65,g2=0.40,h3=0.27,g3=0.32,h4=0.01,g4=0.17)
        M2 = M2 + m2
        M3 = M3 + m3
    M3 = round(M3/N,3)
    M2 = round(M2/N,3)
            
    print(M2,M3)
    

#QCM2(1.002805,0.99,10) para el patron
#QCM2(0.995,0.98,10)  para la 10