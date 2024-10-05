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

        # Calcula os raios efetivos (metade da largura/altura + raio da bola)
        effective_width = self.width / 2 + ball.radius
        effective_height = self.height / 2 + ball.radius

        # Normaliza as distâncias em relação aos raios efetivos
        normalized_x = dx / effective_width
        normalized_y = dy / effective_height

        # Verifica se a bola está tocando ou dentro da elipse
        return (normalized_x**2 + normalized_y**2) <= 1

    def update(self, delta_time):
        # O buraco não precisa de atualização, mas incluímos o método para manter a consistência
        pass