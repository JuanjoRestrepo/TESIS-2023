//Maquinas
MERGE (CNC_Lathe:machine {Name : "CNC_Lathe",Create_Date:'08/03/2023',Update_Date:'08/03/2023',Maintenance_Date:'4/11/2025',
Data_Machine:'Denford',State:'Avalaible',Station:'Lathe'} )
MERGE (CNC_Melling:machine {Name : "CNC_Melling" ,Create_Date:'08/03/2023',Update_Date:'08/03/2023',Maintenance_Date:'4/11/2025',
Data_Machine:'Denford',State:'Avalaible',Station:'Melling'} )
MERGE (UR3:machine {Name : "Robot_UR3" ,Create_Date:'08/03/2023',Update_Date:'08/03/2023',Maintenance_Date:'4/11/2025',
Data_Machine:'Universal Robots',State:'Avalaible',Station:'Inspection'} )
MERGE (Mitsubishi1:machine {Name : "Robot_Melling" ,Create_Date:'08/03/2023',Update_Date:'08/03/2023',Maintenance_Date:'4/11/2025',
Data_Machine:'Mitsubishi',State:'Avalaible',Station:'Lathe'} )
MERGE (Mitsubishi2:machine {Name : "Robot_Lathe" ,Create_Date:'08/03/2023',Update_Date:'08/03/2023',Maintenance_Date:'4/11/2025',
Data_Machine:'Mitsubishi',State:'Avalaible',Station:'Melling'} )

//Storage
MERGE (Storage:storage {Name : "Storage" ,Create_Date:'08/03/2023',Update_Date:'08/03/2023',Maintenance_Date:'4/11/2025',
Data_Machine:'Denford',State:'Avalaible',Location_E:'[[1,3],[1,4],[1,5],[2,3],[2,4],[2,5],[3,3],[3,4],[3,5],[4,3],[4,4],[4,5],[5,3],[5,4],[5,5]]',
Location_A:'[[1,1],[1,2],[2,1],[2,2],[3,1],[3,2],[4,1],[4,2],[5,1],[5,2]]',
Location_Ended:'[[1,1],[1,2],[2,1],[2,2],[3,1],[3,2],[4,1],[4,2],[5,1],[5,2],[1,3],[1,4],[1,5],[2,3],[2,4],[2,5],[3,3],[3,4],[3,5],[4,3],[4,4],[4,5],[5,3],[5,4],[5,5]]',
Available:[10,12]} )

// Tareas pieza 1
MERGE (Get_Material_piece1:piece1 {Name : "ASRS Get Material",Create_Date:'08/03/2023',Update_Date:'08/03/2023',file:'path file'} )
MERGE (Robot_Pick_piece1:piece1 {Name : "Robot Lathe Pick",Create_Date:'08/03/2023',Update_Date:'08/03/2023',file:'path file'} )
MERGE (Lathing_piece1:piece1 {Name : "CNC Lathe Activate",Create_Date:'08/03/2023',Update_Date:'08/03/2023',file:'path file'} )
MERGE (Robot_Drop_piece1:piece1 {Name : "Robot Lathe Drop",Create_Date:'08/03/2023',Update_Date:'08/03/2023',file:'path file'} )
MERGE (Robot_Pick2_piece1:piece1 {Name : "Robot Melling Pick",Create_Date:'08/03/2023',Update_Date:'08/03/2023',file:'path file'} )
MERGE (Melling_piece1:piece1 {Name : "CNC Melling Activate",Create_Date:'08/03/2023',Update_Date:'08/03/2023',file:'path file'} )
MERGE (Robot_Drop2_piece1:piece1 {Name : "Robot Melling Drop",Create_Date:'08/03/2023',Update_Date:'08/03/2023',file:'path file'} )
MERGE (Inspection_piece1:piece1 {Name : "Inspection Activate",Create_Date:'08/03/2023',Update_Date:'08/03/2023',file:'path file'} )
MERGE (Ubicate_piece1:piece1 {Name : "ASRS Ubicate piece",Create_Date:'08/03/2023',Update_Date:'08/03/2023',file:'path file'})

// Tareas pieza 2
MERGE (Get_Material_piece2:piece2 {Name : "ASRS Get Material",Create_Date:'08/03/2023',Update_Date:'08/03/2023',file:'path file'} )
MERGE (Robot_Pick_piece2:piece2 {Name : "Robot Lathe Pick",Create_Date:'08/03/2023',Update_Date:'08/03/2023',file:'path file'} )
MERGE (Lathing_piece2:piece2 {Name : "CNC Lathe Activate",Create_Date:'08/03/2023',Update_Date:'08/03/2023',file:'path file'} )
MERGE (Robot_Drop_piece2:piece2 {Name : "Robot Lathe Drop",Create_Date:'08/03/2023',Update_Date:'08/03/2023',file:'path file'} )
MERGE (Inspection_piece2:piece2 {Name : "Inspection Activate",Create_Date:'08/03/2023',Update_Date:'08/03/2023',file:'path file'} )
MERGE (Ubicate_piece2:piece2 {Name : "ASRS Ubicate piece",Create_Date:'08/03/2023',Update_Date:'08/03/2023',file:'path file'})

