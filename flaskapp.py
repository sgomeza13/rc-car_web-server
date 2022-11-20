from flask import Flask, render_template, request
import time
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")

@app.route('/adelante')
def adelante():
    print("adelante")
    return ("true")

@app.route('/atras')
def atras():
    print("atras")
    return ("true")

@app.route('/izquierda')
def izquierda():
    print("izquierda")
    return ("true")
    
@app.route('/derecha')
def derecha():
    print("derecha")
    return ("True")

@app.route('/detener')
def detener():
    print("detener")
    return ("true")
            
app.run(host= "0.0.0.0", port= 8000)

