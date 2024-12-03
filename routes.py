from main import app
from flask import render_template

#rotas
@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/cadastro")
def blog():
    return render_template("cadastro.html")

@app.route("/acessoCliente")
def acessoCliente():
    return 
