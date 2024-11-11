# import sys
# import pygame
# from models.animation import Animation
# from models.ball import Ball
# from models.obstacle import Obstacle
# from models.vector import Vector
# from models.hole import Hole

# class Game:
    
#     def __init__(self):
#         pygame.init()
#         pygame.mixer.init()


    
#     def run(self):
#         # Inicializa Pygame
#         WIDTH, HEIGHT = 1080, 600
#         FPS = 60

#         # Cria a janela do Pygame
#         screen = pygame.display.set_mode((WIDTH, HEIGHT))
#         pygame.display.set_caption("Super Mini Golf")

#         # Carregar as imagens da moeda
#         coin_images = []
#         for i in range(1, 9):  # Como as imagens vão de coin1 até coin8
#             try:
#                 image = pygame.image.load(f"assets/sprites/coin{i}.png")
#                 coin_images.append(image)
#             except pygame.error as e:
#                 print(f"Erro ao carregar imagem coin{i}: {e}")

#         # Verifica se as imagens foram carregadas corretamente
#         if not coin_images:
#             print("Nenhuma imagem de moeda foi carregada.")
#             return

#         # Lista de sprites para a animação
#         animation = Animation(coin_images, 200)

#         # Load an audio file
#         pygame.mixer.music.load("sounds/music.mp3")
#         putt_sound = pygame.mixer.Sound("sounds/putt.wav")
#         wrong_sound = pygame.mixer.Sound("sounds/wrong12.wav")
#         inHole_sound = pygame.mixer.Sound("sounds/inHole.wav")
#         splash_sound = pygame.mixer.Sound("sounds/splash.wav")

#         # Play the audio
#         pygame.mixer.music.play()

#         # Inicializa a bola
#         ball = Ball(200, 300, 10, (255, 0, 0), WIDTH, HEIGHT)
        
#         # Cria o buraco
#         hole = Hole(900, 580, 40, 20)  # Ajuste a posição e o tamanho conforme necessário

#         image = pygame.image.load("assets/sprites/power.png")
#         rect = image.get_rect(topleft=(300, 300))

#         screen.blit(image, rect)

#         # Cria obstáculos para teste
#         obstacles = [
#             #  LADO ESQUERDO
#             Obstacle(600, 600, "assets/sprites/sandEdge.png"),
#             Obstacle(0, 63, "assets/sprites/sandEdge.png"),
#             Obstacle(0, 126, "assets/sprites/sandEdge.png"),
#             Obstacle(0, 189, "assets/sprites/sandEdge.png"),
#             Obstacle(0, 252, "assets/sprites/sandEdge.png"),
#             Obstacle(0, 315, "assets/sprites/sandEdge.png"),
#             Obstacle(0, 378, "assets/sprites/sandEdge.png"),
#             Obstacle(0, 441, "assets/sprites/sandEdge.png"),
#             Obstacle(0, 504, "assets/sprites/sandEdge.png"),
#             Obstacle(0, 567, "assets/sprites/sandEdge.png"),
            
#             # PAREDE 2
#             #Obstacle(160, 63, "assets/sprites/sandEdge.png"),
#             #Obstacle(160, 126, "assets/sprites/sandEdge.png"),
#             Obstacle(160, 189, "assets/sprites/sandEdge.png"),
#             Obstacle(160, 252, "assets/sprites/sandEdge.png"),
#             Obstacle(160, 315, "assets/sprites/sandEdge.png"),
#             Obstacle(160, 378, "assets/sprites/sandEdge.png"),
#             Obstacle(160, 441, "assets/sprites/sandEdge.png"),
#             Obstacle(160, 504, "assets/sprites/sandEdge.png"),
#             Obstacle(160, 567, "assets/sprites/sandEdge.png"),

