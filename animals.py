import pygame


class Simba(pygame.sprite.Sprite):

    def __init__(self):
       super().__init__()
       self.image = pygame.image.load("images/simba.png")
       self.rect = self.image.get_rect()
