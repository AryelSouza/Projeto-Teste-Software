# Script para inicialização do banco de dados
import sqlite3

conn = sqlite3.connect('biblioteca.db')
c = conn.cursor()

# Criar tabelas
c.execute('''CREATE TABLE IF NOT EXISTS livros
             (id INTEGER PRIMARY KEY, titulo TEXT, autor TEXT, disponivel BOOLEAN)''')

c.execute('''CREATE TABLE IF NOT EXISTS usuarios
             (id INTEGER PRIMARY KEY, nome TEXT, cpf TEXT UNIQUE, senha TEXT)''')

# Inserir dados de exemplo
c.execute("INSERT INTO livros (titulo, autor, disponivel) VALUES ('Clean Code', 'Robert Martin', 1)")
c.execute("INSERT INTO usuarios (nome, cpf, senha) VALUES ('Admin', '12345678900', 'senha123')")

conn.commit()
conn.close()
print("Banco de dados inicializado com sucesso!")
