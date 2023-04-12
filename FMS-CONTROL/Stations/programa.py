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
lathe = API_CNC.cnc(port="/dev/ttyS0")   #el control de flujo por software no esta funcionando para el ttyUSB0

lathe.openclamp()
lathe.opendoor()

r.c.timeout = 30  #aumentar timeout a 30 segundos


"""
lathe.opendoor()
time.sleep(2)
lathe.opendoor()


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
        
    def run_mount(self):
        n = self.n
        self.r.RN(n,n+14)
        
    def run_wait_lathe(self):
        m = self.m
        self.r.RN(m,m+6)
        
        
        
r.c.reset_input_buffer()

 
"""
Secuencia para fabricar una pieza en torno
"""
 

M = lathe_robot(rn,r,0)
#los comandos solo se ejecutan para guardar en el robot despues solo se usa run (RN)
#M.mount_comand()   
#M.wait_lathe_comand()

#time.sleep(10)
#mover pieza del pallet al torno
M.run_mount()
#esperar hasta que termine
r.c.reset_input_buffer()
poi = r.c.read(1)
print(poi)
time.sleep(1)
r.c.reset_input_buffer()
#Cerrar la mordaza del torno
lathe.closeclamp()
time.sleep(2)
#sacar brazo del torno
M.run_wait_lathe()
#espera que salga el brazo
r.c.reset_input_buffer()
poi = r.c.read(1)
print(poi)
print("listo")
lathe.openclamp()
r.c.reset_input_buffer()
#cerrar puerta del torno
#lathe.closedoor()
#time.sleep(2)
#mandar programa
#lathe.nc("O0020.NC")
#time.sleep(5)


"""
#origen .0,+589.0,+300.0,.0,.0
#superior iz 240.0,510.0,170.0,0,0
#superior de -270.0,510.0,170.0,0,0
#inferior iz-270.0,420.0,170.0,0,0
#inferior de 240.0,420.0,170.0,0,0
#altura 106

rv.GO()r.ST()

rv.SP(9,"H")
time.sleep(2)
rv.OG()
time.sleep(8)
rv.GC()
time.sleep(5)
rv.MJ(46.0,6.9,-99.1,88.2,0.0)
time.sleep(4)

rv.send("qcuadrado.txt",0.5)
"""