from models.vector import Vector


class Object:
    def __init__(self, position, speed, acceleration=None, friction=0.98):
        self.position = position
        self.speed = speed
        self.acceleration = acceleration if acceleration else Vector(0, 0)
        self.friction = friction
        
    def physics(self, time: float):
        # Atualiza a velocidade com base na aceleração
        self.speed.x += self.acceleration.x * time
        self.speed.y += self.acceleration.y * time
        
        # Aplica o atrito
        self.speed.x *= self.friction
        self.speed.y *= self.friction
        
        # Atualiza a posição com base na velocidade
        self.position.x += self.speed.x * time
        self.position.y += self.speed.y * time
        
    def apply_friction(self):
        self.speed.x *= self.friction
        self.speed.y *= self.friction