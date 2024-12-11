import pygame
import sys

class Scoreboard:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 30)
        self.background_color = (0, 0, 0)
        self.text_color = (255, 255, 255)
        self.players_scores = []  # Lista de scores
        
        # Carregar scores do arquivo
        self.load_scores()
    
    def add_score(self, name, strokes, coins):
        """Adiciona o score de um jogador e salva no arquivo"""
        self.players_scores.append((name, strokes, coins))
        self.save_scores()  # Salva os scores no arquivo sempre que um novo score é adicionado
    
    def save_scores(self):
        """Salva os scores no arquivo scores.txt"""
        with open("scores.txt", "w") as file:
            for name, strokes, coins in self.players_scores:
                file.write(f"{name},{strokes},{coins}\n")
    
    def load_scores(self):
        """Carrega os scores do arquivo scores.txt"""
        try:
            with open("scores.txt", "r") as file:
                for line in file:
                    name, strokes, coins = line.strip().split(",")
                    self.players_scores.append((name, int(strokes), int(coins)))
        except FileNotFoundError:
            # Se o arquivo não for encontrado, iniciamos uma lista vazia
            self.players_scores = []
    
    def display(self):
        """Exibe a tela de scoreboard"""
        self.screen.fill(self.background_color)

        header_text = self.font.render("Scoreboard", True, self.text_color)
        self.screen.blit(header_text, (350, 50))

        y_offset = 100
        for name, strokes, coins in self.players_scores:
            score_text = self.font.render(f"Nome: {name} - Tacadas: {strokes} - Moedas: {coins}", True, self.text_color)
            self.screen.blit(score_text, (100, y_offset))
            y_offset += 40

        # Adicionando a opção para voltar ao menu
        back_text = self.font.render("Pressione ESC para voltar ao Menu", True, self.text_color)
        self.screen.blit(back_text, (250, 500))

        pygame.display.flip()