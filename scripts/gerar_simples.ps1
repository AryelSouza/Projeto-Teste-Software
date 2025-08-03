# Script Simples para Gerar Diagramas
Write-Host "Gerando diagramas..." -ForegroundColor Green

$projectPath = "C:\Users\vasco\codigos\test_software\Projeto-Teste-Software"
$docsPath = "$projectPath\docs"
$imagesPath = "$docsPath\images"

# Criar diretório de imagens
if (-not (Test-Path $imagesPath)) {
    New-Item -ItemType Directory -Path $imagesPath -Force
    Write-Host "Diretório criado: $imagesPath"
}

# Testar se Java está disponível
try {
    java -version
    Write-Host "Java OK" -ForegroundColor Green
} catch {
    Write-Host "Java não encontrado. Instalando..." -ForegroundColor Yellow
    
    # Tentar instalar Java via winget
    try {
        winget install Microsoft.OpenJDK.17
        Write-Host "Java instalado via winget" -ForegroundColor Green
    } catch {
        Write-Host "Erro ao instalar Java. Instale manualmente de: https://adoptium.net/" -ForegroundColor Red
        exit 1
    }
}

# Baixar PlantUML
$plantUmlPath = "$projectPath\plantuml.jar"
if (-not (Test-Path $plantUmlPath)) {
    Write-Host "Baixando PlantUML..." -ForegroundColor Yellow
    try {
        Invoke-WebRequest -Uri "https://github.com/plantuml/plantuml/releases/latest/download/plantuml-1.2024.0.jar" -OutFile $plantUmlPath
        Write-Host "PlantUML baixado" -ForegroundColor Green
    } catch {
        Write-Host "Erro ao baixar PlantUML" -ForegroundColor Red
        exit 1
    }
}

# Gerar imagens
$diagramas = @(
    "diagramas\plantuml\diagrama_casos_uso.puml",
    "diagramas\plantuml\diagrama_classes.puml",
    "diagramas\plantuml\casos_uso_simples.puml",
    "diagramas\plantuml\classes_simples.puml"
)

foreach ($diagrama in $diagramas) {
    $diagramaPath = "$docsPath\$diagrama"
    if (Test-Path $diagramaPath) {
        Write-Host "Processando: $diagrama" -ForegroundColor Cyan
        
        # Gerar PNG
        java -jar $plantUmlPath -tpng -o images $diagramaPath
        
        # Gerar SVG
        java -jar $plantUmlPath -tsvg -o images $diagramaPath
        
        Write-Host "✅ $diagrama processado" -ForegroundColor Green
    } else {
        Write-Host "❌ $diagrama não encontrado" -ForegroundColor Red
    }
}

# Listar arquivos gerados
Write-Host "`nArquivos gerados:" -ForegroundColor Cyan
Get-ChildItem -Path $imagesPath -Filter "*.png" | ForEach-Object {
    Write-Host "  📄 $($_.Name)" -ForegroundColor Blue
}

Write-Host "`n🎉 Concluído! Imagens salvas em: $imagesPath" -ForegroundColor Green
