from flask import Flask, render_template, request, redirect, url_for
from consultas import obtener_todo, obtener_uno, editar_uno
import json

app = Flask(__name__)

@app.route('/')
def indice():
    return render_template('indice.html')

@app.route('/dinamico/saludo')
def dinamico_saludo():
    saludo = 'Hola mundo!'
    suma = 3 + 4
    lista = ['A', 34, 'hola', 3.33, 'Flask', 'etc...']
    return render_template('saludo.html', datos=saludo, suma=suma, lista=lista)

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        return request.form['entrada']
    elif request.method == 'GET':
        return render_template('formulario.html')

@app.route('/consultas/todo')
def consultas_todo():
    consulta = obtener_todo()
    return render_template('consultar_todo.html', consulta=consulta)

@app.route('/consultas/<titulo>')
def consultas(titulo):
    resultado = obtener_uno(titulo)
    return render_template('consultar_uno.html', resultado=resultado)

@app.route('/edicion/<nombre>')
def edicion(nombre):
    datos = {'description': 'New description'}
    resultado = editar_uno(nombre, datos)
    return redirect(url_for('consultas_todo'))

if __name__ == "__main__":
    app.run()