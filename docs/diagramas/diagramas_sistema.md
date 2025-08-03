# Diagramas do Sistema de Biblioteca

> 📋 **Navegação Rápida**: Este documento contém múltiplas visualizações dos diagramas do sistema:
> - **Casos de Uso Simplificado**: Visão por funcionalidades agrupadas
> - **Fluxo de Operações**: Sequência detalhada das operações
> - **Casos de Uso Tradicional**: Formato clássico UML
> - **Diagrama de Classes**: Estrutura completa do sistema

---

## Diagrama de Casos de Uso Simplificado

### Visão Geral dos Atores e Funcionalidades

```mermaid
graph LR
    %% Atores
    UC[👤 Usuário Comum]
    AD[👨‍💼 Administrador]
    
    %% Funcionalidades Principais
    subgraph "🔐 Autenticação"
        LOGIN[Fazer Login]
        LOGOUT[Fazer Logout]
    end
    
    subgraph "📚 Gestão de Livros"
        LISTAR[Listar Livros]
        EMPRESTAR[Emprestar Livro]
        STATUS[Ver Status]
    end
    
    subgraph "👨‍💼 Administração"
        ADD[Adicionar Livro]
        DEVOLVER[Processar Devolução]
        RELATORIO[Ver Relatórios]
    end
    
    %% Relacionamentos
    UC --> LOGIN
    UC --> LISTAR
    UC --> EMPRESTAR
    UC --> STATUS
    UC --> LOGOUT
    
    AD --> LOGIN
    AD --> LISTAR
    AD --> ADD
    AD --> DEVOLVER
    AD --> RELATORIO
    AD --> LOGOUT
    
    classDef actor fill:#ffcdd2,stroke:#d32f2f,stroke-width:2px
    classDef auth fill:#e8eaf6,stroke:#3f51b5,stroke-width:2px
    classDef user fill:#e1f5fe,stroke:#0277bd,stroke-width:2px
    classDef admin fill:#fff3e0,stroke:#f57c00,stroke-width:2px
    
    class UC,AD actor
    class LOGIN,LOGOUT auth
    class LISTAR,EMPRESTAR,STATUS user
    class ADD,DEVOLVER,RELATORIO admin
```

### Fluxo de Operações Detalhado

```mermaid
flowchart TD
    START([👤 Usuário acessa sistema])
    
    LOGIN{🔐 Login válido?}
    TIPO{👤 Tipo de usuário?}
    
    %% Fluxo Usuário Comum
    USER_MENU[📋 Menu Principal]
    VER_LIVROS[📚 Ver Livros Disponíveis]
    EMPRESTAR[📖 Emprestar Livro]
    VER_STATUS[📊 Ver Meus Empréstimos]
    
    %% Fluxo Administrador
    ADMIN_MENU[👨‍💼 Menu Administrativo]
    ADD_LIVRO[➕ Adicionar Livro]
    DEVOLVER[↩️ Processar Devolução]
    RELATORIO[📈 Ver Relatórios]
    
    %% Operações do Sistema
    VALIDAR[🔍 Validar Disponibilidade]
    REGISTRAR[💾 Registrar Empréstimo]
    ATUALIZAR[🔄 Atualizar Status]
    
    LOGOUT([🚪 Logout])
    
    START --> LOGIN
    LOGIN -->|Sim| TIPO
    LOGIN -->|Não| START
    
    TIPO -->|Usuário| USER_MENU
    TIPO -->|Admin| ADMIN_MENU
    
    USER_MENU --> VER_LIVROS
    USER_MENU --> EMPRESTAR
    USER_MENU --> VER_STATUS
    USER_MENU --> LOGOUT
    
    ADMIN_MENU --> VER_LIVROS
    ADMIN_MENU --> ADD_LIVRO
    ADMIN_MENU --> DEVOLVER
    ADMIN_MENU --> RELATORIO
    ADMIN_MENU --> LOGOUT
    
    EMPRESTAR --> VALIDAR
    VALIDAR --> REGISTRAR
    REGISTRAR --> ATUALIZAR
    ATUALIZAR --> USER_MENU
    
    DEVOLVER --> ATUALIZAR
    
    classDef startEnd fill:#c8e6c9,stroke:#4caf50,stroke-width:3px
    classDef decision fill:#fff3e0,stroke:#ff9800,stroke-width:2px
    classDef userAction fill:#e3f2fd,stroke:#2196f3,stroke-width:2px
    classDef adminAction fill:#fce4ec,stroke:#e91e63,stroke-width:2px
    classDef systemAction fill:#f3e5f5,stroke:#9c27b0,stroke-width:2px
    
    class START,LOGOUT startEnd
    class LOGIN,TIPO,VALIDAR decision
    class USER_MENU,VER_LIVROS,EMPRESTAR,VER_STATUS userAction
    class ADMIN_MENU,ADD_LIVRO,DEVOLVER,RELATORIO adminAction
    class REGISTRAR,ATUALIZAR systemAction
```

