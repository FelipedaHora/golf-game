import sys
import pygame
from models.ball import Ball
from models.obstacle import Obstacle  # Supondo que a classe Obstacle está em models/obstacle.py

class Game:
    
    def __init__(self):
        pygame.init()
    
    def run(self):
        # Inicializa Pygame
        WIDTH, HEIGHT = 1080, 600
        FPS = 60

        # Cria a janela do Pygame
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Super Mini Golf")

        # Inicializa a bola
        ball = Ball(200, 300, 10, (255, 0, 0), WIDTH, HEIGHT)  # Adiciona WIDTH e HEIGHT
        
        # Cria obstáculos para teste
        obstacles = [
            Obstacle(100, 500, "assets/sprites/sandBottom.png"),
            Obstacle(300, 400, "assets/sprites/sandEdge.png"),
            Obstacle(500, 300, "assets/sprites/sandBottom.png"),
            Obstacle(700, 200, "assets/sprites/sandEdge.png")
        ]
        
        object_list = [ball] + obstacles

        # Configura o relógio para controlar a taxa de quadros
        clock = pygame.time.Clock()

        # Loop principal do jogo
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Verifica se o mouse foi clicado
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    ball.handle_input(mouse_pos)

            # Calcula o delta_time
            delta_time = clock.tick(FPS) / 1000.0
            
            # Incrementa a força da bola se necessário
            ball.charge_force(delta_time)
            
            # Atualiza a física dos objetos
            for obj in object_list:
                obj.update(delta_time)

            # Carrega e escala a imagem de fundo
            background_image = pygame.image.load("assets/sprites/back.png")
            background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

            # Renderiza o fundo e os objetos
            screen.blit(background_image, (0, 0))
            for obj in object_list:
                obj.draw(screen)
            
            # Atualiza a tela
            pygame.display.flip()

            # Limita a taxa de quadros
            clock.tick(FPS)

        # Fim! Hora de sair.
        pygame.quit()
