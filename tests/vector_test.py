import sys
import os

# Adicione o diretório raiz do projeto ao sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

import unittest
import math
from models.vector import Vector  # Ajuste o caminho de importação conforme necessário

class TestVector(unittest.TestCase):

    def test_initialization(self):
        v = Vector(3, 4)
        self.assertEqual(v.x, 3)
        self.assertEqual(v.y, 4)

    def test_multiplication(self):
        v = Vector(2, 3)
        v.__mul__(2)
        self.assertEqual(v.x, 4)
        self.assertEqual(v.y, 6)

    def test_division(self):
        v = Vector(4, 6)
        v.__div__(2)
        self.assertEqual(v.x, 2)
        self.assertEqual(v.y, 3)

    def test_set_module(self):
        v = Vector(3, 4)
        v.set_module(10)
        self.assertAlmostEqual(v.module(), 10, places=7)

    def test_module(self):
        v = Vector(3, 4)
        self.assertAlmostEqual(v.module(), 5, places=7)

    def test_prod_int(self):
        v1 = Vector(2, 3)
        v2 = Vector(4, 5)
        result = Vector.prod_int(v1, v2)
        self.assertEqual(result, 23)

    def test_set_module_zero(self):
        v = Vector(0, 0)
        with self.assertRaises(ZeroDivisionError):
            v.set_module(5)

if __name__ == '__main__':
    unittest.main()