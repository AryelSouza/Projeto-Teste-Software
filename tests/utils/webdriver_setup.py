"""
Utilitário para configurar o WebDriver de forma robusta
"""
import os
import platform
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType


def get_chrome_options():
    """Configura as opções do Chrome para testes"""
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument("--allow-running-insecure-content")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-plugins")
    chrome_options.add_argument("--disable-images")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
    
    return chrome_options


def setup_chrome_driver():
    """
    Configura o ChromeDriver com várias estratégias de fallback
    """
    chrome_options = get_chrome_options()
    
    # Estratégia 1: Tentar Chrome for Testing (mais recente)
    try:
        print("Tentando Chrome for Testing...")
        driver_path = ChromeDriverManager(
            chrome_type=ChromeType.CHROMIUM
        ).install()
        
        driver = webdriver.Chrome(
            service=Service(driver_path),
            options=chrome_options
        )
        print(f"✓ Chrome for Testing funcionou: {driver_path}")
        return driver
        
    except Exception as e:
        print(f"✗ Chrome for Testing falhou: {e}")
    
    # Estratégia 2: Tentar versão específica conhecida
    try:
        print("Tentando versão específica do ChromeDriver...")
        driver_path = ChromeDriverManager(version="114.0.5735.90").install()
        
        driver = webdriver.Chrome(
            service=Service(driver_path),
            options=chrome_options
        )
        print(f"✓ Versão específica funcionou: {driver_path}")
        return driver
        
    except Exception as e:
        print(f"✗ Versão específica falhou: {e}")
    
    # Estratégia 3: Tentar versão padrão
    try:
        print("Tentando versão padrão...")
        driver_path = ChromeDriverManager().install()
        
        driver = webdriver.Chrome(
            service=Service(driver_path),
            options=chrome_options
        )
        print(f"✓ Versão padrão funcionou: {driver_path}")
        return driver
        
    except Exception as e:
        print(f"✗ Versão padrão falhou: {e}")
    
    # Estratégia 4: Tentar ChromeDriver do PATH do sistema
    try:
        print("Tentando ChromeDriver do sistema...")
        driver = webdriver.Chrome(options=chrome_options)
        print("✓ ChromeDriver do sistema funcionou")
        return driver
        
    except Exception as e:
        print(f"✗ ChromeDriver do sistema falhou: {e}")
    
    # Se todas as estratégias falharam
    raise Exception(
        "Não foi possível configurar o ChromeDriver. "
        "Verifique se o Chrome está instalado e tente instalar o ChromeDriver manualmente."
    )


def get_driver():
    """Interface simples para obter um driver configurado"""
    return setup_chrome_driver()
