# Projeto de Teste de Software - Sistema de Biblioteca

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.2.3-green)

Este projeto é um sistema de gerenciamento de biblioteca desenvolvido para demonstrar práticas de teste de software. Inclui testes unitários, de API e end-to-end (E2E).

Funcionalidades
Login de usuários

Listagem de livros

Empréstimo de livros

Reset do banco de dados (para testes)

Tecnologias
Backend: Python com Flask

Frontend: HTML, CSS e JavaScript

Testes: pytest, unittest, Selenium

Banco de Dados: Dados em memória (simulado)

Pré-requisitos
Python 3.10 ou superior

pip (gerenciador de pacotes Python)

Google Chrome (para testes E2E)

Instalação
Siga os passos abaixo para configurar o ambiente:

```bash
#1. Clonar o repositório
git clone https://github.com/seu-usuario/Projeto-Teste-Software.git
cd projeto-Teste-Software

#2. Criar e ativar ambiente virtual
python3 -m venv venv
source venv/bin/activate

#3. Instalar dependências do sistema (Linux)
sudo apt install python3.12-venv  # Use sua versão do Python

#4. Instalar dependências do projeto
pip install -r requirements.txt

#5.Executando o Sistema
#Iniciar o servidor backend
python backend/app.py
#O servidor estará disponível em: http://localhost:5000
```
## Acessar o front-end
Abra o navegador e acesse:
http://localhost:5000/static/index.html

Credenciais de teste:

Usuário: Ana

Senha: senha123

## Executando os Testes
Para executar os testes,abra outra janela do terminal enquanto a do servidor ainda esta rodando
```bash
#setup do venv na nova janela do terminal
cd Projeto-Teste-Software
source venv/bin/activate

#Testes Unitários
pytest tests/unit/
#Testes de API
pytest tests/api/
#Testes End-to-End (E2E)
pytest tests/e2e/
#Executar todos os testes
pytest
