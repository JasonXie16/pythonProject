import sys
import pygame
from datetime import datetime
from pygame.locals import *

import random, time
from random import randint
import os

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 900
maxshots = 4
surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


green = (64,235,52)
black = (0,0,0)
white = (255,255,255)
orange = (235,177,52)
red = (235,73,52)
blue = (52,95,235)
points = [(100,100),(200,100),(200,0)]
rect = (100,100,200,200)
grey = (216,218,227)

speed_enemy1 = 2
speed_enemy2 = 2
timer = 60
enemyMaxY = 1000
fps = 60
framePerSecond = pygame.time.Clock()
background = pygame.image.load("gamematerial/background_green_hill.jpg")


pygame.init()

#pygame.mixer.music.load('gamematerial/Sonic The Hedgehog OST - Green Hill Zone.mp3')
#pygame.mixer.music.play(-1)
surface.blit(background,(0,1000))
pygame.display.flip()

SCREENRECT = pygame.Rect(0, 0, 640, 480)

surface.fill(blue)

pygame.display.set_caption("Hello World")

life = 3


main_dir = os.path.split(os.path.abspath(__file__))[0]


def load_image(file):
    file = os.path.join(main_dir, file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s' % (file, pygame.get_error()))
    return surface.convert()
def playerdeath():
    surface.fill(red)
    surface.blit(font_big.render("GAME OVER", True, black), (250, 400))
    surface.blit(font_small.render("Press Escape To End The Game", True, black), (385, 500))
    pygame.display.update()
    for entity in all_sprites:
        entity.kill()
    pressed_keys = pygame.key.get_pressed()
    gameover = True
    waiting = True
    pygame.mixer.music.stop()
    pygame.mixer.Sound('gamematerial/Gameover.wav').play()
    while waiting:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    waiting = False

    pygame.quit()
    sys.exit()
class Enemy(pygame.sprite.Sprite):

    def __init__(self,startposx,speed,direction):
        super().__init__()
        self.image = pygame.image.load("gamematerial/enemyrobotbee.png")
        self.rect = self.image.get_rect()
        self.rect.center = (startposx, 0)
        self.direction = direction
        self.speed = speed
    def killed(self):
        self.kill()
    def move(self):
        if self.direction == "right":
            self.rect.move_ip(self.speed,0)
            if self.rect.right >= SCREEN_WIDTH:
                self.rect.move_ip(0, self.speed + 50)
                if (self.rect.bottom > enemyMaxY):
                    self.rect.top = 0
                    self.rect.center = (random.randint(0,1000), 0)
                self.direction = "left"
        else:
            self.rect.move_ip(self.speed * -1,0)
            if self.rect.left <= 0:
                self.rect.move_ip(0, self.speed + 50)
                if (self.rect.bottom > enemyMaxY):
                    self.rect.top = 0
                    self.rect.center = (random.randint(0,1000), 0)
                self.direction = "right"



    def draw(self, surface):
        surface.blit(self.image, self.rect)

class player1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("gamematerial/sonic_stand_right.png")
        self.reloading = 0
        self.rect = self.image.get_rect(midbottom=SCREENRECT.midbottom)
        self.rect.center = (500, 800)
        self.facing = -1

    def move(self):
        self.pressed_keys = pygame.key.get_pressed()
        self.direction = " "
        self.image = pygame.image.load("gamematerial/sonic_stand_right.png")
        if self.rect.left > 0:
            if self.pressed_keys[K_LEFT]:
                    self.rect.move_ip(-5,0)
                    self.image = pygame.image.load("gamematerial/sonic_move_left.png")
                    self.direction = "left"



        if self.rect.right < SCREEN_WIDTH:
            if self.pressed_keys[K_RIGHT]:
                    self.rect.move_ip(5, 0)
                    self.image = pygame.image.load("gamematerial/sonic_move_right.png")
                    self.direction = "right"

    speedshot = 10
    bounce = 24
    gun_offset = -1
    images = []
    def gunpos(self):
        pos = self.facing = self.gun_offset + self.rect.centerx
        return pos, self.rect.top


    def stand(self):
        if not self.pressed_keys[K_RIGHT] and not self.pressed_keys[K_LEFT]:
            if self.direction == "left":
                self.image = pygame.image.load("gamematerial/sonic_stand_left.png")
            if self.direction == "right":
                self.image = pygame.image.load("gamematerial/sonic_stand_right.png")


    def draw(self, surface):
        surface.blit(self.image, self.rect)




class Shot(pygame.sprite.Sprite):

    speed = -2
    images = []
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=pos)
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=pos)
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=pos)
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=pos)
    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top <= -10:
            self.kill()
        self.rect.move_ip(0, self.speed)
        if self.rect.top <= -10:
            self.kill()
        self.rect.move_ip(0, self.speed)
        if self.rect.top <= -10:
            self.kill()
        self.rect.move_ip(0, self.speed)
        if self.rect.top <= -10:
            self.kill()
        self.rect.move_ip(0, self.speed)

