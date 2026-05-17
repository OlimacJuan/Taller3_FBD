from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from datetime import datetime

app = FastAPI()

# Configuración de MongoDB
# Suponiendo conexión local, cámbialo a tu URI de Mongo Atlas si es necesario
client = MongoClient("mongodb://ISIS2304F07202610:dEmoxvDtNaSn@157.253.236.88:8087/?authSource=admin")
db = client["ISIS2304F07202610"]
coleccion_comentarios = db["comentarios_bares"]
coleccion_eventos = db["eventos"]

@app.get("/bares/{bar_id}/comentarios")
def obtener_comentarios(bar_id: int):
    """
    Retorna todos los comentarios del bar cuyo ID llega por la URL.
    La colección se llama comentarios_bares. El campo de filtro es bar_id.
    """
    # TODO: Completar consulta a MongoDB
    comentarios = list(coleccion_comentarios.find({"bar_id": bar_id}))
    
    # Formateamos el _id de ObjectId a string para poder retornarlo como JSON
    for c in comentarios:
        c["_id"] = str(c["_id"])
        
    return comentarios

@app.post("/bares/{bar_id}/comentarios")
def crear_comentario(bar_id: int, datos: dict):
    """
    Inserta el documento datos en la colección comentarios_bares. 
    """
    # El bar_id y la fecha ya están agregados al documento antes del TODO.
    datos["bar_id"] = bar_id
    datos["fecha"] = datetime.now().isoformat()
    
    # TODO: Completar la inserción
    resultado = coleccion_comentarios.insert_one(datos)
    
    return {"mensaje": "Comentario creado", "id": str(resultado.inserted_id)}

@app.get("/bares/{bar_id}/eventos")
def obtener_eventos(bar_id: int):
    """
    Retorna todos los eventos del bar cuyo ID llega por la URL.
    La colección en MongoDB se llama eventos.
    """
    # TODO: Completar consulta a MongoDB
    eventos = list(coleccion_eventos.find({"bar_id": bar_id}))
    
    for e in eventos:
        e["_id"] = str(e["_id"])
        
    return eventos

@app.post("/bares/{bar_id}/eventos")
def crear_evento(bar_id: int, datos: dict):
    """
    Reciba un documento con la información del evento, le agregue el bar_id 
    y la fecha_creacion, y lo inserte en la colección eventos.
    """
    # El bar_id y la fecha_creacion ya están agregados al documento antes del TODO
    datos["bar_id"] = bar_id
    datos["fecha_creacion"] = datetime.now().isoformat()
    
    # TODO: Completar la inserción
    resultado = coleccion_eventos.insert_one(datos)
    
    return {"mensaje": "Evento creado", "id": str(resultado.inserted_id)}
