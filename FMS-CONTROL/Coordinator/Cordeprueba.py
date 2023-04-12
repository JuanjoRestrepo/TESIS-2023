#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 09:29:04 2018

@author: cap
"""

import sys
sys.path.insert(0, "..")
import logging
import time
import threading
import numpy as np
import webbrowser


try:
    from IPython import embed
except ImportError:
    import code

    def embed():
        vars = globals()
        vars.update(locals())
        shell = code.InteractiveConsole(vars)
        shell.interact()


from opcua import Client, Server
from opcua import ua



class hello_all:
    def __init__(self):
         self.count = 0
         
         
    def say_hello(self,N):
        self.count = self.count + 1
        print("You call video " + str(N))
        if N == "1":
            webbrowser.open('https://www.youtube.com/watch?v=O6Ip2BXRvwo') 
        elif N == "2":
            webbrowser.open('https://www.youtube.com/watch?v=nT7w42-jxOU')
        else:
            print("There are not more that 2 videos")
    def call_count(self):
        return self.count
    
greeting = hello_all()  

def hello_function(sender, Name):
    Name = Name.Value
    t = threading.Thread(target=greeting.say_hello, args=(Name,))
    t.start()
    C = greeting.call_count()
    
    server.set_attribute_value(count_variable.nodeid, ua.DataValue(C))
    return [ua.Variant("Thanks",ua.VariantType.String)]

"""
################################################################################
Inicio del programa
################################################################################
"""
if __name__ == "__main__":

        
        """
        ################################################################################
        creacion del servidor
        ################################################################################
        """
        # now setup our server
        server = Server()
        #server.set_endpoint("opc.tcp://localhost:4840/freeopcua/server/")
        server.set_endpoint("opc.tcp://192.168.43.124:8050/icai/")
        server.set_server_name("Control Manual")
        uri = "http://cap.edu.co"
        idx = server.register_namespace(uri)
        objects = server.get_objects_node()
        Services = objects.add_object(idx, "Services")
        Variables = objects.add_object(idx, "Variables")
       
        """
        ################################################################################
        Servicios
        ################################################################################
        """
        hello = Services.add_method(idx, "video", hello_function, [ua.VariantType.String],[ua.VariantType.String])
       
        """
        ################################################################################
        Variables
        ################################################################################
        """
        count_variable = Variables.add_variable(idx, "Count", 55)
        
        """
        ################################################################################
        inicio del servidor
        ################################################################################
        """
        server.start()
        print("Available loggers are: ", logging.Logger.manager.loggerDict.keys())
        
        embed()
