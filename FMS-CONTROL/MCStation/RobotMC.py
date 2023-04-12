# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 11:09:55 2018

@author: cap
"""
import RVM1
import time



class _RobotMC():

    def __init__(self, SerialPort):
         self.rn = RVM1.program(SerialPort)  #objeto robot para escribir lineas de comandos
         self.r = RVM1.execute(SerialPort)  #objeto robot para ejecutar comandos directamente
         self.n = 160  #linea inicial comandos
         self.m = self.n + 20
         self.p = self.m + 20
         self.q = self.p + 20
         
    def toMC(self):
        #poner la pieza desde el pallet a la prensa
        n= self.n
        rn = self.rn
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
        
    def waitMC(self):
        #salir de cm cuando la prensa sujete la pieza
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
        rn.MO(m,407,"O")        
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
        #tomar la pieza cuando el cnc haya terminado
        p = self.p
        rn = self.rn
        rn.MO(p,404,"O")
        time.sleep(0.5)
        p += 1
        rn.MO(p,407,"O")
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
        #mover la pieza de la presan al pallet
        q = self.q
        rn = self.rn
        rn.MS(q,405,5,"C")
        time.sleep(0.5)
        q += 1
        rn.MS(q,407,5,"C")
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
        rn.TI(q,2)
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
        
    def run_toMC(self):
        n = self.n
        self.r.RN(n,n+15)
        
    def run_waitMC(self):
        m = self.m
        self.r.RN(m,m+7)
     
    def run_pick(self):
        p = self.p
        self.r.RN(p,p+6)
        
    def run_toPallet(self):
        q = self.q
        self.r.RN(q,q+11)