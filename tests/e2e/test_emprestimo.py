import unittest
import requests
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestEmprestimo(unittest.TestCase):
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
        
        # Resetar banco de dados antes de começar
        requests.post(f"{self.base_url}/reset")
        
        # Realizar login
        print("Realizando login...")
        self.driver.get(f"{self.base_url}/")
        
        # Esperar página carregar
        self.wait.until(EC.presence_of_element_located((By.ID, "loginForm")))
        
        self.driver.find_element(By.ID, "username").send_keys("Ana")
        self.driver.find_element(By.ID, "password").send_keys("senha123")
        self.driver.find_element(By.ID, "loginForm").submit()
        
        # Aguardar login completar e seção principal aparecer
        self.wait.until(EC.visibility_of_element_located((By.ID, "mainSection")))
        print("Login realizado com sucesso")
        
        # Pequena pausa adicional
        time.sleep(1)
    
    def test_emprestimo_sucesso(self):
        driver = self.driver
        print("Testando empréstimo bem-sucedido...")
        
        # Aguardar formulário de empréstimo
        self.wait.until(EC.visibility_of_element_located((By.ID, "emprestimoForm")))
        
        # Emprestar livro ID 1
        driver.find_element(By.ID, "livroId").send_keys("1")
        driver.find_element(By.ID, "emprestimoForm").submit()
        
        print("Aguardando mensagem de sucesso...")
        try:
            message_element = self.wait.until(
                EC.visibility_of_element_located((By.ID, "emprestimoMessage"))
            )
            print(f"Mensagem: {message_element.text}")
            self.assertIn("sucesso", message_element.text.lower())
            driver.save_screenshot("docs/evidencias/emprestimo_sucesso.png")
        except Exception as e:
            print(f"Erro durante o teste: {str(e)}")
            driver.save_screenshot("docs/evidencias/emprestimo_error.png")
            raise
    
    def test_emprestimo_livro_indisponivel(self):
        driver = self.driver
        print("Testando empréstimo com livro indisponível...")
        
        # Aguardar formulário de empréstimo
        self.wait.until(EC.visibility_of_element_located((By.ID, "emprestimoForm")))
        
        # Primeiro empréstimo (sucesso)
        driver.find_element(By.ID, "livroId").send_keys("1")
        driver.find_element(By.ID, "emprestimoForm").submit()
        
        # Aguardar mensagem do primeiro empréstimo
        self.wait.until(
            EC.visibility_of_element_located((By.ID, "emprestimoMessage"))
        )
        
        # Pequena pausa para garantir estado atualizado
        time.sleep(1)
        
        # Tentar emprestar o mesmo livro novamente
        print("Tentando empréstimo do mesmo livro...")
        driver.find_element(By.ID, "livroId").clear()
        driver.find_element(By.ID, "livroId").send_keys("1")
        driver.find_element(By.ID, "emprestimoForm").submit()
        
        print("Aguardando mensagem de erro...")
        try:
            message_element = self.wait.until(
                EC.visibility_of_element_located((By.ID, "emprestimoMessage"))
            )
            print(f"Mensagem: {message_element.text}")
            self.assertIn("indisponível", message_element.text.lower())
            driver.save_screenshot("docs/evidencias/emprestimo_falha.png")
        except Exception as e:
            print(f"Erro durante o teste: {str(e)}")
            driver.save_screenshot("docs/evidencias/emprestimo_error.png")
            raise
    
    def tearDown(self):
        print("Finalizando driver...")
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
