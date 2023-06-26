#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 15:11:16 2017

@author: cap
"""
##sudo chmod 666 /dev/ttyS0  
import time
"""
from osbrain import run_agent
from osbrain import run_nameserver
from osbrain import AgentAddress
"""
import serial
import RobotT
import API_CNC

"""
###############################################################################
instancia de modulo
###############################################################################
"""
port = serial.Serial(port = "COM4", baudrate=9600, parity="O", bytesize=7, stopbits=2,xonxoff = False)
t = API_CNC.cnc(port="COM3")
R = RobotT._RobotT(port)
        
#time.sleep(10)
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
Enseñar posiciones del robot
###############################################################################
"""        

def teachT():
    R.toT()   
    R.waitT()
    R.pick()
    R.toPallet()   
  
"""
###############################################################################
Configuraciones iniciarles
###############################################################################
"""
def ConfTStation():
    t.openclamp()
    t.opendoor()
    t.openclamp()
    t.opendoor()
    t.closeclamp() 
    R.r.c.timeout = 30  #aumentar timeout a 30 segundos  

def RunTStation(TEvent, NPieza):
    """
    ###############################################################################
    Secuencia para fabricar una pieza en el centro de mecanizado
    ###############################################################################
    """
    ###############################################################################
    #mover pieza del pallet al cm
    t.openclamp()
    time.sleep(2)
    R.run_toT()
    ###############################################################################
    #esperar hasta que termine
    R.r.c.reset_input_buffer()
    poi = R.r.c.read(1)
    print(poi)
    time.sleep(1)
    ###############################################################################
    #Cerrar la mordaza del cm y esperar a que agarre
    t.closeclamp()
    time.sleep(2)
    ###############################################################################
    #sacar brazo del torno
    R.run_waitT()
    ###############################################################################
    #espera que salga el brazo
    R.r.c.reset_input_buffer()
    poi = R.r.c.read(1)
    print(poi)
    time.sleep(1)
    ###############################################################################
    #cerrar la puerta  cuando el brazo este afuera
    t.closedoor()
    time.sleep(1)  #hay que esperar a que cierre antes de seguir
    ###############################################################################
    #enviar el programa para que se fabrique la pieza
    #recordar que esto debe ser de acuerdo a base de datos y rfid
    if NPieza == 1:
        t.nc("NC/BOTELLA.NC")
    elif NPieza == 2:
        t.nc("NC/SOLDADO.NC")
    else:
        t.nc("NC/EJE.NC")        
        
        
    ch = 0
    ###############################################################################
    #esto envia comando de abrir puerta 200 veces para llenar buffer, 
    while ch < 100:
        t.code("M38")
        ch = ch +1
    time.sleep(1)  #esperar suficiente para que se termine en programa antes de mandar el robot
                    #a futuro hacerlo con la salida digital del cnc
    ###############################################################################
    #mandar al robot a desmontar la pieza
    R.run_pick()
    ###############################################################################
    #espera que  el brazo este en posicion
    R.r.c.reset_input_buffer()
    poi = R.r.c.read(1)
    print(poi)
    time.sleep(1)
    ###############################################################################
    #abrir la sujecion
    t.openclamp()
    time.sleep(2)
    ###############################################################################
    #Llevar la pieza al pallet
    R.run_toPallet()
    ###############################################################################
    #enviar evento al coordinador
    TEvent.event.State = 1
    time.sleep(10)
    t.closeclamp()
    TEvent.trigger()
    print("trigget")
    
ConfTStation()

    
