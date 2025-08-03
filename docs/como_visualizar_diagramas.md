# Como Visualizar os Diagramas

## 📐 Diagramas Disponíveis

O projeto inclui documentação visual completa com:

1. **Diagrama de Casos de Uso** - Interações entre atores e sistema
2. **Diagrama de Classes** - Estrutura e relacionamentos das classes
3. **Especificação Detalhada** - Casos de uso com fluxos principais e alternativos

## 🔧 Ferramentas para Visualização

### 1. PlantUML (Recomendado)

**Extensão instalada**: `jebbs.plantuml`

**Como usar**:
1. Abra os arquivos `.puml` no VS Code
2. Pressione `Ctrl+Shift+P` (ou `Cmd+Shift+P` no Mac)
3. Digite "PlantUML: Preview Current Diagram"
4. O diagrama será renderizado em uma aba lateral

**Arquivos PlantUML**:
- `docs/diagrama_casos_uso.puml` - Casos de uso (versão completa)
- `docs/diagrama_classes.puml` - Classes (versão completa)
- `docs/casos_uso_simples.puml` - Casos de uso (versão simplificada)
- `docs/classes_simples.puml` - Classes (versão simplificada)

**⚠️ Se encontrar problemas, use as versões simplificadas primeiro!**

### 2. Mermaid (Alternativa)

**Extensão instalada**: `bierner.markdown-mermaid`

**Como usar**:
1. Abra o arquivo `docs/diagramas_sistema.md`
2. Pressione `Ctrl+Shift+V` para visualizar preview do Markdown
3. Os diagramas Mermaid serão renderizados automaticamente

### 3. Ferramentas Online

Se preferir visualizar online:

**PlantUML Online**:
- Acesse: https://www.plantuml.com/plantuml/uml/
- Copie e cole o conteúdo dos arquivos `.puml`

**Mermaid Live Editor**:
- Acesse: https://mermaid.live/
- Copie e cole o código Mermaid do arquivo `.md`

## 📁 Localização dos Arquivos

```
docs/
├── diagrama_casos_uso.puml     # Casos de uso (PlantUML)
├── diagrama_classes.puml       # Classes (PlantUML)
├── diagramas_sistema.md        # Ambos diagramas (Mermaid)
├── casos_de_uso.md            # Especificação detalhada
├── relatorio_teste.md         # Relatório de testes
└── requisitos.md              # Requisitos do sistema
```

## 🎨 Exportação de Imagens

### Via PlantUML (VS Code)
1. Visualize o diagrama no preview
2. Clique com botão direito na imagem
3. Selecione "Save as..." para salvar como PNG/SVG

### Via Linha de Comando (se PlantUML estiver instalado)
```bash
# Instalar PlantUML (requer Java)
# Baixar plantuml.jar de https://plantuml.com/download

# Gerar PNG
java -jar plantuml.jar docs/diagrama_casos_uso.puml

# Gerar SVG
java -jar plantuml.jar -tsvg docs/diagrama_casos_uso.puml
```

## 🎨 Gerando Imagens para GitHub

Para que os diagramas apareçam diretamente no GitHub como imagens:

### Método 1: Scripts Automáticos (Recomendado)
```powershell
# Windows PowerShell - Testar ambiente primeiro
.\scripts\testar_ambiente.ps1

# Se tudo estiver OK, gerar as imagens
.\scripts\gerar_diagramas.ps1
```

```bash
# Linux/Mac - Dar permissão e executar
chmod +x scripts/gerar_diagramas.sh
./scripts/gerar_diagramas.sh
```

### Método 2: GitHub Actions (Automático)
O projeto inclui um workflow que gera as imagens automaticamente quando arquivos `.puml` são modificados.

**Para executar manualmente:**
1. Ir para "Actions" no GitHub
2. Selecionar "Gerar Diagramas UML"  
3. Clicar em "Run workflow"

