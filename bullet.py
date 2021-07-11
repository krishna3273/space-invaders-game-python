from os import path
import time
import pygame
WIDTH = 480
HEIGHT = 480
FPS =60
# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.image = pygame.transform.scale(self.image,(self.rect.width, 60))
    def update(self):
        self.rect.y +=self.speedy
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()
