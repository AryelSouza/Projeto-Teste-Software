# Especificação de Casos de Uso - Sistema de Biblioteca

## UC01: Fazer Login

| Campo | Descrição |
|-------|-----------|
| **ID** | UC01 |
| **Nome** | Fazer Login |
| **Ator Principal** | Usuário Comum, Administrador |
| **Interessados** | Usuários do sistema |
| **Pré-condições** | Sistema disponível e acessível |
| **Garantias de Sucesso** | Usuário autenticado com interface apropriada exibida |
| **Cenário Principal** | 1. Usuário acessa a página inicial do sistema<br>2. Sistema exibe formulário de login<br>3. Usuário insere nome de usuário e senha<br>4. Sistema valida credenciais<br>5. Sistema identifica tipo de usuário (comum/admin)<br>6. Sistema exibe interface principal apropriada<br>7. Sistema oculta formulário de login |
| **Extensões** | **3a.** Campos obrigatórios vazios:<br>&nbsp;&nbsp;3a.1. Sistema exibe mensagem de erro<br>&nbsp;&nbsp;3a.2. Retorna ao passo 3<br>**4a.** Credenciais inválidas:<br>&nbsp;&nbsp;4a.1. Sistema exibe mensagem de erro<br>&nbsp;&nbsp;4a.2. Retorna ao passo 3 |
| **Frequência** | Alta |
| **Prioridade** | Alta |

---

## UC02: Listar Livros

| Campo | Descrição |
|-------|-----------|
| **ID** | UC02 |
| **Nome** | Listar Livros |
| **Ator Principal** | Usuário Comum, Administrador |
| **Interessados** | Usuários que desejam consultar o catálogo |
| **Pré-condições** | Usuário autenticado no sistema |
| **Garantias de Sucesso** | Lista de livros exibida com status atual |
| **Cenário Principal** | 1. Sistema carrega lista de livros automaticamente após login<br>2. Sistema exibe cada livro com: ID, título, status (disponível/indisponível)<br>3. Sistema atualiza lista em tempo real conforme mudanças |
| **Extensões** | **2a.** Nenhum livro cadastrado:<br>&nbsp;&nbsp;2a.1. Sistema exibe mensagem informativa |
| **Frequência** | Muito Alta |
| **Prioridade** | Alta |

---

## UC03: Emprestar Livro

| Campo | Descrição |
|-------|-----------|
| **ID** | UC03 |
| **Nome** | Emprestar Livro |
| **Ator Principal** | Usuário Comum, Administrador |
| **Interessados** | Usuários que desejam emprestar livros |
| **Pré-condições** | Usuário autenticado e livro disponível |
| **Garantias de Sucesso** | Livro emprestado e registro criado |
| **Cenário Principal** | 1. Usuário visualiza lista de livros disponíveis<br>2. Usuário insere ID do livro desejado<br>3. Sistema valida ID do livro<br>4. Sistema verifica disponibilidade<br>5. Sistema registra empréstimo com data/hora atual<br>6. Sistema marca livro como indisponível<br>7. Sistema exibe mensagem de sucesso<br>8. Sistema atualiza lista de livros |
| **Extensões** | **3a.** ID do livro inválido:<br>&nbsp;&nbsp;3a.1. Sistema exibe mensagem de erro<br>&nbsp;&nbsp;3a.2. Retorna ao passo 2<br>**4a.** Livro indisponível:<br>&nbsp;&nbsp;4a.1. Sistema exibe mensagem informando indisponibilidade<br>&nbsp;&nbsp;4a.2. Retorna ao passo 2 |
| **Frequência** | Alta |
| **Prioridade** | Alta |

---

## UC06: Adicionar Livro

| Campo | Descrição |
|-------|-----------|
| **ID** | UC06 |
| **Nome** | Adicionar Livro |
| **Ator Principal** | Administrador |
| **Interessados** | Administradores do sistema |
| **Pré-condições** | Usuário autenticado como administrador |
| **Garantias de Sucesso** | Novo livro adicionado ao catálogo |
| **Cenário Principal** | 1. Admin acessa painel administrativo<br>2. Admin seleciona aba "Adicionar Livro"<br>3. Admin insere título do livro<br>4. Admin submete formulário<br>5. Sistema valida dados obrigatórios<br>6. Sistema gera novo ID para o livro<br>7. Sistema adiciona livro como disponível<br>8. Sistema exibe mensagem de sucesso<br>9. Sistema limpa formulário<br>10. Sistema atualiza lista de livros |
| **Extensões** | **5a.** Título não informado:<br>&nbsp;&nbsp;5a.1. Sistema exibe mensagem de erro<br>&nbsp;&nbsp;5a.2. Retorna ao passo 3 |
| **Frequência** | Média |
| **Prioridade** | Média |

---

## UC08: Processar Devolução

| Campo | Descrição |
|-------|-----------|
| **ID** | UC08 |
| **Nome** | Processar Devolução |
| **Ator Principal** | Administrador |
| **Interessados** | Administradores e usuários com empréstimos |
| **Pré-condições** | Usuário autenticado como admin e empréstimo ativo existente |
| **Garantias de Sucesso** | Livro devolvido e disponibilizado |
| **Cenário Principal** | 1. Admin acessa painel administrativo<br>2. Admin seleciona aba "Devoluções"<br>3. Sistema lista empréstimos ativos<br>4. Admin seleciona empréstimo para devolução<br>5. Sistema confirma operação via popup<br>6. Admin confirma devolução<br>7. Sistema registra data/hora da devolução<br>8. Sistema marca livro como disponível<br>9. Sistema exibe mensagem de sucesso<br>10. Sistema atualiza listas de empréstimos e livros |
| **Extensões** | **5a.** Empréstimo já devolvido:<br>&nbsp;&nbsp;5a.1. Sistema exibe mensagem de erro<br>&nbsp;&nbsp;5a.2. Atualiza lista automaticamente |
| **Frequência** | Alta |
| **Prioridade** | Alta |

