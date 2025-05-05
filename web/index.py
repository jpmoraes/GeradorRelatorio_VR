import requests
from flask import Flask, request, jsonify, send_from_directory
from model.Avaliacao import avaliacao
from controller.email_route import email_bp

app = Flask(__name__)

#Registrando o Blueprint no Flask com um prefixo '/model'
app.register_blueprint(avaliacao, url_prefix='/avaliacao')
app.register_blueprint(email_bp, url_prefix='/avaliacao')

@app.route('/')
def index():
    try:
        return send_from_directory('.', 'index.html')  # Serve index.html da pasta atual
    except FileNotFoundError:
        return 'index.html not found', 404

# Serve os arquivos CSS (no diretório css)
@app.route('/css/<path:filename>')
def serve_css(filename):
    return send_from_directory('css', filename)

# Serve os arquivos JavaScript (no diretório js)
@app.route('/js/<path:filename>')
def serve_js(filename):
    return send_from_directory('js', filename)

# Serve os arquivos de vídeo (no diretório asset)
@app.route('/asset/<path:filename>')
def serve_asset(filename):
    return send_from_directory('asset', filename)

# Iniciar o servidor Flask
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)