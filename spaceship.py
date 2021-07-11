from os import path
import pygame
import time
from bullet1 import Bullet1
from bullet2 import Bullet2
WIDTH = 480
HEIGHT = 480
# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
class Player(pygame.sprite.Sprite):
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(img,(60,60))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 20
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = WIDTH/2-30
        self.rect.bottom = HEIGHT
        self.speedx = 0
    def update(self):
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot1(self,all_sprites,bullets1):
        bullet = Bullet1(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets1.add(bullet)
    def shoot2(self,all_sprites,bullets2):
        bullet = Bullet2(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets2.add(bullet)
