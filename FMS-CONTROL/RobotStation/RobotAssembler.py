# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 11:09:55 2018

@author: cap
"""
from RVM1 import execute, program
import time


class _RobotAssembler():

    def __init__(self, SerialPort):
         self.n = 160  #linea inicial comandos
         self.n2 = self.n
         self.m = self.n + 30
         self.m2 = self.m
         self.p = self.m + 20
         self.q = self.p + 20
         self.r = execute(SerialPort)
         self.rn = program(SerialPort)
         
    def PICK(self):
        #mover la pieza del pallet a la mesa
        n= self.n
        rn = self.rn
        rn.MO(n,550,"O") 
        
        n += 1
        rn.SP(n,8,"H")        
      
        n += 1
        rn.MO(n,551,"O")

        n += 1
        rn.SP(n,5,"H")        
  
        n += 1
        rn.MS(n,552,10,"O")

        n += 1
        rn.GC(n)

        n += 1
        rn.TI(n,5)
  
        n += 1
        rn.MS(n,551,10,"C")

        n += 1
        rn.SP(n,8,"H")        

        n += 1
        rn.MO(n,550,"C")
   
        n += 1
        rn.MO(n,553,"C")
        
        n += 1
        rn.MO(n,554,"C")

        n += 1
        rn.SP(n,5,"H")        

        n += 1
        rn.MO(n,555,"C")
        
        n += 1
        rn.GO(n)
   
        n += 1
        rn.TI(n,2)
     
        n += 1
        rn.SP(n,9,"H")        
   
        n += 1
        rn.MO(n,556,"O")

        n += 1
        rn.MO(n,550,"O")
        
        n += 1
        rn.WH(n)
        
        n += 1
        rn.RS(n)
        
        self.n2 = n
        print(n)
    
    def PUT(self):
        #mover la pieza al pallet
        m= self.m
        rn = self.rn
        
        rn.MO(m,550,"O") 
        
        m += 1
        rn.SP(m,6,"H")        
      
        m += 1
        rn.MO(m,556,"O")

        m += 1
        rn.SP(m,5,"H")        
  
        m += 1
        rn.MS(m,555,5,"O")

        m += 1
        rn.GC(m)

        m += 1
        rn.TI(m,5)
  
        m += 1
        rn.MO(m,556,"C")

        m += 1
        rn.SP(m,8,"H")        

        m += 1
        rn.MO(m,550,"C")
   
        m += 1
        rn.MO(m,551,"C")
        
        m += 1
        rn.SP(m,4,"H")
        
        m += 1
        rn.MS(m,552,5, "C")       
        
        m += 1
        rn.GO(m)
   
        m += 1
        rn.TI(m,2)
     
        m += 1
        rn.SP(m,9,"H")        
   
        m += 1
        rn.MO(m,551,"O")

        m += 1
        rn.MO(m,550,"O")
        
        #m += 1
        #rn.WH(m)
        
        m += 1
        rn.RS(m)
        
        self.m2 = m
        print(m)
   
    
    
    def runPICK(self):
        n = self.n
        
        if self.n2 == n:
            self.PICK()
            time.sleep(1)
        self.r.RN(n,self.n2)
        
    def runPUT(self):
        m = self.m
        if self.m2 == m:
            self.PUT()
            time.sleep(1)
        self.r.RN(m,self.m2)
