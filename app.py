from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, Flask !!</h1>', 200


@app.route('/versao')
def versao():
    versao = "1.1.0"
    return f"App v{versao}"


@app.get("/saudar/<usuario>") 
def bemvindo(usuario):
   return f"<h1>Bem-vindo, {usuario.capitalize()}!<h1>"


@app.route('/quadrado/<int:n>')
def quadrado(n):
    resultado = n ** 2
    return f"{n}² = {resultado}"


@app.route('/home')
def home():
    return redirect('/')


@app.route('/pagina')
def pagina():
    return render_template("pagina.html")