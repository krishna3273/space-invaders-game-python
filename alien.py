import pygame
from os import path
import random
import time
# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
class Mob(pygame.sprite.Sprite):
    hit=0
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(img, (60, 60))
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        self.image.set_colorkey(BLACK)
        self.rect.x=random.choice([0,60,120,180,240,300,360,420])
        self.rect.y =random.choice([0,60])
        self.born=pygame.time.get_ticks()
        self.last_update = pygame.time.get_ticks()
    def update(self):
        now=pygame.time.get_ticks()
        if(now-self.born>8000):
            self.kill()
