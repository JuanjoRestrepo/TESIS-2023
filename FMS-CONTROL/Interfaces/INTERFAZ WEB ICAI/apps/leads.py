# -*- coding: utf-8 -*-
import json
import math

import pandas as pd
import flask
import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import plotly.plotly as py
from plotly import graph_objs as go

from app import app, control_buttom



layout = [
    html.Div(
        [
            html.Div(        
                [
                        html.P("ASRS"),
                        control_buttom("Poner material en la banda","poner"),
                        control_buttom("Recoger producto de la banda","recoger")
                ],
                className="four columns chart_div",
                ),
            html.Div(        
                [
                        html.P("Estacion de Torneado"),
                        control_buttom("Tornear pieza","run_torno"),
                        control_buttom("Abrir puerta","abrir_torno"),
                        control_buttom("Cerrar puerta","cerrar_torno"),
                        control_buttom("Reset robot","reset_torno"),
                ],
                className="four columns chart_div",
                ),
            html.Div(        
                [
                        html.P("Estacion de fresado"),
                        control_buttom("Fresar pieza","run_fresadora"),
                        control_buttom("Abrir puerta","abrir_fresadora"),
                        control_buttom("Cerrar puerta","cerrar_fresadora"),
                        control_buttom("Reset robot","reset_fresadora"),
                ],
                className="four columns chart_div",
                )
        ],
        className="row",
        style={"marginTop": "5px"}
    ),
            
    html.Div(
        [
            html.Div(        
                [
                        html.P("Estacion de Control de Calidad por Vision Computacional"),

                ],
                className="four columns chart_div",
                ),
            html.Div(        
                [
                        html.P("Estacion de Ensamble Asistido por Robot"),
                        control_buttom("Recoger pieza","recoger_robot"),
                        control_buttom("Poner Pieza","poner_robot"),
                        control_buttom("Cerrar gripper","cerrar_robot"),
                        control_buttom("Abrir gripper","abrir_robot"),
                        control_buttom("Reset","reset_robot"),
                ],
                className="four columns chart_div",
                ),
            html.Div(        
                [
                        html.P("Banda Transportadora"),
                        control_buttom("Piston 1","p1"),
                        control_buttom("Piston 2","p2"),
                        control_buttom("Piston 3","p3"),
                        control_buttom("Piston 4","p4"),
                        control_buttom("Piston 5","p5"),
                      
                ],
                className="four columns chart_div",
                )
        ],
        className="row",
        style={"marginTop": "5px"}
    ),


]

