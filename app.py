from flask import Flask, render_template, request
import math

app = Flask(__name__)

def calcular_gradiente(x, y):
    denominador = 3 * x * y + 2 * x ** 2 - y
    derivada_x = (3 * y + 4 * x) / denominador
    derivada_y = (3 * x - 1) / denominador
    return derivada_x, derivada_y

def producto_punto(v1, v2):
    return sum(a * b for a, b in zip(v1, v2))

def direccion_constante(gradiente):
    return (-gradiente[1], gradiente[0])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    x = float(request.form['x'])
    y = float(request.form['y'])
    
    grad_x, grad_y = calcular_gradiente(x, y)
    
    direccion_mayor_aumento = (grad_x, grad_y)
    
    direccion_equivocada = (1, -0.5)
    cambio_temp = producto_punto(direccion_mayor_aumento, direccion_equivocada)
  
    direccion_constante_temp = direccion_constante((grad_x, grad_y))

    return render_template('resultado.html', 
                           gradiente_x=grad_x, gradiente_y=grad_y, 
                           cambio_temp=cambio_temp, 
                           direccion_constante_x=direccion_constante_temp[0], 
                           direccion_constante_y=direccion_constante_temp[1])

if __name__ == '__main__':
    app.run(debug=True)
