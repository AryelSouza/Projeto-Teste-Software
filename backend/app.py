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
    {"id": 1, "nome": "Ana", "ativo": True, "senha": "senha123", "tipo": "usuario"},
    {"id": 2, "nome": "João", "ativo": True, "senha": "abc123", "tipo": "usuario"},
    {"id": 3, "nome": "Admin", "ativo": True, "senha": "admin123", "tipo": "admin"}
]
emprestimos = []  # Log de empréstimos
proximo_id_livro = 3

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
            return jsonify({
                "status": "sucesso", 
                "mensagem": "Login realizado",
                "usuario": {
                    "id": usuario["id"],
                    "nome": usuario["nome"],
                    "tipo": usuario["tipo"]
                }
            }), 200
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
        data = request.json
        usuario_id = data.get('usuario_id') if data else None
        
        livro = next((l for l in livros if l['id'] == livro_id), None)
        if not livro:
            return jsonify({"erro": "Livro não encontrado"}), 404
        
        if not livro['disponivel']:
            return jsonify({"erro": "Livro indisponível"}), 400
        
        livro['disponivel'] = False
        
        # Registra o empréstimo
        from datetime import datetime
        emprestimo = {
            "id": len(emprestimos) + 1,
            "livro_id": livro_id,
            "titulo_livro": livro['titulo'],
            "usuario_id": usuario_id,
            "data_emprestimo": datetime.now().isoformat(),
            "data_devolucao": None
        }
        emprestimos.append(emprestimo)
        
        return jsonify({"mensagem": "Livro emprestado com sucesso", "emprestimo_id": emprestimo["id"]}), 200
    except Exception as e:
        return jsonify({"erro": f"Erro interno: {str(e)}"}), 500

# Rotas de Admin
@app.route('/admin/livros', methods=['POST'])
def adicionar_livro():
    try:
        data = request.json
        titulo = data.get('titulo')
        
        if not titulo:
            return jsonify({"erro": "Título é obrigatório"}), 400
        
        global proximo_id_livro
        novo_livro = {
            "id": proximo_id_livro,
            "titulo": titulo,
            "disponivel": True
        }
        livros.append(novo_livro)
        proximo_id_livro += 1
        
        return jsonify({"mensagem": "Livro adicionado com sucesso", "livro": novo_livro}), 201
    except Exception as e:
        return jsonify({"erro": f"Erro interno: {str(e)}"}), 500

@app.route('/admin/devolver/<int:emprestimo_id>', methods=['POST'])
def devolver_livro(emprestimo_id):
    try:
        emprestimo = next((e for e in emprestimos if e['id'] == emprestimo_id and e['data_devolucao'] is None), None)
        if not emprestimo:
            return jsonify({"erro": "Empréstimo não encontrado ou livro já devolvido"}), 404
        
        # Marca o livro como disponível
        livro = next((l for l in livros if l['id'] == emprestimo['livro_id']), None)
        if livro:
            livro['disponivel'] = True
        
        # Registra a devolução
        from datetime import datetime
        emprestimo['data_devolucao'] = datetime.now().isoformat()
        
        return jsonify({"mensagem": "Livro devolvido com sucesso"}), 200
    except Exception as e:
        return jsonify({"erro": f"Erro interno: {str(e)}"}), 500

@app.route('/admin/emprestimos', methods=['GET'])
def listar_emprestimos():
    try:
        return jsonify(emprestimos), 200
    except Exception as e:
        return jsonify({"erro": f"Erro interno: {str(e)}"}), 500

@app.route('/admin/emprestimos/ativos', methods=['GET'])
def listar_emprestimos_ativos():
    try:
        emprestimos_ativos = [e for e in emprestimos if e['data_devolucao'] is None]
        return jsonify(emprestimos_ativos), 200
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
