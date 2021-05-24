import random
import pygame
from config import WIDTH, HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT
from assets import PLAYER_RIMG, PLAYER_LIMG, PLAYER_LWALK, PLAYER_RWALK

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[PLAYER_RIMG]
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH / 2
        self.rect.y = HEIGHT / 2
        self.speedx = 0
        self.speedy = 10
        self.wleft = False #Verificar movimento p/ esquerda para iniciar animação
        self.wright = False #Verificar movimento p/ direita para iniciar animação
        self.wcount = 0 #Contagem p/ os frames do movimento
        self.jump = False #Verificr se está pulando

    def update(self, assets):
        #imagem parado
        if self.wright and self.wleft:
            self.image = assets[PLAYER_RIMG]
        else:
            #Imagens de movimentação p/ esquerda
            if self.wleft:
                self.wcount += 0.1
                if self.wcount >= len(assets[PLAYER_LWALK]):
                    self.wcount = 0
                self.image = self.assets[PLAYER_LWALK][int(self.wcount)]
                self.image = pygame.transform.scale(self.image, (PLAYER_WIDTH, PLAYER_HEIGHT))
            #Imagens de movimentação p/ direita
            elif self.wright:
                self.wcount += 0.1
                if self.wcount >= len(assets[PLAYER_RWALK]):
                    self.wcount = 0
                self.image = self.assets[PLAYER_RWALK][int(self.wcount)]
                self.image = pygame.transform.scale(self.image, (PLAYER_WIDTH, PLAYER_HEIGHT))
            else:
                self.image = assets[PLAYER_RIMG]

        # Atualizando a posição
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.jump == True:
            if self.rect.y <= 400:
                self.jump = False
            self.rect.y -=20
 
        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    # def walk(self):
    #     if self.wleft:

    #     if self.wright:

    def jumping(self):
        self.jump = True