from flask import Blueprint, request, jsonify
import sqlite3

# Definindo o Blueprint
avaliacao = Blueprint('avaliacao', __name__)

# Função para conectar ao banco de dados
def conectar_db():
    conn = sqlite3.connect('avaliacao.db')
    conn.row_factory = sqlite3.Row
    return conn

# Rota para inserir dados da avaliação
@avaliacao.route('/avaliacao', methods=['POST'])
def inserir_avaliacao():
    dados = request.json

    nome = dados.get('nome')
    email = dados.get('email')
    experiencia_geral = dados.get('experiencia_geral')
    contribuicao_engajamento = dados.get('contribuicao_engajamento')
    expectativa_feedback = dados.get('expectativa_feedback')
    motivacao_aprendizado = dados.get('motivacao_aprendizado')
    aspectos_mais_gostou = dados.get('aspectos_mais_gostou')
    interesse_futuro = dados.get('interesse_futuro')

    # Validação básica
    if not nome or not email:
        return jsonify({"error": "Nome e email são obrigatórios"}), 400

    conn = conectar_db()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO avaliacoes (
            nome, email, experiencia_geral, contribuicao_engajamento,
            expectativa_feedback, motivacao_aprendizado, aspectos_mais_gostou, interesse_futuro
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        nome, email, experiencia_geral, contribuicao_engajamento,
        expectativa_feedback, motivacao_aprendizado, aspectos_mais_gostou, interesse_futuro
    ))

    conn.commit()
    conn.close()

    return jsonify({"message": "Avaliação registrada com sucesso!"}), 201
