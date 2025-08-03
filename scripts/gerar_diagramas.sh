#!/bin/bash
# 🎨 Script para Gerar Imagens dos Diagramas PlantUML
# Autor: GitHub Copilot  
# Data: 2024

echo "🎨 Iniciando geração de imagens dos diagramas UML..."
echo ""

# Verificar se Java está instalado
if ! command -v java &> /dev/null; then
    echo "❌ Erro: Java não encontrado!"
    echo "📥 Instale Java com:"
    echo "  Ubuntu/Debian: sudo apt install openjdk-17-jre"
    echo "  macOS: brew install openjdk@17"
    echo "  CentOS/RHEL: sudo yum install java-17-openjdk"
    exit 1
fi

JAVA_VERSION=$(java -version 2>&1 | head -n 1)
echo "✅ Java encontrado: $JAVA_VERSION"

# Definir caminhos
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DOCS_PATH="$PROJECT_ROOT/docs"
IMAGES_PATH="$DOCS_PATH/images"
PLANTUML_JAR="$PROJECT_ROOT/plantuml.jar"

echo "📁 Diretório do projeto: $PROJECT_ROOT"
echo "📁 Diretório docs: $DOCS_PATH"
echo "📁 Diretório imagens: $IMAGES_PATH"
echo ""

# Criar diretório de imagens se não existir
if [ ! -d "$IMAGES_PATH" ]; then
    mkdir -p "$IMAGES_PATH"
    echo "✅ Diretório de imagens criado: $IMAGES_PATH"
else
    echo "✅ Diretório de imagens já existe: $IMAGES_PATH"
fi

# Baixar PlantUML se não existir
if [ ! -f "$PLANTUML_JAR" ]; then
    echo "📥 Baixando PlantUML..."
    if command -v wget &> /dev/null; then
        wget "https://github.com/plantuml/plantuml/releases/latest/download/plantuml-1.2024.0.jar" -O "$PLANTUML_JAR"
    elif command -v curl &> /dev/null; then
        curl -L "https://github.com/plantuml/plantuml/releases/latest/download/plantuml-1.2024.0.jar" -o "$PLANTUML_JAR"
    else
        echo "❌ Erro: wget ou curl não encontrado para baixar PlantUML"
        exit 1
    fi
    
    if [ $? -eq 0 ]; then
        echo "✅ PlantUML baixado com sucesso!"
    else
        echo "❌ Erro ao baixar PlantUML"
        exit 1
    fi
else
    echo "✅ PlantUML já existe: $PLANTUML_JAR"
fi

echo ""

# Lista de diagramas para gerar
DIAGRAMAS=(
    "diagramas/plantuml/diagrama_casos_uso.puml"
    "diagramas/plantuml/diagrama_classes.puml"
    "diagramas/plantuml/casos_uso_simples.puml"
    "diagramas/plantuml/classes_simples.puml"
)

SUCESSOS=0
ERROS=0

for DIAGRAMA in "${DIAGRAMAS[@]}"; do
    DIAGRAMA_PATH="$DOCS_PATH/$DIAGRAMA"
    
    if [ -f "$DIAGRAMA_PATH" ]; then
        echo "🔄 Processando: $DIAGRAMA"
        
        # Gerar PNG
        if java -jar "$PLANTUML_JAR" -tpng -o images "$DIAGRAMA_PATH"; then
            # Gerar SVG
            if java -jar "$PLANTUML_JAR" -tsvg -o images "$DIAGRAMA_PATH"; then
                echo "  ✅ PNG e SVG gerados com sucesso!"
                ((SUCESSOS++))
            else
                echo "  ❌ Erro ao gerar SVG para $DIAGRAMA"
                ((ERROS++))
            fi
        else
            echo "  ❌ Erro ao gerar PNG para $DIAGRAMA"
            ((ERROS++))
        fi
    else
        echo "⚠️  Diagrama não encontrado: $DIAGRAMA"
        ((ERROS++))
    fi
done

echo ""
echo "📊 Resultado da geração:"
echo "  ✅ Sucessos: $SUCESSOS"
echo "  ❌ Erros: $ERROS"

# Listar arquivos gerados
echo ""
echo "📋 Arquivos gerados:"
if ls "$IMAGES_PATH"/*.{png,svg} 1> /dev/null 2>&1; then
    for FILE in "$IMAGES_PATH"/*.{png,svg}; do
        if [ -f "$FILE" ]; then
            SIZE=$(du -h "$FILE" | cut -f1)
            BASENAME=$(basename "$FILE")
            echo "  📄 $BASENAME ($SIZE)"
        fi
    done
else
    echo "  ⚠️  Nenhum arquivo de imagem encontrado"
fi

echo ""
if [ $ERROS -eq 0 ]; then
    echo "🎉 Geração concluída com sucesso!"
    echo "📁 Imagens salvas em: $IMAGES_PATH"
    echo "🔗 Agora você pode fazer commit das imagens para o GitHub!"
else
    echo "⚠️  Geração concluída com alguns erros."
    echo "📖 Consulte o arquivo docs/solucao_diagramas.md para resolver problemas."
fi

echo ""
echo "Pressione Enter para continuar..."
read