## Diagrama de Casos de Uso Tradicional

```mermaid
graph TB
    %% Atores
    USER((👤<br/>Usuário<br/>Comum))
    ADMIN((👨‍💼<br/>Administrador))
    
    %% Sistema
    subgraph SISTEMA["📚 Sistema de Biblioteca"]
        
        subgraph AUTH["🔐 Autenticação"]
            LOGIN[Login]
            LOGOUT[Logout]
        end
        
        subgraph CATALOGO["📋 Catálogo"]
            LISTAR[Listar Livros]
            BUSCAR[Buscar Livro]
        end
        
        subgraph EMPRESTIMO["📖 Empréstimos"]
            EMPRESTAR[Emprestar Livro]
            STATUS[Ver Status]
        end
        
        subgraph ADMIN_FUNC["👨‍💼 Administração"]
            ADD[Adicionar Livro]
            DEVOLVER[Devolver Livro]
            RELATORIOS[Relatórios]
        end
    end
    
    %% Relacionamentos Usuário
    USER --- LOGIN
    USER --- LISTAR
    USER --- BUSCAR
    USER --- EMPRESTAR
    USER --- STATUS
    USER --- LOGOUT
    
    %% Relacionamentos Admin (herda do usuário + funções admin)
    ADMIN --- LOGIN
    ADMIN --- LISTAR
    ADMIN --- BUSCAR
    ADMIN --- ADD
    ADMIN --- DEVOLVER
    ADMIN --- RELATORIOS
    ADMIN --- LOGOUT
    
    %% Estilos
    classDef ator fill:#ffebee,stroke:#c62828,stroke-width:3px
    classDef sistema fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
    classDef auth fill:#e8eaf6,stroke:#3f51b5,stroke-width:2px
    classDef catalogo fill:#e0f2f1,stroke:#00695c,stroke-width:2px
    classDef emprestimo fill:#fff3e0,stroke:#ef6c00,stroke-width:2px
    classDef admin fill:#fce4ec,stroke:#ad1457,stroke-width:2px
    
    class USER,ADMIN ator
    class SISTEMA sistema
    class LOGIN,LOGOUT auth
    class LISTAR,BUSCAR catalogo
    class EMPRESTAR,STATUS emprestimo
    class ADD,DEVOLVER,RELATORIOS admin
```

## Diagrama de Classes

