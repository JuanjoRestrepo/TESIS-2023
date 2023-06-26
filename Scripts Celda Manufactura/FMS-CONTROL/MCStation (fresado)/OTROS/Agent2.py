# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 12:45:57 2018

@author: cap
"""


import time
from osbrain import run_agent
from osbrain import run_nameserver




if __name__ == '__main__':

    # System deployment
    ns = run_nameserver()
    alice = run_agent('Alice')

    addr = alice.bind('PUB', alias='main', addr = "/run/user/1000/MS")
    print(addr)
    # Send messages
    time.sleep(10)
    alice.send('main', 'gracias',topic="run")
    print("OK")
