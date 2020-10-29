from flask import Flask, render_template, request, redirect, url_for
from rpg_consultas import obtener_todo, obtener_uno, editar_uno
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def indice():
    usuarios = obtener_todo()
    tipo = "jugador"
    usuario = obtener_uno(tipo)
    return render_template('index.html', usuarios=usuarios, usuario=usuario)


if __name__ == "__main__":
    app.run()