```mermaid
classDiagram
    %% Classes de Modelo
    class Usuario {
        -int id
        -string nome
        -string senha
        -boolean ativo
        -string tipo
        +__init__(id, nome, senha)
        +validarCredenciais(senha) boolean
        +isAdmin() boolean
        +ativar() void
        +desativar() void
    }
    
    class Livro {
        -int id
        -string titulo
        -boolean disponivel
        +__init__(id, titulo)
        +emprestar() boolean
        +devolver() boolean
        +isDisponivel() boolean
        +setDisponivel(status) void
    }
    
    class Emprestimo {
        -int id
        -int livro_id
        -string titulo_livro
        -int usuario_id
        -datetime data_emprestimo
        -datetime data_devolucao
        +__init__(livro_id, usuario_id)
        +devolver() void
        +isDevolvido() boolean
        +getDuracao() int
    }
    
    %% Classes de Controle
    class BibliotecaController {
        -List~Livro~ livros
        -List~Usuario~ usuarios
        -List~Emprestimo~ emprestimos
        -int proximo_id_livro
        +login(username, password) dict
        +listarLivros() List~Livro~
        +emprestarLivro(livro_id, usuario_id) dict
        +resetDatabase() dict
    }
    
    class AdminController {
        +adicionarLivro(titulo) dict
        +devolverLivro(emprestimo_id) dict
        +listarEmprestimos() List~Emprestimo~
        +listarEmprestimosAtivos() List~Emprestimo~
        +validarPrivilegios(usuario) boolean
    }
    
    class AuthController {
        +autenticar(username, password) Usuario
        +validarCredenciais(usuario, senha) boolean
        +controlarAcesso(usuario, recurso) boolean
        +logout(usuario) void
    }
    
    %% Classes de Interface
    class WebInterface {
        -HTMLElement loginForm
        -HTMLElement mainSection
        -HTMLElement adminSection
        +showMessage(message, isSuccess) void
        +loadLivros() void
        +showLoginForm() void
        +showMainSection() void
        +showAdminSection() void
        +logout() void
    }
    
    class APIEndpoints {
        +postLogin()
        +getLivros()
        +postEmprestarLivro()
        +postAdminLivros()
        +postAdminDevolver()
        +getAdminEmprestimos()
        +getAdminEmprestimosAtivos()
        +postReset()
    }
    
    %% Especializações
    class UsuarioComum {
        +podeEmprestar() boolean
    }
    
    class Administrador {
        +podeGerenciarSistema() boolean
        +podeVisualizarLogs() boolean
    }
    
    %% Classes Utilitárias
    class DatabaseSimulator {
        +initializeLivros()$ List~Livro~
        +initializeUsuarios()$ List~Usuario~
        +resetToDefaults()$ void
    }
    
    class ValidationUtils {
        +validateRequired(field)$ boolean
        +validateCredentials(user, pass)$ boolean
        +sanitizeInput(input)$ string
    }
    
    %% Relacionamentos
    BibliotecaController *-- Livro : gerencia
    BibliotecaController *-- Usuario : controla
    BibliotecaController *-- Emprestimo : registra
    
    AdminController ..> BibliotecaController : usa
    AuthController ..> Usuario : autentica
    WebInterface ..> BibliotecaController : comunica
    WebInterface ..> AdminController : comunica
    APIEndpoints ..> BibliotecaController : expõe
    APIEndpoints ..> AdminController : expõe
    
    Emprestimo --> Livro : refere-se a
    Emprestimo --> Usuario : pertence a
    Usuario "1" -- "0..*" Emprestimo : realiza
    
    Usuario <|-- UsuarioComum : herda
    Usuario <|-- Administrador : herda
    
    BibliotecaController ..> DatabaseSimulator : inicializa
    BibliotecaController ..> ValidationUtils : valida
    AdminController ..> ValidationUtils : valida
```

## Detalhamento dos Casos de Uso

### UC01: Fazer Login
- **Ator**: Usuário Comum, Administrador
- **Pré-condições**: Sistema disponível
- **Fluxo Principal**: 
  1. Usuário acessa a tela de login
  2. Insere credenciais (nome e senha)
  3. Sistema valida credenciais
  4. Sistema identifica tipo de usuário
  5. Sistema exibe interface apropriada
- **Pós-condições**: Usuário autenticado no sistema

### UC03: Emprestar Livro
- **Ator**: Usuário Comum, Administrador
- **Pré-condições**: Usuário logado, livro disponível
- **Fluxo Principal**:
  1. Usuário seleciona livro para empréstimo
  2. Sistema verifica disponibilidade
  3. Sistema registra empréstimo
  4. Sistema atualiza status do livro
  5. Sistema confirma operação
- **Pós-condições**: Livro emprestado, registro criado

### UC06: Adicionar Livro
- **Ator**: Administrador
- **Pré-condições**: Usuário com privilégios de admin
- **Fluxo Principal**:
  1. Admin acessa painel administrativo
  2. Seleciona opção "Adicionar Livro"
  3. Insere dados do livro (título obrigatório)
  4. Sistema valida dados
  5. Sistema adiciona livro ao catálogo
- **Pós-condições**: Novo livro disponível no sistema

## Arquitetura do Sistema

O sistema segue o padrão **MVC (Model-View-Controller)** com separação clara de responsabilidades:

- **Model**: Classes `Usuario`, `Livro`, `Emprestimo`
- **View**: `WebInterface`, `APIEndpoints`
- **Controller**: `BibliotecaController`, `AdminController`, `AuthController`

### Características Arquiteturais:
- ✅ **Separação de Responsabilidades**
- ✅ **Baixo Acoplamento**
- ✅ **Alta Coesão**
- ✅ **Reutilização de Código**
- ✅ **Facilidade de Manutenção**
- ✅ **Testabilidade**
