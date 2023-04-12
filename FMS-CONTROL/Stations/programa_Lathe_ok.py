#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 15:11:16 2017

@author: cap
"""
##sudo chmod 666 /dev/ttyS0  
import Robot
import time
import API_CNC

r = Robot.execute(port ='/dev/ttyUSB0')
rn = Robot.program(port="/dev/ttyUSB0")
lathe = API_CNC.cnc(port="/dev/ttyS0")   #el control de flujo por software no esta funcionando para el ttyUSB0



"""
r.PD(n,11.3,163.2,375.2,-89.1,86.6)   #descanso en espera de ordenes
time.sleep(0.5)
r.PD(n+1,447.8,18.0,350.0,0.0,176.0)  #antes de agarrar pieza del pallet
time.sleep(0.5)
r.PD(n+2,+554.1,+19.8,+221.7,.0,+176.0)  #posicion de agarrar la pieza en el palet
time.sleep(0.5)
r.PD(n+3,547.8,18.0,321.0,0.0,176.0)  #posicion despues de agarrar la pieza en el palet
time.sleep(0.5)
r.PD(n+4,-158.7,+39.6,+375.1,-89.1,+86.6) #antes de entrar al torno
time.sleep(0.5)
r.PD(n+5,-418,88.6,407.2,0,86) #dentro del torno
time.sleep(0.5)
r.PD(n+6,-431.0,-.5,+407.4,.0,+86.0) -431.0,-1.6,+405.7,.0,+86.0' #mandril
"""


class lathe_robot():

    def __init__(self,robot_lineas,robot_ejecutar,xyz):
         self.rn = robot_lineas  #objeto robot para escribir lineas de comandos
         self.r = robot_ejecutar  #objeto robot para ejecutar comandos directamente
         self.n = 160  #linea inicial comandos
         self.xyz = xyz  #posicion de la pieza
         self.m = self.n + 20
         self.p = self.m + 20
         self.q = self.p + 20
         
    
    def mount_comand(self):
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
        
    def wait_lathe_comand(self):
        m= self.m
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
        
    def unmount(self):
        p = self.p
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
        
    def put_in_pallet(self):
        q = self.q
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
        rn.MO(q,401,"O")
        time.sleep(0.5)
        q += 1
        rn.MO(q,400,"C")
        time.sleep(0.5)
        q += 1
        rn.WH(q)
        print(q)
        
    def run_mount(self):
        n = self.n
        self.r.RN(n,n+14)
        
    def run_wait_lathe(self):
        m = self.m
        self.r.RN(m,m+6)
        
    def run_unmount(self):
        p = self.p
        self.r.RN(p,p+5)
        
    def run_put_in_pallet(self):
        q = self.q
        self.r.RN(q,q+9) 
        
#time.sleep(10)
        
"""
###############################################################################
Condiciones iniciales
###############################################################################
"""        
lathe.openclamp()
lathe.opendoor()
lathe.openclamp()
lathe.opendoor()
r.c.timeout = 30  #aumentar timeout a 30 segundos        
     
"""
###############################################################################
instancia de modulo
###############################################################################
"""
        
M = lathe_robot(rn,r,0)  
      
"""
###############################################################################
Configuracion del robot, predefinir secuencias
###############################################################################
"""
#solo se debe crear una ves y sobre escribir si se cambia alguna posicion
#M.mount_comand()   
#M.wait_lathe_comand()
#M.unmount()
#M.put_in_pallet()
 

 
"""
###############################################################################
Secuencia para fabricar una pieza en el centro de mecanizado
###############################################################################
"""
###############################################################################
#mover pieza del pallet al cm
time.sleep(2)
M.run_mount()
###############################################################################
#esperar hasta que termine
r.c.reset_input_buffer()
poi = r.c.read(1)
print(poi)
time.sleep(1)
###############################################################################
#Cerrar la mordaza del cm y esperar a que agarre
lathe.closeclamp()
time.sleep(2)
###############################################################################
#sacar brazo del torno
M.run_wait_lathe()
###############################################################################
#espera que salga el brazo
r.c.reset_input_buffer()
poi = r.c.read(1)
print(poi)
time.sleep(1)
###############################################################################
#cerrar la puerta  cuando el brazo este afuera
lathe.closedoor()
time.sleep(1)  #hay que esperar a que cierre antes de seguir
###############################################################################
#enviar el programa para que se fabrique la pieza
#recordar que esto debe ser de acuerdo a base de datos y rfid
lathe.nc("AM.NC")
ch = 0
###############################################################################
#esto envia comando de abrir puerta 200 veces para llenar buffer, 
while ch < 200:
    lathe.code("M38")
    ch = ch +1
time.sleep(1)  #esperar suficiente para que se termine en programa antes de mandar el robot
                #a futuro hacerlo con la salida digital del cnc
###############################################################################
#mandar al robot a desmontar la pieza
M.run_unmount()
###############################################################################
#espera que  el brazo este en posicion
r.c.reset_input_buffer()
poi = r.c.read(1)
print(poi)
time.sleep(1)
###############################################################################
#abrir la sujecion
lathe.openclamp()
time.sleep(2)
###############################################################################
#Llevar la pieza al pallet
M.run_put_in_pallet()