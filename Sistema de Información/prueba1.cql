//Sistema
MERGE (System:system{name : "System",create_date:'4/11/2023',Update_Date:'4/11/2023',Maintenance_Date:'4/11/2025'})

//Maquinas
MERGE (CNC_Torno:machine {name : "CNC_Torno",create_date:'4/11/2023',Update_Date:'4/11/2023',Maintenance_Date:'4/11/2025',
Data_Machine:'Denford',State:'Avalaible'} )
MERGE (CNC_Melling:machine {name : "CNC_Melling" ,create_date:'4/11/2023',Update_Date:'4/11/2023',Maintenance_Date:'4/11/2025',
Data_Machine:'Denford',State:'Avalaible'} )
MERGE (Storage:machine {name : "Storage" ,create_date:'4/11/2023',Update_Date:'4/11/2023',Maintenance_Date:'4/11/2025',
Data_Machine:'Denford',State:'Avalaible'} )
MERGE (UR3:machine {name : "Robot_UR3" ,create_date:'4/11/2023',Update_Date:'4/11/2023',Maintenance_Date:'4/11/2025',
Data_Machine:'universal Robots',State:'Avalaible'} )
MERGE (Mitsubishi1:machine {name : "Robot_Fresado" ,create_date:'4/11/2023',Update_Date:'4/11/2023',Maintenance_Date:'4/11/2025',
Data_Machine:'Mitsubishi',State:'Avalaible'} )
MERGE (Mitsubishi2:machine {name : "Robot_Torno" ,create_date:'4/11/2023',Update_Date:'4/11/2023',Maintenance_Date:'4/11/2025',
Data_Machine:'Mitsubishi',State:'Avalaible'} )

// Procesos Torno
MERGE (Torno_Empack_P1:proccess {name : "Torno_Empack_P1",create_date:'4/11/2023',Update_Date:'4/11/2023',File:'txt.NC'} )
MERGE (Torno_Empack_P2:proccess {name : "Torno_Empack_P2",create_date:'4/11/2023',Update_Date:'4/11/2023',File:'txt.NC'} )
MERGE (Torno_Empack_P3:proccess {name : "Torno_Empack_P3",create_date:'4/11/2023',Update_Date:'4/11/2023',File:'txt.NC'} )
MERGE (Torno_Aluminium_P1:proccess {name : "Torno_Aluminium_P1",create_date:'4/11/2023',Update_Date:'4/11/2023',File:'txt.NC'} )
MERGE (Torno_Aluminium_P2:proccess {name : "Torno_Aluminium_P2",create_date:'4/11/2023',Update_Date:'4/11/2023',File:'txt.NC'} )
MERGE (Torno_Aluminium_P3:proccess {name : "Torno_Aluminium_P3",create_date:'4/11/2023',Update_Date:'4/11/2023',File:'txt.NC'} )

// Procesos Fresado
MERGE (Melling_Empack_P1:proccess {name : "Melling_Empack_P1",create_date:'4/11/2023',Update_Date:'4/11/2023',File:'txt.NC'} )
MERGE (Melling_Aluminium_P1:proccess {name : "Melling_Aluminium_P1",create_date:'4/11/2023',Update_Date:'4/11/2023',File:'txt.NC'} )

// Procesos Inspeccion
MERGE (Inspection_P1:proccess {name : "Inspection_P1",create_date:'4/11/2023',Update_Date:'4/11/2023',File:'txt.NC'} )
MERGE (Inspection_P2:proccess {name : "Inspection_P2",create_date:'4/11/2023',Update_Date:'4/11/2023',File:'txt.NC'} )
MERGE (Inspection_P3:proccess {name : "Inspection_P3",create_date:'4/11/2023',Update_Date:'4/11/2023',File:'txt.NC'} )

// Piezas
MERGE (Piece1:piece {name : "Piece1",create_date:'4/11/2023',Update_Date:'4/11/2023',Produced:5} )
MERGE (Piece2:piece {name : "Piece2",create_date:'4/11/2023',Update_Date:'4/11/2023',Produced:15} )
MERGE (Piece3:piece {name : "Piece3",create_date:'4/11/2023',Update_Date:'4/11/2023',Produced:25} )

