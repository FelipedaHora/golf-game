import pygame
from system.image_rendering import scale_image

class AssetsPort:
    background = scale_image(pygame.image.load("assets/sprites/back.png"), 0.55)
    sand = scale_image(pygame.image.load("assets/sprites/sand.png"), 0.55)
    water = scale_image(pygame.image.load("assets/sprites/water.png"), 0.55)
    sandBottom = scale_image(pygame.image.load("assets/sprites/sandBottom.png"), 0.55)
    sandEdge = scale_image(pygame.image.load("assets/sprites/sandEdge.png"), 0.55)
    coin5 = scale_image(pygame.image.load("assets/sprites/coin5.png"), 0.55)
    # coin10 = scale_image(pygame.image.load("assets/sprites/coin10.png"), 0.55)
    # coin20 = scale_image(pygame.image.load("assets/sprites/coin20.png"), 0.55)
    # coin50 = scale_image(pygame.image.load("assets/sprites/coin50.png"), 0.55)
    power = scale_image(pygame.image.load("assets/sprites/power.png"), 0.55)