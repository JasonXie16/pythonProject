import pygame
pg = pygame



class Shot(pg.sprite.Sprite):


    speed = -11
    images = []

    def __init__(self, pos):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load("gamematerial/bomb.png")
        self.rect = self.image.get_rect(midbottom=pos)

    def update(self):

        self.rect.move_ip(0, self.speed)
        if self.rect.bottom >= 470:
            Explosion(self)
            self.kill()


Shot.update()