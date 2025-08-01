import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from backend.usuario import Usuario

class TestUsuario(unittest.TestCase):
    def test_criacao_usuario(self):
        usuario = Usuario(1, "Maria", "senha456")
        self.assertEqual(usuario.nome, "Maria")
        self.assertTrue(usuario.ativo)
    
    def test_desativar_usuario(self):
        usuario = Usuario(2, "Carlos", "teste123")
        usuario.ativo = False
        self.assertFalse(usuario.ativo)

if __name__ == '__main__':
    unittest.main()
