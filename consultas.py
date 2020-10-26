from pymongo import MongoClient

cliente = MongoClient {'localhost', 27017} #instancia de coneción
db = cliente['ejemplo'] #accedemos a la tabla específica
coleccion = db.tabla1 # se crea la tabla o se accede segun sea el caso

def obtener_todo():
    cursor = coleccion.find()
    return list(cursor)

def obtener_uno(titulo):
    resultado = coleccion.find_one({'nombre': titulo})
    return resultado

def insertar_uno(datos):
    id = coleccion.insert_one(datos)
    return id

def editar_uno(nombre, datos):
    resultado = coleccion.update_one({'nombre': nombre},
        {'$set' {'correo': datos['correo']}})
    return str(resultado)