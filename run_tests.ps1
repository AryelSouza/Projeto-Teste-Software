# Script para executar testes E2E com servidor Flask
Write-Host "=== Iniciando Sistema de Testes E2E ===" -ForegroundColor Green

# Verificar se estamos no ambiente virtual
if (-not $env:VIRTUAL_ENV) {
    Write-Host "AVISO: Ambiente virtual não detectado. Ativando..." -ForegroundColor Yellow
    & ".\venv\Scripts\Activate.ps1"
}

Write-Host "Iniciando servidor Flask..." -ForegroundColor Cyan
$serverJob = Start-Job -ScriptBlock {
    Set-Location $using:PWD
    python backend/app.py
}

Write-Host "Aguardando servidor inicializar..." -ForegroundColor Yellow
Start-Sleep -Seconds 7  # Aumentado para 7 segundos

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
    exit 1
}

Write-Host "Executando testes E2E..." -ForegroundColor Cyan
pytest tests/e2e/ -v -s

Write-Host "`nFinalizando servidor..." -ForegroundColor Yellow
Stop-Job $serverJob -ErrorAction SilentlyContinue
Remove-Job $serverJob -ErrorAction SilentlyContinue

Write-Host "=== Testes finalizados ===" -ForegroundColor Green
