import pygame
from models.animation import Animation
from models.object import Object
from models.vector import Vector

class Coin(Object):
    def __init__(self, x, y, images, frame_duration):
        super().__init__(Vector(x, y), Vector(0, 0))  # Moeda é estática por padrão
        self.animation = Animation(images, frame_duration)
        self.radius = 20  # Definido um raio para a moeda para colisão circular
        self.collected = False

    def update(self, delta_time):
        self.animation.update(delta_time)  # Atualiza a animação

    def draw(self, screen):
        # Desenha a animação no local da moeda
        if not self.collected:
            self.animation.draw(screen, (int(self.position.x - self.radius), int(self.position.y - self.radius)))

    def get_rect(self):
        # Define o retângulo de colisão para a moeda
        return pygame.Rect(
            self.position.x - self.radius,
            self.position.y - self.radius,
            self.radius * 2,
            self.radius * 2
        )

    def detect_collision(self, ball):
        # Calcula a distância entre o centro da bola e o centro da moeda
        distance = ((self.position.x - ball.position.x) ** 2 + (self.position.y - ball.position.y) ** 2) ** 0.5
        # Verifica se a distância é menor que a soma dos raios da bola e da moeda
        return distance < (self.radius + ball.radius)
    
    def collect(self):
        """Marca a moeda como coletada para remoção."""
        self.collected = True

    def should_remove(self):
        """Verifica se a moeda deve ser removida."""
        return self.collected
