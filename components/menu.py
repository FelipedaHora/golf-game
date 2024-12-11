import pygame
import sys

class Menu:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1080, 600))  # Ajuste conforme necessário
        pygame.display.set_caption("Menu do Jogo")

        # Carregar imagem de fundo e botões
        self.background = pygame.image.load("assets/sprites/WALLPAPER.png")
        self.button_play = pygame.image.load("assets/sprites/botao-jogar.png")
        self.button_exit = pygame.image.load("assets/sprites/botao-sair.png")
        self.button_scores = pygame.image.load("assets/sprites/botao-scores.png")

        # Definir posições dos botões
        self.button_play_rect = self.button_play.get_rect(center=(395, 562))
        self.button_exit_rect = self.button_exit.get_rect(center=(693, 562))
        self.button_scores_rect = self.button_scores.get_rect(center=(993, 50))

        # Definir o cursor padrão e o cursor clicável
        self.default_cursor = pygame.SYSTEM_CURSOR_ARROW
        self.clickable_cursor = pygame.SYSTEM_CURSOR_HAND

    def display_menu(self):
        # Desenhar fundo e botões
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.button_play, self.button_play_rect)
        self.screen.blit(self.button_exit, self.button_exit_rect)
        self.screen.blit(self.button_scores, self.button_scores_rect)
        
        pygame.display.flip()

    def run(self):
        running = True
        while running:
            self.display_menu()
            mouse_pos = pygame.mouse.get_pos()
            cursor_changed = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Clique esquerdo do mouse
                        # Verificar se o botão "Jogar" foi clicado
                        if self.button_play_rect.collidepoint(mouse_pos):
                            return "Iniciar Jogo"
                        
                        # Verificar se o botão "Sair" foi clicado
                        elif self.button_exit_rect.collidepoint(mouse_pos):
                            return "Sair"
                        
                        # Verificar se o botão "Scores" foi clicado
                        elif self.button_scores_rect.collidepoint(mouse_pos):
                            return "Scores"
            
            # Verificar se o mouse está sobre algum dos botões
            if self.button_play_rect.collidepoint(mouse_pos) or self.button_exit_rect.collidepoint(mouse_pos):
                pygame.mouse.set_cursor(self.clickable_cursor)
                cursor_changed = True
            else:
                pygame.mouse.set_cursor(self.default_cursor)

            # Garantir que o cursor seja atualizado apenas quando necessário
            if not cursor_changed:
                pygame.mouse.set_cursor(self.default_cursor)
