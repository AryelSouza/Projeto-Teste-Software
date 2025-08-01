import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from backend.livro import Livro

class TestLivro(unittest.TestCase):
    def test_emprestar_livro_disponivel(self):
        livro = Livro(1, "Python Testing")
        self.assertTrue(livro.disponivel)
        self.assertTrue(livro.emprestar())
        self.assertFalse(livro.disponivel)
    
    def test_emprestar_livro_indisponivel(self):
        livro = Livro(2, "Clean Code")
        livro.emprestar()
        self.assertFalse(livro.emprestar())
        self.assertFalse(livro.disponivel)
    
    def test_devolver_livro(self):
        livro = Livro(3, "Refactoring")
        livro.emprestar()
        livro.devolver()
        self.assertTrue(livro.disponivel)

if __name__ == '__main__':
    unittest.main()
