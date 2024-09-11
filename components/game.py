import sys
import pygame
from models.animation import Animation
from models.ball import Ball
from models.obstacle import Obstacle
from models.vector import Vector
from models.hole import Hole

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

        explosion_animation = Animation("assets/sprites/coin3.png", 64, 64, 8, 0.1)

        # Load an audio file
        pygame.mixer.music.load("sounds/music.mp3")

        # Play the audio

        # Inicializa a bola
        ball = Ball(200, 300, 10, (255, 0, 0), WIDTH, HEIGHT)
        
        # Cria o buraco
        hole = Hole(900, 580, 40, 20)  # Ajuste a posição e o tamanho conforme necessário

        image = pygame.image.load("assets/sprites/power.png")
        rect = image.get_rect(topleft=(300, 300))

        screen.blit(image, rect)

        # Cria obstáculos para teste
        obstacles = [
            #  LADO ESQUERDO
            Obstacle(600, 600, "assets/sprites/sandEdge.png"),
            Obstacle(0, 63, "assets/sprites/sandEdge.png"),
            Obstacle(0, 126, "assets/sprites/sandEdge.png"),
            Obstacle(0, 189, "assets/sprites/sandEdge.png"),
            Obstacle(0, 252, "assets/sprites/sandEdge.png"),
            Obstacle(0, 315, "assets/sprites/sandEdge.png"),
            Obstacle(0, 378, "assets/sprites/sandEdge.png"),
            Obstacle(0, 441, "assets/sprites/sandEdge.png"),
            Obstacle(0, 504, "assets/sprites/sandEdge.png"),
            Obstacle(0, 567, "assets/sprites/sandEdge.png"),
            
            # PAREDE 2
            #Obstacle(160, 63, "assets/sprites/sandEdge.png"),
            #Obstacle(160, 126, "assets/sprites/sandEdge.png"),
            Obstacle(160, 189, "assets/sprites/sandEdge.png"),
            Obstacle(160, 252, "assets/sprites/sandEdge.png"),
            Obstacle(160, 315, "assets/sprites/sandEdge.png"),
            Obstacle(160, 378, "assets/sprites/sandEdge.png"),
            Obstacle(160, 441, "assets/sprites/sandEdge.png"),
            Obstacle(160, 504, "assets/sprites/sandEdge.png"),
            Obstacle(160, 567, "assets/sprites/sandEdge.png"),

            #  LADO DIREITO
            Obstacle(0, 0, "assets/sprites/sandEdge.png"),
            Obstacle(0, 63, "assets/sprites/sandEdge.png"),
            Obstacle(0, 126, "assets/sprites/sandEdge.png"),
            Obstacle(0, 189, "assets/sprites/sandEdge.png"),
            Obstacle(0, 252, "assets/sprites/sandEdge.png"),
            Obstacle(0, 315, "assets/sprites/sandEdge.png"),
            Obstacle(0, 378, "assets/sprites/sandEdge.png"),
            Obstacle(0, 441, "assets/sprites/sandEdge.png"),
            Obstacle(0, 504, "assets/sprites/sandEdge.png"),
            Obstacle(0, 567, "assets/sprites/sandEdge.png"),


            Obstacle(17, 585, "assets/sprites/sandBottom.png"),
            Obstacle(54, 585, "assets/sprites/sandBottom.png"),
            Obstacle(117, 585, "assets/sprites/sandBottom.png"),
            Obstacle(180, 585, "assets/sprites/sandBottom.png"),
            Obstacle(243, 585, "assets/sprites/sandBottom.png"),
            Obstacle(306, 585, "assets/sprites/sandBottom.png"),
            Obstacle(369, 585, "assets/sprites/sandBottom.png"),
            Obstacle(432, 585, "assets/sprites/sandBottom.png"),
            Obstacle(495, 585, "assets/sprites/sandBottom.png"),
            Obstacle(558, 585, "assets/sprites/sandBottom.png"),
            Obstacle(621, 585, "assets/sprites/sandBottom.png"),
            Obstacle(684, 585, "assets/sprites/sandBottom.png"),
            Obstacle(747, 585, "assets/sprites/sandBottom.png"),
            Obstacle(810, 585, "assets/sprites/sandBottom.png"),
        ]

        object_list = [ball] + obstacles + [hole]

        # Configura o relógio para controlar a taxa de quadros
        clock = pygame.time.Clock()

        # Loop principal do jogo
        PHYSICS_FPS = 240  # Frequência de atualização da física
        render_fps = 60    # Frequência de renderização
        physics_time_step = 1.0 / PHYSICS_FPS

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
            delta_time = clock.tick(render_fps) / 1000.0
            
            # Incrementa a força da bola se necessário
            ball.charge_force(delta_time)

            explosion_animation.update(delta_time)
            
            # Atualização da física em subpassos
            time_accumulator = 0
            while time_accumulator < delta_time:
                # Atualiza a física dos objetos
                for obj in object_list:
                    if isinstance(obj, (Ball, Obstacle)):
                        obj.update(physics_time_step)

                # Checa colisões com obstáculos
                for obstacle in obstacles:
                    if self.check_collision(ball, obstacle):
                        self.handle_collision(ball, obstacle)

                # Verifica se a bola entrou no buraco
                if hole.check_collision(ball):
                    print("Parabéns! Você venceu!")
                    pygame.quit()
                    sys.exit()

                time_accumulator += physics_time_step

            # Carrega e escala a imagem de fundo (isso pode ser feito fora do loop principal para otimização)
            background_image = pygame.image.load("assets/sprites/back.png")
            background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

            # Renderiza o fundo e os objetos
            screen.blit(background_image, (0, 0))
            for obj in object_list:
                obj.draw(screen)
            
            # Atualiza a tela
            pygame.display.flip()

        # Fim! Hora de sair.
        pygame.quit()

    def check_collision(self, ball, obstacle):
        # Simples checagem de colisão retangular
        if (ball.position.x + ball.radius > obstacle.position.x and
            ball.position.x - ball.radius < obstacle.position.x + obstacle.width and
            ball.position.y + ball.radius > obstacle.position.y and
            ball.position.y - ball.radius < obstacle.position.y + obstacle.height):
            return True
        return False

    def handle_collision(self, ball, obstacle):
        ball_rect = ball.get_rect()
        obstacle_rect = pygame.Rect(obstacle.position.x, obstacle.position.y, obstacle.width, obstacle.height)

        if ball_rect.colliderect(obstacle_rect):
            # Calcula a penetração em cada direção
            left_penetration = ball_rect.right - obstacle_rect.left
            right_penetration = obstacle_rect.right - ball_rect.left
            top_penetration = ball_rect.bottom - obstacle_rect.top
            bottom_penetration = obstacle_rect.bottom - ball_rect.top

            # Determina a direção de menor penetração
            min_penetration = min(left_penetration, right_penetration, top_penetration, bottom_penetration)

            if min_penetration == left_penetration:
                ball.position.x = obstacle_rect.left - ball.radius
                if ball.speed.x > 0:
                    ball.speed.x *= -0.6
            elif min_penetration == right_penetration:
                ball.position.x = obstacle_rect.right + ball.radius
                if ball.speed.x < 0:
                    ball.speed.x *= -0.6
            elif min_penetration == top_penetration:
                ball.position.y = obstacle_rect.top - ball.radius
                if ball.speed.y > 0:
                    ball.speed.y *= -0.6
            elif min_penetration == bottom_penetration:
                ball.position.y = obstacle_rect.bottom + ball.radius
                if ball.speed.y < 0:
                    ball.speed.y *= -0.6

            # Aplica um pequeno atrito na direção perpendicular à colisão
            if min_penetration in (left_penetration, right_penetration):
                ball.speed.y *= 0.95
            else:
                ball.speed.x *= 0.95 