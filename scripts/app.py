from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/')
def ola_mundo():
    return "a api está no ar"

@app.route('/soma_produtos/')
def somaprodutos():
    dados = pd.read_csv('../basestratadas/Dados_Kabum_trt.csv')
    total_preco = dados['Preço'].sum()
    resposta = {'total_preco': total_preco}
    return jsonify(resposta)

app.run(debug=True)