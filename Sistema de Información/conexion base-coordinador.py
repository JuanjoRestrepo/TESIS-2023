import numpy as np
import random
import pandas as pd
from neo4j import GraphDatabase
from datetime import datetime


# CONEXION A BASE DE DATOS
conexion_DB = GraphDatabase.driver(uri = "bolt://localhost:7687", auth = ("neo4j", "admin123") )
session = conexion_DB.session()

def relation(rel,typea,typeb,namea,nameb):
    session.run("MATCH (a:"+str(typea)+"),(b:"+str(typeb)+") WHERE a.name= '"+str(namea)+"' AND b.name= '"+str(nameb)+"' CREATE (a)-[r:"+str(rel)+"]->(b)")

def create_order (material,amount,piece,process):

    # Crear un ID unico
    date = datetime.now()
    order_id = material[0]+"P"+piece[-1]+"_"+str(date.year)+"_"+str(date.day)+"_"+str(date.month)+"_C"+str(amount) # Material + Pieza + Fecha + Cantidad

    # Crea orden
    session.run("MERGE (order_"+ str(order_id) +":order {name: 'order_"+ str(order_id)+"',create_date:'"+str(date)+"',Update_Date:'"+str(date)+"',End_Date:'0',ID:'"+str(order_id)+"',State:'Created',Amount:'"+str(amount)+"'})")
    
    # Relacion Sistema con Orden
    relation('ORDER','system','order','System',"order_"+ str(order_id))

    # Relacion Orden con Pieza
    relation('PIECE','order','piece',"order_"+ str(order_id),piece)

    # Relacion Orden con Material
    relation('MATERIAL','order','material',"order_"+ str(order_id),material)
    
    # Relacion Orden con Proceso
    for i in process:
        relation('PROCESS','order','proccess',"order_"+ str(order_id),i)
    
    return(print("Orden creada con ID:",order_id))


create_order('Empack',10,'Piece1',['Torno_Empack_P1','Melling_Empack_P1','Inspection_P1'])

"""
def get_data(tx):
    return

def update_data(tx):
    return

def modificate_order():
    return 

def relacion_con_dato():
    return 

def delete_data():
    return
"""