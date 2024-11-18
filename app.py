from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/')
def ola_mundo():
    return "a api está no ar"

@app.route('/media_produtos/')
def mediaprodutos():
    dados = pd.read_csv('./basestratadas/Dados_Kabum_trt.csv')
    media_preco = dados['Preço'].mean()
    resposta = {'media_preco': media_preco}
    return jsonify(resposta)

@app.route('/mediana_produtos/')
def medianaprodutos():
    dados = pd.read_csv('./basestratadas/Dados_Kabum_trt.csv')
    mediana_preco = dados['Preço'].median()
    resposta = {'mediana_preco': mediana_preco}
    return jsonify(resposta)


app.run(debug=True)