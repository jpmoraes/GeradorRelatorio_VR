from flask import Blueprint, request, jsonify
from controller.enviar_email import enviar_email

email_bp = Blueprint('email', __name__)

@email_bp.route('/enviar-email', methods=['POST'])
def enviar_email_route():
    data = request.get_json()
    nome = data.get('nome')
    email = data.get('email')

    if not nome or not email:
        return jsonify({"error": "Nome e e-mail são obrigatórios."}), 400

    try:
        assunto = "Documentos Gerados"
        corpo = f"Olá {nome}, segue o documento de avaliação em anexo. Obrigado por participar da atividade imersiva!"
        anexo_path = "resultado.pdf"
        enviar_email(email, assunto, corpo, anexo_path)
        return jsonify({"message": "E-mail enviado com sucesso."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
