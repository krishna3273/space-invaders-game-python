#importing required modules
import pygame
import random
from os import path
import time


#loading some conatants
BLACK = (0, 0, 0)
WIDTH = 480
HEIGHT = 480
FPS =60


#intialising pygame and creating screen
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MYGAME!")
clock = pygame.time.Clock()



#loading required game variables
img_dir =path.dirname(__file__)
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets1 = pygame.sprite.Group()
bullets2=pygame.sprite.Group()
background = pygame.image.load(path.join(img_dir, "starfield.png")).convert()
alien_img=pygame.image.load(path.join(img_dir,'blockerMad.png')).convert()
player_img = pygame.image.load(path.join(img_dir, "playerShip1_orange.png")).convert()



#importing other classes
from spaceship import Player
from alien import Mob



# Game logic
background_rect = background.get_rect()
player = Player(player_img)
all_sprites.add(player)
running = True
m = Mob(alien_img)
all_sprites.add(m)
mobs.add(m)
prev=pygame.time.get_ticks()


#counting score
score=0
#Game loop
while running:
    clock.tick(FPS)
    
    #process inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot1(all_sprites,bullets1)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                player.shoot2(all_sprites,bullets2)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                player.rect.centerx+=60
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.rect.centerx-=60



    #update
    all_sprites.update()
    now=pygame.time.get_ticks()
    hits = pygame.sprite.groupcollide(mobs, bullets2,False,True)
    for hit in hits:
        hit.born=now-3000
        if hit.hit==0:
            hit.hit=1
            score+=1
        
    hits = pygame.sprite.groupcollide(mobs, bullets1,True,True)
    for hit in hits:
        if hit.hit==0:
            score+=1
    hits = pygame.sprite.spritecollide(player, mobs, False, pygame.sprite.collide_circle)
    if hits:
        running = False
    if(now-prev>10000):
        m=Mob(alien_img)
        all_sprites.add(m)
        mobs.add(m)
        prev=now



    #draw/render
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    pygame.display.flip()


#Game over
pygame.quit()
print(score)
