import pygame
from models.object import Object
from models.vector import Vector

class Hole(Object):
    def __init__(self, x, y, width, height):
        super().__init__(Vector(x, y), Vector(0, 0))
        self.width = width
        self.height = height
        self.color = (0, 0, 0)  # Cor preta para o buraco

    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, (self.position.x, self.position.y, self.width, self.height))

    def check_collision(self, ball):
        # Calcula o centro do buraco
        hole_center_x = self.position.x + self.width / 2
        hole_center_y = self.position.y + self.height / 2

        # Calcula a distância entre o centro da bola e o centro do buraco
        dx = abs(ball.position.x - hole_center_x)
        dy = abs(ball.position.y - hole_center_y)

        # Normaliza as distâncias em relação aos raios do buraco
        normalized_x = dx / (self.width / 2)
        normalized_y = dy / (self.height / 2)

        # Verifica se a bola está dentro da elipse
        return (normalized_x**2 + normalized_y**2) <= 1

    def update(self, delta_time):
        # O buraco não precisa de atualização, mas incluímos o método para manter a consistência
        pass