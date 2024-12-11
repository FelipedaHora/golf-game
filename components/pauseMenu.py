import pygame
import sys

class PauseMenu:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        
        # Carregar imagens dos botões para o menu de pausa
        self.button_resume = pygame.image.load("assets/sprites/botao-retornar.png")
        self.button_sound = pygame.image.load("assets/sprites/botao-retornar.png")
        self.button_exit = pygame.image.load("assets/sprites/botao-retornar.png")

        self.button_resume = pygame.transform.scale(self.button_resume, (30, 30))
        self.button_sound = pygame.transform.scale(self.button_sound, (30, 30))
        self.button_exit = pygame.transform.scale(self.button_exit, (30, 30))

        # Definir posições dos botões
        self.button_resume_rect = self.button_resume.get_rect(center=(400, 250))
        self.button_sound_rect = self.button_sound.get_rect(center=(400, 350))
        self.button_exit_rect = self.button_exit.get_rect(center=(400, 450))

        # Estado do som (True = ativado, False = desativado)
        self.sound_on = True

        # Configuração de fontes
        self.font = pygame.font.Font(None, 36)
        
        # Definir o cursor padrão e o cursor clicável
        self.default_cursor = pygame.SYSTEM_CURSOR_ARROW
        self.clickable_cursor = pygame.SYSTEM_CURSOR_HAND

    def display_pause_menu(self):
        # Preencher a tela com um fundo semitransparente
        self.screen.fill((0, 0, 0, 128))  # Fundo preto translúcido

        # Desenhar os botões
        self.screen.blit(self.button_resume, self.button_resume_rect)
        self.screen.blit(self.button_sound, self.button_sound_rect)
        self.screen.blit(self.button_exit, self.button_exit_rect)

        # Desenhar o texto ao lado de cada botão
        resume_text = self.font.render("Retornar ao Jogo", True, (255, 255, 255))
        sound_text = self.font.render("Som: Ativado" if self.sound_on else "Som: Desativado", True, (255, 255, 255))
        exit_text = self.font.render("Sair", True, (255, 255, 255))

        # Posicionar o texto à direita dos botões
        self.screen.blit(resume_text, (self.button_resume_rect.right + 10, self.button_resume_rect.centery - resume_text.get_height() // 2))
        self.screen.blit(sound_text, (self.button_sound_rect.right + 10, self.button_sound_rect.centery - sound_text.get_height() // 2))
        self.screen.blit(exit_text, (self.button_exit_rect.right + 10, self.button_exit_rect.centery - exit_text.get_height() // 2))

        pygame.display.flip()

    def run(self):
        running = True
        while running:
            self.display_pause_menu()
            mouse_pos = pygame.mouse.get_pos()
            cursor_changed = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Clique esquerdo do mouse
                        # Verificar se "Retornar ao Jogo" foi clicado
                        if self.button_resume_rect.collidepoint(mouse_pos):
                            return "Retornar ao Jogo"

                        # Verificar se "Som" foi clicado
                        elif self.button_sound_rect.collidepoint(mouse_pos):
                            self.sound_on = not self.sound_on
                            if self.sound_on:
                                    if not pygame.mixer.music.get_busy():  # Verifica se a música está tocando
                                        pygame.mixer.music.unpause()  # Retoma a música se não estiver tocando
                            else:
                                pygame.mixer.music.pause()  # Pausa a música


                        # Verificar se "Sair" foi clicado
                        elif self.button_exit_rect.collidepoint(mouse_pos):
                            return "Sair"

            # Alterar o cursor se estiver sobre um botão
            if (self.button_resume_rect.collidepoint(mouse_pos) or 
                self.button_sound_rect.collidepoint(mouse_pos) or 
                self.button_exit_rect.collidepoint(mouse_pos)):
                pygame.mouse.set_cursor(self.clickable_cursor)
                cursor_changed = True
            else:
                pygame.mouse.set_cursor(self.default_cursor)

            if not cursor_changed:
                pygame.mouse.set_cursor(self.default_cursor)
