# -*- coding: utf-8 -*-
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import flask
import plotly.plotly as py
from plotly import graph_objs as go
import math
from app import app, server,indicator
from opcua import Client, Server
from opcua import ua

Cordinator = Client("opc.tcp://192.168.43.124:8050/icai/")
Cordinator.connect()
rootC = Cordinator.get_root_node()
print(rootC)
# entrar a servicios
services = rootC.get_child(["0:Objects", "2:Services"])
#print(services)
#variables = root.get_child(["0:Objects", "2:Variables"])
#print(variables)
