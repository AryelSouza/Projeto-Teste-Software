# Relatório de Testes - Sistema de Biblioteca

## Funcionalidades testadas:
1. RF01: Login de usuário
2. RF02: Listagem de livros  
3. RF03: Empréstimo de livros
4. RF04: Reset do banco de dados
5. RF05: Validação de dados

## Justificativas:
1. RF01: O login é a porta de entrada do sistema e garante que apenas usuários autenticados tenham acesso às funcionalidades protegidas. É uma funcionalidade crítica para a segurança, controle de sessão e privacidade de dados. Falhas aqui comprometem todo o sistema.

2. RF02: É uma das funcionalidades mais utilizadas no sistema e está diretamente ligada à experiência do usuário. Testá-la garante que a busca e apresentação dos dados do acervo estejam corretas e acessíveis. Erros nessa parte impactam a usabilidade e confiabilidade da aplicação.

3. RF03: Essa funcionalidade representa o núcleo da operação de uma biblioteca. Testes garantem que o processo de empréstimo funcione corretamente, respeitando as regras (como disponibilidade de livros, usuário com pendências, etc.). Erros aqui podem levar a inconsistências no banco de dados ou falhas nos relatórios.

4. RF04: Embora não esteja diretamente relacionada ao uso comum, essa funcionalidade é essencial para ambientes de teste e manutenção. Foi testada para garantir que o sistema possa retornar ao estado inicial de forma segura, sem deixar registros órfãos ou dados corrompidos.

5. RF05: Garantir que os dados inseridos pelo usuário estejam corretos é fundamental para a integridade do sistema. Esta funcionalidade foi testada para prevenir entradas inválidas, como campos obrigatórios vazios, e-mails mal formatados, ou tentativas de injeção de código. Testá-la ajuda a evitar falhas de segurança e dados inconsistentes.



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
