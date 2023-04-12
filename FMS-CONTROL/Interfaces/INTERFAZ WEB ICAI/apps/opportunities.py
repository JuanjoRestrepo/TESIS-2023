# -*- coding: utf-8 -*-
import math
import json
from datetime import date
import dateutil.parser

import pandas as pd
import flask
import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import plotly.plotly as py
from plotly import graph_objs as go
from opcua import Client, Server
from opcua import ua

from app import app, indicator, supervision_station, sensor_state

"""
MC = Client("opc.tcp://192.168.200.100:4841/MC/")
T = Client("opc.tcp://192.168.200.100:8000/T/")
ASRS = Client("opc.tcp://192.168.200.100:4842/ASRS/")
Transport = Client("opc.tcp://192.168.200.100:4840/ARD/")
#QC = Client("opc.tcp://192.168.200.100:8080/QC/")
ASS = Client("opc.tcp://192.168.200.100:4000/ASS/")
"""
Cordinator = Client("opc.tcp://192.168.1.51:4000/Control/")

Cordinator.connect()
CordinatorRoot = Cordinator.get_root_node()
OPCpedidos = CordinatorRoot.get_child(["0:Objects", "2:Variables", "2:pedidos"])
print(OPCpedidos)
print(OPCpedidos.get_value())
layout = [

    #indicators row
    html.Div(
        [
            indicator(
                "#00cc96",
                "Pedidos",
                "pedidos_indicator",
            ),
            indicator(
                "#119DFF",
                "Terminadas",
                "terminados_indicator",
            ),
            indicator(
                "#EF553B",
                "Fabricando",
                "fabricando_indicator",
            ),
        ],
        className="row",
    ),

    #fila 1
    html.Div(
        [
            html.Div(
                [
                    html.P("Condiciones Ambientales"),
                    dcc.Graph(
                        id="converted_count",
                        style={"height": "90%", "width": "98%"},
                        config=dict(displayModeBar=False),
                    ),
                ],
                className="eight columns chart_div",
                ),

            html.Div(
                [
                    html.P("Sistema de recuperación y almacenamiento automatizado"),
                    
                ],
                className="four columns chart_div"
            ),
        ],
        className="row",
        style={"marginTop": "5px"}
    ),
    #fila 2
    html.Div(
        [
            supervision_station("Estacion de Torneado","Estado_torno","Conteo_torno","Ocupacion_torno"),
            supervision_station("Estacion de Fresado","Estado_fresadora","Conteo_fresadora","Ocupacion_fresadora"),        
            supervision_station("Estacion de Control de Calidad por Vision Computacional","Estado_calidad","Conteo_calidad","Ocupacion_calidad"),
        ],
        className="row",
        style={"marginTop": "5px"}
    ),

    #fila 4
    html.Div(
        [
            supervision_station("Estacion de Ensamble Asistido por Robot","Estado_robot","Conteo_robot","Ocupacion_robot"),
                    
            html.Div(
                        
                [
                    html.P("Banda Transportadora"),
                    sensor_state("Sensor 1","s1"),
                    sensor_state("Sensor 2","s2"),
                    sensor_state("Sensor 3","s3"),
                    sensor_state("Sensor 4","s4"),
                    sensor_state("Sensor 5","s5"),
                                
                ],
                className="eight columns chart_div",
                ),


        ],
        className="row",
        style={"marginTop": "5px"}
    ),

]


"""
Call Backs 
indicadores
"""

@app.callback(
    Output("pedidos_indicator", "children"),
    [Input("opportunities_df", "children")],
)
def pedidos_indicator_callback(df):
    
    return 98
    
@app.callback(
    Output("terminados_indicator", "children"),
    [Input("opportunities_df", "children")],
)
def terminados_indicator_callback(df):

    return 44

@app.callback(
    Output("fabricando_indicator", "children"),
    [Input("opportunities_df", "children")],
)
def fabricando_indicator_callback(df):

    return 23

"""
Call Backs 
ESTACION TORNEADO
"""

@app.callback(
    Output("Estado_torno", "children"),
    [Input("opportunities_df", "children")],
)
def estado_torno_callback(df):

    return 889

@app.callback(
    Output("Conteo_torno", "children"),
    [Input("opportunities_df", "children")],
)
def piezas_torno_callback(df):

    return 55

@app.callback(
    Output("Ocupacion_torno", "children"),
    [Input("opportunities_df", "children")],
)
def ocupacion_torno_callback(df):

    return 23

"""
Call Backs 
ESTACION FRESADO
"""
@app.callback(
    Output("Estado_fresadora", "children"),
    [Input("opportunities_df", "children")],
)
def estado_fresadora_callback(df):

    return 999

@app.callback(
    Output("Conteo_fresadora", "children"),
    [Input("opportunities_df", "children")],
)
def piezas_fresadora_callback(df):

    return 555

@app.callback(
    Output("Ocupacion_fresadora", "children"),
    [Input("opportunities_df", "children")],
)
def ocupacion_fresadora_callback(df):

    return 234

"""
Call Backs 
ESTACION CALIDAD
"""
@app.callback(
    Output("Estado_calidad", "children"),
    [Input("opportunities_df", "children")],
)
def estado_calidad_callback(df):

    return 889

@app.callback(
    Output("Conteo_calidad", "children"),
    [Input("opportunities_df", "children")],
)
def piezas_calidad_callback(df):

    return 55

@app.callback(
    Output("Ocupacion_calidad", "children"),
    [Input("opportunities_df", "children")],
)
def ocupacion_calidad_callback(df):

    return 23

"""
Call Backs 
ESTACION ROBOT
"""
@app.callback(
    Output("Estado_robot", "children"),
    [Input("opportunities_df", "children")],
)
def estado_robot_callback(df):

    return 889

@app.callback(
    Output("Conteo_robot", "children"),
    [Input("opportunities_df", "children")],
)
def piezas_robot_callback(df):

    return 55

@app.callback(
    Output("Ocupacion_robot", "children"),
    [Input("opportunities_df", "children")],
)
def ocupacion_robot_callback(df):

    return 23

"""
Call Backs 
ESTACION SENSORES
"""
@app.callback(
    Output("s1", "children"),
    [Input("opportunities_df", "children")],
)
def estado_sensor1_callback(df):

    return 889

@app.callback(
    Output("s2", "children"),
    [Input("opportunities_df", "children")],
)
def piezas_sensor2_callback(df):

    return 55

@app.callback(
    Output("s3", "children"),
    [Input("opportunities_df", "children")],
)
def ocupacion_sensor3_callback(df):

    return 23

@app.callback(
    Output("s4", "children"),
    [Input("opportunities_df", "children")],
)
def ocupacion_sensor4_callback(df):

    return 23

@app.callback(
    Output("s5", "children"),
    [Input("opportunities_df", "children")],
)
def ocupacion_sensor5_callback(df):

    return 23