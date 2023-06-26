#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 15:11:16 2017

@author: cap
"""
##sudo chmod 666 /dev/ttyS0  
import Robot
import Robot2
import time
import API_CNC

r = Robot.robot(port ='/dev/ttyUSB0')
rn = Robot2.robot2(port="/dev/ttyUSB0")
mc = API_CNC.cnc(port="/dev/ttyS0")   #el control de flujo por software no esta funcionando para el ttyUSB0

mc.openclamp()
mc.opendoor()

r.c.timeout = 30  #aumentar timeout a 30 segundos


"""
mc.opendoor()
time.sleep(2)
mc.opendoor()

n= 400
r.PD(n,+4.6,+169.9,+371.4,-88.9,+93.6)   #descanso en espera de ordenes
time.sleep(0.5)
r.PD(n+1,424.4,2.3,358.9,+1.2,183.4)  #antes de agarrar pieza del pallet
time.sleep(0.5)
r.PD(n+2,526.7,0.1,227.4,1.2,183.1)  #posicion de agarrar la pieza en el palet
time.sleep(0.5)
r.PD(n+3,526.7,0.1,325.0,1.2,183.1)  #posicion despues de agarrar la pieza en el palet
time.sleep(0.5)
r.PD(n+4,-218.9,264.6,541.5,-1.1,184.7) #antes de entrar al cm
time.sleep(0.5)
r.PD(n+5,-505.3,-50.8,+510.3,-1.1,+184.7) #dentro del cm
time.sleep(0.5)
r.PD(n+6,-503.7,-52.5,471.7,-1.3,183.3)  #prensa

"""

class mc_robot():

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
        
    def wait_mc_comand(self):
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
        
    def run_wait_mc(self):
        m = self.m
        self.r.RN(m,m+6)
     
    def run_unmount(self):
        p = self.p
        self.r.RN(p,p+5)
        
    def run_put_in_pallet(self):
        q = self.q
        self.r.RN(q,q+9)
   
time.sleep(10)
"""
###############################################################################
Condiciones iniciales
###############################################################################
"""        
mc.openclamp()
mc.opendoor()
mc.openclamp()
mc.opendoor()
r.c.timeout = 30  #aumentar timeout a 30 segundos 
     
"""
###############################################################################
instancia de modulo
###############################################################################
"""
        
M = mc_robot(rn,r,0)  
      
"""
###############################################################################
Configuracion del robot, predefinir secuencias
###############################################################################
"""
#solo se debe crear una ves y sobre escribir si se cambia alguna posicion
M.mount_comand()   
M.wait_mc_comand()
M.unmount()
M.put_in_pallet
 
"""
###############################################################################
Secuencia para fabricar una pieza en el centro de mecanizado
###############################################################################
"""
###############################################################################
#mover pieza del pallet al cm
M.run_mount()
###############################################################################
#esperar hasta que termine
r.c.reset_input_buffer()
poi = r.c.read(1)
print(poi)
time.sleep(1)
###############################################################################
#Cerrar la mordaza del cm y esperar a que agarre
mc.closeclamp()
time.sleep(2)
###############################################################################
#sacar brazo del torno
M.run_wait_mc()
###############################################################################
#espera que salga el brazo
r.c.reset_input_buffer()
poi = r.c.read(1)
print(poi)
time.sleep(1)
###############################################################################
#cerrar la puerta  cuando el brazo este afuera
mc.closedoor()
time.sleep(1)  #hay que esperar a que cierre antes de seguir
###############################################################################
#enviar el programa para que se fabrique la pieza
#recordar que esto debe ser de acuerdo a base de datos y rfid
mc.nc("O0021.NC")
time.sleep(8)  #esperar suficiente para que se termine en programa antes de mandar el robot
                #a futuro hacerlo con la salida digital del cnc
###############################################################################
#esto envia comando de abrir puerta 200 veces para llenar buffer, 
ch = 0
while ch < 200:
    mc.code("M38")
    ch = ch +1
time.sleep(1)  #esperar suficiente para que se termine el programa antes de mandar el robot
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
mc.openclamp()
time.sleep(2)
###############################################################################
#Llevar la pieza al pallet
M.run_put_in_pallet()
