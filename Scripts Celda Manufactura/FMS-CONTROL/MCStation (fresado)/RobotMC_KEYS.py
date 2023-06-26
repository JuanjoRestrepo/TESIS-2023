# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 11:09:55 2018

@author: cap
"""
import RVM1
import time


#r = Robot.execute(port ='/dev/ttyUSB0')
#rn = Robot.program(port="/dev/ttyUSB0")
#


class _RobotMC():
    def __init__(self, SerialPort):
         self.n = 50  #linea inicial comandos
         self.n2 = self.n
         self.m = self.n + 30
         self.m2 = self.m
         self.p = self.m + 30
         self.p2 = self.p
         self.q = self.p + 30
         self.q2 = self.q
         self.r = RVM1.execute(SerialPort)
         self.rn = RVM1.program(SerialPort)
         self.state1 = False
         self.state2 = False
         
         
    def M1(self):
        #llevar la pieza del pallet a la prensa
        p = self.p
        rn = self.rn
        rn.MO(p,550,"O")
        p += 1
        rn.SP(p,8,"H")
        p += 1
        rn.MO(p,551,"O")
        p += 1
        rn.MO(p,552,"O")
        p += 1
        rn.SP(p,4,"H")
        p += 1
        rn.MS(p,553,8,"O")
        p += 1
        rn.GC(p)
        p += 1
        rn.TI(p,2)
        p += 1
        rn.MS(p,552,8,"C")
        p += 1
        rn.SP(p,8,"H")
        p += 1
        rn.MO(p,551,"C")
        p += 1
        rn.MO(p,550,"C")
        p += 1
        rn.MO(p,554,"C")
        p += 1
        rn.MO(p,555,"C")
        p += 1
        rn.MO(p,556,"C")
        p += 1
        rn.MO(p,557,"C")
        p += 1
        rn.SP(p,1,"H")
        p += 1
        rn.MS(p,558,5,"C")
        p += 1
        rn.WH(p)
        p += 1
        rn.GC(p)
        self.p2 = p
        
    def M2(self):
        #salir de la maquina y esperar a que termine de aquinar
        n = self.n
        rn = self.rn
        rn.GO(n)
        n += 1
        rn.TI(n,1)
        n += 1
        rn.SP(n,9,"H")
        n += 1
        rn.MO(n,557,"O")
        n += 1
        rn.MO(n,556,"O")
        n += 1
        rn.MO(n,555,"O")
        n += 1
        rn.MO(n,554,"O")
        n += 1
        rn.MO(n,550,"O")
        n += 1
        rn.WH(n)
        n += 1
        rn.MO(n,550,"O")
        self.n2 = n      
    
        
    def M3(self):
        #entrar a la maquina a sujetar la pieza en la prensa antes de llevarla al pallet
        q = self.q
        rn = self.rn
        rn.SP(q,9,"H")
        q += 1
        rn.MO(q,554,"O")
        q += 1
        rn.MO(q,555,"O")
        q += 1
        rn.MO(q,556,"O")
        q += 1
        rn.MO(q,557,"O")
        q += 1
        rn.SP(q,2,"H")
        q += 1
        rn.MO(q,558,"O")
        q += 1
        rn.GC(q)
        q += 1
        rn.WH(q)
        q += 1
        rn.GC(q)
        self.q2 = q
        
    def M4(self):
        #sacar la pieza de la prensa y llevarla al pallet, despues ir a esperar 
        m = self.m
        rn = self.rn
        rn.MO(m,557,"C")
        m += 1
        rn.SP(m,8,"H")
        m += 1
        rn.MO(m,556,"C")
        m += 1
        rn.MO(m,555,"C")
        m += 1
        rn.MO(m,554,"C")
        m += 1
        rn.MO(m,550,"C")
        m += 1
        rn.MO(m,551,"C")
        m += 1
        rn.MO(m,552,"C")
        m += 1
        rn.SP(m,3,"H")
        m += 1
        rn.MS(m,553,8,"C")
        m += 1
        rn.GO(m)
        m += 1
        rn.SP(m,8,"H")
        m += 1
        rn.MS(m,552,5,"O")
        m += 1
        rn.MO(m,551,"O")
        m += 1
        rn.MO(m,550,"O")
        m += 1
        rn.WH(m)
        m += 1
        rn.MO(m,550,"O")
        self.m2 = m
        
    def runM1(self):
        p = self.p
        p2 = self.p2
        self.r.c.reset_input_buffer()
        if p == p2:
            self.M1()   
        time.sleep(0.5)
        self.r.RN(p,self.p2)
        print("Moviendo Robot")
        waitOK = self.r.c.read(1)
        print("Fin del movimiento del robot")
        
    def runM2(self):
        n = self.n
        n2 = self.n2
        self.r.c.reset_input_buffer()
        if n == n2:
            self.M2()
        time.sleep(0.5)
        self.r.RN(n,self.n2)
        print("Moviendo Robot")
        waitOK = self.r.c.read(1)
        print("Fin del movimiento del robot")
     
    def runM3(self):
        q = self.q
        q2 = self.q2
        self.r.c.reset_input_buffer()
        if q == q2:
            self.M3()
        time.sleep(0.5)
        self.r.RN(q,self.q2)
        print("Moviendo Robot")
        waitOK = self.r.c.read(1)
        print("Fin del movimiento del robot")
        
    def runM4(self):
        m = self.m
        m2 = self.m2
        self.r.c.reset_input_buffer()
        if m == m2:
            self.M4()
        time.sleep(0.5)
        self.r.RN(m,self.m2)
        print("Moviendo Robot")
        waitOK = self.r.c.read(1)
        print("Fin del movimiento del robot")
        
R = _RobotMC('/dev/ttyUSB0')
