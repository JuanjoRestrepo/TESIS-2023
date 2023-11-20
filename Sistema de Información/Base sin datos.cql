//Maquinas
MERGE (CNC_Lathe:machine {Name : "CNC_Lathe",Create_Date:'9/23/2023',Update_Date:'9/23/2023',Maintenance_Date:'4/11/2025',
Data_Machine:'Denford',State:'Avalaible',Station:'Lathe'} )
MERGE (CNC_Melling:machine {Name : "CNC_Melling" ,Create_Date:'9/23/2023',Update_Date:'9/23/2023',Maintenance_Date:'4/11/2025',
Data_Machine:'Denford',State:'Avalaible',Station:'Melling'} )
MERGE (UR3:machine {Name : "Robot_UR3" ,Create_Date:'9/23/2023',Update_Date:'9/23/2023',Maintenance_Date:'4/11/2025',
Data_Machine:'Universal Robots',State:'Avalaible',Station:'Inspection'} )
MERGE (Mitsubishi1:machine {Name : "Robot_Melling" ,Create_Date:'9/23/2023',Update_Date:'9/23/2023',Maintenance_Date:'4/11/2025',
Data_Machine:'Mitsubishi',State:'Avalaible',Station:'Lathe'} )
MERGE (Mitsubishi2:machine {Name : "Robot_Lathe" ,Create_Date:'9/23/2023',Update_Date:'9/23/2023',Maintenance_Date:'4/11/2025',
Data_Machine:'Mitsubishi',State:'Avalaible',Station:'Melling'} )
MERGE (ASRS:machine {Name : "ASRS" ,Create_Date:'9/23/2023',Update_Date:'9/23/2023',Maintenance_Date:'4/11/2025',
Data_Machine:'Denford',State:'Avalaible',Station:'ASRS'})
MERGE (Conveyor_Lathe:machine {Name : "Conveyor_Lathe" ,Create_Date:'9/23/2023',Update_Date:'9/23/2023',Maintenance_Date:'4/11/2025',
Data_Machine:'Conveyors',State:'Avalaible'})
MERGE (Conveyor_Melling:machine {Name : "Conveyor_Melling" ,Create_Date:'9/23/2023',Update_Date:'9/23/2023',Maintenance_Date:'4/11/2025',
Data_Machine:'Conveyors',State:'Avalaible'})
MERGE (Conveyor_ASRS:machine {Name : "Conveyor_ASRS" ,Create_Date:'9/23/2023',Update_Date:'9/23/2023',Maintenance_Date:'4/11/2025',
Data_Machine:'Conveyors',State:'Avalaible'})
MERGE (Conveyor_Inspection:machine {Name : "Conveyor_Inspection" ,Create_Date:'9/23/2023',Update_Date:'9/23/2023',Maintenance_Date:'4/11/2025',
Data_Machine:'Conveyors',State:'Avalaible'})

//Stations
MERGE (Station_Melling:station {Name : "Station_Melling" ,Create_Date:'9/23/2023',Update_Date:'9/23/2023',State:'Avalaible'})
MERGE (Station_Lathe:station{Name : "Station_Lathe" ,Create_Date:'9/23/2023',Update_Date:'9/23/2023',State:'Avalaible'})
MERGE (Station_Inspection:station {Name : "Station_Inspection" ,Create_Date:'9/23/2023',Update_Date:'9/23/2023',State:'Avalaible'})
MERGE (Station_ASRS:station {Name : "Station_ASRS" ,Create_Date:'9/23/2023',Update_Date:'9/23/2023',State:'Avalaible'})

//Materiales
MERGE (Empack:material{Name : "Empack" ,Create_Date:'9/23/2023',Update_Date:'9/23/2023',Location:'[[1,3],[1,4],[1,5],[2,3],[2,4],[2,5],[3,3],[3,4],[3,5],[4,3],[4,4],[4,5],[5,3],[5,4],[5,5]]',
Used:'[]',Available:'15'})
MERGE (Aluminio:material{Name : "Aluminio" ,Create_Date:'9/23/2023',Update_Date:'9/23/2023',Location:'[[1,1],[1,2],[2,1],[2,2],[3,1],[3,2],[4,1],[4,2],[5,1],[5,2]]',
Used:'[]',Available:'10'})

// Piezas
MERGE (Piece1:piece {Name : "Piece1",Create_date:'9/23/2023',Update_Date:'9/23/2023',Produced:'0'} )
MERGE (Piece2:piece {Name : "Piece2",Create_date:'9/23/2023',Update_Date:'9/23/2023',Produced:'0'} )
MERGE (Piece3:piece {Name : "Piece3",Create_date:'9/23/2023',Update_Date:'9/23/2023',Produced:'0'} )

// RELACIONES
MERGE (ASRS)-[:MATERIAL]->(Empack)
MERGE (ASRS)-[:MATERIAL]->(Aluminio)

// RELACION ESTACION - MAQUINA
MERGE (Station_Lathe)-[:MACHINE]->(CNC_Lathe)
MERGE (Station_Lathe)-[:MACHINE]->(Mitsubishi2)
MERGE (Station_Lathe)-[:MACHINE]->(Conveyor_Lathe)
MERGE (Station_Melling)-[:MACHINE]->(CNC_Melling)
MERGE (Station_Melling)-[:MACHINE]->(Mitsubishi1)
MERGE (Station_Melling)-[:MACHINE]->(Conveyor_Melling)
MERGE (Station_Inspection)-[:MACHINE]->(UR3)
MERGE (Station_Inspection)-[:MACHINE]->(Conveyor_Inspection)
MERGE (Station_ASRS)-[:MACHINE]->(ASRS)
MERGE (Station_ASRS)-[:MACHINE]->(Conveyor_ASRS)

// RELACION PIECES - STATIONS

MERGE (Piece1)-[:STEP{Number:"1",File:"Station_ASRS"}]->(Station_ASRS)
MERGE (Piece1)-[:STEP{Number:"2",File:"Station_Lathe"}]->(Station_Lathe)
MERGE (Piece1)-[:STEP{Number:"3",File:"Station_Melling"}]->(Station_Melling)
MERGE (Piece1)-[:STEP{Number:"4",File:"Station_Inspection"}]->(Station_Inspection)
MERGE (Piece1)-[:STEP{Number:"5",File:"Station_ASRS2"}]->(Station_ASRS)

MERGE (Piece2)-[:STEP{Number:"1",File:"Station_ASRS"}]->(Station_ASRS)
MERGE (Piece2)-[:STEP{Number:"2",File:"Station_Lathe"}]->(Station_Lathe)
MERGE (Piece2)-[:STEP{Number:"3",File:"Station_Inspection"}]->(Station_Inspection)
MERGE (Piece2)-[:STEP{Number:"4",File:"Station_ASRS2"}]->(Station_ASRS)

MERGE (Piece3)-[:STEP{Number:"1",File:"Station_ASRS"}]->(Station_ASRS)
MERGE (Piece3)-[:STEP{Number:"2",File:"Station_Lathe"}]->(Station_Lathe)
MERGE (Piece3)-[:STEP{Number:"3",File:"Station_Inspection"}]->(Station_Inspection)
MERGE (Piece3)-[:STEP{Number:"4",File:"Station_ASRS2"}]->(Station_ASRS)

