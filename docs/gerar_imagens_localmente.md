# 🎨 Gerar Imagens dos Diagramas Localmente

Este guia explica como gerar as imagens dos diagramas PlantUML localmente para uso no GitHub.

## 📋 Pré-requisitos

### 1. Java (obrigatório)
```bash
# Verificar se Java está instalado
java -version

# Se não estiver instalado:
# Windows: baixar do https://adoptium.net/
# Ubuntu/Debian: sudo apt install openjdk-17-jre
# macOS: brew install openjdk@17
```

### 2. PlantUML JAR (baixar automaticamente)
O script baixará automaticamente o PlantUML se necessário.

## 🚀 Métodos de Geração

### Método 1: Script Automático (Recomendado)

**Windows PowerShell:**
```powershell
# Criar e executar o script
.\scripts\gerar_diagramas.ps1
```

**Linux/Mac:**
```bash
# Dar permissão e executar
chmod +x scripts/gerar_diagramas.sh
./scripts/gerar_diagramas.sh
```

### Método 2: Comandos Manuais

```bash
# 1. Baixar PlantUML (se necessário)
wget https://github.com/plantuml/plantuml/releases/latest/download/plantuml-1.2024.0.jar -O plantuml.jar

# 2. Criar diretório para imagens
mkdir -p docs/images

# 3. Gerar imagens PNG
java -jar plantuml.jar -tpng -o images docs/diagrama_casos_uso.puml
java -jar plantuml.jar -tpng -o images docs/diagrama_classes.puml
java -jar plantuml.jar -tpng -o images docs/casos_uso_simples.puml
java -jar plantuml.jar -tpng -o images docs/classes_simples.puml

# 4. Gerar imagens SVG (melhor qualidade)
java -jar plantuml.jar -tsvg -o images docs/diagrama_casos_uso.puml
java -jar plantuml.jar -tsvg -o images docs/diagrama_classes.puml
java -jar plantuml.jar -tsvg -o images docs/casos_uso_simples.puml
java -jar plantuml.jar -tsvg -o images docs/classes_simples.puml
```

## 📁 Estrutura de Arquivos Gerados

```
docs/
├── images/
│   ├── diagrama_casos_uso.png      # Casos de uso (PNG)
│   ├── diagrama_casos_uso.svg      # Casos de uso (SVG)
│   ├── diagrama_classes.png        # Classes (PNG)
│   ├── diagrama_classes.svg        # Classes (SVG)
│   ├── casos_uso_simples.png       # Casos de uso simples (PNG)
│   ├── casos_uso_simples.svg       # Casos de uso simples (SVG)
│   ├── classes_simples.png         # Classes simples (PNG)
│   └── classes_simples.svg         # Classes simples (SVG)
└── *.puml                          # Arquivos fonte PlantUML
```

## 🔄 Automação via GitHub Actions

O projeto inclui um workflow que gera as imagens automaticamente:

1. **Trigger automático:** Quando arquivos `.puml` são modificados
2. **Trigger manual:** Workflow dispatch no GitHub
3. **Commit automático:** As imagens são commitadas automaticamente

Para executar manualmente no GitHub:
1. Ir para "Actions" no repositório
2. Selecionar "Gerar Diagramas UML"
3. Clicar em "Run workflow"

## 🎯 Verificação

Após a geração, verificar se as imagens foram criadas:

```bash
# Listar imagens geradas
ls -la docs/images/

# Verificar tamanho dos arquivos
du -h docs/images/*.png
du -h docs/images/*.svg
```

## 🛠️ Solução de Problemas

### Erro: "Java não encontrado"
```bash
# Instalar Java
# Windows: https://adoptium.net/
# Ubuntu: sudo apt install openjdk-17-jre
# macOS: brew install openjdk@17
```

### Erro: "Arquivo não encontrado"
```bash
# Verificar se os arquivos .puml existem
ls docs/*.puml

# Verificar se o PlantUML foi baixado
ls plantuml.jar
```

### Imagens não aparecendo no GitHub
1. Verificar se as imagens foram commitadas
2. Aguardar alguns minutos para o cache do GitHub atualizar
3. Verificar os links no README.md

## 📝 Uso no README

As imagens podem ser referenciadas no README.md:

```markdown
![Diagrama de Casos de Uso](docs/images/diagrama_casos_uso.png)
![Diagrama de Classes](docs/images/diagrama_classes.png)
```

## 🎉 Resultado

Depois da geração, os diagramas estarão disponíveis como:
- ✅ Imagens PNG para visualização rápida
- ✅ Imagens SVG para qualidade vetorial
- ✅ Links funcionais no README
- ✅ Visualização automática no GitHub
