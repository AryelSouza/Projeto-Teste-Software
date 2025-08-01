# Requisitos do Sistema

## Requisitos Funcionais
1. RF01: Login de usuário
   - O sistema deve permitir que usuários autentiquem com CPF e senha
   
2. RF02: Cadastro de livros
   - Bibliotecários devem poder cadastrar novos livros
   
3. RF03: Empréstimo de livros
   - Sistema deve registrar empréstimos vinculando usuário e livro
   - Não permitir empréstimo se livro estiver indisponível

## Requisitos Não Funcionais
1. RNF01: Performance
   - Tempo de resposta < 2s para 90% das requisições
   
2. RNF02: Segurança
   - Autenticação via JWT
   - Proteção contra ataques de injeção SQL
