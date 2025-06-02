import requests
from flask import Flask, request, jsonify, send_from_directory
from model.Avaliacao import avaliacao
from controller.email_route import email_bp
from flask_cors import CORS
import os
from main import feedbackia

# Criação do app Flask
app = Flask(__name__, static_folder="static")
CORS(app)  # Libera CORS para todas as rotas

# Registro de blueprints
app.register_blueprint(avaliacao, url_prefix='/avaliacao')
app.register_blueprint(email_bp, url_prefix='/avaliacao')
app.register_blueprint(feedbackia)

# Rota principal – serve a entrevista
@app.route('/')
def index():
    try:
        return send_from_directory('.', 'entrevista.html')
    except FileNotFoundError:
        return 'entrevista.html não encontrado', 404

# Rota /avaliacao – pode ser usada para testes ou render de uma segunda página
@app.route('/avaliacao')
def avaliacao_page():
    try:
        return send_from_directory('.', 'index.html')
    except FileNotFoundError:
        return 'index.html não encontrado', 404

# Serve arquivos estáticos da pasta /css
@app.route('/css/<path:filename>')
def serve_css(filename):
    return send_from_directory('css', filename)

# Serve arquivos estáticos da pasta /js
@app.route('/js/<path:filename>')
def serve_js(filename):
    return send_from_directory('js', filename)

# Serve arquivos de mídia da pasta /asset (como vídeos 360)
@app.route('/asset/<path:filename>')
def serve_asset(filename):
    return send_from_directory('asset', filename)

# Exemplo de endpoint para o tempo 00:24 do vídeo
@app.route('/mensagem_ia', methods=['POST'])
def acao_24_segundos():
    print("Requisição recebida aos 24 segundos!")
    return jsonify({"mensagem": "Requisição recebida com sucesso!"}), 200

# Executa o servidor
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)

