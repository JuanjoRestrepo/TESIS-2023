# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 12:45:01 2018

@author: cap
"""

import time
from osbrain import run_agent
from osbrain import run_nameserver
from osbrain import AgentAddress

def log_message(agent, message):
    agent.log_info('Received: %s' % message)


if __name__ == '__main__':

    # System deployment
    ns = run_nameserver()
    bob = run_agent('Bob')

    # System configuration
    add = AgentAddress("ipc", "/run/user/1000/MS", "PUSH", "server", "pickle")
    bob.connect(add , handler=log_message)

