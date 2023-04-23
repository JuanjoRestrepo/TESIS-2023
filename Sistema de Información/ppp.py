from neo4j import GraphDatabase

#
uri = "bolt://localhost:7687"
user = "neo4j"
password ="admin123"

class Neo4jService(object):

    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def crear_orden(self,tx,amount):
        order_id=9
        date= '4/17/2023'
        tx.run("MERGE (order_"+ str(order_id) +":order {name: 'order_"+ str(order_id)+"',create_date:'"+str(date)+"',Update_Date:'"+str(date)+"',End_Date:'',ID:'"+str(order_id)+"',State:'Created',Amount:'"+str(amount)+"'})")

    def crear_relacion(self,tx,relacion,a,b,datoa,datob):
        tx.run("MATCH (a:$tipoa {name: $datoa}) "
               "MATCH (b:$tipob {name: $datob}) "
               "MERGE (a)-[:$rel]->(b)",rel= relacion,tipoa=a,tipob=b,
               nombre_persona=datoa, nombre_modelo=datob)


neo4j = Neo4jService.Neo4jService(uri, user, password)

with neo4j._driver.session() as session:

    session.write_transaction(neo4j.crear_relacion, "ORDER" , "order","system","order_4","System")

