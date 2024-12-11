import pygame
from components.menu import Menu
from components.game import Game
from components.scoreboards import Scoreboard    

def main():
    menu = Menu()
    option_selected = menu.run()
    
    if option_selected == "Iniciar Jogo":
        game = Game()
        game.run()
    elif option_selected == "Sair":
        print("Saindo do jogo...")
    elif option_selected == "Scores":
               # Exibe o scoreboard quando a opção "Scores" for selecionada
        screen = pygame.display.set_mode((1080, 600))  # Ajuste o tamanho da tela conforme necessário
        scoreboard = Scoreboard(screen)
        running_scoreboard = True
        while running_scoreboard:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running_scoreboard = False  # Fecha a tela de scoreboard
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # Se pressionar ESC, voltar ao menu
                        running_scoreboard = False  # Fecha a tela de scoreboard

            scoreboard.display()  # Exibe o scoreboard na tela

        # Retorna ao Menu após fechar o Scoreboard
        main()  # Chama novamente o método main para voltar ao menu


if __name__ == "__main__":
    main()
