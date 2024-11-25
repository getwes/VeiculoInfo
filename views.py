from main import app

#rotas
@app.route("/")
def homepage():
    return "meu site no flask"

@app.route("/blog")
def blog():
    return "meu blog"