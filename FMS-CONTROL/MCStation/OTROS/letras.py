#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 15:16:36 2017

@author: cap
"""
#sudo chmod 666 /dev/ttyS0 
import RVM1
import time


rvi = RVM1.execute(port="/dev/ttyS0")
rv = RVM1.program(port="/dev/ttyS0")


A = (10,1,12,7,5)
B = (10,0,2,3,6,4,8,12,10)
C = (12,10,0,2)
D = (10,0,1,3,9,11,10)
E = (12,10,4,8,4,0,2)
F = (10,4,8,4,0,2)
G = (2,0,10,12,8,6)
H = (10,0,4,8,12,2)
I = (10,12,11,1,0,2)
J = (10,12,2)
K = (10,12,4,2,4,12)
L = (0,10,12)
M = (10,0,6,2,12)
N = (10,0,12,2)
O = (10,0,2,12,10)
P = (10,0,2,8,4)
Q = (12,10,0,2,12,6)
R = (10,0,2,8,4,12)
S = (10,12,8,4,0,2)
T = (11,1,0,2)
U = (0,10,12,2)
V = (0,11,2)
W = (0,10,6,12,2)
Z = (0,2,10,12)
X = (10,2,6,0,12)
Y = (10,2,6,0)

PALABRA = (M,U,R,C,I,E,L,A,G,O)

Cuadrante = (301,321,341,361,381,401,421,441,461,481)
def le(Le,Cu,n):
    rv.MA(n,Cu+Le[0],263,"C")
    n=n+1
    for i in Le:
        rv.MS(n,Cu+i,20,"C")
        n=n+1
    rv.MA(n,Cu+i,263,"C")
    n=n+1
    return n  
n = 10
rvi.SP(9,"H")
rvi.MO(100,"O")
time.sleep(5)
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
for j in PALABRA:
    n=le(j,Cuadrante[m],n)
    m=m+1
    
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
