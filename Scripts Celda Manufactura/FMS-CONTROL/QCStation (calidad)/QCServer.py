#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 15:11:16 2017

@author: cap
"""
##sudo chmod 666 /dev/ttyS0  
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

import time

import threading
from QCStation import QCM
Check = True

  
def run(sender,N):
    t1 = threading.Thread(target=QCM, args=(event,))
    t1.start()
    print("ready")
    return [ua.Variant(1,ua.VariantType.Int32)] #retorno del metodo opc ua
    
    
  
if __name__ == "__main__":
    
      
    logging.basicConfig(level=logging.WARN)

    server = Server()
    server.set_endpoint("opc.tcp://192.168.200.100:8080/QC/")
    server.set_server_name("QCStation")

    # setup our own namespace
    uri = "http://QCStation.javerianacali.edu.co"
    idx = server.register_namespace(uri)

    # get Objects node, this is where we should put our custom stuff
    objects = server.get_objects_node()

    # populating our address space
    Services = objects.add_object(idx, "Services")
    RunfQC_method = Services.add_method(idx, "RunQC", run,[ua.VariantType.Int32],[ua.VariantType.Int32])
    
    #Event
    etype = server.create_custom_event_type(idx, 'fin')
    etype.add_property(3,"State",ua.Variant(0,ua.VariantType.Int32))
    event = server.get_event_generator(etype, Services)
    # starting!

    server.start()
    print("Available loggers are: ", logging.Logger.manager.loggerDict.keys())
    try:
        embed()
    finally:
        server.stop()