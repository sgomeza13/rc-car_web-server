from flask import Flask, render_template, request
from datetime import time
import random
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    legend = 'Temperatura'
    labels = [  '12:00PM', '12:10PM', '12:20PM', '12:30PM', '12:40PM', '12:50PM',
                '1:00PM', '1:10PM', '1:20PM', '1:30PM', '1:40PM', '1:50PM',
                '2:00PM', '2:10PM', '2:20PM', '2:30PM', '2:40PM', '2:50PM']
    values = [random.randint(10,40) for _ in range(17)]
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

