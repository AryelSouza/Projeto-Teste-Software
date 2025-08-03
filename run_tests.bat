@echo off
set TIPO=%1
if "%TIPO%"=="" set TIPO=all

echo === Sistema de Testes - Biblioteca ===
echo Tipo de teste: %TIPO%

if "%TIPO%"=="unit" goto run_unit
if "%TIPO%"=="api" goto run_api  
if "%TIPO%"=="e2e" goto run_e2e
if "%TIPO%"=="admin" goto run_admin
if "%TIPO%"=="all" goto run_all

echo Tipo de teste invalido. Use: all, unit, api, e2e, admin
goto end

:run_unit
echo Executando testes unitarios...
python -m pytest tests/unit/ -v
goto end

:run_api
echo Executando testes de API...
python -m pytest tests/api/ -v
goto end

:run_e2e
echo Iniciando servidor Flask...
start /B python backend/app.py
timeout /t 7 /nobreak >nul
echo Executando testes E2E...
python -m pytest tests/e2e/ -v -s
taskkill /F /IM python.exe 2>nul
goto end

:run_admin
echo Executando testes de admin...
python -m pytest tests/unit/test_admin.py tests/api/test_admin_api.py -v
echo Iniciando servidor para testes E2E de admin...
start /B python backend/app.py
timeout /t 7 /nobreak >nul
python -m pytest tests/e2e/test_admin_e2e.py tests/e2e/test_usuario_normal.py -v -s
taskkill /F /IM python.exe 2>nul
goto end

:run_all
echo Executando todos os testes...
python -m pytest tests/unit/ -v
python -m pytest tests/api/ -v
echo Iniciando servidor para testes E2E...
start /B python backend/app.py
timeout /t 7 /nobreak >nul
python -m pytest tests/e2e/ -v -s
taskkill /F /IM python.exe 2>nul

:end
echo === Testes finalizados ===
pause