---

## UC09: Visualizar Logs de Empréstimos

| Campo | Descrição |
|-------|-----------|
| **ID** | UC09 |
| **Nome** | Visualizar Logs de Empréstimos |
| **Ator Principal** | Administrador |
| **Interessados** | Administradores do sistema |
| **Pré-condições** | Usuário autenticado como administrador |
| **Garantias de Sucesso** | Histórico completo de empréstimos exibido |
| **Cenário Principal** | 1. Admin acessa painel administrativo<br>2. Admin seleciona aba "Logs de Empréstimos"<br>3. Sistema carrega histórico completo<br>4. Sistema exibe cada empréstimo com:<br>&nbsp;&nbsp;- ID do empréstimo<br>&nbsp;&nbsp;- Título do livro<br>&nbsp;&nbsp;- ID do usuário<br>&nbsp;&nbsp;- Data de empréstimo<br>&nbsp;&nbsp;- Data de devolução (se aplicável)<br>5. Sistema diferencia visualmente empréstimos devolvidos |
| **Extensões** | **3a.** Nenhum empréstimo registrado:<br>&nbsp;&nbsp;3a.1. Sistema exibe mensagem informativa |
| **Frequência** | Média |
| **Prioridade** | Baixa |

---

## UC10: Listar Empréstimos Ativos

| Campo | Descrição |
|-------|-----------|
| **ID** | UC10 |
| **Nome** | Listar Empréstimos Ativos |
| **Ator Principal** | Administrador |
| **Interessados** | Administradores do sistema |
| **Pré-condições** | Usuário autenticado como administrador |
| **Garantias de Sucesso** | Lista de empréstimos não devolvidos exibida |
| **Cenário Principal** | 1. Admin acessa painel administrativo<br>2. Admin seleciona aba "Devoluções"<br>3. Sistema filtra empréstimos sem data de devolução<br>4. Sistema exibe lista de empréstimos ativos<br>5. Sistema disponibiliza botão "Devolver" para cada item |
| **Extensões** | **3a.** Nenhum empréstimo ativo:<br>&nbsp;&nbsp;3a.1. Sistema exibe mensagem informativa |
| **Frequência** | Alta |
| **Prioridade** | Média |

---

## UC13: Controlar Acesso

| Campo | Descrição |
|-------|-----------|
| **ID** | UC13 |
| **Nome** | Controlar Acesso |
| **Ator Principal** | Sistema |
| **Interessados** | Todos os usuários |
| **Pré-condições** | Usuário logado no sistema |
| **Garantias de Sucesso** | Interface apropriada exibida baseada no tipo de usuário |
| **Cenário Principal** | 1. Sistema identifica tipo de usuário logado<br>2. Sistema verifica privilégios do usuário<br>3. Para usuário comum:<br>&nbsp;&nbsp;3.1. Sistema exibe seção principal<br>&nbsp;&nbsp;3.2. Sistema oculta seção administrativa<br>4. Para administrador:<br>&nbsp;&nbsp;4.1. Sistema exibe seção principal<br>&nbsp;&nbsp;4.2. Sistema exibe seção administrativa<br>5. Sistema aplica regras de negócio apropriadas |
| **Extensões** | **2a.** Tipo de usuário inválido:<br>&nbsp;&nbsp;2a.1. Sistema força logout<br>&nbsp;&nbsp;2a.2. Retorna à tela de login |
| **Frequência** | Muito Alta |
| **Prioridade** | Crítica |

---

## Matriz de Rastreabilidade dos Casos de Uso

| Caso de Uso | Requisito Funcional | Teste Unitário | Teste API | Teste E2E | Status |
|-------------|-------------------|----------------|-----------|-----------|---------|
| UC01 | RF01 | ✅ test_usuario.py | ✅ test_api.py | ✅ test_login.py | 100% |
| UC02 | RF02, RF03 | ✅ test_livro.py | ✅ test_api.py | ✅ Todos os testes | 100% |
| UC03 | RF04 | ✅ test_admin.py | ✅ test_api.py | ✅ test_emprestimo.py | 100% |
| UC06 | RF03 | ✅ test_admin.py | ✅ test_admin_api.py | ✅ test_admin_e2e.py | 100% |
| UC08 | RF05 | ✅ test_admin.py | ✅ test_admin_api.py | ✅ test_admin_e2e.py | 100% |
| UC09 | RF06 | ✅ test_admin.py | ✅ test_admin_api.py | ✅ test_admin_e2e.py | 100% |
| UC10 | RF06 | ✅ test_admin.py | ✅ test_admin_api.py | ✅ test_admin_e2e.py | 100% |
| UC13 | RF02 | ✅ test_admin.py | ✅ test_admin_api.py | ✅ test_usuario_normal.py | 100% |

## Glossário

- **Usuário Comum**: Pessoa com acesso básico ao sistema para consulta e empréstimo
- **Administrador**: Pessoa com privilégios especiais para gerenciar o sistema
- **Empréstimo Ativo**: Empréstimo sem data de devolução registrada
- **Livro Disponível**: Livro que pode ser emprestado (não está em empréstimo ativo)
- **Livro Indisponível**: Livro que está atualmente emprestado
- **Log de Empréstimo**: Registro histórico de todas as transações de empréstimo
