import unittest
import pygame
from models.vector import Vector
from models.ball import Ball

class BallTestCase(unittest.TestCase):
    
    def setUp(self):
        # Inicializa o Pygame e cria um objeto Ball para os testes
        pygame.init()
        self.ball = Ball(x=100, y=100, radius=10, color=(255, 0, 0), width=800, height=600)

    def test_initialization(self):
        # Testa se a bola foi inicializada corretamente
        self.assertEqual(self.ball.position, Vector(100, 100))
        self.assertEqual(self.ball.radius, 10)
        self.assertEqual(self.ball.color, (255, 0, 0))
        self.assertEqual(self.ball.speed, Vector(0, 0))
        self.assertEqual(self.ball.acceleration, Vector(0, 900))  # Gravidade reduzida
        self.assertFalse(self.ball.is_charging)

    def test_handle_input_start_charge(self):
        # Simula o início do carregamento
        mouse_pos = (150, 150)
        self.ball.handle_input(mouse_pos)
        self.assertTrue(self.ball.is_charging)

    def test_handle_input_stop_charge(self):
        # Simula o início e parada do carregamento
        mouse_pos = (150, 150)
        self.ball.handle_input(mouse_pos)  # Inicia carregamento
        self.ball.handle_input(mouse_pos)  # Para carregamento
        self.assertFalse(self.ball.is_charging)

    def test_force_application(self):
        # Testa se a força está sendo aplicada corretamente
        self.ball.start_charge((150, 150))
        self.ball.charge_start_time = pygame.time.get_ticks() - 2000  # Simula 2 segundos de carregamento
        self.ball.stop_charge((200, 200))
        
        expected_force = min(2 * 2500, self.ball.max_force)
        magnitude = (self.ball.speed.x**2 + self.ball.speed.y**2)**0.5
        self.assertAlmostEqual(magnitude, expected_force, delta=1.0)

    def test_collision_bottom(self):
        # Simula uma colisão com a parte inferior da tela
        self.ball.position.y = 590
        self.ball.speed.y = 200
        self.ball.handle_collisions()
        self.assertEqual(self.ball.position.y, 600 - self.ball.radius)
        self.assertAlmostEqual(self.ball.speed.y, -200 * 0.65, delta=0.1)

    def test_collision_top(self):
        # Simula uma colisão com a parte superior da tela
        self.ball.position.y = 5
        self.ball.speed.y = -200
        self.ball.handle_collisions()
        self.assertEqual(self.ball.position.y, self.ball.radius)
        self.assertAlmostEqual(self.ball.speed.y, 200 * 0.65, delta=0.1)

    def test_collision_left(self):
        # Simula uma colisão com a parede esquerda
        self.ball.position.x = 5
        self.ball.speed.x = -200
        self.ball.handle_collisions()
        self.assertEqual(self.ball.position.x, self.ball.radius)
        self.assertAlmostEqual(self.ball.speed.x, 200 * 0.8, delta=0.1)

    def test_collision_right(self):
        # Simula uma colisão com a parede direita
        self.ball.position.x = 795
        self.ball.speed.x = 200
        self.ball.handle_collisions()
        self.assertEqual(self.ball.position.x, 800 - self.ball.radius)
        self.assertAlmostEqual(self.ball.speed.x, -200 * 0.8, delta=0.1)

    def test_draw(self):
        # Testa se a bola é desenhada sem erros
        screen = pygame.Surface((800, 600))
        try:
            self.ball.draw(screen)
        except Exception as e:
            self.fail(f"draw() method raised an exception: {e}")

    def tearDown(self):
        # Encerra o Pygame após os testes
        pygame.quit()

if __name__ == "__main__":
    unittest.main()
