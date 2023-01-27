// Maquinas
MERGE (maquina1:machine {name : "Maquina_Torno"} )
MERGE (maquina2:machine {name : "Robot_Torno"} )
MERGE (maquina3:machine {name : "Maquina_CM"} ) //CM CENTRO MECANIZADO
MERGE (maquina4:machine {name : "Robot_CM"} )
MERGE (maquina5:machine {name : "Robot_Inspeccion"} )

// Procesos
MERGE (proceso1:proccess {name : "Torno"} )
MERGE (proceso2:proccess {name : "CM"} )
MERGE (proceso3:proccess {name : "Inspeccion"} )

// Piezas
MERGE (pieza1:piece {name : "Ficha_ajedrez"} )
MERGE (pieza2:piece {name : "Estrella"} )

// Materiales
MERGE (material_1:material {name : "Metal"} )
MERGE (material_2:material {name : "Plastico"} )

// Ordenes
MERGE (orden_1:order {name : "Orden_1"} )
MERGE (orden_2:order {name : "Orden_2"} )

// RELACIONES

// RELACION CELDA - ORDENES
MERGE (celda)-[:ORDER]->(orden_1)
MERGE (celda)-[:ORDER]->(orden_2)

// RELACION ORDEN - PIEZA
MERGE (orden_1)-[:PIECE]->(pieza1)
MERGE (orden_2)-[:PIECE]->(pieza2)

// RELACION PIEZA - PROCESO
MERGE (pieza1)-[:PROCESS]->(proceso1)
MERGE (pieza1)-[:PROCESS]->(proceso2)
MERGE (pieza2)-[:PROCESS]->(proceso2)
MERGE (pieza2)-[:PROCESS]->(proceso3)

// RELACION PIEZA - MATERIAL
MERGE (pieza1)-[:MATERIAL]->(material_1)
MERGE (pieza2)-[:MATERIAL]->(material_2)

// RELACION PROCESO - MAQUINA
MERGE (proceso1)-[:MACHINE]->(maquina1)
MERGE (proceso1)-[:MACHINE]->(maquina2)
MERGE (proceso2)-[:MACHINE]->(maquina3)
MERGE (proceso2)-[:MACHINE]->(maquina4)
MERGE (proceso3)-[:MACHINE]->(maquina5)
