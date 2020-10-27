from flask import Flask, render_template, request, redirect, url_for
from consultas import obtener_todo, obtener_uno, editar_uno
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def indice():
    usuarios = obtener_todo
    return render_template('indice.html', usuarios=usuarios)

if __name__ == "__main__":
    app.run()