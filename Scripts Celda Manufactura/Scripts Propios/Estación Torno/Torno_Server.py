"""
Modify on Wed May  5 16:24:52 2023

@author: juandavid.contreras

Server para la estacion Torno 
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
from Torno_Station import RunTStation  





def run(sender,N):
    #ejecutar manufactura en torno
    N = N.Value
    t = threading.Thread(target=RunTStation, args=(event,N))
    t.start()
    print("Torno ready")
    return [ua.Variant(1,ua.VariantType.Int32)]


if __name__ == "__main__":

    logging.basicConfig(level=logging.WARN)

    server = Server()
    # IP a la que esta conectado el computador en la red del CAP
    server.set_endpoint("opc.tcp://192.168.0.100:8000/T/")
    server.set_server_name("TStation")
    print("\n============================ CONECTADO A TORNO ============================\n")

    # setup our own namespace
    uri = "http://TStation/.javerianacali.edu.co"
    idx = server.register_namespace(uri)

    # get Objects node, this is where we should put our custom stuff
    objects = server.get_objects_node()

    # populating our address space

    Services = objects.add_object(idx, "Services")
    RunT_method = Services.add_method(idx, "RunT", run,[ua.VariantType.Int32],[ua.VariantType.Int32])
    
    #Evento
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