#             #  LADO DIREITO
#             Obstacle(0, 0, "assets/sprites/sandEdge.png"),
#             Obstacle(0, 63, "assets/sprites/sandEdge.png"),
#             Obstacle(0, 126, "assets/sprites/sandEdge.png"),
#             Obstacle(0, 189, "assets/sprites/sandEdge.png"),
#             Obstacle(0, 252, "assets/sprites/sandEdge.png"),
#             Obstacle(0, 315, "assets/sprites/sandEdge.png"),
#             Obstacle(0, 378, "assets/sprites/sandEdge.png"),
#             Obstacle(0, 441, "assets/sprites/sandEdge.png"),
#             Obstacle(0, 504, "assets/sprites/sandEdge.png"),
#             Obstacle(0, 567, "assets/sprites/sandEdge.png"),
#             Obstacle(17, 585, "assets/sprites/sandBottom.png"),
#             Obstacle(54, 585, "assets/sprites/sandBottom.png"),
#             Obstacle(117, 585, "assets/sprites/sandBottom.png"),
#             Obstacle(180, 585, "assets/sprites/sandBottom.png"),
#             Obstacle(243, 585, "assets/sprites/sandBottom.png"),
#             Obstacle(306, 585, "assets/sprites/sandBottom.png"),
#             Obstacle(369, 585, "assets/sprites/sandBottom.png"),
#             Obstacle(432, 585, "assets/sprites/sandBottom.png"),
#             Obstacle(495, 585, "assets/sprites/sandBottom.png"),
#             Obstacle(558, 585, "assets/sprites/sandBottom.png"),
#             Obstacle(621, 585, "assets/sprites/sandBottom.png"),
#             Obstacle(684, 585, "assets/sprites/sandBottom.png"),
#             Obstacle(747, 585, "assets/sprites/sandBottom.png"),
#             Obstacle(810, 585, "assets/sprites/sandBottom.png"),
#         ]

#         object_list = [ball] + obstacles + [hole]

#         # Configura o relógio para controlar a taxa de quadros
#         clock = pygame.time.Clock()

#         # Loop principal do jogo
#         PHYSICS_FPS = 240  # Frequência de atualização da física
#         render_fps = 60    # Frequência de renderização
#         physics_time_step = 1.0 / PHYSICS_FPS

#         while True:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     sys.exit()

#                 # Verifica se o mouse foi clicado
#                 if event.type == pygame.MOUSEBUTTONDOWN:
#                     mouse_pos = pygame.mouse.get_pos()
#                     ball.handle_input(mouse_pos)
                    

#             # Calcula o delta_time
#             delta_time = clock.tick(render_fps) / 1000.0
            
#             animation.update(delta_time)
                
#             # Incrementa a força da bola se necessário
#             ball.charge_force(delta_time)
            
#             # Atualização da física em subpassos
#             time_accumulator = 0
#             while time_accumulator < delta_time:
#                 # Atualiza a física dos objetos
#                 for obj in object_list:
#                     if isinstance(obj, (Ball, Obstacle)):
#                         obj.update(physics_time_step)

#                 # Checa colisões com obstáculos
#                 for obstacle in obstacles:
#                     if self.check_collision(ball, obstacle):
#                         self.handle_collision(ball, obstacle)

#                 # Verifica se a bola entrou no buraco
#                 if hole.check_collision(ball):
#                     inHole_sound.play()
#                     print("Parabéns! Você venceu!")
#                     pygame.quit()
#                     sys.exit()

#                 time_accumulator += physics_time_step

#             # Carrega e escala a imagem de fundo (isso pode ser feito fora do loop principal para otimização)
#             background_image = pygame.image.load("assets/sprites/back.png")
#             background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

#             # Renderiza o fundo e os objetos
#             screen.blit(background_image, (0, 0))

#             # Desenha a animação na tela
#             animation.draw(screen, (400, 300))

#             for obj in object_list:
#                 obj.draw(screen)
            
#             # Atualiza a tela
#             pygame.display.flip()

#         # Fim! Hora de sair.
#         pygame.quit()

#     def check_collision(self, ball, obstacle):
#         # Simples checagem de colisão retangular
#         if (ball.position.x + ball.radius > obstacle.position.x and
#             ball.position.x - ball.radius < obstacle.position.x + obstacle.width and
#             ball.position.y + ball.radius > obstacle.position.y and
#             ball.position.y - ball.radius < obstacle.position.y + obstacle.height):
#             return True
#         return False

#     def handle_collision(self, ball, obstacle):
#         ball_rect = ball.get_rect()
#         obstacle_rect = pygame.Rect(obstacle.position.x, obstacle.position.y, obstacle.width, obstacle.height)

#         if ball_rect.colliderect(obstacle_rect):
#             # Calcula a penetração em cada direção
#             left_penetration = ball_rect.right - obstacle_rect.left
#             right_penetration = obstacle_rect.right - ball_rect.left
#             top_penetration = ball_rect.bottom - obstacle_rect.top
#             bottom_penetration = obstacle_rect.bottom - ball_rect.top

