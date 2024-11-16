import sqlite3
from flask import Flask, render_template, request, redirect 
from dati import pievienot_lietotaju

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def index():
    
    return render_template("index.html")

@app.route("/pievienot", methods=["POST","GET"])
def pievienot():
    if request.method == "POST":
        vards = request.form['name'].capitalize()
        uzvards = request.form['surname'].capitalize()
        lietotajvards = request.form['username'].capitalize()
        if vards and uzvards:
            pievienot_lietotaju(vards, uzvards, lietotajvards)
    return render_template("pievienot.html")

@app.route("/registracija")
def registracija():
    return render_template("registracija.html")







if __name__ == '__main__':
    app.run(debug=True, port = 5000)