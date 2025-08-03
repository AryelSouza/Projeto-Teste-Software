from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder='static')
CORS(app)

# Banco de dados simulado
livros = [
    {"id": 1, "titulo": "Python Testing", "disponivel": True},
    {"id": 2, "titulo": "Clean Code", "disponivel": True}
]
usuarios = [
    {"id": 1, "nome": "Ana", "ativo": True, "senha": "senha123"},
    {"id": 2, "nome": "João", "ativo": True, "senha": "abc123"}
]

@app.route('/')
def home():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return jsonify({"erro": "Usuário e senha são obrigatórios"}), 400
        
        usuario = next((u for u in usuarios if u['nome'] == username and u['senha'] == password), None)
        if usuario:
            return jsonify({"status": "sucesso", "mensagem": "Login realizado"}), 200
        else:
            return jsonify({"erro": "Credenciais inválidas"}), 401
    except Exception as e:
        return jsonify({"erro": f"Erro interno: {str(e)}"}), 500

@app.route('/livros', methods=['GET'])
def listar_livros():
    return jsonify(livros), 200

@app.route('/emprestar/<int:livro_id>', methods=['POST'])
def emprestar_livro(livro_id):
    try:
        livro = next((l for l in livros if l['id'] == livro_id), None)
        if not livro:
            return jsonify({"erro": "Livro não encontrado"}), 404
        
        if not livro['disponivel']:
            return jsonify({"erro": "Livro indisponível"}), 400
        
        livro['disponivel'] = False
        return jsonify({"mensagem": "Livro emprestado com sucesso"}), 200
    except Exception as e:
        return jsonify({"erro": f"Erro interno: {str(e)}"}), 500

@app.route('/reset', methods=['POST'])
def reset_database():
    global livros
    try:
        livros = [
            {"id": 1, "titulo": "Python Testing", "disponivel": True},
            {"id": 2, "titulo": "Clean Code", "disponivel": True}
        ]
        return jsonify({"mensagem": "Banco de dados resetado"}), 200
    except Exception as e:
        return jsonify({"erro": f"Erro ao resetar banco: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
