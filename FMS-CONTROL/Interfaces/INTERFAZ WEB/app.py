import math

import pandas as pd
import flask
import dash
import dash_core_components as dcc
import dash_html_components as html
import dateutil.parser

#from sfManager import sf_Manager

server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server)
app.config.suppress_callback_exceptions = True

#sf_manager = sf_Manager()

millnames = ["", " K", " M", " B", " T"] # used to convert numbers





#returns top indicator div
def indicator(color, text, id_value):
    return html.Div(
        [
            
            html.P(
                text,
                className="twelve columns indicator_text"
            ),
            html.P(
                id = id_value,
                className="indicator_value"
            ),
        ],
        className="four columns indicator",
        
    )
 

def sensor_state(nombre, id_value):
    return html.Div(
        [
            
            html.P(
                nombre,
                className="twelve columns indicator_text"
            ),
            html.P(
                id = id_value,
                className="indicator_value",
                style={'fontSize': 45}
            ),
        ],
        className="two columns indicator",
        style={"marginLeft": 15,"marginRight": 15,"marginTop": 30}
    )       


def supervision_station(titulo, id1, id2,id3):
    return html.Div(        
                [
                    html.P(titulo),
                    html.Div(
                        [
                           html.P("Estado:  ",className="six columns",style={"line-height":"65px"}),     
                           html.P(
                                   id = id1,
                                   className="six columns",
                                   style={'fontSize': 45}
                                  ),
                        ],
                         className="row",
                         style={'marginBottom': 5, 'marginTop': 5 } 
                        ),
                    html.Div(
                        [
                           html.P("Piezas Atendidas:  ",className="six columns",style={"line-height":"65px"}),    
                           html.P(
                                   id = id2,
                                   className="six columns",
                                   style={'fontSize': 45}
                                  ),
                        ],
                         className="row",
                         style={"marginTop": "5px"}  ,        
                        ),
                    html.Div(
                        [
                           html.P("Porcentaje de Ocupacion:  ",className="six columns",style={"line-height":"65px"}),    
                           html.P(
                                   id = id3,
                                   className="six columns",
                                   style={'fontSize': 45}
                                  ),
                        ],
                         className="row",
                         style={"marginTop": "5px"}  ,        
                        ),
                                
                ],
                className="four columns chart_div",
                )
                        
def control_buttom(nombre,idx):
     return html.Div(
                 html.Button(nombre, id=idx),
                 className="row",
                 style={"marginLeft": 15,"marginRight": 15,"marginTop": 15,"text-align": "center"}
                    )