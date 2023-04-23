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

// Procesos Inspección
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

// RELACIONES

// RELACION SISTEMA - STORAGE
MERGE (System)-[:MACHINE]->(Storage)

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