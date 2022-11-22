from flask import Flask, render_template, request
from datetime import time
import random
import serial
import datetime
labels = []
values = []
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=5)
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    temp = random.randint(10,40)
    hora = datetime.datetime.now()
    horaFormato = f'{hora.hour}:{hora.minute}:{hora.second}'
    legend = 'Temperatura'
    if (len(labels) <= 20): 
        labels.append(horaFormato)
        values.append(temp)
    labels.pop()
    values.pop()
    labels.append(horaFormato)
    values.append(temp)
    print(labels)
    print(values)
    return render_template("index.html", values=values, labels=labels, legend=legend)

@app.route('/adelante')
def adelante():
    ser.write(b'set on\n')
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
    ser.write(b'set off\n')
    print("detener")
    return ("true")
           

if __name__ == "__main__":
    app.run(host= "0.0.0.0", port= 8000)

