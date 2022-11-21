from flask import Flask, render_template, request
from datetime import time

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    legend = 'Monthly Data'
    labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    values = [10, 9, 8, 7, 6, 4, 7, 8]
    return render_template("index.html", values=values, labels=labels, legend=legend)

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
           

if __name__ == "__main__":
    app.run(host= "0.0.0.0", port= 8000)