#             # Determina a direção de menor penetração
#             min_penetration = min(left_penetration, right_penetration, top_penetration, bottom_penetration)

#             if min_penetration == left_penetration:
#                 ball.position.x = obstacle_rect.left - ball.radius
#                 if ball.speed.x > 0:
#                     ball.speed.x *= -0.6
#             elif min_penetration == right_penetration:
#                 ball.position.x = obstacle_rect.right + ball.radius
#                 if ball.speed.x < 0:
#                     ball.speed.x *= -0.6
#             elif min_penetration == top_penetration:
#                 ball.position.y = obstacle_rect.top - ball.radius
#                 if ball.speed.y > 0:
#                     ball.speed.y *= -0.6
#             elif min_penetration == bottom_penetration:
#                 ball.position.y = obstacle_rect.bottom + ball.radius
#                 if ball.speed.y < 0:
#                     ball.speed.y *= -0.6

#             # Aplica um pequeno atrito na direção perpendicular à colisão
#             if min_penetration in (left_penetration, right_penetration):
#                 ball.speed.y *= 0.95
#             else:
#                 ball.speed.x *= 0.95 

import sys
import pygame 
from components.pauseMenu import PauseMenu
from models.animation import Animation
from models.ball import Ball
from models.coin import Coin
from models.obstacle import Obstacle
from models.vector import Vector
from models.hole import Hole

