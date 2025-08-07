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

## Requisitos Legais
1. LGPD (Lei Geral de Proteção de Dados - Lei nº 13.709/2018)
O sistema deve seguir a LGPD, pois coleta e armazena dados de usuários. Isso implica:

- Obter consentimento explícito para o uso de dados pessoais.

- Garantir o direito de acesso, correção, exclusão e portabilidade dos dados do usuário.

- Armazenar dados com segurança e protegê-los contra acesso não autorizado.

- Ter uma política de privacidade clara.

2. Código de Defesa do Consumidor (CDC - Lei nº 8.078/1990)
- Se a biblioteca for parte de uma instituição que oferece serviços aos usuários (por exemplo, cobrança de taxas por atraso ou reserva), o sistema deve:

- Informar de forma clara os termos de uso e eventuais cobranças.

- Permitir acesso a histórico de empréstimos e taxas.

