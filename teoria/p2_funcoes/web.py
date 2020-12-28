# pip3 install flask
# which pip3 -  caminho da instalacao do pip3
from flask import Flask, render_template
from historico import ler_historico
from calculadora import soma, subtracao, multiplicacao, divisao

app = Flask(__name__)

titulo_app = 'Calculadora Olist'

@app.route('/')
def index():
    somar = {'nome':'somar', 'rota':'/somar' }
    subtrair = {'nome':'subtrair', 'rota':'/subtrair' }
    multiplicar = {'nome':'multiplicar', 'rota':'/multiplicar' }
    dividir = {'nome':'dividir', 'rota':'/dividir' }
    historico = {'nome':'historico', 'rota':'/historico' }
    lista = [somar, subtrair, multiplicar, dividir, historico]
    return render_template('index.html', nome=titulo_app, lista=lista )

@app.route('/somar')
def somar():
    n1 = 3.0
    n2 = 5.0
    resultado = soma(n1, n2)
    return render_template('somar.html',nome=titulo_app, resultado=resultado)

@app.route('/subtrair')
def subtrair():
    n1 = 3.0
    n2 = 5.0
    resultado = subtracao(n1, n2)
    return render_template('subtrair.html',nome=titulo_app, resultado=resultado)
    
@app.route('/multiplicar')
def multiplicar():
    n1 = 3.0
    n2 = 5.0
    resultado = multiplicacao(n1, n2)
    return render_template('multiplicar.html',nome=titulo_app, resultado=resultado)

@app.route('/dividir')
def dividir():
    n1 = 10.0
    n2 = 3.0
    resultado = divisao(n1, n2)
    resultado = f'{resultado:.2f}'
    return render_template('dividir.html',nome=titulo_app, resultado=resultado)

@app.route('/historico') 
def listar_historico():
    lista_linhas = ler_historico()
    return render_template('historico.html', lista = lista_linhas)
app.run(debug=True)

