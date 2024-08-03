import pygame
from models.object import Object
from models.vector import Vector

class Ball(Object):
    def __init__(self, x, y, radius, color, width, height):
        super().__init__(Vector(x, y), Vector(0, 0))
        self.radius = radius
        self.color = color
        self.width = width
        self.height = height
        self.charge_time = 0
        self.is_charging = False

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
        force = min(charge_duration, 2.0) * 500  # Ajuste a força conforme necessário
        direction = Vector(mouse_pos[0] - self.position.x, mouse_pos[1] - self.position.y)
        magnitude = (direction.x**2 + direction.y**2)**0.5
        direction.x /= magnitude
        direction.y /= magnitude
        self.speed = Vector(direction.x * force, direction.y * force)  # Corrigido para considerar a direção positiva

    def charge_force(self, delta_time):
        if self.is_charging:
            self.charge_time += delta_time

    def update(self, delta_time):
        self.physics(delta_time)
        # Corrigir a física da colisão
        if self.position.y + self.radius > self.height:
            self.position.y = self.height - self.radius
            self.speed.y *= -0.6
        if self.position.y - self.radius < 0:
            self.position.y = self.radius
            self.speed.y *= -0.6
        if self.position.x - self.radius < 0:
            self.position.x = self.radius
            self.speed.x *= -0.6
        elif self.position.x + self.radius > self.width:
            self.position.x = self.width - self.radius
            self.speed.x *= -0.6

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), self.radius)
