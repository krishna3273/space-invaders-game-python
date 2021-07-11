from bullet import Bullet
import pygame
from os import path
import time
img_dir =path.dirname(__file__)
class Bullet2(Bullet):
    def __init__(self,x,y):
        Bullet.__init__(self,x,y,bullet2_img)
        self.speedy=-2
bullet2_img = pygame.image.load(path.join(img_dir, "laserBlue16.png")).convert()
