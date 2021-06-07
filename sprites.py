import pygame
import random
import os
from config import WIDTH, HEIGHT, PLAYER_HEIGHT, PLAYER_WIDTH, CAPIVARA_HEIGHT, CAPIVARAMOTO_WIDTH, IMG_DIR, SND_DIR, player, CAPIVARAMOTO_HEIGHT, CAPIVARA_WIDTH
from assets import PLAYER_R_IMG, BOLINHO_IMG, REFRI_IMG, CAPIVARA_R_IMG, CAPIVARAMOTO_R_IMG, VIDA3, VIDA2, VIDA1, assets

#Classes do Jogador
class Player(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.spritesl = []
        self.spritesr = []
        self.spritesr.append(pygame.image.load(os.path.join(IMG_DIR, 'guitas_move_r-1.png').convert_alpha()))
        self.spritesr.append(pygame.image.load(os.path.join(IMG_DIR, 'guitas_move_r-2.png').convert_alpha()))
        self.spritesr.append(pygame.image.load(os.path.join(IMG_DIR, 'guitas_move_r-3.png').convert_alpha()))
        self.spritesr.append(pygame.image.load(os.path.join(IMG_DIR, 'guitas_move_r-4.png').convert_alpha()))
        self.spritesl.append(pygame.image.load(os.path.join(IMG_DIR, 'guitas_move_l-1.png').convert_alpha()))
        self.spritesl.append(pygame.image.load(os.path.join(IMG_DIR, 'guitas_move_l-2.png').convert_alpha()))
        self.spritesl.append(pygame.image.load(os.path.join(IMG_DIR, 'guitas_move_l-3.png').convert_alpha()))
        self.spritesl.append(pygame.image.load(os.path.join(IMG_DIR, 'guitas_move_l-4.png').convert_alpha()))
        self.image = assets[PLAYER_R_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH / 2
        self.rect.y = HEIGHT-60
        self.speedx = 0
        self.speedy = 10
        self.wleft = False #Verificar movimento p/ esquerda para iniciar animação
        self.wright = False #Verificar movimento p/ direita para iniciar animação
        self.wcount = 0 #Contagem p/ os frames do movimento
        self.jump = False #Verificar se está pulando

    def update(self):
        #imagem parado
        if self.wright and self.wleft:
            self.image = player.image
        else:
            #Imagens de movimentação p/ esquerda
            if self.wleft:
                self.wcount += 0.1
                if self.wcount >= len(self.spritesl):
                    self.wcount = 0
                self.image = self.spritesl[int(self.wcount)]
                self.image = pygame.transform.scale(self.image, (PLAYER_WIDTH, PLAYER_HEIGHT))
            #Imagens de movimentação p/ direita
            elif self.wright:
                self.wcount += 0.1
                if self.wcount >= len(self.spritesr):
                    self.wcount = 0
                self.image = self.spritesr[int(self.wcount)]
                self.image = pygame.transform.scale(self.image, (PLAYER_WIDTH, PLAYER_HEIGHT))
            else:
                self.image = assets[PLAYER_R_IMG]

        # Atualizando a posição
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.jump == True:
            if self.rect.y <= 180:
                self.jump = False
            self.rect.y -=20
 
        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT-70:
            self.rect.bottom = HEIGHT-70

    def jumping(self):
        self.jump = True
#Classes dos Bolinhos
class Bolinho(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = assets[BOLINHO_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50, WIDTH-50)
        self.rect.y = random.randint(250, 500)
    
    def update(self):
        self.rect.x += 0
        self.rect.y += 0
#Classes dos Refri
class Refri(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = assets[REFRI_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50, WIDTH-50)
        self.rect.y = random.randint(250, 500)
    
    def update(self):
        self.rect.x += 0
        self.rect.y += 0
class Capivara(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.spritesl = []
        self.spritesr = []
        self.spritesr.append(pygame.image.load(os.path.join(IMG_DIR, 'capivara_move_r-1.png').convert_alpha()))
        self.spritesr.append(pygame.image.load(os.path.join(IMG_DIR, 'capivara_move_r-2.png').convert_alpha()))
        self.spritesl.append(pygame.image.load(os.path.join(IMG_DIR, 'capivara_move_l-1.png').convert_alpha()))
        self.spritesl.append(pygame.image.load(os.path.join(IMG_DIR, 'capivara_move_l-2.png').convert_alpha()))
        self.image = assets[CAPIVARA_R_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.start_or_end = random.randint(1,2)
        if self.start_or_end == 1:
            self.rect.x = 0 - CAPIVARA_WIDTH
            self.speedx = 5
        else:
            self.rect.x = WIDTH + CAPIVARA_WIDTH
            self.speedx = -5
        self.rect.y = 440
        self.speedy = 0
        self.wcount = 0 #Contagem p/ os frames do movimento

    def update(self):
        # Atualizando a posição da capivara
        self.rect.x += self.speedx
        # novas posições e velocidades
        if self.start_or_end == 1:
            if self.rect.left > WIDTH:
                self.start_or_end = random.randint(1,2)
                if self.start_or_end == 1:
                    self.rect.x = 0 - CAPIVARA_WIDTH
                    self.speedx = 5
                else:
                    self.rect.x = WIDTH + CAPIVARA_WIDTH
                    self.speedx = -5
        else:
            if self.rect.right < 0:
                self.start_or_end = random.randint(1,2)
                if self.start_or_end == 1:
                    self.rect.x = 0 - CAPIVARA_WIDTH
                    self.speedx = 5
                else:
                    self.rect.x = WIDTH + CAPIVARA_WIDTH
                    self.speedx = -5
        #Imagens de movimentação p/ esquerda
        if self.speedx < 0:
            self.wcount += 0.1
            if self.wcount >= len(self.spritesl):
                self.wcount = 0
            self.image = self.spritesl[int(self.wcount)]
            self.image = pygame.transform.scale(self.image, (CAPIVARA_WIDTH, CAPIVARA_HEIGHT))
            self.mask = pygame.mask.from_surface(self.image)
        #Imagens de movimentação p/ direita
        elif self.speedx > 0:
            self.wcount += 0.1
            if self.wcount >= len(self.spritesr):
                self.wcount = 0
            self.image = self.spritesr[int(self.wcount)]
            self.image = pygame.transform.scale(self.image, (CAPIVARA_WIDTH, CAPIVARA_HEIGHT))
            self.mask = pygame.mask.from_surface(self.image)
        else:
            self.image = assets[CAPIVARA_R_IMG]
            self.mask = pygame.mask.from_surface(self.image)

    def stop(self):
        self.rect.x = 0 - CAPIVARA_WIDTH
        self.speedx = 0

class Capivara2(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.spritesl = []
        self.spritesr = []
        self.spritesr.append(pygame.image.load(os.path.join(IMG_DIR, 'capivara_move_r-1.png').convert_alpha()))
        self.spritesr.append(pygame.image.load(os.path.join(IMG_DIR, 'capivara_move_r-2.png').convert_alpha()))
        self.spritesl.append(pygame.image.load(os.path.join(IMG_DIR, 'capivara_move_l-1.png').convert_alpha()))
        self.spritesl.append(pygame.image.load(os.path.join(IMG_DIR, 'capivara_move_l-2.png').convert_alpha()))
        self.image = assets[CAPIVARA_R_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.start_or_end = random.randint(1,2)
        if self.start_or_end == 1:
            self.rect.x = 0 - CAPIVARA_WIDTH
            self.speedx = random.randint(4, 8)
        else:
            self.rect.x = WIDTH + CAPIVARA_WIDTH
            self.speedx = random.randint(-8, -4)
        self.rect.y = 440
        self.speedy = 0
        self.wcount = 0 #Contagem p/ os frames do movimento

    def update(self):
        # Atualizando a posição da capivara
        self.rect.x += self.speedx
        # novas posições e velocidades
        if self.start_or_end == 1:
            if self.rect.left > WIDTH:
                self.start_or_end = random.randint(1,2)
                if self.start_or_end == 1:
                    self.rect.x = 0 - CAPIVARA_WIDTH
                    self.speedx = random.randint(4, 8)
                else:
                    self.rect.x = WIDTH + CAPIVARA_WIDTH
                    self.speedx = random.randint(-8, -4)
        else:
            if self.rect.right < 0:
                self.start_or_end = random.randint(1,2)
                if self.start_or_end == 1:
                    self.rect.x = 0 - CAPIVARA_WIDTH
                    self.speedx = random.randint(4, 8)
                else:
                    self.rect.x = WIDTH + CAPIVARA_WIDTH
                    self.speedx = random.randint(-8, -4)
        #Imagens de movimentação p/ esquerda
        if self.speedx < 0:
            self.wcount += 0.1
            if self.wcount >= len(self.spritesl):
                self.wcount = 0
            self.image = self.spritesl[int(self.wcount)]
            self.image = pygame.transform.scale(self.image, (CAPIVARA_WIDTH, CAPIVARA_HEIGHT))
            self.mask = pygame.mask.from_surface(self.image)
        #Imagens de movimentação p/ direita
        elif self.speedx > 0:
            self.wcount += 0.1
            if self.wcount >= len(self.spritesr):
                self.wcount = 0
            self.image = self.spritesr[int(self.wcount)]
            self.image = pygame.transform.scale(self.image, (CAPIVARA_WIDTH, CAPIVARA_HEIGHT))
            self.mask = pygame.mask.from_surface(self.image)
        else:
            self.image = assets[CAPIVARA_R_IMG]
            self.mask = pygame.mask.from_surface(self.image)
class CapivaraMoto(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.spritesl = []
        self.spritesr = []
        self.spritesr.append(pygame.image.load(os.path.join(IMG_DIR, 'capivara_moto_r-1.png').convert_alpha()))
        self.spritesr.append(pygame.image.load(os.path.join(IMG_DIR, 'capivara_moto_r-2.png').convert_alpha()))
        self.spritesl.append(pygame.image.load(os.path.join(IMG_DIR, 'capivara_moto_l-1.png').convert_alpha()))
        self.spritesl.append(pygame.image.load(os.path.join(IMG_DIR, 'capivara_moto_l-2.png').convert_alpha()))
        self.image = assets[CAPIVARAMOTO_R_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.start_or_end = random.randint(1,2)
        if self.start_or_end == 1:
            self.rect.x = 0 - CAPIVARAMOTO_WIDTH
            self.speedx = random.randint(14, 18)
        else:
            self.rect.x = WIDTH + CAPIVARAMOTO_WIDTH
            self.speedx = random.randint(-18, -14)
        self.rect.y = 320
        self.speedy = 0
        self.wcount = 0 #Contagem p/ os frames do movimento

    def update(self):
        # Atualizando a posição da capivara de moto
        self.rect.x += self.speedx
        # novas posições e velocidades
        if self.start_or_end == 1:
            if self.rect.left > WIDTH:
                self.start_or_end = random.randint(1,2)
                if self.start_or_end == 1:
                    self.rect.x = 0 - CAPIVARAMOTO_WIDTH
                    self.speedx = random.randint(12, 14)
                else:
                    self.rect.x = WIDTH + CAPIVARAMOTO_WIDTH
                    self.speedx = random.randint(-14, -12)
        else:
            if self.rect.right < 0:
                self.start_or_end = random.randint(1,2)
                if self.start_or_end == 1:
                    self.rect.x = 0 - CAPIVARAMOTO_WIDTH
                    self.speedx = random.randint(12, 14)
                else:
                    self.rect.x = WIDTH + CAPIVARAMOTO_WIDTH
                    self.speedx = random.randint(-14, -12)
        #Imagens de movimentação p/ esquerda
        if self.speedx < 0:
            self.wcount += 0.1
            if self.wcount >= len(self.spritesl):
                self.wcount = 0
            self.image = self.spritesl[int(self.wcount)]
            self.image = pygame.transform.scale(self.image, (CAPIVARAMOTO_WIDTH, CAPIVARAMOTO_HEIGHT))
            self.mask = pygame.mask.from_surface(self.image)
        #Imagens de movimentação p/ direita
        elif self.speedx > 0:
            self.wcount += 0.1
            if self.wcount >= len(self.spritesr):
                self.wcount = 0
            self.image = self.spritesr[int(self.wcount)]
            self.image = pygame.transform.scale(self.image, (CAPIVARAMOTO_WIDTH, CAPIVARAMOTO_HEIGHT))
            self.mask = pygame.mask.from_surface(self.image)
        else:
            self.image = assets[CAPIVARA_R_IMG]
            self.mask = pygame.mask.from_surface(self.image)

# Desenhando as vidas
class Vidas(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[VIDA3]
        self.rect = self.image.get_rect()
        self.rect.x = 900
        self.rect.y = 10
        self.vidas = 3 #contador de vidas

    # Muda imagem das vidas
    def update(self):
        if self.vidas == 3:
            self.image = assets[VIDA3]
        elif self.vidas == 2:
            self.image = assets[VIDA2]
        else:
            self.image = assets[VIDA1]

