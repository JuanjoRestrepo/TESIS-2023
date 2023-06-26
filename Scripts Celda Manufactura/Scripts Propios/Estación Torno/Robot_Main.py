"""
Modify on Wed May  5 16:24:52 2023

@author: controlcap2

Programa de ejecucion para el manejo de robot 
"""

import Robot_Functions
import time



class Robot_T():

    def __init__(self, SerialPort):
         self.rn = Robot_Functions.program(port = SerialPort)  #objeto robot para escribir lineas de comandos
         self.r = Robot_Functions.execute(port = SerialPort)  #objeto robot para ejecutar comandos directamente
         self.n = 160  #linea inicial comandos
         self.m = self.n + 20
         self.p = self.m + 20
         self.q = self.p + 20
         
    
    def toT(self):
        rn = self.rn
        n= self.n
        rn.MO(n,400,"O")        
        time.sleep(0.5)
        n += 1
        rn.SP(n,8,"H")        
        time.sleep(0.5)
        n += 1
        rn.MO(n,401,"O")
        time.sleep(0.5)
        n += 1
        rn.SP(n,5,"H")        
        time.sleep(0.5)
        n += 1
        rn.MO(n,402,"O")
        time.sleep(0.5)
        n += 1
        rn.GC(n)
        time.sleep(0.5)
        n += 1
        rn.TI(n,5)
        time.sleep(0.5)
        n += 1
        rn.MS(n,403,5,"C")
        time.sleep(0.5)
        n += 1
        rn.SP(n,8,"H")        
        time.sleep(0.5)
        n += 1
        rn.MO(n,400,"C")
        time.sleep(0.5)
        n += 1
        rn.MO(n,404,"C")
        time.sleep(0.5)
        n += 1
        rn.MO(n,405,"C")
        time.sleep(0.5)
        n += 1
        rn.SP(n,4,"H")        
        time.sleep(0.5)
        n += 1
        rn.MO(n,406,"C")
        time.sleep(0.5)
        n += 1
        rn.WH(n)
        print(n)
        
    def waitT(self):
        m= self.m
        rn = self.rn
        rn.SP(m,8,"H")        
        time.sleep(0.5)
        m += 1
        rn.GO(m)        
        time.sleep(0.5)
        m += 1        
        rn.MO(m,405,"O")        
        time.sleep(0.5)
        m += 1
        rn.MO(m,404,"O")
        time.sleep(0.5)
        m += 1
        rn.MO(m,400,"O")
        time.sleep(0.5)
        m += 1
        rn.WH(m)
        print(m)
        
    def pick(self):
        p = self.p
        rn = self.rn
        rn.MO(p,404,"O")
        time.sleep(0.5)
        p += 1
        rn.MO(p,405,"O")
        time.sleep(0.5)
        p += 1
        rn.MO(p,406,"O")
        time.sleep(0.5)
        p += 1
        rn.GC(p)
        time.sleep(0.5)
        p += 1
        rn.WH(p)
        print(p)
        
    def toPallet(self):
        q = self.q
        rn = self.rn
        rn.MS(q,405,5,"C")
        time.sleep(0.5)
        q += 1
        rn.MO(q,404,"C")
        time.sleep(0.5)
        q += 1
        rn.MO(q,400,"C")
        time.sleep(0.5)
        q += 1
        rn.MO(q,403,"C")
        time.sleep(0.5)
        q += 1
        rn.MS(q,402,8,"C")
        time.sleep(0.5)
        q += 1
        rn.GO(q)
        time.sleep(0.5)
        q += 1
        rn.TI(q,3)
        time.sleep(0.5)
        q += 1
        rn.MO(q,401,"O")
        time.sleep(0.5)
        q += 1
        rn.MO(q,400,"C")
        time.sleep(0.5)
        q += 1
        rn.WH(q)
        print(q)
        
    def run_toT(self):
        n = self.n
        self.r.RN(n,n+15)
        
    def run_waitT(self):
        m = self.m
        self.r.RN(m,m+6)
        
    def run_pick(self):
        p = self.p
        self.r.RN(p,p+5)
        
    def run_toPallet(self):
        q = self.q
        self.r.RN(q,q+10) 