class Bomb(pygame.sprite.Sprite):
    speedbomb = 5
    images = []
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        if random.randint(0,1) == 1:
            self.rect = self.image.get_rect(midbottom=enemy1.rect.move(0, 5).midbottom)
        else:
            self.rect = self.image.get_rect(midbottom=enemy2.rect.move(0, 5).midbottom)

    def update(self):
        self.rect.move_ip(0, self.speedbomb)
        if self.rect.bottom >= 850:
            self.image = pygame.image.load("gamematerial/explosion1.gif")
            if self.rect.bottom >= 900:
                self.kill()
                pygame.mixer.Sound('gamematerial/boom.wav').play()
        if pygame.sprite.spritecollide(player1, bomb, 0, 0):
            self.rect.bottom = 1000
            self.rect.bottom = 1000
            global life
            life = life - 1
            self.image = pygame.image.load("gamematerial/explosion1.gif")
            if life == 0:
                surface.fill(red)
                surface.blit(font_big.render("GAME OVER", True, black), (250, 400))
                surface.blit(font_small.render("Press Escape To End The Game", True, black), (385, 500))
                pygame.display.update()
                for entity in all_sprites:
                    entity.kill()
                pressed_keys = pygame.key.get_pressed()
                gameover = True
                waiting = True
                pygame.mixer.music.stop()
                time.sleep(1)
                pygame.mixer.Sound('gamematerial/Gameover.wav').play()
                while waiting:
                    clock.tick(fps)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            waiting = False
                            running = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                waiting = False

                pygame.quit()
                sys.exit()



enemy1 = Enemy(random.randint(0,1000),10,"right")
enemy2 = Enemy(random.randint(0,1000),5,"left")
shots = pygame.sprite.Group()
bomb = pygame.sprite.Group()
player1 = player1()
enemies = pygame.sprite.Group()
all_sprites  = pygame.sprite.Group()
enemies.add(enemy1)
enemies.add(enemy2)
all = pygame.sprite.RenderUpdates()
all_sprites.add(player1)
all_sprites.add(enemy1)
all_sprites.add(enemy2)
Shot.containers = shots, all
Bomb.containers = bomb, all
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)
font_small = pygame.font.SysFont('Consolas', 15)
font_big = pygame.font.SysFont('Consolas', 100)
font2 = pygame.font.SysFont('arimo', 40)
counter, text = 60, '60'.rjust(3)
run = True
Shot.images = [load_image("gamematerial/shot.gif"),pygame.SRCALPHA]
Bomb.images = [load_image("gamematerial/bomb.gif")]
points = 0
while run:
    surface.blit(font.render("Timer:" + text, True, white), (32, 48))
    surface.blit(font.render("Points:" + str(points), True, green), (32, 100))
    surface.blit(font2.render("Health: " + str(life), True, red), (850, 48))
    surface.blit(font2.render("Ammo: " + str(maxshots - len(shots)), True, orange), (850, 100))
    pygame.display.flip()
    clock.tick(60)
    all.clear(surface, background)
    all.update()
    for e in pygame.event.get():
        if e.type == INC_SPEED:
            speed_enemy1 += 1
            speed_enemy2 += 1
        if e.type == pygame.USEREVENT:
            counter -= 1
            text = str(counter).rjust(3) if counter > 0 else pygame.quit()
        if e.type == pygame.QUIT:
            run = False
        pressed_keys = pygame.key.get_pressed()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                if not len(shots) == maxshots:
                    Shot.update(Shot(player1.gunpos()))
                    pygame.mixer.Sound('gamematerial/car_door.wav').play()

    surface.blit(background, (0,0))
    surface.blit(font.render("Timer:" + text, True, white), (32, 48))
    surface.blit(font2.render("Health: " + str(life), True, red), (850, 48))
    surface.blit(font.render("Points:" + str(points), True, green), (32, 100))
    surface.blit(font2.render("Ammo: " + str(maxshots - len(shots)), True, orange), (850, 100))
    for entity in all_sprites:
        surface.blit(entity.image, entity.rect)
        entity.move()
    for allenemy in enemies:
        if pygame.sprite.spritecollideany(allenemy,shots):
            points += 1
            allenemy.kill()



    for allenemy in enemies:
        if pygame.sprite.collide_rect(player1, allenemy):
            pygame.mixer.Sound('gamematerial/PygameTutorial_3_0/crash.wav').play()
            life = life - 1
            allenemy.kill()
            if life == 0:
                playerdeath()





    enemy1.move()
    enemy1.draw(surface)
    enemy2.move()
    enemy2.draw(surface)
    player1.move()
    player1.stand()
    player1.draw(surface)
    if random.randint(1,40) == 1:
        Bomb.update(Bomb())

        #pygame.mixer.Sound('gamematerial/bombthrow3.wav').play()
    dirty = all.draw(surface)
    pygame.display.update(dirty)
    framePerSecond.tick(fps)