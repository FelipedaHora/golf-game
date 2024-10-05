import sys
import os

# Adicione o diretório raiz do projeto ao sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

import unittest
from models.vector import Vector
from models.object import Object  # Ajuste o caminho de importação conforme necessário

class TestObject(unittest.TestCase):

    def setUp(self):
        self.initial_position = Vector(0, 0)
        self.initial_speed = Vector(1, 1)
        self.initial_acceleration = Vector(0.5, 0.5)

    def test_initialization(self):
        obj = Object(self.initial_position, self.initial_speed, self.initial_acceleration)
        self.assertEqual(obj.position.x, 0)
        self.assertEqual(obj.position.y, 0)
        self.assertEqual(obj.speed.x, 1)
        self.assertEqual(obj.speed.y, 1)
        self.assertEqual(obj.acceleration.x, 0.5)
        self.assertEqual(obj.acceleration.y, 0.5)
        self.assertEqual(obj.friction, 0.98)

    def test_initialization_default_acceleration(self):
        obj = Object(self.initial_position, self.initial_speed)
        self.assertEqual(obj.acceleration.x, 0)
        self.assertEqual(obj.acceleration.y, 0)

    def test_physics_update(self):
        obj = Object(self.initial_position, self.initial_speed, self.initial_acceleration)
        obj.physics(1)  # Simulate 1 second
        
        # Expected values after 1 second:
        # Speed: (1 + 0.5) * 0.98 = 1.47 for both x and y
        # Position: 0 + 1.47 = 1.47 for both x and y
        self.assertAlmostEqual(obj.speed.x, 1.47, places=2)
        self.assertAlmostEqual(obj.speed.y, 1.47, places=2)
        self.assertAlmostEqual(obj.position.x, 1.47, places=2)
        self.assertAlmostEqual(obj.position.y, 1.47, places=2)

    def test_apply_friction(self):
        obj = Object(self.initial_position, self.initial_speed)
        obj.apply_friction()
        self.assertAlmostEqual(obj.speed.x, 0.98, places=2)
        self.assertAlmostEqual(obj.speed.y, 0.98, places=2)

    def test_physics_no_acceleration(self):
        obj = Object(self.initial_position, self.initial_speed)
        obj.physics(1)  # Simulate 1 second
        
        # Expected values after 1 second:
        # Speed: 1 * 0.98 = 0.98 for both x and y
        # Position: 0 + 0.98 = 0.98 for both x and y
        self.assertAlmostEqual(obj.speed.x, 0.98, places=2)
        self.assertAlmostEqual(obj.speed.y, 0.98, places=2)
        self.assertAlmostEqual(obj.position.x, 0.98, places=2)
        self.assertAlmostEqual(obj.position.y, 0.98, places=2)

if __name__ == '__main__':
    unittest.main()