class Game:
    
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

    
    def run(self):
        # Inicializa Pygame
        WIDTH, HEIGHT = 1080, 600
        FPS = 60

        # Cria a janela do Pygame
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Super Mini Golf")

        # Carrega as imagens da animação de moeda
        coin_images = [
            pygame.image.load(f"assets/sprites/coin{i}.png") for i in range(1, 9)
        ]

        exploson_images = [
            pygame.image.load(f"assets/sprites/explosion-{i}.png") for i in range(1, 9)
        ]

        # Defina o tamanho desejado
        LARGURA_DESEJADA = 60
        ALTURA_DESEJADA = 70

        flags_images = [
            pygame.transform.scale(
                pygame.image.load(f"assets/sprites/ANIMATION-0{i}.png"),
                (LARGURA_DESEJADA, ALTURA_DESEJADA)
            ) for i in range(1, 7)
        ]

        frame_duration = 0.1  # Duração de cada quadro em segundos

        # Lista de moedas no jogo

        coins = [
            Coin(45, 84, coin_images, frame_duration),
            Coin(200, 150, coin_images, frame_duration),
            Coin(910, 38, coin_images, frame_duration)
        ]

        # Inicializa a animação
        #animationCoin = Animation(coin_images, 200)

        collected_coins = 0

        animationExplosion = Animation(exploson_images, 200)

        animationFlag = Animation(flags_images, 200)

        # Carrega sons
        pygame.mixer.music.load("sounds/music.mp3")
        putt_sound = pygame.mixer.Sound("sounds/putt.wav")
        wrong_sound = pygame.mixer.Sound("sounds/wrong12.wav")
        inHole_sound = pygame.mixer.Sound("sounds/inHole.wav")
        splash_sound = pygame.mixer.Sound("sounds/splash.wav")
        bouncing_sound = pygame.mixer.Sound("sounds/bouncing_ball.wav")

        pygame.mixer.music.play()

        # Inicializa a bola e o buraco
        ball = Ball(100, 500 , 10, (255, 0, 0), WIDTH, HEIGHT, animationExplosion)
        hole = Hole(1000, 580, 30, 10)

        # Carrega a imagem de fundo uma vez, fora do loop
        background_image = pygame.image.load("assets/sprites/back.png")
        background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

        # Cria o menu de pausa
        menuIcon = pygame.image.load("assets/sprites/MENU.png")
        menuIcon = pygame.transform.scale(menuIcon, (40, 40))
        menu_rect = menuIcon.get_rect(center=(100, 100))
        


        font = pygame.font.Font(None, 36)  # Você pode ajustar o tamanho ou usar uma fonte personalizada

        # Obstáculos
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
                    Obstacle(0, 450, "assets/sprites/sandBottom.png"),
                    Obstacle(0, 100, "assets/sprites/sandBottom.png"),
                    
                    # PAREDE 2
                    #Obstacle(160, 63, "assets/sprites/sandEdge.png"),
                    #Obstacle(160, 126, "assets/sprites/sandEdge.png"),
                    Obstacle(190, 189, "assets/sprites/sandEdge.png"),
                    Obstacle(190, 252, "assets/sprites/sandEdge.png"),
                    Obstacle(190, 315, "assets/sprites/sandEdge.png"),
                    Obstacle(190, 378, "assets/sprites/sandEdge.png"),
                    Obstacle(190, 441, "assets/sprites/sandEdge.png"),
                    Obstacle(190, 504, "assets/sprites/sandEdge.png"),
                    Obstacle(190, 567, "assets/sprites/sandEdge.png"),
                    

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
                    Obstacle(873, 585, "assets/sprites/sandBottom.png"),
                    Obstacle(879, 585, "assets/sprites/sandBottom.png"),
                    
                    Obstacle(960, 583, "assets/sprites/green.png"),
                    Obstacle(960, 588, "assets/sprites/green.png"),
                    Obstacle(960, 593, "assets/sprites/green.png"),
                    Obstacle(1019, 583, "assets/sprites/green.png"),
                    Obstacle(1019, 588, "assets/sprites/green.png"),
                    Obstacle(1019, 593, "assets/sprites/green.png"),

                    Obstacle(944, 536, "assets/sprites/sandEdge.png"),
                    Obstacle(944, 472, "assets/sprites/sandEdge.png"),
                    Obstacle(944, 408, "assets/sprites/sandEdge.png"),
                    Obstacle(944, 344, "assets/sprites/sandEdge.png"),
                    Obstacle(944, 280, "assets/sprites/sandEdge.png"),
                    Obstacle(944, 0, "assets/sprites/sandEdge.png"),

                    Obstacle(880, 48, "assets/sprites/sandBottom.png"),
                ]

        object_list = [ball] + obstacles + [hole]

        # Relógio para controle de FPS
        clock = pygame.time.Clock()

        # Definindo o par do único buraco
        par_do_buraco = 4  # Exemplo: buraco par 4

        def calcular_pontuacao_unico_buraco(tacadas):
            # Calcula a diferença entre o número de tacadas e o par do buraco
            diferenca = tacadas - par_do_buraco

            if tacadas == 1:
                return "Hole-in-One"
            elif diferenca <= -3:
                return "Albatross"
            elif diferenca == -2:
                return "Eagle"
            elif diferenca == -1:
                return "Birdie"
            elif diferenca == 0:
                return "Par"
            elif diferenca == 1:
                return "Bogey"
            elif diferenca == 2:
                return "Double Bogey"
            elif diferenca == 3:
                return "Triple Bogey"
            else:
                return f"{diferenca} Tacadas acima do par"

        def show_victory_screen(screen, font):
            # Preenche a tela com preto
            screen.fill((0, 0, 0))
            
            pontuacao = calcular_pontuacao_unico_buraco(ball.count_plays)

            # Textos individuais
            victory_text = "Parabéns! Você venceu!"
            pontuacao_text = f"Pontuação: {pontuacao}"
            moedas_text = f"{collected_coins} moedas coletadas"

            # Renderizar cada linha de texto
            victory_surface = font.render(victory_text, True, (255, 255, 255))
            pontuacao_surface = font.render(pontuacao_text, True, (255, 255, 255))
            moedas_surface = font.render(moedas_text, True, (255, 255, 255))

            # Obtém as dimensões da tela
            screen_width = screen.get_width()
            screen_height = screen.get_height()

            # Calcula as posições Y para cada linha de texto
            spacing = 10  # Espaço entre as linhas
            total_height = victory_surface.get_height() + pontuacao_surface.get_height() + moedas_surface.get_height() + (2 * spacing)
            start_y = (screen_height // 2) - (total_height // 2)

            # Posiciona e desenha o texto no centro da tela, linha por linha
            victory_rect = victory_surface.get_rect(center=(screen_width // 2, start_y))
            screen.blit(victory_surface, victory_rect)

            pontuacao_rect = pontuacao_surface.get_rect(center=(screen_width // 2, start_y + victory_surface.get_height() + spacing))
            screen.blit(pontuacao_surface, pontuacao_rect)

            moedas_rect = moedas_surface.get_rect(center=(screen_width // 2, pontuacao_rect.bottom + spacing))
            screen.blit(moedas_surface, moedas_rect)
            pygame.display.flip()

            # Espera por um clique do mouse ou tecla pressionada para continuar
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return False  # Indica que o jogo deve ser encerrado
                    if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                        waiting = False

            return True  # Indica que o jogo pode continuar (se necessário)
        

        # Loop principal do jogo
        while True:
            # Eventos de input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Verifica se o mouse foi clicado
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()

                    # Verifica se o clique foi no ícone do menu (posição 995,10 com tamanho 40x40)
                    menu_rect = pygame.Rect(995, 10, 40, 40)
                    if menu_rect.collidepoint(mouse_pos):
                        pause_menu = PauseMenu()
                        option_selected = pause_menu.run()
                        
                        if option_selected == "Retornar ao Jogo":
                            continue
                        elif option_selected == "Menu":
                            Menu()  # Redireciona ao menu principal
                            continue  # Retorna para o loop para exibir o menu principal
                    else:
                        ball.handle_input(mouse_pos)  # Se não clicou no menu, processa o input da bola
                    #ball.handle_input(mouse_pos)

                 # Verifica se a tecla 'P' foi pressionada para pausar o jogo
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        pause_menu = PauseMenu()
                        option_selected = pause_menu.run()

                        if option_selected == "Retornar ao Jogo":
                            continue  # Sai do menu de pausa e continua o loop principal
                        elif option_selected == "Sair":
                            pygame.quit()
                            sys.exit()

            # Atualiza o tempo e a animação
            delta_time = clock.tick(FPS) / 1000.0
            #animationCoin.update(delta_time)
            animationFlag.update(delta_time)  # Atualiza a animação

            # Incrementa a força da bola
            ball.charge_force(delta_time)

            # Atualiza a física dos objetos
            for obj in object_list:
                if isinstance(obj, (Ball, Obstacle)):
                    obj.update(delta_time)

            # Checa colisões com obstáculos
            for obstacle in obstacles:
                if self.check_collision(ball, obstacle):
                    self.handle_collision(ball, obstacle)
                    
            # Verifica se a bola entrou no buraco
            if hole.check_collision(ball):
                inHole_sound.play()
                pygame.time.wait(1000)
                if show_victory_screen(screen, font):
                    pygame.quit()
                    sys.exit()

            # Renderiza o fundo
            screen.blit(background_image, (0, 0))

            screen.blit(menuIcon, (995, 10))

            # Renderiza a animação no topo
            #animationCoin.draw(screen, (10, 150))
            animationFlag.draw(screen, (1013, 515))  # Atualiza a posição conforme necessário

            # Atualiza e desenha as moedas
            for coin in coins:
                coin.update(delta_time)
                coin.draw(screen)
                if not coin.collected and coin.detect_collision(ball):
                    coin.collect()
                    collected_coins += 1
                    

            # Renderiza os objetos
            for obj in object_list:
                obj.draw(screen)

            # Atualiza a tela
            pygame.display.flip()

    def check_collision(self, ball, obstacle):
        # Checagem de colisão retangular
        if (ball.position.x + ball.radius > obstacle.position.x and
            ball.position.x - ball.radius < obstacle.position.x + obstacle.width and
            ball.position.y + ball.radius > obstacle.position.y and
            ball.position.y - ball.radius < obstacle.position.y + obstacle.height):
            return True
        return False

    def handle_collision(self, ball, obstacle):
        # Lógica de colisão entre bola e obstáculo
        ball_rect = ball.get_rect()
        obstacle_rect = pygame.Rect(obstacle.position.x, obstacle.position.y, obstacle.width, obstacle.height)

        if ball_rect.colliderect(obstacle_rect):
            # Calcula a penetração e ajusta a posição da bola
            left_penetration = ball_rect.right - obstacle_rect.left
            right_penetration = obstacle_rect.right - ball_rect.left
            top_penetration = ball_rect.bottom - obstacle_rect.top
            bottom_penetration = obstacle_rect.bottom - ball_rect.top

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

            # Aplica atrito
            if min_penetration in (left_penetration, right_penetration):
                ball.speed.y *= 0.95
            else:
                ball.speed.x *= 0.95

            #bouncing_sound = pygame.mixer.Sound("sounds/bouncing_ball.wav")
            #bouncing_sound.play()





    
    

