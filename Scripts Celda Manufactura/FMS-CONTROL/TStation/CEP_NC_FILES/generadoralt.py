# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 15:56:58 2018

@author: juandavid.contreras

Programa de generacion aleatoria de vectores para la practica de control
estadistico de procesos

Total piezas: 120
piezas defectuosas: 45
piezas por lote: 30
numero de lotes: 4
tipo 0  = 12-19,30
suma 30
tipo 1 = 12.5-19.5
tipo 2 = 11.5-18.5
suma 55
tipo 3 = 12.7-19.7
tipo 4 = 11.3-18.3
suma 15
tipo 5 = 13-20
tipo 6 = 11-18
suma 15
tipo 7 = 13.5-20.5
tipo 8 = 10.5-17.5
suma 10
tipo 9 = 14-21
tipo 10 = 10-17
suma5
"""

from random import randint,sample

N = 30 #numero de piezas por lote
L = 4 #numero de lotes
#V = np.zeros((L,N),dtype=int)  #matriz de orden de piezas
#T = np.array([[30,0],[25,0],[30,0],[8,0],[7,0],[7,0],[8,0],[5,0],[5,0],[2,0],[3,0]])
t0 = 30
t1 = randint(2,45)
t2 = 45-t1
t3 = randint(2,15)
t4 = 15 - t3
t5 = randint(2,15)
t6 = 15 - t5
t7 = randint(1,10)
t8 = 10 - t7
t9 = randint(1,5)
t10 = 5 - t9
T = t0*[0]+t1*[1]+t2*[2]+t3*[3]+t4*[4]+t5*[6]+t6*[6]+t7*[7]+t8*[8]+t9*[9]+t10*[10]
for i in range(2):
    T = sample(T,len(T))

T1 = T[0:N]
T2 = T[N:2*N]
T3 = T[2*N:3*N]
T4 = T[3*N:4*N]