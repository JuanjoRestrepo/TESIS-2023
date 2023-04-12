#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 17:54:47 2018

@author: cap
"""

import time
import threading
#sudo chmod 666 /dev/ttyUSB0 
import sys
sys.path.insert(0, "..")
import logging

try:
    from IPython import embed
except ImportError:
    import code

    def embed():
        vars = globals()
        vars.update(locals())
        shell = code.InteractiveConsole(vars)
        shell.interact()


from opcua import ua, uamethod, Server
from DEMOStation import ESCRIBIR as ES
from DEMOStation import PLAY as PL
from DEMOStation import PICK as PI
from DEMOStation import Ogripper,Cgripper, Mover, NT,RS

# method to be exposed through server

def ESCRIBIR(parent, Station):
    S1 = threading.Thread(target=ES,args=())
    S1.start()
    print("Moving Robot")
    return [ua.Variant(4, ua.VariantType.Int32)]
def PLAY(parent, Station):
    S2 = threading.Thread(target=PL,args=())
    S2.start()
    print("Moving Robot")
    return [ua.Variant(4, ua.VariantType.Int32)]
def PICK(parent, Station):
    S3 = threading.Thread(target=PI,args=())
    S3.start()
    print("Moving Robot")
    return [ua.Variant(4, ua.VariantType.Int32)]
def GO(parent, Station):
    S3 = threading.Thread(target=Ogripper,args=())
    S3.start()
    print("Moving Robot")
    return [ua.Variant(4, ua.VariantType.Int32)]
def GC(parent, Station):
    S3 = threading.Thread(target=Cgripper,args=())
    S3.start()
    print("Moving Robot")
    return [ua.Variant(4, ua.VariantType.Int32)]
def MO(parent, Station):
    Station = Station.value
    S3 = threading.Thread(target=Mover,args=(Station))
    S3.start()
    print("Moving Robot")
    return [ua.Variant(4, ua.VariantType.Int32)]
def NT1(parent, Station):
    S3 = threading.Thread(target=NT,args=())
    S3.start()
    print("Moving Robot")
    return [ua.Variant(4, ua.VariantType.Int32)]
def RS1(parent, Station):
    S3 = threading.Thread(target=RS,args=())
    S3.start()
    print("Moving Robot")
    return [ua.Variant(4, ua.VariantType.Int32)]
if __name__ == "__main__":
    # optional: setup logging
    logging.basicConfig(level=logging.WARN)

    # now setup our server
    server = Server()
    #server.set_endpoint("opc.tcp://localhost:4840/freeopcua/server/")
    server.set_endpoint("opc.tcp://172.17.5.61:4000/DEMO/")
    server.set_server_name("Robot Server")

    # setup our own namespace
    uri = "http://cap.edu.co"
    idx = server.register_namespace(uri)

    # get Objects node, this is where we should put our custom stuff
    objects = server.get_objects_node()

    # populating our address space
    Services = objects.add_object(idx, "Services")
    
    E = Services.add_method(idx, "ESCRIBIR", ESCRIBIR, [ua.VariantType.Int32],[ua.VariantType.Int32])
    P = Services.add_method(idx, "PLAY", PLAY, [ua.VariantType.Int32],[ua.VariantType.Int32])
    PK = Services.add_method(idx, "PICK", PICK, [ua.VariantType.Int32],[ua.VariantType.Int32])
    f1 = Services.add_method(idx, "GO", GO, [ua.VariantType.Int32],[ua.VariantType.Int32])
    f2 = Services.add_method(idx, "GC", GC, [ua.VariantType.Int32],[ua.VariantType.Int32])
    f3 = Services.add_method(idx, "NT", NT1, [ua.VariantType.Int32],[ua.VariantType.Int32])
    f4 = Services.add_method(idx, "MO", MO, [ua.VariantType.Int32],[ua.VariantType.Int32])
    f5 = Services.add_method(idx, "RS", RS1, [ua.VariantType.Int32],[ua.VariantType.Int32])
    # Creating a custom event
    server.start()
    print("Available loggers are: ", logging.Logger.manager.loggerDict.keys())
    try:
        print("Ready")
        embed()
    finally:
        server.stop()
