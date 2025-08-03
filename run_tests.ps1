# Script para executar todos os testes do sistema
param(
    [string]$tipo = "all"  # all, unit, api, e2e, admin
)

Write-Host "=== Sistema de Testes - Biblioteca ===" -ForegroundColor Green
Write-Host "Tipo de teste: $tipo" -ForegroundColor Cyan

# Verificar se estamos no ambiente virtual
if (-not $env:VIRTUAL_ENV) {
    Write-Host "AVISO: Ambiente virtual não detectado. Ativando..." -ForegroundColor Yellow
    & ".\venv\Scripts\Activate.ps1"
}

# Criar diretório de evidências se não existir
if (-not (Test-Path "docs/evidencias")) {
    New-Item -ItemType Directory -Path "docs/evidencias" -Force | Out-Null
    Write-Host "✓ Diretório de evidências criado" -ForegroundColor Green
}

function Run-UnitTests {
    Write-Host "`n=== Executando Testes Unitários ===" -ForegroundColor Cyan
    python -m pytest tests/unit/ -v
}

function Run-ApiTests {
    Write-Host "`n=== Executando Testes de API ===" -ForegroundColor Cyan
    python -m pytest tests/api/ -v
}

function Run-E2ETests {
    Write-Host "`n=== Executando Testes E2E ===" -ForegroundColor Cyan
    
    Write-Host "Iniciando servidor Flask..." -ForegroundColor Yellow
    $serverJob = Start-Job -ScriptBlock {
        Set-Location $using:PWD
        python backend/app.py
    }

    Write-Host "Aguardando servidor inicializar..." -ForegroundColor Yellow
    Start-Sleep -Seconds 7

    # Verificar se o servidor está respondendo
    $serverReady = $false
    $attempts = 0
    while (-not $serverReady -and $attempts -lt 3) {
        try {
            $response = Invoke-WebRequest -Uri "http://localhost:5000" -Method Get -TimeoutSec 5 -ErrorAction Stop
            Write-Host "✓ Servidor Flask iniciado com sucesso!" -ForegroundColor Green
            $serverReady = $true
        } catch {
            $attempts++
            Write-Host "✗ Tentativa $attempts: Servidor Flask não respondeu. Aguardando..." -ForegroundColor Yellow
            Start-Sleep -Seconds 3
        }
    }

    if (-not $serverReady) {
        Write-Host "✗ Erro: Servidor Flask não iniciou corretamente!" -ForegroundColor Red
        Stop-Job $serverJob -ErrorAction SilentlyContinue
        Remove-Job $serverJob -ErrorAction SilentlyContinue
        return $false
    }

    try {
        python -m pytest tests/e2e/ -v -s
        $testResult = $LASTEXITCODE
    } finally {
        Write-Host "Finalizando servidor..." -ForegroundColor Yellow
        Stop-Job $serverJob -ErrorAction SilentlyContinue
        Remove-Job $serverJob -ErrorAction SilentlyContinue
    }
    
    return $testResult -eq 0
}

function Run-AdminTests {
    Write-Host "`n=== Executando Testes de Admin ===" -ForegroundColor Cyan
    Write-Host "Testes unitários de admin..." -ForegroundColor Yellow
    python -m pytest tests/unit/test_admin.py -v
    
    Write-Host "`nTestes de API de admin..." -ForegroundColor Yellow
    python -m pytest tests/api/test_admin_api.py -v
    
    Write-Host "`nTestes E2E de admin..." -ForegroundColor Yellow
    
    # Iniciar servidor para testes E2E de admin
    $serverJob = Start-Job -ScriptBlock {
        Set-Location $using:PWD
        python backend/app.py
    }
    
    Start-Sleep -Seconds 7
    
    try {
        python -m pytest tests/e2e/test_admin_e2e.py tests/e2e/test_usuario_normal.py -v -s
    } finally {
        Stop-Job $serverJob -ErrorAction SilentlyContinue
        Remove-Job $serverJob -ErrorAction SilentlyContinue
    }
}

# Executar testes baseado no parâmetro
switch ($tipo) {
    "unit" { Run-UnitTests }
    "api" { Run-ApiTests }
    "e2e" { Run-E2ETests }
    "admin" { Run-AdminTests }
    "all" {
        Write-Host "Executando todos os testes..." -ForegroundColor Cyan
        Run-UnitTests
        Run-ApiTests
        $e2eResult = Run-E2ETests
        
        if ($e2eResult) {
            Write-Host "`n✓ Todos os testes executados com sucesso!" -ForegroundColor Green
        } else {
            Write-Host "`n✗ Alguns testes falharam!" -ForegroundColor Red
        }
    }
    default {
        Write-Host "Tipo de teste inválido. Use: all, unit, api, e2e, admin" -ForegroundColor Red
        exit 1
    }
}

Write-Host "`n=== Testes finalizados ===" -ForegroundColor Green
