# Relatório de Testes - Sistema de Biblioteca

## Funcionalidades testadas:
1. RF01: Login de usuário
2. RF02: Listagem de livros  
3. RF03: Empréstimo de livros
4. RF04: Reset do banco de dados
5. RF05: Validação de dados

## Resultados dos testes:

### Testes Unitários
| Classe/Funcionalidade | Caso de Teste | Resultado | Descrição |
|----------------------|---------------|-----------|-----------|
| Livro | Emprestar livro disponível | ✅ Sucesso | Livro muda status para indisponível |
| Livro | Emprestar livro indisponível | ✅ Sucesso | Retorna falso, mantém status |
| Livro | Devolver livro | ✅ Sucesso | Livro volta a ficar disponível |
| Usuario | Criação de usuário | ✅ Sucesso | Usuário criado com dados corretos |
| Usuario | Desativar usuário | ✅ Sucesso | Status do usuário alterado |

### Testes de API
| Endpoint | Caso de Teste | Resultado | Descrição |
|----------|---------------|-----------|-----------|
| POST /login | Login com credenciais válidas | ✅ Sucesso | Retorna status 200 |
| POST /login | Login com credenciais inválidas | ✅ Sucesso | Retorna status 401 |
| GET /livros | Listar todos os livros | ✅ Sucesso | Retorna lista de livros |
| POST /emprestar/1 | Emprestar livro disponível | ✅ Sucesso | Livro emprestado com sucesso |

### Testes de Login (RF01)
| Caso de Teste | Resultado | Evidência |
|---------------|-----------|-----------|
| Login com credenciais válidas | ✅ Sucesso | [login_sucesso.png](evidencias/login_sucesso.png) |
| Login com campos vazios | ✅ Sucesso | [login_falha.png](evidencias/login_falha.png) |

### Testes de Empréstimo (RF03)
| Caso de Teste | Resultado | Evidência |
|---------------|-----------|-----------|
| Empréstimo de livro disponível | ✅ Sucesso | [emprestimo_sucesso.png](evidencias/emprestimo_sucesso.png) |
| Tentativa de empréstimo de livro indisponível | ✅ Sucesso | [emprestimo_falha.png](evidencias/emprestimo_falha.png) |

## Resumo Executivo:
| Tipo de Teste | Total | Passou | Falhou | Taxa de Sucesso |
|---------------|-------|--------|--------|-----------------|
| Testes Unitários | 5 | 5 | 0 | 100% |
| Testes de API | 4 | 4 | 0 | 100% |
| Testes E2E | 4 | 4 | 0 | 100% |
| **TOTAL** | **13** | **13** | **0** | **100%** |

## Cobertura de Testes:
- ✅ **Login de usuários** - Testado em API e E2E
- ✅ **Listagem de livros** - Testado em API
- ✅ **Empréstimo de livros** - Testado em unitário, API e E2E
- ✅ **Validação de dados** - Testado em todos os níveis
- ✅ **Interface do usuário** - Testado com Selenium WebDriver

## Conclusão:
Todos os testes foram executados com sucesso (100% de aprovação). O sistema está funcionando conforme especificado. A cobertura de testes abrange todas as funcionalidades críticas nos três níveis: unitário, API e end-to-end. O ChromeDriver foi configurado corretamente e os testes E2E estão estáveis.
