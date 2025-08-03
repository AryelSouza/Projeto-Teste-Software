# Projeto de Teste de Software - Sistema de Biblioteca

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.3.3-green)
![Selenium](https://img.shields.io/badge/Selenium-4.15.0-orange)
![Tests](https://img.shields.io/badge/Tests-13_Passing-brightgreen)

Este projeto é um sistema de gerenciamento de biblioteca desenvolvido para demonstrar práticas de teste de software. Inclui testes unitários, de API e end-to-end (E2E) com **ChromeDriver funcionando perfeitamente**.

## ✨ Funcionalidades

- 🔐 Login de usuários
- 📚 Listagem de livros  
- 📖 Empréstimo de livros
- 🔄 Reset do banco de dados (para testes)
- 🧪 Suite completa de testes automatizados

## 🛠️ Tecnologias
- **Backend:** Python com Flask
- **Frontend:** HTML, CSS e JavaScript
- **Testes:** pytest, unittest, Selenium WebDriver
- **Banco de Dados:** Dados em memória (simulado)
- **Automação:** Scripts PowerShell/Batch para execução completa

## 📋 Pré-requisitos
- Python 3.10 ou superior
- pip (gerenciador de pacotes Python)
- Google Chrome (para testes E2E)
- Windows PowerShell (recomendado)

## 🚀 Instalação
Siga os passos abaixo para configurar o ambiente:

### Windows (PowerShell)
```powershell
# 1. Clonar o repositório
git clone https://github.com/seu-usuario/Projeto-Teste-Software.git
cd Projeto-Teste-Software

# 2. Criar e ativar ambiente virtual  
python -m venv venv
.\venv\Scripts\Activate.ps1

# 3. Instalar dependências do projeto
pip install -r requirements.txt
```

### Linux/Mac (Bash)
```bash
# 1. Clonar o repositório
git clone https://github.com/seu-usuario/Projeto-Teste-Software.git
cd Projeto-Teste-Software

# 2. Criar e ativar ambiente virtual
python3 -m venv venv
source venv/bin/activate

# 3. Instalar dependências do sistema (se necessário)
sudo apt install python3-venv  # Ubuntu/Debian

# 4. Instalar dependências do projeto
pip install -r requirements.txt
```

## 🖥️ Executando o Sistema

### Iniciar o servidor backend
```bash
python backend/app.py
```
**O servidor estará disponível em:** http://localhost:5000
## Acessar o front-end
Abra o navegador e acesse: **http://localhost:5000/**

**Credenciais de teste:**
- **Usuário:** Ana  
- **Senha:** senha123

## 🧪 Executando os Testes

### Método 1: Automático (Recomendado) 🚀
Use os scripts prontos para executar todos os testes com servidor automático:

**Windows PowerShell:**
```powershell
.\run_tests.ps1
```

**Windows CMD:**
```cmd
run_tests.bat
```

### Método 2: Manual 🔧
Para executar os testes manualmente, você precisa de **dois terminais**:

**Terminal 1 - Servidor:**
```bash
# Ativar ambiente virtual
cd Projeto-Teste-Software
.\venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Iniciar servidor
python backend/app.py
```

**Terminal 2 - Testes:**
```bash
# Ativar ambiente virtual
cd Projeto-Teste-Software
.\venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Executar testes específicos
pytest tests/unit/ -v          # Testes Unitários
pytest tests/api/ -v           # Testes de API  
pytest tests/e2e/ -v           # Testes End-to-End
pytest -v                      # Todos os testes
```

### Comandos Úteis de Teste 🎯
```bash
# Testar apenas funcionalidade de login
pytest tests/e2e/test_login.py -v

# Testar apenas funcionalidade de empréstimos
pytest tests/e2e/test_emprestimo.py -v

# Executar com saída detalhada (debug)
pytest tests/e2e/ -v -s

# Executar um teste específico
pytest tests/e2e/test_login.py::TestLogin::test_login_sucesso -v
```

## 📊 Resultados Esperados
Quando tudo estiver funcionando corretamente:
- ✅ **Testes Unitários:** 5 testes passando
- ✅ **Testes de API:** 4 testes passando  
- ✅ **Testes E2E:** 4 testes passando
- 🎉 **Total:** 13 testes passando

## 🛠️ Solução de Problemas

### Problema: ChromeDriver não funciona
```bash
# Limpar cache do WebDriver Manager
rm -rf ~/.wdm  # Linux/Mac
# rmdir /s %USERPROFILE%\.wdm  # Windows

# O webdriver-manager baixará automaticamente a versão correta
```

### Problema: Servidor não responde
```bash
# Verificar se a porta 5000 está ocupada
netstat -an | findstr "5000"  # Windows  
# lsof -i :5000               # Linux/Mac

# Matar processos na porta 5000 se necessário
taskkill /F /IM python.exe    # Windows
# pkill -f "python backend/app.py"  # Linux/Mac
```

### Problema: Ambiente virtual corrompido
```bash
# Remover e recriar ambiente virtual
rmdir /s venv                 # Windows
# rm -rf venv                 # Linux/Mac

python -m venv venv
.\venv\Scripts\activate       # Windows
# source venv/bin/activate    # Linux/Mac

pip install -r requirements.txt
```

## 🏆 Status do Projeto
- ✅ ChromeDriver funcionando corretamente
- ✅ Servidor Flask configurado  
- ✅ Testes automatizados implementados
- ✅ Interface web responsiva
- ✅ Scripts de automação prontos

**Projeto pronto para uso e demonstração! 🎉**
