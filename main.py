from components.menu import Menu
from components.game import Game    

def main():
    menu = Menu()
    option_selected = menu.run()
    
    if option_selected == "Iniciar Jogo":
        game = Game()
        game.run()
    elif option_selected == "Sair":
        print("Saindo do jogo...")

if __name__ == "__main__":
    main()
