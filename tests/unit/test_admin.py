"""
Testes unitários para funcionalidades de administrador
"""
import unittest
import json
from unittest.mock import patch, MagicMock
import sys
import os

# Adicionar o diretório backend ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'backend'))

from app import app

class TestAdmin(unittest.TestCase):
    def setUp(self):
        """Configuração inicial para cada teste"""
        self.app = app.test_client()
        self.app.testing = True
        
        # Reset do banco para estado inicial
        self.app.post('/reset')
    
    def test_adicionar_livro_sucesso(self):
        """Teste: adicionar livro com sucesso"""
        response = self.app.post('/admin/livros',
                                data=json.dumps({'titulo': 'Novo Livro de Teste'}),
                                content_type='application/json')
        
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertIn('mensagem', data)
        self.assertIn('Livro adicionado com sucesso', data['mensagem'])
        self.assertIn('livro', data)
        self.assertEqual(data['livro']['titulo'], 'Novo Livro de Teste')
    
    def test_adicionar_livro_sem_titulo(self):
        """Teste: adicionar livro sem título deve falhar"""
        response = self.app.post('/admin/livros',
                                data=json.dumps({}),
                                content_type='application/json')
        
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('erro', data)
        self.assertIn('Título é obrigatório', data['erro'])
    
    def test_listar_emprestimos_vazio(self):
        """Teste: listar empréstimos quando não há nenhum"""
        response = self.app.get('/admin/emprestimos')
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data, [])
    
    def test_listar_emprestimos_ativos_vazio(self):
        """Teste: listar empréstimos ativos quando não há nenhum"""
        response = self.app.get('/admin/emprestimos/ativos')
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data, [])
    
    def test_devolver_livro_inexistente(self):
        """Teste: devolver livro com ID de empréstimo inexistente"""
        response = self.app.post('/admin/devolver/999')
        
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.data)
        self.assertIn('erro', data)
        self.assertIn('Empréstimo não encontrado', data['erro'])
    
    def test_fluxo_completo_emprestimo_devolucao(self):
        """Teste: fluxo completo de empréstimo e devolução"""
        # 1. Emprestar um livro
        emprestimo_response = self.app.post('/emprestar/1',
                                           data=json.dumps({'usuario_id': 1}),
                                           content_type='application/json')
        
        self.assertEqual(emprestimo_response.status_code, 200)
        emprestimo_data = json.loads(emprestimo_response.data)
        emprestimo_id = emprestimo_data['emprestimo_id']
        
        # 2. Verificar que o empréstimo aparece na lista de ativos
        ativos_response = self.app.get('/admin/emprestimos/ativos')
        ativos_data = json.loads(ativos_response.data)
        self.assertEqual(len(ativos_data), 1)
        self.assertEqual(ativos_data[0]['id'], emprestimo_id)
        self.assertIsNone(ativos_data[0]['data_devolucao'])
        
        # 3. Devolver o livro
        devolucao_response = self.app.post(f'/admin/devolver/{emprestimo_id}')
        self.assertEqual(devolucao_response.status_code, 200)
        devolucao_data = json.loads(devolucao_response.data)
        self.assertIn('devolvido com sucesso', devolucao_data['mensagem'])
        
        # 4. Verificar que não há mais empréstimos ativos
        ativos_response2 = self.app.get('/admin/emprestimos/ativos')
        ativos_data2 = json.loads(ativos_response2.data)
        self.assertEqual(len(ativos_data2), 0)
        
        # 5. Verificar que o empréstimo aparece no histórico com data de devolução
        historico_response = self.app.get('/admin/emprestimos')
        historico_data = json.loads(historico_response.data)
        self.assertEqual(len(historico_data), 1)
        self.assertIsNotNone(historico_data[0]['data_devolucao'])
        
        # 6. Verificar que o livro está disponível novamente
        livros_response = self.app.get('/livros')
        livros_data = json.loads(livros_response.data)
        livro_1 = next(l for l in livros_data if l['id'] == 1)
        self.assertTrue(livro_1['disponivel'])
    
    def test_devolver_livro_ja_devolvido(self):
        """Teste: tentar devolver livro que já foi devolvido"""
        # 1. Emprestar um livro
        emprestimo_response = self.app.post('/emprestar/1',
                                           data=json.dumps({'usuario_id': 1}),
                                           content_type='application/json')
        emprestimo_data = json.loads(emprestimo_response.data)
        emprestimo_id = emprestimo_data['emprestimo_id']
        
        # 2. Devolver o livro
        self.app.post(f'/admin/devolver/{emprestimo_id}')
        
        # 3. Tentar devolver novamente
        response = self.app.post(f'/admin/devolver/{emprestimo_id}')
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.data)
        self.assertIn('já devolvido', data['erro'])

if __name__ == '__main__':
    unittest.main()
