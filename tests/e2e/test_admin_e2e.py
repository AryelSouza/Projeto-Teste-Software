"""
Testes End-to-End para funcionalidades de administrador
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

class TestAdminE2E(unittest.TestCase):
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
        
        # Realizar login como admin
        print("Realizando login como admin...")
        self.driver.get(f"{self.base_url}/")
        
        # Esperar página carregar
        self.wait.until(EC.presence_of_element_located((By.ID, "loginForm")))
        
        self.driver.find_element(By.ID, "username").send_keys("Admin")
        self.driver.find_element(By.ID, "password").send_keys("admin123")
        self.driver.find_element(By.ID, "loginForm").submit()
        
        # Aguardar login completar e seção principal aparecer
        self.wait.until(EC.visibility_of_element_located((By.ID, "mainSection")))
        
        # Aguardar seção de admin aparecer
        self.wait.until(EC.visibility_of_element_located((By.ID, "adminSection")))
        print("Login de admin realizado com sucesso")
        
        # Pequena pausa adicional
        time.sleep(1)
    
    def test_admin_section_visible(self):
        """Teste: seção de admin deve estar visível para administradores"""
        admin_section = self.driver.find_element(By.ID, "adminSection")
        self.assertFalse("hidden" in admin_section.get_attribute("class"))
        
        # Verificar se as abas estão presentes
        self.assertTrue(self.driver.find_element(By.XPATH, "//button[contains(text(), 'Adicionar Livro')]"))
        self.assertTrue(self.driver.find_element(By.XPATH, "//button[contains(text(), 'Devoluções')]"))
        self.assertTrue(self.driver.find_element(By.XPATH, "//button[contains(text(), 'Logs')]"))
        
        self.driver.save_screenshot("docs/evidencias/admin_section_visible.png")
    
    def test_adicionar_livro_sucesso(self):
        """Teste: adicionar novo livro com sucesso"""
        # A aba de adicionar livro já deve estar ativa por padrão
        add_book_tab = self.driver.find_element(By.ID, "addBookTab")
        self.assertTrue("active" in add_book_tab.get_attribute("class"))
        
        # Preencher formulário
        titulo_input = self.driver.find_element(By.ID, "novoTitulo")
        titulo_input.send_keys("Livro Teste E2E")
        
        # Submeter formulário
        add_book_form = self.driver.find_element(By.ID, "addBookForm")
        add_book_form.submit()
        
        # Aguardar mensagem de sucesso
        print("Aguardando mensagem de sucesso...")
        try:
            message_element = self.wait.until(
                EC.visibility_of_element_located((By.ID, "addBookMessage"))
            )
            print(f"Mensagem: {message_element.text}")
            self.assertIn("sucesso", message_element.text.lower())
            
            # Verificar se o campo foi limpo
            titulo_input = self.driver.find_element(By.ID, "novoTitulo")
            self.assertEqual(titulo_input.get_attribute("value"), "")
            
            self.driver.save_screenshot("docs/evidencias/adicionar_livro_sucesso.png")
            
        except Exception as e:
            print(f"Erro durante o teste: {str(e)}")
            self.driver.save_screenshot("docs/evidencias/adicionar_livro_error.png")
            raise
    
    def test_visualizar_logs_emprestimos(self):
        """Teste: visualizar logs de empréstimos"""
        # Primeiro, realizar um empréstimo para ter dados nos logs
        # Ir para a seção de empréstimo
        emprestimo_form = self.driver.find_element(By.ID, "emprestimoForm")
        livro_id_input = self.driver.find_element(By.ID, "livroId")
        livro_id_input.send_keys("1")
        emprestimo_form.submit()
        
        # Aguardar empréstimo ser processado
        time.sleep(2)
        
        # Ir para a aba de logs
        logs_btn = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Logs')]")
        logs_btn.click()
        
        # Aguardar aba de logs carregar
        time.sleep(2)
        
        # Verificar se os logs foram carregados
        logs_container = self.driver.find_element(By.ID, "logsEmprestimos")
        emprestimo_items = logs_container.find_elements(By.CLASS_NAME, "emprestimo-item")
        
        self.assertGreater(len(emprestimo_items), 0, "Deveria haver pelo menos um empréstimo nos logs")
        
        # Verificar conteúdo do primeiro empréstimo
        primeiro_emprestimo = emprestimo_items[0]
        self.assertIn("Livro:", primeiro_emprestimo.text)
        self.assertIn("Data Empréstimo:", primeiro_emprestimo.text)
        self.assertIn("Em andamento", primeiro_emprestimo.text)
        
        self.driver.save_screenshot("docs/evidencias/logs_emprestimos.png")
    
    def test_devolver_livro_sucesso(self):
        """Teste: devolver livro com sucesso"""
        # Primeiro, realizar um empréstimo
        emprestimo_form = self.driver.find_element(By.ID, "emprestimoForm")
        livro_id_input = self.driver.find_element(By.ID, "livroId")
        livro_id_input.send_keys("1")
        emprestimo_form.submit()
        
        # Aguardar empréstimo ser processado
        time.sleep(2)
        
        # Ir para a aba de devoluções
        returns_btn = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Devoluções')]")
        returns_btn.click()
        
        # Aguardar aba de devoluções carregar
        time.sleep(2)
        
        # Verificar se há empréstimos ativos
        returns_container = self.driver.find_element(By.ID, "emprestimosAtivos")
        emprestimo_items = returns_container.find_elements(By.CLASS_NAME, "emprestimo-item")
        
        self.assertGreater(len(emprestimo_items), 0, "Deveria haver pelo menos um empréstimo ativo")
        
        # Clicar no botão de devolver do primeiro empréstimo
        devolver_btn = emprestimo_items[0].find_element(By.CLASS_NAME, "devolver-btn")
        devolver_btn.click()
        
        # Aguardar e aceitar o alert (confirmação)
        try:
            alert = self.wait.until(EC.alert_is_present())
            alert_text = alert.text
            print(f"Alert text: {alert_text}")
            self.assertIn("devolvido com sucesso", alert_text.lower())
            alert.accept()
        except Exception as e:
            print(f"Erro com alert: {e}")
        
        # Aguardar página atualizar
        time.sleep(2)
        
        # Verificar que não há mais empréstimos ativos
        returns_container = self.driver.find_element(By.ID, "emprestimosAtivos")
        # Pode aparecer mensagem "Nenhum empréstimo ativo" ou lista vazia
        texto_container = returns_container.text
        self.assertTrue(
            "Nenhum empréstimo ativo" in texto_container or 
            len(returns_container.find_elements(By.CLASS_NAME, "emprestimo-item")) == 0,
            "Não deveria haver empréstimos ativos após a devolução"
        )
        
        self.driver.save_screenshot("docs/evidencias/devolver_livro_sucesso.png")
    
    def test_navegacao_entre_abas_admin(self):
        """Teste: navegação entre as abas de administração"""
        # Verificar aba inicial (Adicionar Livro)
        add_book_tab = self.driver.find_element(By.ID, "addBookTab")
        self.assertTrue("active" in add_book_tab.get_attribute("class"))
        
        # Ir para aba de devoluções
        returns_btn = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Devoluções')]")
        returns_btn.click()
        time.sleep(1)
        
        returns_tab = self.driver.find_element(By.ID, "returnsTab")
        self.assertTrue("active" in returns_tab.get_attribute("class"))
        
        # Verificar que aba anterior não está mais ativa
        add_book_tab = self.driver.find_element(By.ID, "addBookTab")
        self.assertFalse("active" in add_book_tab.get_attribute("class"))
        
        # Ir para aba de logs
        logs_btn = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Logs')]")
        logs_btn.click()
        time.sleep(1)
        
        logs_tab = self.driver.find_element(By.ID, "logsTab")
        self.assertTrue("active" in logs_tab.get_attribute("class"))
        
        # Verificar que aba anterior não está mais ativa
        returns_tab = self.driver.find_element(By.ID, "returnsTab")
        self.assertFalse("active" in returns_tab.get_attribute("class"))
        
        self.driver.save_screenshot("docs/evidencias/navegacao_abas_admin.png")
    
    def tearDown(self):
        """Limpeza após cada teste"""
        print("Finalizando driver...")
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