// Tareas pieza 3
MERGE (Get_Material_piece3:piece3 {Name : "ASRS Get Material",Create_Date:'08/03/2023',Update_Date:'08/03/2023',file:'path file'} )
MERGE (Robot_Pick_piece3:piece3 {Name : "Robot Lathe Pick",Create_Date:'08/03/2023',Update_Date:'08/03/2023',file:'path file'} )
MERGE (Lathing_piece3:piece3 {Name : "CNC Lathe Activate",Create_Date:'08/03/2023',Update_Date:'08/03/2023',file:'path file'} )
MERGE (Robot_Drop_piece3:piece3 {Name : "Robot Lathe Drop",Create_Date:'08/03/2023',Update_Date:'08/03/2023',file:'path file'} )
MERGE (Inspection_piece3:piece3 {Name : "Inspection Activate",Create_Date:'08/03/2023',Update_Date:'08/03/2023',file:'path file'} )
MERGE (Ubicate_piece3:piece3 {Name : "ASRS Ubicate piece",Create_Date:'08/03/2023',Update_Date:'08/03/2023',file:'path file'})


// RELACIONES

// RELACION PASOS - MAQUINA
MERGE (Get_Material_piece1)-[:MACHINE]->(Storage)
MERGE (Robot_Pick_piece1)-[:MACHINE]->(Mitsubishi1)
MERGE (Lathing_piece1)-[:MACHINE]->(CNC_Lathe)
MERGE (Robot_Drop_piece1)-[:MACHINE]->(Mitsubishi1)
MERGE (Robot_Pick2_piece1)-[:MACHINE]->(Mitsubishi2)
MERGE (Melling_piece1)-[:MACHINE]->(CNC_Melling)
MERGE (Robot_Drop2_piece1)-[:MACHINE]->(Mitsubishi2)
MERGE (Inspection_piece1)-[:MACHINE]->(UR3)
MERGE (Ubicate_piece1)-[:MACHINE]->(Storage)

MERGE (Get_Material_piece2)-[:MACHINE]->(Storage)
MERGE (Robot_Pick_piece2)-[:MACHINE]->(Mitsubishi1)
MERGE (Lathing_piece2)-[:MACHINE]->(CNC_Lathe)
MERGE (Robot_Drop_piece2)-[:MACHINE]->(Mitsubishi1)
MERGE (Inspection_piece2)-[:MACHINE]->(UR3)
MERGE (Ubicate_piece2)-[:MACHINE]->(Storage)

MERGE (Get_Material_piece3)-[:MACHINE]->(Storage)
MERGE (Robot_Pick_piece3)-[:MACHINE]->(Mitsubishi1)
MERGE (Lathing_piece3)-[:MACHINE]->(CNC_Lathe)
MERGE (Robot_Drop_piece3)-[:MACHINE]->(Mitsubishi1)
MERGE (Inspection_piece3)-[:MACHINE]->(UR3)
MERGE (Ubicate_piece3)-[:MACHINE]->(Storage)

//RELACIONES ENTRE PASOS

MERGE (Get_Material_piece1)-[:STEP2]->(Robot_Pick_piece1)
MERGE (Robot_Pick_piece1)-[:STEP3]->(Lathing_piece1)
MERGE (Lathing_piece1)-[:STEP4]->(Robot_Drop_piece1)
MERGE (Robot_Drop_piece1)-[:STEP5]->(Robot_Pick2_piece1)
MERGE (Robot_Pick2_piece1)-[:STEP6]->(Melling_piece1)
MERGE (Melling_piece1)-[:STEP7]->(Robot_Drop2_piece1)
MERGE (Robot_Drop2_piece1)-[:STEP8]->(Inspection_piece1)
MERGE (Inspection_piece1)-[:STEP9]->(Ubicate_piece1)

MERGE (Get_Material_piece2)-[:STEP2]->(Robot_Pick_piece2)
MERGE (Robot_Pick_piece2)-[:STEP3]->(Lathing_piece2)
MERGE (Lathing_piece2)-[:STEP4]->(Robot_Drop_piece2)
MERGE (Robot_Drop_piece2)-[:STEP5]->(Inspection_piece2)
MERGE (Inspection_piece2)-[:STEP6]->(Ubicate_piece2)

MERGE (Get_Material_piece3)-[:STEP2]->(Robot_Pick_piece3)
MERGE (Robot_Pick_piece3)-[:STEP3]->(Lathing_piece3)
MERGE (Lathing_piece3)-[:STEP4]->(Robot_Drop_piece3)
MERGE (Robot_Drop_piece3)-[:STEP5]->(Inspection_piece3)
MERGE (Inspection_piece3)-[:STEP6]->(Ubicate_piece3)