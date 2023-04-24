#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 09:41:39 2018

@author: root
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 16:25:52 2018

@author: controlcap2
"""

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
import threading  


def PUT(sender,N):
    #ejecutar manufactura en torno
    t = threading.Thread(target=RunPUT, args=(event,N))
    t.start()
    print("ready")
    return [ua.Variant(1,ua.VariantType.Int32)]

def WAIT(sender,N):
    #ejecutar manufactura en torno
    t = threading.Thread(target=RunWAIT, args=(event,))
    t.start()
    print("ready")
    return [ua.Variant(1,ua.VariantType.Int32)]

def PICK(sender,N):
    #ejecutar manufactura en torno
    t = threading.Thread(target=RunPICK, args=(event,N))
    t.start()
    print("ready")
    return [ua.Variant(1,ua.VariantType.Int32)]

if __name__ == "__main__":

    logging.basicConfig(level=logging.WARN)

    server = Server()
    server.set_endpoint("opc.tcp://192.168.200.100:4840/ASRS/")
    server.set_server_name("ASRSStation")

    # setup our own namespace
    uri = "http://ASRSStation.javerianacali.edu.co"
    idx = server.register_namespace(uri)

    # get Objects node, this is where we should put our custom stuff
    objects = server.get_objects_node()

    # populating our address space

    Services = objects.add_object(idx, "Services")
    RunPUT_method = Services.add_method(idx, "RunPUT", PUT,[ua.VariantType.Int32],[ua.VariantType.Int32])
    RunWAIT_method = Services.add_method(idx, "RunWAIT", WAIT,[ua.VariantType.Int32],[ua.VariantType.Int32])
    RunPICK_method = Services.add_method(idx, "RunPICK", PICK,[ua.VariantType.Int32],[ua.VariantType.Int32])
    #Eventos
    etype = server.create_custom_event_type(idx, 'fin')
    etype.add_property(2,"State",ua.Variant(0,ua.VariantType.Int32))
    event = server.get_event_generator(etype, Services)

    # starting!
    server.start()
    print("Available loggers are: ", logging.Logger.manager.loggerDict.keys())
    try:
        embed()
    finally:
        server.stop()