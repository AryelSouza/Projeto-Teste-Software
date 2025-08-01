import requests
import unittest
import time

BASE_URL = "http://localhost:5000"

class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        time.sleep(2)
    
    def setUp(self):
        try:
            response = requests.post(f"{BASE_URL}/reset")
            self.assertEqual(response.status_code, 200)
        except requests.exceptions.ConnectionError:
            self.fail("Não foi possível conectar ao servidor")
    
    def test_login_sucesso(self):
        response = requests.post(
            f"{BASE_URL}/login",
            json={"username": "Ana", "password": "senha123"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("sucesso", response.json()['status'])
    
    def test_login_falha(self):
        response = requests.post(
            f"{BASE_URL}/login",
            json={"username": "Ana", "password": "senha_errada"}
        )
        self.assertEqual(response.status_code, 401)
        self.assertIn("Credenciais inválidas", response.json()['erro'])
    
    def test_emprestimo_sucesso(self):
        response = requests.post(f"{BASE_URL}/emprestar/1")
        self.assertEqual(response.status_code, 200)
        self.assertIn("sucesso", response.json()['mensagem'])
        
        response = requests.post(f"{BASE_URL}/emprestar/1")
        self.assertEqual(response.status_code, 400)
        self.assertIn("indisponível", response.json()['erro'])
    
    def test_emprestimo_livro_inexistente(self):
        response = requests.post(f"{BASE_URL}/emprestar/999")
        self.assertEqual(response.status_code, 404)
        self.assertIn("não encontrado", response.json()['erro'].lower())

if __name__ == '__main__':
    unittest.main(verbosity=2)
