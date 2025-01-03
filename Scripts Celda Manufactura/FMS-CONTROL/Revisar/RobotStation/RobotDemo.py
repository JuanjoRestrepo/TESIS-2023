# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 11:09:55 2018

@author: cap
"""
from RVM1 import execute, program
import time


#r = Robot.execute(port ='/dev/ttyUSB0')
#rn = Robot.program(port="/dev/ttyUSB0")

"""
posiciones:
PD(400,-155.8,-53.3,+360.9,-87.4,.0) #espera
PD(401,-287.2,-390.4,+137.4,-1.4,.0) #arriba del pallet 
PD(402,-287.2,-390.4,+64.2,-1.4,.0) #pieza en pallet 
PD(403,+4.2,+164.6,+360.9,-87.4,.0) #Antes de poner en la mesa 
PD(404,.0,+468.9,+50.2,-1.7,.0) #en la mesa 
"""
class _DEMO():

    def __init__(self, SerialPort='/dev/ttyS0'):
         self.n = 10  #linea inicial comandos
         self.n2 = self.n
         self.m = self.n + 200
         self.m2 = self.m
         self.p = self.m + 150
         self.p2 = self.p
         self.r = execute(port = SerialPort)
         self.rn = program(port = SerialPort)
    def PICK(self):
        #mover la pieza del pallet a la mesa
        p= self.p
        rn = self.rn
        rn.MO(p,550,"O")        
        
        p += 1
        rn.SP(p,8,"H")        
        
        p += 1
        rn.MO(p,551,"O")
        
        p += 1
        rn.SP(p,5,"H")        
        
        p += 1
        rn.MO(p,552,"O")
        
        p += 1
        rn.GC(p)
        
        p += 1
        rn.TI(p,5)
        
        p += 1
        rn.MS(p,551,10,"C")
        
        p += 1
        rn.SP(p,8,"H")        
        
        p += 1
        rn.MO(p,550,"C")
        
        p += 1
        rn.MO(p,553,"C")
        
        p += 1
        rn.SP(p,7,"H")        
       
        p += 1
        rn.MO(p,554,"C")
       
        p += 1
        rn.GO(p)
      
        p += 1
        rn.TI(p,5)
        
        p += 1
        rn.SP(p,9,"H")        
       
        p += 1
        rn.MO(p,553,"O")
        
        p += 1
        rn.MO(p,550,"O")
        
        p += 1
        rn.MO(p,550,"O")
        self.p2 = p
        print(p)
        
    def le(self,Le,Cu,n):
        #programar movimiento para las letras
        rn = self.rn
        rn.MA(n,Cu+Le[0],263,"C")
        n=n+1
        for i in Le:
            rn.MS(n,Cu+i,20,"C")
            n=n+1
        rn.MA(n,Cu+i,263,"C")
        n=n+1
        return n 
    
    def PICK_PUT(self,t1,b1,t2,b2,p0,m):
        #movimiento 1
        rn = self.rn
        rn.MO(m,t1,"O")        
        m += 1
        rn.MO(m,b1,"O")        
        m += 1
        rn.GC(m)        
        m += 1 
        rn.TI(m,10)
        m=m+1
        rn.MS(m,t1,5,"C")
        m=m+1
        rn.MO(m,p0,"C")        
        m += 1
        rn.MO(m,t2,"C")        
        m += 1
        rn.MS(m,b2,5,"C")
        m=m+1
        rn.GO(m)        
        m += 1 
        rn.TI(m,5)
        m=m+1
        rn.MO(m,t2,"O")        
        m += 1
        rn.MO(m,p0,"O")        
        m += 1
        return m
        #movimiento 2
    def ESCRIBIR(self):
        #mover la pieza del pallet a la mesa
        rn = self.rn
        n = self.n
        le = self.le
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
        
        PALABRA = (J,A,V,E,R,I,A,N,A)
        
        Cuadrante = (301,321,341,361,381,401,421,441,461,481)
        
        rn.SP(n,5,"H")
        n=n+1
        rn.MO(n,100,"O")
        n=n+1
        rn.MO(n,260,"O")
        n=n+1
        rn.MO(n,261,"O") 
        n=n+1
        rn.GC(n)
        n=n+1
        rn.TI(n,10)
        n=n+1
        rn.MO(n,260,"C")
        n=n+1
        rn.SP(n,9,"H")
        n=n+1
        rn.MO(n,262,"C")
        n=n+1
        m=0
        for j in PALABRA:
            n=le(j,Cuadrante[m],n)
            m=m+1
            
        rn.MO(n,260,"C")
        n=n+1
        rn.MO(n,261,"C")
        n=n+1
        rn.GO(n)
        n=n+1
        rn.TI(n,10)
        n=n+1
        rn.MO(n,260,"O")
        n=n+1
        rn.MO(n,100,"O")
        n=n+1
        rn.MO(n,100,"O")
        self.n2 = n
        return n
    
    def PLAY(self):
        m= self.m
        rn = self.rn
        move = self.PICK_PUT
        p0 = 50
        p1t = 51
        p1b = 52
        p2t = 53
        p2b = 54
        p3t = 55
        p3b = 56
        p4t = 57
        p4b = 58
        rn.MO(m,p0,"O") 
        m += 1 
        rn.SP(m,9,"H")            
        m += 1
        #movimiento 1
        m = move(p3t,p3b,p1t,p1b,p0,m)
        #movimiento 2
        m = move(p3t,p3b,p2t,p2b,p0,m)
        #movimiento 3
        m = move(p4t,p4b,p2t,p2b,p0,m)
        #movimiento 4
        m = move(p1t,p1b,p3t,p3b,p0,m)
        #movimiento 5
        m = move(p4t,p4b,p1t,p1b,p0,m)
        #movimiento 6
        m = move(p3t,p3b,p1t,p1b,p0,m)
        #movimiento 7
        m = move(p2t,p2b,p4t,p4b,p0,m)
        #movimiento 8
        m = move(p2t,p2b,p3t,p3b,p0,m)
        #movimiento 9
        m = move(p1t,p1b,p3t,p3b,p0,m)
        #movimiento 10
        m = move(p4t,p4b,p2t,p2b,p0,m)
        #movimiento 11
        m = move(p1t,p1b,p4t,p4b,p0,m)
        #movimiento 12
        m = move(p2t,p2b,p4t,p4b,p0,m)
        rn.MO(m,100,"O")
        m += 1
        rn.MO(m,100,"O")
        self.m2 = m
   
    def rESCRIBIR(self):
        n = self.n
        n2 = self.n2
        self.r.RN(n,n2)
    def rPLAY(self):
        m = self.m
        m2 = self.m2
        self.r.RN(m,m2)
    
    def rPICK(self):
        p = self.p
        p2 = self.p2
        self.r.RN(p,p2)
        
    def ogripper(self):
        self.r.GO()
    
    def cgripper(self):
        self.r.GC()
        
    def mover(self,pos):
        self.r.GC(pos,"O")
        
    def Nest(self):
        self.r.NT()
    
    def reset(self):
        self.r.RS()