// Materiales
MERGE (Empack:material {name : "Empack",create_date:'4/11/2023',Update_Date:'4/11/2023',Avalaible:5,Location:'Down'} )
MERGE (Aluminium:material {name : "Aluminium",create_date:'4/11/2023',Update_Date:'4/11/2023',Avalaible:25,Location:'Up'} )

// Ordenes
MERGE (orden_1:order {name : "Orden_1",create_date:'4/11/2023',Update_Date:'4/11/2023',End_Date:'',
ID:'1',State:'Processing', Amount:10})
MERGE (orden_2:order {name : "Orden_2",create_date:'4/11/2023',Update_Date:'4/11/2023',End_Date:'',
ID:'12',State:'Processing', Amount:5})
MERGE (orden_3:order {name : "Orden_3",create_date:'4/11/2023',Update_Date:'4/11/2023',End_Date:'4/11/2023',
ID:'123',State:'Ended', Amount:6})


// RELACIONES

// RELACION SISTEMA - STORAGE
MERGE (System)-[:MACHINE]->(Storage)

// RELACION CELDA - ORDENES
MERGE (System)-[:ORDER]->(orden_1)
MERGE (System)-[:ORDER]->(orden_2)
MERGE (System)-[:ORDER]->(orden_3)

// RELACION ORDEN - PIEZA
MERGE (orden_1)-[:PIECE]->(Piece1)
MERGE (orden_2)-[:PIECE]->(Piece2)
MERGE (orden_3)-[:PIECE]->(Piece3)

// RELACION ORDEN - PROCESO
MERGE (orden_1)-[:PROCESS]->(Torno_Aluminium_P1)
MERGE (orden_1)-[:PROCESS]->(Melling_Aluminium_P1)
MERGE (orden_1)-[:PROCESS]->(Inspection_P1)

MERGE (orden_2)-[:PROCESS]->(Torno_Empack_P2)
MERGE (orden_2)-[:PROCESS]->(Inspection_P2)

MERGE (orden_3)-[:PROCESS]->(Torno_Empack_P3)
MERGE (orden_3)-[:PROCESS]->(Inspection_P3)

// RELACION ORDEN - MATERIAL
MERGE (orden_1)-[:MATERIAL]->(Aluminium)
MERGE (orden_2)-[:MATERIAL]->(Empack)
MERGE (orden_3)-[:MATERIAL]->(Empack)


// RELACION PROCESO - MAQUINA
MERGE (Torno_Aluminium_P1)-[:MACHINE]->(CNC_Torno)
MERGE (Torno_Aluminium_P1)-[:MACHINE]->(Mitsubishi2)
MERGE (Melling_Aluminium_P1)-[:MACHINE]->(CNC_Melling)
MERGE (Melling_Aluminium_P1)-[:MACHINE]->(Mitsubishi1)

MERGE (Torno_Empack_P1)-[:MACHINE]->(CNC_Torno)
MERGE (Torno_Empack_P1)-[:MACHINE]->(Mitsubishi2)
MERGE (Melling_Empack_P1)-[:MACHINE]->(CNC_Melling)
MERGE (Melling_Empack_P1)-[:MACHINE]->(Mitsubishi1)

MERGE (Inspection_P1)-[:MACHINE]->(UR3)


MERGE (Torno_Empack_P2)-[:MACHINE]->(CNC_Torno)
MERGE (Torno_Empack_P2)-[:MACHINE]->(Mitsubishi2)

MERGE (Torno_Aluminium_P2)-[:MACHINE]->(CNC_Torno)
MERGE (Torno_Aluminium_P2)-[:MACHINE]->(Mitsubishi2)

MERGE (Inspection_P2)-[:MACHINE]->(UR3)

MERGE (Torno_Empack_P3)-[:MACHINE]->(CNC_Torno)
MERGE (Torno_Empack_P3)-[:MACHINE]->(Mitsubishi2)

MERGE (Torno_Aluminium_P3)-[:MACHINE]->(CNC_Torno)
MERGE (Torno_Aluminium_P3)-[:MACHINE]->(Mitsubishi2)

MERGE (Inspection_P3)-[:MACHINE]->(UR3)

// ELIMINAR TODO MATCH (n) DETACH DELETE n
// MOSTRAR TODO MATCH (n) RETURN n
