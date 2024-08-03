import pygame
from models.object import Object
from models.vector import Vector

import pygame
from models.vector import Vector

class Obstacle(Object):
    def __init__(self, x, y, image_path):
        # Inicializa a posição e a velocidade
        position = Vector(x, y)
        speed = Vector(0, 0)
        super().__init__(position, speed)
        
        # Carrega a imagem do obstáculo e obtém seu retângulo de colisão
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, screen):
        # Desenha o obstáculo na tela
        screen.blit(self.image, self.rect.topleft)

    def update(self, delta_time):
        # Atualiza a posição com base na velocidade (se necessário)
        self.physics(delta_time)
        self.rect.topleft = (self.position.x, self.position.y)
        
    def check_collision(self, ball):
        # Verifica se a bola colidiu com o obstáculo
        ball_rect = pygame.Rect(
            ball.position.x - ball.radius,
            ball.position.y - ball.radius,
            ball.radius * 2,
            ball.radius * 2
        )
        return self.rect.colliderect(ball_rect)

