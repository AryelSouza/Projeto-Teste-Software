"""
Testes de API para funcionalidades de administrador
"""
import unittest
import json
import requests
import time
import subprocess
import os
import signal

class TestAdminAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Iniciar servidor Flask para testes"""
        cls.base_url = 'http://localhost:5000'
        cls.server_process = None
        
        try:
            # Verificar se servidor já está rodando
            response = requests.get(cls.base_url, timeout=2)
            print("Servidor já está rodando")
        except requests.exceptions.RequestException:
            # Iniciar servidor
            import sys
            backend_path = os.path.join(os.path.dirname(__file__), '..', '..', 'backend')
            sys.path.insert(0, backend_path)
            
            cls.server_process = subprocess.Popen(
                ['python', 'app.py'],
                cwd=backend_path,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            
            # Aguardar servidor inicializar
            max_attempts = 30
            for attempt in range(max_attempts):
                try:
                    response = requests.get(cls.base_url, timeout=2)
                    print(f"Servidor iniciado com sucesso (tentativa {attempt + 1})")
                    break
                except requests.exceptions.RequestException:
                    if attempt == max_attempts - 1:
                        raise Exception("Não foi possível inicializar o servidor")
                    time.sleep(1)
    
    @classmethod
    def tearDownClass(cls):
        """Parar servidor Flask"""
        if cls.server_process:
            try:
                cls.server_process.terminate()
                cls.server_process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                cls.server_process.kill()
                cls.server_process.wait()
    
    def setUp(self):
        """Reset do banco antes de cada teste"""
        try:
            requests.post(f'{self.base_url}/reset', timeout=10)
        except requests.exceptions.RequestException:
            pass
    
    def test_adicionar_livro_api(self):
        """Teste de API: adicionar livro"""
        data = {'titulo': 'Livro de Teste API'}
        response = requests.post(
            f'{self.base_url}/admin/livros',
            json=data,
            timeout=10
        )
        
        self.assertEqual(response.status_code, 201)
        result = response.json()
        self.assertIn('mensagem', result)
        self.assertIn('Livro adicionado com sucesso', result['mensagem'])
        self.assertEqual(result['livro']['titulo'], 'Livro de Teste API')
    
    def test_adicionar_livro_sem_titulo_api(self):
        """Teste de API: adicionar livro sem título"""
        response = requests.post(
            f'{self.base_url}/admin/livros',
            json={},
            timeout=10
        )
        
        self.assertEqual(response.status_code, 400)
        result = response.json()
        self.assertIn('erro', result)
        self.assertIn('Título é obrigatório', result['erro'])
    
    def test_listar_emprestimos_api(self):
        """Teste de API: listar empréstimos"""
        response = requests.get(f'{self.base_url}/admin/emprestimos', timeout=10)
        
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertIsInstance(result, list)
    
    def test_listar_emprestimos_ativos_api(self):
        """Teste de API: listar empréstimos ativos"""
        response = requests.get(f'{self.base_url}/admin/emprestimos/ativos', timeout=10)
        
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertIsInstance(result, list)
    
    def test_devolver_livro_inexistente_api(self):
        """Teste de API: devolver livro inexistente"""
        response = requests.post(f'{self.base_url}/admin/devolver/999', timeout=10)
        
        self.assertEqual(response.status_code, 404)
        result = response.json()
        self.assertIn('erro', result)
        self.assertIn('Empréstimo não encontrado', result['erro'])
    
    def test_fluxo_emprestimo_devolucao_api(self):
        """Teste de API: fluxo completo de empréstimo e devolução"""
        # 1. Emprestar livro
        emprestimo_response = requests.post(
            f'{self.base_url}/emprestar/1',
            json={'usuario_id': 1},
            timeout=10
        )
        self.assertEqual(emprestimo_response.status_code, 200)
        emprestimo_data = emprestimo_response.json()
        emprestimo_id = emprestimo_data['emprestimo_id']
        
        # 2. Verificar empréstimos ativos
        ativos_response = requests.get(f'{self.base_url}/admin/emprestimos/ativos', timeout=10)
        ativos_data = ativos_response.json()
        self.assertEqual(len(ativos_data), 1)
        self.assertEqual(ativos_data[0]['id'], emprestimo_id)
        
        # 3. Devolver livro
        devolucao_response = requests.post(f'{self.base_url}/admin/devolver/{emprestimo_id}', timeout=10)
        self.assertEqual(devolucao_response.status_code, 200)
        
        # 4. Verificar que não há empréstimos ativos
        ativos_response2 = requests.get(f'{self.base_url}/admin/emprestimos/ativos', timeout=10)
        ativos_data2 = ativos_response2.json()
        self.assertEqual(len(ativos_data2), 0)
        
        # 5. Verificar livro disponível
        livros_response = requests.get(f'{self.base_url}/livros', timeout=10)
        livros_data = livros_response.json()
        livro_1 = next(l for l in livros_data if l['id'] == 1)
        self.assertTrue(livro_1['disponivel'])
    
    def test_login_admin_retorna_tipo(self):
        """Teste de API: login de admin retorna tipo de usuário"""
        login_data = {
            'username': 'Admin',
            'password': 'admin123'
        }
        response = requests.post(
            f'{self.base_url}/login',
            json=login_data,
            timeout=10
        )
        
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result['status'], 'sucesso')
        self.assertIn('usuario', result)
        self.assertEqual(result['usuario']['tipo'], 'admin')
        self.assertEqual(result['usuario']['nome'], 'Admin')

if __name__ == '__main__':
    unittest.main()
