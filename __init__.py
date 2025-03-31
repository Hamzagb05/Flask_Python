from flask import Flask
from flask import render_template
from flask import json

app = Flask(name)

@app.route('/<int:valeur>')
def exercice(valeur):
    etoiles = ''
    for i in range(valeur):
        etoiles += '' valeur + '<br>'
    return etoiles

if name == "main":
    app.run(debug=True)
