"""
Modify on Wed May  5 16:24:52 2023

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
        dnc.write(str.encode(line)+ b"\n")
        print (str.encode(line)+ b"\n")
    
    def M(self,code):
        dnc = self.dnc 
        if code < 10:
            scode = "M0"+str(code)
        else:
            scode = "M"+str(code)
        
        dnc.write(str.encode(scode)+ b";\n")   
        
    def spindle_cw(self): 
        # husillo horario
        dnc = self.dnc 
        dnc.write(b"M03;\n")
        
    def spindle_ccw(self): 
        # husillo anti-horario
        dnc = self.dnc 
        dnc.write(b"M04;\n")
        
    def stop_spindle(self): 
        # Parar husillo
        dnc = self.dnc 
        dnc.write(b"M05;\n")
        
    def change_tool(self, Tool):
        # cambiar herramienta
        dnc = self.dnc 
        dnc.write(b"M06 " + str.encode(Tool) + b";\n")

    def open_clamp(self):
        # Abrir prensa
        dnc = self.dnc 
        dnc.write(b"M010;\n") 
        
    def close_clamp(self):
        # Cerrar prensa
        dnc = self.dnc 
        dnc.write(b"M011;\n")
    
    def open_chuck(self):
        # Abrir mandril
        dnc = self.dnc 
        dnc.write(b"M010;\n")
        
    def close_chuck(self):
        # Cerrar mandril
        dnc = self.dnc 
        dnc.write(b"M011;\n")  

    def open_and_stop(self):
        # Abrir y parar
        dnc = self.dnc 
        dnc.write(b"M037;\n")
     
    def open_door(self):
        dnc = self.dnc 
        dnc.write(b"M38;\n")
        
    def close_door(self):
        dnc = self.dnc 
        dnc.write(b"M39;\n")    
        
        
        
         
    

