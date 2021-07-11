from bullet import Bullet
import pygame
from os import path
import time
img_dir =path.dirname(__file__)
class Bullet1(Bullet):
    def __init__(self,x,y):
        Bullet.__init__(self,x,y,bullet1_img)
        self.speedy=-1
bullet1_img = pygame.image.load(path.join(img_dir, "laserRed16.png")).convert()
