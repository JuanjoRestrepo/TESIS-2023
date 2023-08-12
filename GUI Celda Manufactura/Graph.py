import numpy as np
import random
import pandas as pd
from neo4j import GraphDatabase
from datetime import datetime


class graph():

    def __init__(self):
        conexion_DB = GraphDatabase.driver(uri = "bolt://localhost:7687", auth = ("prueba", "12345678") )
        self.session = conexion_DB.session()

    def relation(self,rel,typea,typeb,namea,nameb):
        # Crear relaciones entre nodos
        session = self.session
        session.run("MATCH (a:"+str(typea)+"),(b:"+str(typeb)+") WHERE a.Name= '"+str(namea)+"' AND b.Name= '"+str(nameb)+"' CREATE (a)-[r:"+str(rel)+"]->(b)")
    
    def Separate_dict(self,dict):
        keys =[]
        values =[]
        for valor in dict :
            for res in valor.values():
                keys.append(list(res.keys()))
                values.append(list(res.values()))
        return(keys,values)

    def create_order (self,material,amount,piece,location):
        session = self.session

        # Crear un ID unico
        date = datetime.now()
        order_id = material[0]+"P"+piece[-1]+"_"+str(date.year)+"_"+str(date.day)+"_"+str(date.month)+"_C"+str(amount) +"_H"+str(date.hour)+"_T"+str(date.minute) # Material + Pieza + Fecha + Cantidad + Hora
        
        # Crea orden
        session.run("CREATE (order_"+ str(order_id) +":order {Name:'"+str(order_id)+"',Create_Date:'"+str(date)+"',Update_Date:'"+str(date)+"',End_Date:'',ID_Order:'"+str(order_id)+"',State:'Created',Amount:'"+str(amount)+"',Material:'"+str(material)+"', Piece:'"+str(piece)+"',Type_Error:'',Amount_Error:'', Locations:'"+str(location)+"'})")
        
        # Relacion Orden con Piece
        self.relation('PIECE','order',piece,order_id,'ASRS Get Material')

        return([order_id,str(date),"",material,piece,amount,"",'Created',""])


    def get_data_especific(self,type,filter,name):
        # Trae la información de un nodo
        session = self.session
        info = session.run("MATCH (n:"+ str(type)+"{"+ str(filter)+":'"+ str(name)+"'}) RETURN properties(n) ORDER BY n.Create_Date ASC")
        return (self.Separate_dict(info.data()))
    
    def get_data(self,type):
        # Trae la información de un nodo
        session = self.session
        info = session.run("MATCH (n:"+ str(type)+") RETURN n AS "+ str(type))
        return (self.Separate_dict(info.data()))
    
    def get_data_relation(self,typea,namea,typeb,nameb,rel):
        # Trae la información dentro de la relación entre nodos
        session = self.session
        info = session.run("MATCH (a:"+ str(typea)+"{Name:'"+ str(namea)+"'})-[r:"+ str(rel)+"]->(b:"+ str(typeb)+"{Name:'"+ str(nameb)+"'}) RETURN properties(r)")
        return (self.Separate_dict(info.data()))
    
    def update_data(self,name,type,info,property):
        # Actualiza la información de un nodo, dependiendo de la propiedad e información a modificar
        session = self.session
        n = 0
        for i in property:
            session.run("MATCH (n:"+ str(type)+"{Name:'"+str(name)+"'})  SET n."+ str(i)+" = '"+ str(info[n])+"'")
            n += 1

    def create_relation_data(self,rel,data,typea,typeb,namea,nameb):
        # Crear relaciones entre nodos con un json como etiqueta
        session = self.session
        session.run("MATCH (a:"+str(typea)+"),(b:"+str(typeb)+") WHERE a.Name= '"+str(namea)+"' AND b.Name= '"+str(nameb)+"' CREATE (a)-[:"+str(rel)+" {"+str(data)+"}]->(b)")

    def delete_node(self,type,name):
        # Elimina un nodo a partir de su nombre 
        session = self.session
        session.run("MATCH (n:"+ str(type)+"{Name:'"+ str(name)+"'}) DETACH DELETE n")
    
    def delete_relation(self,rel,namea,nameb,typea,typeb):
        session = self.session
        session.run("MATCH (a:"+str(typea)+")-[r:"+str(rel)+"]->(b:"+str(typeb)+") WHERE a.Name= '"+str(namea)+"' AND b.Name= '"+str(nameb)+"' DELETE r" )

    def close(self):
        # Cierra sesión con Neo4j
        session = self.session
        session.close()
    

run = graph()
#run.create_order('Aluminio',5,'piece1')  
#run.delete_relation('PIECE','AP1_2023_10_8_C5_H18_T43','ASRS Get Material','order','piece1')