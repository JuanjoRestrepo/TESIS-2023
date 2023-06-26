#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 19:59:38 2018

@author: controlcap2
"""


from osbrain import run_agent
from osbrain import run_nameserver, AgentAddress

if __name__ == '__main__':

    # System deployment
    ns = run_nameserver()
    TControlAgent = run_agent('TControl')
    
    S1 = AgentAddress("ipc", "/run/user/1000/T",'REP', "server","pickle")
    TControlAgent.connect(S1, alias = "RUN") 
    
    TControlAgent.send("RUN","2")
    Ans = TControlAgent.recv("RUN")
    print(Ans)