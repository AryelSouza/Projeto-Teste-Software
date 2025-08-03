# 📋 Índice da Documentação

Este diretório contém toda a documentação técnica do Sistema de Biblioteca.

## 📁 Estrutura da Documentação

### 📐 Diagramas UML
- **[diagramas/](diagramas/)** - Diagramas do sistema
  - **[diagramas_sistema.md](diagramas/diagramas_sistema.md)** - Diagramas Mermaid (visualização direta no GitHub)
  - **[plantuml/](diagramas/plantuml/)** - Código-fonte dos diagramas PlantUML
    - `diagrama_casos_uso.puml` - Diagrama de casos de uso completo
    - `diagrama_classes.puml` - Diagrama de classes completo  
    - `casos_uso_simples.puml` - Versão simplificada dos casos de uso
    - `classes_simples.puml` - Versão simplificada das classes

### 📝 Especificações
- **[casos-de-uso/](casos-de-uso/)** - Documentação de casos de uso
  - `casos_de_uso.md` - Especificação detalhada dos casos de uso
- **[requisitos.md](requisitos.md)** - Requisitos funcionais e não funcionais do sistema

### 📊 Testes e Evidências  
- **[relatorio_teste.md](relatorio_teste.md)** - Relatório completo de testes
- **[evidencias/](evidencias/)** - Screenshots e evidências dos testes

### 🖼️ Imagens Geradas
- **[images/](images/)** - Imagens PNG/SVG dos diagramas PlantUML
  - Geradas automaticamente via GitHub Actions ou scripts locais

## 🎯 Links Rápidos

| Documento | Descrição |
|-----------|-----------|
| [Casos de Uso](casos-de-uso/casos_de_uso.md) | Especificação completa dos casos de uso |
| [Requisitos](requisitos.md) | Requisitos funcionais e não funcionais |
| [Relatório de Testes](relatorio_teste.md) | Resultados dos testes automatizados |
| [Diagramas Mermaid](diagramas/diagramas_sistema.md) | Diagramas visualizáveis diretamente no GitHub |

## 🔧 Geração de Diagramas

Para gerar as imagens dos diagramas PlantUML:

```bash
# Windows
.\scripts\gerar_simples.ps1

# Linux/Mac  
./scripts/gerar_diagramas.sh
```

## 📋 Convenções

- **Diagramas PlantUML**: Código em `diagramas/plantuml/`, imagens em `images/`
- **Diagramas Mermaid**: Código e visualização em `diagramas/diagramas_sistema.md`
- **Evidências**: Screenshots organizados por funcionalidade em `evidencias/`
- **Versionamento**: Todos os arquivos são versionados no Git
