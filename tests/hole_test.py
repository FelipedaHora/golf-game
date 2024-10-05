import sys
import os

# Adicione o diretório raiz do projeto ao sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

import unittest
import pygame
from models.ball import Ball
from models.hole import Hole
from models.vector import Vector

class HoleTestCase(unittest.TestCase):

    def setUp(self):
        # Inicializa o Pygame e cria um objeto Hole para os testes
        pygame.init()
        self.hole = Hole(x=200, y=200, width=50, height=50)
        self.ball = Ball(x=210, y=210, radius=10, color=(255, 0, 0), width=800, height=600)

    def test_initialization(self):
        # Testa se o buraco foi inicializado corretamente
        self.assertEqual(self.hole.position, Vector(200, 200))
        self.assertEqual(self.hole.width, 50)
        self.assertEqual(self.hole.height, 50)
        self.assertEqual(self.hole.color, (0, 0, 0))

    def test_draw(self):
        # Testa se o buraco é desenhado sem erros
        screen = pygame.Surface((800, 600))
        try:
            self.hole.draw(screen)
        except Exception as e:
            self.fail(f"draw() method raised an exception: {e}")

    def test_check_collision_inside(self):
        # Testa se a colisão é detectada corretamente quando a bola está dentro do buraco
        self.ball.position = Vector(220, 220)  # Coloca a bola dentro do buraco
        self.assertTrue(self.hole.check_collision(self.ball))

    def test_check_collision_border(self):
        # Testa se a colisão é detectada corretamente quando a bola está na borda do buraco
        self.ball.position = Vector(200, 200)  # Coloca a bola na borda do buraco
        self.assertTrue(self.hole.check_collision(self.ball))

    def test_check_collision_outside(self):
        # Testa se a colisão é detectada corretamente quando a bola está fora do buraco
        self.ball.position = Vector(300, 300)  # Coloca a bola fora do buraco
        self.assertFalse(self.hole.check_collision(self.ball))

    def test_check_collision_edge_case(self):
        # Testa se a colisão é detectada corretamente quando a bola está exatamente no limite do buraco
        self.ball.position = Vector(225, 200)  # Coloca a bola exatamente na borda do buraco (limite direito)
        self.assertTrue(self.hole.check_collision(self.ball))

    def test_update_method(self):
        # Testa se o método update não gera erros
        try:
            self.hole.update(0.016)  # Passa um delta_time típico (16ms)
        except Exception as e:
            self.fail(f"update() method raised an exception: {e}")

    def tearDown(self):
        # Encerra o Pygame após os testes
        pygame.quit()

if __name__ == "__main__":
    unittest.main()
