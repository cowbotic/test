from flask import Flask, render_template, url_for, request
import os, socket, sys, random, time, math, functools

#####################################################################
#Métodos de ayuda y cálculo
def sample(p):
    x, y = random.random(),random.random()
    return 1 if x*x + y*y < 1 else 0

def calcula_pi(p):
    return 4.0*(functools.reduce(lambda a, b: a + b, map(sample,range(0, p))))/p

#####################################################################

app = Flask(__name__)

@app.route('/')
def hello():
  return render_template('hello.html')

@app.route("/maquina")
def maquina():
    machine_name=socket.gethostname()
    return render_template('maquina.html',machine=machine_name)

@app.route('/calcula', methods=['GET', 'POST'])
def calcula():
    if request.method=='POST':
        num_puntos=int(request.form['primercampo'])
        start_time = time.time()
        valor=calcula_pi(num_puntos)
        tiempo = time.time()-start_time
        error=abs(math.pi-valor)

        return render_template('calculado.html', puntos=num_puntos, valor=valor, tiempo=tiempo, error=error)
    else :
        return render_template('calcula.html')

if __name__ == '__main__':
  app.run()


