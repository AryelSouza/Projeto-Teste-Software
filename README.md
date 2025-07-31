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

#1. Instalar dependências:
```bash
pip install -r requirements.txt
#2.Iniciar aplicação
python backend/app.py
#3.Executar testes
# Todos os testes
pytest
# Testes específicos
pytest tests/unit/test_livro.py
pytest tests/api/test_api.py
