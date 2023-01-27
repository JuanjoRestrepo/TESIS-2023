// Creamos Nodos

// Estructura
// CREATE(NODO:ETIQUETA {PROPIEDAD: ""})

CREATE (luis:person {name: "Luis"})
CREATE (felipe:person {name: "Felipe"})
CREATE (carlos:person {name: "Carlos"})
CREATE (andres:person {name: "Andres"})

// Universidades
CREATE (ud:universidad {name: "U_distrital"})
CREATE (jave:universidad {name: "U_Javeriana"})

// Deportes
CREATE (futbol:deporte {name: "Futbol"})
CREATE (tenis:deporte {name: "Tenis"})

// Carreras
CREATE (ing_sistemas:carrera {name: "Ing_sistemas"})
CREATE (ing_electronica:carrera {name: "Ing_electronica"})

// Materias
CREATE (calc_diferencial:materia {name: "Calculo_diferencial"})

// Creamos Relaciones entre Nodos
CREATE (luis)-[:FRIENDS]->(felipe)
CREATE (felipe)-[:FRIENDS]->(carlos)
CREATE (luis)-[:FRIENDS]->(andres)
CREATE (luis)-[:FRIENDS]->(carlos)

CREATE (luis)-[:STUDENT]->(ud)
CREATE (felipe)-[:STUDENT]->(jave)
CREATE (carlos)-[:STUDENT]->(ud)
CREATE (andres)-[:STUDENT]->(jave)

CREATE (luis)-[:SUBJECT]->(calc_diferencial)
CREATE (felipe)-[:SUBJECT]->(calc_diferencial)
CREATE (carlos)-[:SUBJECT]->(calc_diferencial)
CREATE (andres)-[:SUBJECT]->(calc_diferencial)

CREATE (luis)-[:PLAYER]->(futbol)
CREATE (andres)-[:PLAYER]->(futbol)
CREATE (felipe)-[:PLAYER]->(tenis)

CREATE (luis)-[:CAREER]->(ing_sistemas)
CREATE (felipe)-[:CAREER]->(ing_electronica)
CREATE (carlos)-[:CAREER]->(ing_electronica)
CREATE (andres)-[:CAREER]->(ing_sistemas)


// VER TODOS LOS NODOS
// n para seleccionar todo
MATCH (n) RETURN n

// Actualizar NODO

MATCH (luis:person {name: "Luis"})
SET luis.birthday = date("2023")
RETURN luis

//Cambiamos Nombre a Luis

MATCH (luis:person {name: "Luis"})
SET luis.name = "Esteban"
RETURN luis

// DELETE
MATCH (carlos:person {name: "Carlos"})
DETACH DELETE carlos

// AGREGAMOS NUEVO NODO

CREATE (oscar:person {name: "Oscar"})

// Ahora si se hizo bien la relacion
MATCH (oscar:person), (ud:universidad)
WHERE oscar.name = "Oscar" AND ud.name = "U_distrital"
CREATE (oscar)-[:STUDENT]->(ud)

// QUEDO MAL
MATCH (oscar:person {name: "Oscar"})
DETACH DELETE oscar