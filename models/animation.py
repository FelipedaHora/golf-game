import pygame

class Animation:
    def __init__(self, image_list, frame_duration):
        """
        image_list: Lista de imagens (sprites) para a animação.
        frame_duration: Duração de cada frame em milissegundos.
        """
        self.image_list = image_list  # Lista de imagens (sprites)
        self.frame_duration = frame_duration  # Duração de cada frame (em ms)
        self.current_frame = 0  # Índice do frame atual
        self.time_accumulator = 0  # Acumula o tempo para troca de frame
        self.image = self.image_list[self.current_frame]  # Imagem inicial

    def update(self, delta_time):
        """
        Atualiza o frame da animação com base no tempo decorrido.
        delta_time: Tempo decorrido desde o último frame.
        """
        self.time_accumulator += delta_time

        # Verifica se já passou o tempo suficiente para mudar de frame
        if self.time_accumulator >= self.frame_duration:
            self.time_accumulator = 0  # Reinicia o acumulador de tempo
            self.current_frame += 1  # Passa para o próximo frame
            
            # Se chegar ao final da lista, volta ao início (loop)
            if self.current_frame >= len(self.image_list):
                self.current_frame = 0

            # Atualiza a imagem para o frame atual
            self.image = self.image_list[self.current_frame]

    def draw(self, screen, position):
        """
        Desenha a animação na tela.
        screen: Superfície onde será desenhada a animação.
        position: Posição (x, y) para desenhar a animação.
        """
        screen.blit(self.image, position)