### Estrutura Resultante
```
docs/
├── images/
│   ├── diagrama_casos_uso.png     # Casos de uso
│   ├── diagrama_casos_uso.svg     # Casos de uso (vetorial)
│   ├── diagrama_classes.png       # Classes
│   ├── diagrama_classes.svg       # Classes (vetorial)
│   └── ...outros diagramas...
```

### Scripts Disponíveis

| Script | Função |
|--------|--------|
| `scripts/testar_ambiente.ps1` | Testa se o ambiente está configurado |
| `scripts/gerar_diagramas.ps1` | Gera imagens PNG/SVG (Windows) |
| `scripts/gerar_diagramas.sh` | Gera imagens PNG/SVG (Linux/Mac) |

## 📊 Características dos Diagramas

### Diagrama de Casos de Uso
- ✅ **8 casos de uso principais** mapeados
- ✅ **3 atores** identificados (Usuário, Admin, Sistema)
- ✅ **Relacionamentos** include, extend e herança
- ✅ **Anotações explicativas** para regras de negócio

### Diagrama de Classes
- ✅ **11 classes principais** modeladas
- ✅ **Padrão MVC** implementado
- ✅ **Relacionamentos** completos (herança, composição, associação)
- ✅ **Estereótipos** Entity, Controller, Boundary
- ✅ **Métodos e atributos** detalhados

### Especificação de Casos de Uso
- ✅ **Fluxos principais** e alternativos
- ✅ **Pré e pós-condições** definidas
- ✅ **Frequência e prioridade** classificadas
- ✅ **Matriz de rastreabilidade** com testes
- ✅ **Glossário** de termos técnicos

## 🔍 Dicas de Visualização

1. **Zoom**: Use `Ctrl + Mouse Wheel` para ajustar zoom nos diagramas
2. **Navegação**: Clique e arraste para mover diagramas grandes
3. **Atualização**: Diagramas são atualizados automaticamente ao salvar
4. **Cores**: Diagramas usam cores para diferenciar tipos de elementos

## ❓ Solução de Problemas

### "Nenhum diagrama válido encontrado"
**Soluções em ordem de prioridade:**

1. **Teste as versões simplificadas primeiro**:
   - Abra `casos_uso_simples.puml` ou `classes_simples.puml`
   - Estas versões têm sintaxe mais básica e compatível

2. **Verifique a configuração do PlantUML**:
   - `Ctrl+Shift+P` → "PlantUML: Check PlantUML Environment"
   - Deve mostrar Java instalado e PlantUML funcionando

3. **Instale/atualize Java**:
   ```bash
   # Windows (via winget)
   winget install Microsoft.OpenJDK.11
   
   # Ou baixe de: https://adoptium.net/
   ```

4. **Reinstale a extensão PlantUML**:
   - Desinstale: `Ctrl+Shift+X` → busque "PlantUML" → Uninstall
   - Reinstale: `Ctrl+Shift+X` → busque "PlantUML" → Install

5. **Configure servidor alternativo**:
   - `Ctrl+Shift+P` → "Preferences: Open Settings (JSON)"
   - Adicione:
   ```json
   {
     "plantuml.server": "https://www.plantuml.com/plantuml",
     "plantuml.render": "PlantUMLServer"
   }
   ```

### PlantUML não renderiza
- **Problema**: Java não encontrado
- **Solução**: Instale OpenJDK 11+ e reinicie o VS Code

### Mermaid não aparece no preview
- Verifique se a extensão Mermaid está habilitada
- Recarregue o VS Code (`Ctrl+Shift+P` → "Reload Window")
- Use o visualizador online como alternativa

### Performance lenta
- Diagramas grandes podem demorar para renderizar
- Use as versões simplificadas para teste rápido
- Configure servidor online se local estiver lento

## 📚 Recursos Adicionais

- [Documentação PlantUML](https://plantuml.com/)
- [Sintaxe Mermaid](https://mermaid-js.github.io/mermaid/)
- [UML Reference](https://www.uml-diagrams.org/)
- [Padrões de Design](https://refactoring.guru/design-patterns)
