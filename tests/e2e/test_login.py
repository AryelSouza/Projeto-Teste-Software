import unittest
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-web-security")
        chrome_options.add_argument("--allow-running-insecure-content")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--window-size=1920,1080")
        
        try:
            print("Instalando ChromeDriver...")
            driver_path = ChromeDriverManager().install()
            print(f"✓ ChromeDriver instalado: {driver_path}")
        except Exception as e:
            print(f"✗ Erro ao instalar ChromeDriver: {e}")
            raise e
        
        self.driver = webdriver.Chrome(
            service=Service(driver_path),
            options=chrome_options
        )
        self.base_url = "http://localhost:5000"
        self.wait = WebDriverWait(self.driver, 15)
    
    def test_login_sucesso(self):
        driver = self.driver
        print("Acessando página de login...")
        driver.get(f"{self.base_url}/")
        
        # Esperar página carregar
        self.wait.until(EC.presence_of_element_located((By.ID, "loginForm")))
        
        print("Preenchendo formulário...")
        driver.find_element(By.ID, "username").send_keys("Ana")
        driver.find_element(By.ID, "password").send_keys("senha123")
        driver.find_element(By.ID, "loginForm").submit()
        
        print("Aguardando mensagem...")
        try:
            # Verificar se a seção principal aparece (indicando login bem-sucedido)
            print("Aguardando seção principal aparecer...")
            self.wait.until(EC.visibility_of_element_located((By.ID, "mainSection")))
            
            # Verificar se a seção de login foi escondida
            login_section = driver.find_element(By.ID, "loginSection")
            self.assertTrue("hidden" in login_section.get_attribute("class"), 
                          "Seção de login deveria estar escondida após login")
            
            print("Login bem-sucedido!")
            driver.save_screenshot("docs/evidencias/login_sucesso.png")
            
        except Exception as e:
            print(f"Erro durante o teste: {str(e)}")
            print("Conteúdo atual da página:")
            print(driver.page_source[:1000])
            driver.save_screenshot("docs/evidencias/login_error.png")
            raise
    
    def test_login_falha_campos_vazios(self):
        driver = self.driver
        print("Testando login com campos vazios...")
        driver.get(f"{self.base_url}/")
        
        # Esperar página carregar
        self.wait.until(EC.presence_of_element_located((By.ID, "loginForm")))
        
        driver.find_element(By.ID, "loginForm").submit()
        
        print("Aguardando mensagem de erro...")
        try:
            message_element = self.wait.until(
                EC.visibility_of_element_located((By.ID, "loginMessage"))
            )
            print(f"Mensagem de erro: {message_element.text}")
            self.assertIn("obrigatório", message_element.text.lower())
            driver.save_screenshot("docs/evidencias/login_falha.png")
        except Exception as e:
            print(f"Erro durante o teste: {str(e)}")
            driver.save_screenshot("docs/evidencias/login_error.png")
            raise
    
    def tearDown(self):
        print("Finalizando driver...")
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
