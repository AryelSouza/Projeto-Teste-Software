"""
Teste E2E para verificar que usuários normais não têm acesso ao painel de admin
"""
import unittest
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUsuarioNormalE2E(unittest.TestCase):
    def setUp(self):
        """Configuração inicial para cada teste"""
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
    
    def test_usuario_normal_nao_ve_admin(self):
        """Teste: usuário normal não deve ver seção de admin"""
        # Realizar login como usuário normal
        print("Realizando login como usuário normal...")
        self.driver.get(f"{self.base_url}/")
        
        # Esperar página carregar
        self.wait.until(EC.presence_of_element_located((By.ID, "loginForm")))
        
        self.driver.find_element(By.ID, "username").send_keys("Ana")
        self.driver.find_element(By.ID, "password").send_keys("senha123")
        self.driver.find_element(By.ID, "loginForm").submit()
        
        # Aguardar login completar e seção principal aparecer
        self.wait.until(EC.visibility_of_element_located((By.ID, "mainSection")))
        print("Login de usuário normal realizado com sucesso")
        
        # Pequena pausa adicional
        time.sleep(1)
        
        # Verificar que a seção de admin está escondida
        admin_section = self.driver.find_element(By.ID, "adminSection")
        self.assertTrue("hidden" in admin_section.get_attribute("class"),
                       "Seção de admin deveria estar escondida para usuários normais")
        
        # Verificar que elementos de empréstimo normal estão visíveis
        emprestimo_form = self.driver.find_element(By.ID, "emprestimoForm")
        self.assertFalse("hidden" in emprestimo_form.get_attribute("class"))
        
        livros_list = self.driver.find_element(By.ID, "livrosList")
        self.assertTrue(livros_list.is_displayed())
        
        self.driver.save_screenshot("docs/evidencias/usuario_normal_sem_admin.png")
        print("✓ Usuário normal não tem acesso ao painel de admin")
    
    def tearDown(self):
        """Limpeza após cada teste"""
        print("Finalizando driver...")
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
