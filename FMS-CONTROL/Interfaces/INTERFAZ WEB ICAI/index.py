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
import time
import socket

nombre_equipo = socket.gethostname()
IP = socket.gethostbyname(nombre_equipo)

Cordinator = Client("opc.tcp://192.168.43.124:8050/icai/")
Cordinator.connect()
rootC = Cordinator.get_root_node()
print(rootC)
# entrar a servicios
services = rootC.get_child(["0:Objects", "2:Services"])
print(services)
variable = rootC.get_child(["0:Objects", "2:Variables", "2:Count"])
print(variable)


app.layout = html.Div(
    [
        # header
        html.Div([

            html.Span("Application for ICAI", className='app-title'),
            
            html.Div(
                html.Img(src='https://s3-us-west-1.amazonaws.com/plotly-tutorials/logo/new-branding/dash-logo-by-plotly-stripe-inverted.png',height="100%")
                ,style={"float":"right","height":"100%"})
            ],
            className="row header"
            ),       
                
        # divs that save dataframe for each tab
        html.Div(
                #sf_manager.get_opportunities().to_json(orient="split"),  # opportunities df
                id="opportunities_df",
                style={"display": "none"},
            ),
        #contenido
        html.Div(
        [
            indicator(
                "#00cc96",
                "Reques Counter",
                "count_text",
            ),
            dcc.Interval(
            id='interval-component',
            interval=1*1000, # in milliseconds
            n_intervals=0
            ),
            html.Div(
                    [
                        
                        html.P(
                            "Please Call Me",
                            className="twelve columns indicator_text"
                        ),
                                  
                            html.Div([html.P("Name:",className="twelve columns indicator_text",style={"marginLeft": 15,"marginRight": 15,"marginTop": 15,"text-align": "left"}),dcc.Input(id='input-box', type='text',style={"marginLeft": 15,"marginRight": 15,"marginTop": 15,"text-align": "center"})]),
                            html.Button('Click', id='button',style={"marginLeft": 15,"marginRight": 15,"marginTop": 15,"text-align": "center"})
                    ],
                    className="four columns chart_div",

                    
                ),
            html.Div(
                    [
                        
                        html.P(
                            "Output",
                            className="twelve columns indicator_text"
                        ),
                            html.Div(id='output-container-button',
                            children='Enter a value and press submit') 
                    ],
                    className="four columns indicator",
                    
                ),
        ],
        className="row",
    ),        
        
        html.Link(href="https://use.fontawesome.com/releases/v5.2.0/css/all.css",rel="stylesheet"),
        html.Link(href="https://cdn.rawgit.com/plotly/dash-app-stylesheets/2d266c578d2a6e8850ebce48fdb52759b2aef506/stylesheet-oil-and-gas.css",rel="stylesheet"),
        html.Link(href="https://fonts.googleapis.com/css?family=Dosis", rel="stylesheet"),
        html.Link(href="https://fonts.googleapis.com/css?family=Open+Sans", rel="stylesheet"),
        html.Link(href="https://fonts.googleapis.com/css?family=Ubuntu", rel="stylesheet"),
        html.Link(href="https://cdn.rawgit.com/amadoukane96/8a8cfdac5d2cecad866952c52a70a50e/raw/cd5a9bf0b30856f4fc7e3812162c74bfc0ebe011/dash_crm.css", rel="stylesheet")
    ],
    className="row",
    style={"margin": "0%"},
)


"""
Call Backs 
indicadores
"""

@app.callback(
    Output("count_text", "children"),
    [Input('interval-component', 'n_intervals')],
)
def count_callback(df):
    val = variable.get_value()
    return str(val)


@app.callback(
    dash.dependencies.Output('output-container-button', 'children'),
    [dash.dependencies.Input('button', 'n_clicks')],
    [dash.dependencies.State('input-box', 'value')])
def update_output(n_clicks, value):
    services.call_method("2:video",value)
    time.sleep(2)
    return 'YOU ARE IN "{}" AND CALL METHOD WITH ARGUMENT "{}"'.format(services,value)


if __name__ == "__main__":
    app.run_server(debug=False,port=8080,host="192.168.43.124")
