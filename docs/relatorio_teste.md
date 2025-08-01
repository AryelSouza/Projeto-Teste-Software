# Relatório de Testes - Sistema de Biblioteca

## Funcionalidades testadas:
1. RF01: Login de usuário
2. RF03: Empréstimo de livros

## Resultados dos testes:

### Testes de Login (RF01)
| Caso de Teste | Resultado | Evidência |
|---------------|-----------|-----------|
| Login com credenciais válidas | Sucesso | [login_sucesso.png](evidencias/login_sucesso.png) |
| Login com campos vazios | Falha | [login_falha.png](evidencias/login_falha.png) |

### Testes de Empréstimo (RF03)
| Caso de Teste | Resultado | Evidência |
|---------------|-----------|-----------|
| Empréstimo de livro disponível | Sucesso | [emprestimo_sucesso.png](evidencias/emprestimo_sucesso.png) |
| Tentativa de empréstimo de livro indisponível | Falha | [emprestimo_falha.png](evidencias/emprestimo_falha.png) |

## Conclusão:
Os testes cobriram os principais fluxos das funcionalidades críticas. Os casos de falha foram documentados para correção futura.
