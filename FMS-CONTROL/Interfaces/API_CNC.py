# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 11:05:03 2017

@author: juandavid.contreras

Programa para el manejo de maquinas cnc 
"""
import serial
class cnc:
    
    def __init__(self, port):
         self.p = port
         self.dnc = serial.Serial(port=self.p,baudrate=2400,rtscts=0,stopbits=2,dsrdtr=0,xonxoff=1,parity="E",bytesize=7,timeout=2)
         
    def nc(self,file):
        dnc = self.dnc
        f = open(file,"rb")
        number = 0
        for i in f:
            print(number)
            dnc.write(i)
            number += 1
            
    def code(self,line):
        dnc = self.dnc
        dnc.write(str.encode(line)+ b";\n")
        print (str.encode(line)+ b";\n")
    def codee(self,line):
        dnc = self.dnc
        dnc.write(str.encode(line)+ b";\n")
    
    def M(self,code):
        dnc = self.dnc 
        if code < 10:
            scode = "M0"+str(code)
        else:
            scode = "M"+str(code)
        
        dnc.write(str.encode(scode)+ b";\n")   
        
    def spindlecw(self):
        dnc = self.dnc 
        dnc.write(b"M03;\n")
        
    def husillohorario(self):
        self.spindlecw()
        
    def spindleccw(self):
        dnc = self.dnc 
        dnc.write(b"M04;\n")
        
    def husilloantihorario(self):
        self.spindleccw()
        
    def stopspindle(self):
        dnc = self.dnc 
        dnc.write(b"M05;\n")
    
    def pararhusillo(self):
        self.stopspindle()
        
    def changetool(self, Tool):
        dnc = self.dnc 
        dnc.write(b"M06 " + str.encode(Tool) + b";\n")
    
    def cambiarherramienta(self, Herramienta):
        self.changetool(Herramienta)  
        
    def openclamp(self):
        dnc = self.dnc 
        dnc.write(b"M010;\n")
    
    def abrirprensa(self):
        self.openclamp()   
        
    def closeclamp(self):
        dnc = self.dnc 
        dnc.write(b"M011;\n")
    
    def cerrarprensa(self):
        self.closeclamp()
    
    def openchuck(self):
        dnc = self.dnc 
        dnc.write(b"M010;\n")
    
    def abrirmandril(self):
        self.openchuck()   
        
    def closechuck(self):
        dnc = self.dnc 
        dnc.write(b"M011;\n")
    
    def cerrarmandril(self):
        self.closechuck()    

    def openandstop(self):
        dnc = self.dnc 
        dnc.write(b"M037;\n")
    
    def abriryparar(self):
        self.closechuck()  
     
    def opendoor(self):
        dnc = self.dnc 
        dnc.write(b"M38;\n")
        print("M38;\n")
        
    def abrirpuerta(self):
        self.opendoor()
        
    def closedoor(self):
        dnc = self.dnc 
        dnc.write(b"M39;\n")
    
    def cerrarpuerta(self):
        self.closedoor()      
        
        
        
         
    

