import pygame
from models.object import Object
from models.vector import Vector

class Ball(Object):

    def __init__(self, x, y, radius, color, width, height, animation=None):
        super().__init__(Vector(x, y), Vector(0, 0), Vector(0, 900))  # Gravidade reduzida
        self.radius = radius
        self.color = color
        self.width = width
        self.height = height
        self.charge_time = 0
        self.is_charging = False
        self.max_force = 7500  # Força máxima aumentada~
        # Animação associada à bola
        self.animation = animation
        self.is_animating = False
        self.count_plays = 0

    def handle_input(self, mouse_pos):
        if not self.is_charging:
            self.start_charge(mouse_pos)
        else:
            self.stop_charge(mouse_pos)

    def start_charge(self, mouse_pos):
        self.charge_start_time = pygame.time.get_ticks()
        self.is_charging = True

    def stop_charge(self, mouse_pos):
        self.is_charging = False
        charge_duration = (pygame.time.get_ticks() - self.charge_start_time) / 1000.0
        force = min(charge_duration * 2500, self.max_force)  # Taxa de carregamento aumentada

        # Calcula a direção inicial
        direction = Vector(mouse_pos[0] - self.position.x, mouse_pos[1] - self.position.y)
        
        # Normaliza a direção
        magnitude = (direction.x**2 + direction.y**2)**0.5
        if magnitude != 0:
            direction.x /= magnitude
            direction.y /= magnitude
        
        # Aplica um leve favorecimento horizontal
        horizontal_bias = 1.2  # Aumenta ligeiramente a componente horizontal
        vertical_bias = 1.0    # Mantém a componente vertical inalterada
        
        adjusted_direction = Vector(
            direction.x * horizontal_bias,
            direction.y * vertical_bias
        )
        
        # Normaliza a direção ajustada
        adjusted_magnitude = (adjusted_direction.x**2 + adjusted_direction.y**2)**0.5
        if adjusted_magnitude != 0:
            adjusted_direction.x /= adjusted_magnitude
            adjusted_direction.y /= adjusted_magnitude
        
        # Aplica a força à direção ajustada
        self.speed = Vector(adjusted_direction.x * force, adjusted_direction.y * force)

        putt_sound = pygame.mixer.Sound("sounds/putt.wav")

        # Play the audio
        putt_sound.play()

        # Inicia a animação
        if self.animation:
            self.is_animating = True
            self.animation.current_frame = 0
            self.animation.elapsed_time = 0

        # Incrementa o número de jogadas
        self.count_plays += 1


    def charge_force(self, delta_time):
        if self.is_charging:
            self.charge_time += delta_time

    def update(self, delta_time):
        self.physics(delta_time)
        self.handle_collisions()

        # Atualiza a animação, se estiver ativa
        if self.is_animating and self.animation:
            self.animation.update(delta_time * 700)

            # Se a animação tiver completado todos os quadros, pare a animação
            if self.animation.current_frame == len(self.animation.images) - 1:
                self.is_animating = False

    def get_rect(self):
        return pygame.Rect(
            self.position.x - self.radius,
            self.position.y - self.radius,
            self.radius * 2,
            self.radius * 2
        )

    def handle_collisions(self):
        if self.position.y + self.radius > self.height:
            self.position.y = self.height - self.radius
            self.speed.y *= -0.65  # Reduzido ligeiramente para mais realismo
        if self.position.y - self.radius < 0:
            self.position.y = self.radius
            self.speed.y *= -0.65
        if self.position.x - self.radius < 0:
            self.position.x = self.radius
            self.speed.x *= -0.8  # Mantido mais alto para movimento horizontal
        elif self.position.x + self.radius > self.width:
            self.position.x = self.width - self.radius
            self.speed.x *= -0.8

    def draw(self, screen):
        # Desenha a animação atrás da bola
        if self.is_animating and self.animation:
            position = (self.position.x - self.animation.images[0].get_width() // 2,
                        self.position.y - self.animation.images[0].get_height() // 2)
            self.animation.draw(screen, position)

        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), self.radius)
