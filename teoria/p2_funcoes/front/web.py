# pip3 install flask
# which pip3 -  caminho da instalacao do pip3
import sys  
sys.path.append('teoria/p2_funcoes')

from back.historico import ler_historico
from back.calculadora import soma, subtracao, multiplicacao, divisao
from teste import funcao_teste

from flask import Flask, render_template, request

app = Flask(__name__)

titulo_app = 'Calculadora Olist'

@app.route('/')
def index():
    somar = {'nome':'somar', 'rota':'/somar' }
    subtrair = {'nome':'subtrair', 'rota':'/subtrair' }
    multiplicar = {'nome':'multiplicar', 'rota':'/multiplicar' }
    dividir = {'nome':'dividir', 'rota':'/dividir' }
    #historico = {'nome':'historico', 'rota':'/historico' }
    lista = [somar, subtrair, multiplicar, dividir]#, historico]
    return render_template('index.html', nome=titulo_app, lista=lista )

@app.route('/calcular')
def calcular():
    n1 = float(request.args.get('num1'))
    n2 = float(request.args.get('num2'))
    operacao = request.args.get('operacao')
    if operacao == 'somar':
        resultado = soma(n1, n2)
    elif operacao == 'subtrair':
        resultado = subtracao(n1, n2)
    elif operacao == 'multiplicar':    
        resultado = multiplicacao(n1, n2)
    elif operacao == 'dividir':
        resultado = divisao(n1, n2)
    else:
        return 'Operação invalida'
    return f'O resultado da {operacao} entre {n1} e {n2} é {resultado}' 

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