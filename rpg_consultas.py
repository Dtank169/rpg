from pymongo import MongoClient

cliente = MongoClient('localhost', 27017)
#coleccion = db.prueba
db = cliente['dbrpg']
datos = db.usuario

def obtener_todo():
    cursor = datos.find()
    return list(cursor)

def obtener_uno(titulo):
    resultado = datos.find_one({'nombre': titulo})
    return resultado

def insertar_uno(datos):
    id = datos.insert_one(datos)
    return id

def editar_uno(nombre, datos):
    resultado = datos.update_one({'nombre': nombre}, 
        {'$set': {'tipo': datos['tipo']}})
    return str(resultado.modified_count)