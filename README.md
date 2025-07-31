# Projeto de Teste de Software - Sistema de Biblioteca

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.2.3-green)

Repositório com implementação e testes de um sistema de gerenciamento de biblioteca

## 📂 Estrutura do Projeto
backend/ - Implementação do sistema

tests/ - Testes automatizados (E2E, unitários e API)

docs/ - Documentação e evidências de testes

scripts/ - Scripts auxiliares

## ⚙️ Como Executar
```bash
#0. Crie e ative o ambiente virtual:
python3 -m venv venv
source venv/bin/activate

#1. Instalar dependências:
pip install -r requirements.txt

#2.Iniciar aplicação
python backend/app.py

#3.Executar testes
# Todos os testes
pytest
# Testes específicos
pytest tests/unit/test_livro.py
pytest tests/api/test_api.py

#4.Para desativar o ambiente virtual após o uso:
deactivate
