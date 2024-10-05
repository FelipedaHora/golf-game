class Animation:
    def __init__(self, images, frame_duration):

        self.images = images
        self.frame_duration = frame_duration  # Duração de cada frame (em milissegundos)
        self.current_frame = 0
        self.elapsed_time = 0

    def update(self, delta_time):
        # Atualiza o tempo decorrido
        self.elapsed_time += delta_time * 1000  # Converte delta_time de segundos para milissegundos

        # Verifica se o tempo decorrido é suficiente para mudar para o próximo frame
        if self.elapsed_time >= self.frame_duration:
            self.current_frame += 1
            self.elapsed_time = 0  # Reseta o tempo decorrido

            # Loop da animação (reinicia quando chegar ao último frame)
            if self.current_frame >= len(self.images):
                self.current_frame = 0

    def draw(self, surface, position):
        current_image = self.images[self.current_frame]
        surface.blit(current_image, position)
