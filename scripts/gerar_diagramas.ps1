# 🎨 Script para Gerar Imagens dos Diagramas PlantUML
# Autor: GitHub Copilot
# Data: 2024

Write-Host "🎨 Iniciando geração de imagens dos diagramas UML..." -ForegroundColor Cyan
Write-Host ""

# Verificar se Java está instalado
try {
    $javaVersion = java -version 2>&1
    Write-Host "✅ Java encontrado: $($javaVersion[0])" -ForegroundColor Green
} catch {
    Write-Host "❌ Erro: Java não encontrado!" -ForegroundColor Red
    Write-Host "📥 Baixe e instale Java de: https://adoptium.net/" -ForegroundColor Yellow
    Write-Host "📋 Após instalar, reinicie o PowerShell e execute novamente." -ForegroundColor Yellow
    exit 1
}

# Definir caminhos
$projectRoot = Split-Path -Parent $PSScriptRoot
$docsPath = Join-Path $projectRoot "docs"
$imagesPath = Join-Path $docsPath "images"
$plantUmlJar = Join-Path $projectRoot "plantuml.jar"

Write-Host "📁 Diretório do projeto: $projectRoot" -ForegroundColor Blue
Write-Host "📁 Diretório docs: $docsPath" -ForegroundColor Blue
Write-Host "📁 Diretório imagens: $imagesPath" -ForegroundColor Blue
Write-Host ""

# Criar diretório de imagens se não existir
if (-not (Test-Path $imagesPath)) {
    New-Item -ItemType Directory -Path $imagesPath -Force | Out-Null
    Write-Host "✅ Diretório de imagens criado: $imagesPath" -ForegroundColor Green
} else {
    Write-Host "✅ Diretório de imagens já existe: $imagesPath" -ForegroundColor Green
}

# Baixar PlantUML se não existir
if (-not (Test-Path $plantUmlJar)) {
    Write-Host "📥 Baixando PlantUML..." -ForegroundColor Yellow
    try {
        $plantUmlUrl = "https://github.com/plantuml/plantuml/releases/latest/download/plantuml-1.2024.0.jar"
        Invoke-WebRequest -Uri $plantUmlUrl -OutFile $plantUmlJar
        Write-Host "✅ PlantUML baixado com sucesso!" -ForegroundColor Green
    } catch {
        Write-Host "❌ Erro ao baixar PlantUML: $($_.Exception.Message)" -ForegroundColor Red
        exit 1
    }
} else {
    Write-Host "✅ PlantUML já existe: $plantUmlJar" -ForegroundColor Green
}

Write-Host ""

# Lista de diagramas para gerar
$diagramas = @(
    "diagramas\plantuml\diagrama_casos_uso.puml",
    "diagramas\plantuml\diagrama_classes.puml", 
    "diagramas\plantuml\casos_uso_simples.puml",
    "diagramas\plantuml\classes_simples.puml"
)

$sucessos = 0
$erros = 0

foreach ($diagrama in $diagramas) {
    $diagramaPath = Join-Path $docsPath $diagrama
    
    if (Test-Path $diagramaPath) {
        Write-Host "🔄 Processando: $diagrama" -ForegroundColor Cyan
        
        try {
            # Gerar PNG
            $argsPng = @("-jar", $plantUmlJar, "-tpng", "-o", "images", $diagramaPath)
            Start-Process -FilePath "java" -ArgumentList $argsPng -Wait -NoNewWindow
            
            # Gerar SVG  
            $argsSvg = @("-jar", $plantUmlJar, "-tsvg", "-o", "images", $diagramaPath)
            Start-Process -FilePath "java" -ArgumentList $argsSvg -Wait -NoNewWindow
            
            Write-Host "  ✅ PNG e SVG gerados com sucesso!" -ForegroundColor Green
            $sucessos++
        } catch {
            Write-Host "  ❌ Erro ao processar $diagrama`: $($_.Exception.Message)" -ForegroundColor Red
            $erros++
        }
    } else {
        Write-Host "⚠️  Diagrama não encontrado: $diagrama" -ForegroundColor Yellow
        $erros++
    }
}

Write-Host ""
Write-Host "📊 Resultado da geração:" -ForegroundColor Cyan
Write-Host "  ✅ Sucessos: $sucessos" -ForegroundColor Green
Write-Host "  ❌ Erros: $erros" -ForegroundColor Red

# Listar arquivos gerados
Write-Host ""
Write-Host "📋 Arquivos gerados:" -ForegroundColor Cyan
$imageFiles = Get-ChildItem -Path $imagesPath -Filter "*.png" 2>$null
if ($imageFiles) {
    foreach ($file in $imageFiles) {
        $size = [math]::Round($file.Length / 1KB, 2)
        Write-Host "  📄 $($file.Name) ($size KB)" -ForegroundColor Blue
    }
} else {
    Write-Host "  ⚠️  Nenhum arquivo de imagem encontrado" -ForegroundColor Yellow
}

Write-Host ""
if ($erros -eq 0) {
    Write-Host "🎉 Geração concluída com sucesso!" -ForegroundColor Green
    Write-Host "📁 Imagens salvas em: $imagesPath" -ForegroundColor Blue
    Write-Host "🔗 Agora você pode fazer commit das imagens para o GitHub!" -ForegroundColor Yellow
} else {
    Write-Host "⚠️  Geração concluída com alguns erros." -ForegroundColor Yellow
    Write-Host "📖 Consulte o arquivo docs/solucao_diagramas.md para resolver problemas." -ForegroundColor Blue
}

Write-Host ""
Write-Host "Pressione Enter para continuar..." -ForegroundColor Gray
Read-Host
