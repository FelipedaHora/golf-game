import pygame
from models.object import Object
from models.vector import Vector

class Obstacle(Object):
    def __init__(self, x, y, image_path):
        # Initialize position and speed
        position = Vector(x, y)
        speed = Vector(0, 0)
        super().__init__(position, speed)
        
        # Load the obstacle image and get its rect (for collision detection)
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(topleft=(x, y))
        
        # Set width and height based on the image's dimensions
        self.width = self.rect.width
        self.height = self.rect.height

    def draw(self, screen):
        # Draw the obstacle on the screen
        screen.blit(self.image, self.rect.topleft)

    def update(self, delta_time):
        # Update position based on speed (if necessary)
        self.physics(delta_time)
        self.rect.topleft = (self.position.x, self.position.y)
        
    def check_collision(self, ball):
        # Check if the ball collided with the obstacle
        ball_rect = pygame.Rect(
            ball.position.x - ball.radius,
            ball.position.y - ball.radius,
            ball.radius * 2,
            ball.radius * 2
        )
        return self.rect.colliderect(ball_rect)
