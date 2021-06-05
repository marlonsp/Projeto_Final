import pygame
import random

pygame.init()
pygame.mixer.init()

WIDTH = 1100
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Jogo.v9')
pygame.mixer.music.set_volume(0.4)

BLACK = (0, 0, 0)

teste = pygame.image.load('assets/img/player_test.png')
pygame.display.set_icon(teste)
# ----- Inicia assets
PLAYER_WIDTH = 120
PLAYER_HEIGHT = 120

CAPIVARA_WIDTH = 120
CAPIVARA_HEIGHT = 100

CAPIVARAMOTO_WIDTH = 220
CAPIVARAMOTO_HEIGHT = 220

assets = {}
assets['background1'] = pygame.image.load('assets/img/fundo1.png')
assets['background1'] = pygame.transform.scale(assets['background1'], (WIDTH, HEIGHT))
assets['background2'] = pygame.image.load('assets/img/fundo2.png')
assets['background2'] = pygame.transform.scale(assets['background2'], (WIDTH, HEIGHT))
assets['background3'] = pygame.image.load('assets/img/fundo3.png')
assets['background3'] = pygame.transform.scale(assets['background3'], (WIDTH, HEIGHT))
assets['charchoose_img'] = pygame.image.load('assets/img/char_choose.png')
assets['charchoose_img'] = pygame.transform.scale(assets['charchoose_img'], (WIDTH, HEIGHT))
assets['init_img'] = pygame.image.load('assets/img/init_img.png')
assets['init_img'] = pygame.transform.scale(assets['init_img'], (WIDTH, HEIGHT))
assets['telafim_img'] = pygame.image.load('assets/img/telafim_img.png')
assets['telafim_img'] = pygame.transform.scale(assets['telafim_img'], (WIDTH, HEIGHT))
assets['instructions_img'] = pygame.image.load('assets/img/instructions_img.png')
assets['instructions_img'] = pygame.transform.scale(assets['instructions_img'], (WIDTH, HEIGHT))
assets['instructions2_img'] = pygame.image.load('assets/img/fase2start.png')
assets['instructions2_img'] = pygame.transform.scale(assets['instructions2_img'], (WIDTH, HEIGHT))
assets['instructions3_img'] = pygame.image.load('assets/img/fase3start.png')
assets['instructions3_img'] = pygame.transform.scale(assets['instructions3_img'], (WIDTH, HEIGHT))
assets['player_r_img'] = pygame.image.load('assets/img/guitas_r.png').convert_alpha()
assets['player_r_img'] = pygame.transform.scale(assets['player_r_img'], (PLAYER_WIDTH, PLAYER_HEIGHT))
assets['player_l_img'] = pygame.image.load('assets/img/guitas_l.png').convert_alpha()
assets['player_l_img'] = pygame.transform.scale(assets['player_l_img'], (PLAYER_WIDTH, PLAYER_HEIGHT))
assets['bolinho_img'] = pygame.image.load('assets/img/bolinho_caipira.png').convert_alpha()
assets['bolinho_img'] = pygame.transform.scale(assets['bolinho_img'], (60, 60))
assets['refri_img'] = pygame.image.load('assets/img/refri.png').convert_alpha()
assets['refri_img'] = pygame.transform.scale(assets['refri_img'], (60, 60))
assets["score_font"] = pygame.font.Font('assets/font/lunchds.ttf', 50)
assets['capivara_r_img'] = pygame.image.load('assets/img/capivara_move_r-1.png').convert_alpha()
assets['capivara_r_img'] = pygame.transform.scale(assets['capivara_r_img'], (CAPIVARA_WIDTH, CAPIVARA_HEIGHT))
assets['capivara_l_img'] = pygame.image.load('assets/img/capivara_move_l-1.png').convert_alpha()
assets['capivara_l_img'] = pygame.transform.scale(assets['capivara_l_img'], (CAPIVARA_WIDTH, CAPIVARA_HEIGHT))
assets['capivaramoto_r_img'] = pygame.image.load('assets/img/capivara_moto_r-1.png').convert_alpha()
assets['capivaramoto_r_img'] = pygame.transform.scale(assets['capivaramoto_r_img'], (CAPIVARA_WIDTH, CAPIVARA_HEIGHT))
assets['vida=3'] = pygame.image.load('assets/img/vida1.png').convert_alpha()
assets['vida=3'] = pygame.transform.scale(assets['vida=3'], (200, 200))
assets['vida=2'] = pygame.image.load('assets/img/vida2.png').convert_alpha()
assets['vida=2'] = pygame.transform.scale(assets['vida=2'], (200, 200))
assets['vida=1'] = pygame.image.load('assets/img/vida3.png').convert_alpha()
assets['vida=1'] = pygame.transform.scale(assets['vida=1'], (200, 200))
assets['eat_sound'] = pygame.mixer.Sound('assets/snd/eat_snd.mp3')
pygame.mixer.music.load('assets/snd/prnp_sndtrack.mp3')
pygame.mixer.music.set_volume(0.2)
clock = pygame.time.Clock()
FPS = 60

#Classes do Jogador
class Player(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.spritesl = []
        self.spritesr = []
        self.spritesr.append(pygame.image.load('assets/img/guitas_move_r-1.png').convert_alpha())
        self.spritesr.append(pygame.image.load('assets/img/guitas_move_r-2.png').convert_alpha())
        self.spritesr.append(pygame.image.load('assets/img/guitas_move_r-3.png').convert_alpha())
        self.spritesr.append(pygame.image.load('assets/img/guitas_move_r-4.png').convert_alpha())
        self.spritesl.append(pygame.image.load('assets/img/guitas_move_l-1.png').convert_alpha())
        self.spritesl.append(pygame.image.load('assets/img/guitas_move_l-2.png').convert_alpha())
        self.spritesl.append(pygame.image.load('assets/img/guitas_move_l-3.png').convert_alpha())
        self.spritesl.append(pygame.image.load('assets/img/guitas_move_l-4.png').convert_alpha())
        self.image = assets['player_r_img']
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
                self.image = assets['player_r_img']

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
        self.image = assets['bolinho_img']
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
        self.image = assets['refri_img']
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
        self.spritesr.append(pygame.image.load('assets/img/capivara_move_r-1.png').convert_alpha())
        self.spritesr.append(pygame.image.load('assets/img/capivara_move_r-2.png').convert_alpha())
        self.spritesl.append(pygame.image.load('assets/img/capivara_move_l-1.png').convert_alpha())
        self.spritesl.append(pygame.image.load('assets/img/capivara_move_l-2.png').convert_alpha())
        self.image = assets['capivara_r_img']
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
            self.image = assets['capivara_r_img']
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
        self.spritesr.append(pygame.image.load('assets/img/capivara_move_r-1.png').convert_alpha())
        self.spritesr.append(pygame.image.load('assets/img/capivara_move_r-2.png').convert_alpha())
        self.spritesl.append(pygame.image.load('assets/img/capivara_move_l-1.png').convert_alpha())
        self.spritesl.append(pygame.image.load('assets/img/capivara_move_l-2.png').convert_alpha())
        self.image = assets['capivara_r_img']
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
            self.image = assets['capivara_r_img']
            self.mask = pygame.mask.from_surface(self.image)

class CapivaraMoto(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.spritesl = []
        self.spritesr = []
        self.spritesr.append(pygame.image.load('assets/img/capivara_moto_r-1.png').convert_alpha())
        self.spritesr.append(pygame.image.load('assets/img/capivara_moto_r-2.png').convert_alpha())
        self.spritesl.append(pygame.image.load('assets/img/capivara_moto_l-1.png').convert_alpha())
        self.spritesl.append(pygame.image.load('assets/img/capivara_moto_l-2.png').convert_alpha())
        self.image = assets['capivaramoto_r_img']
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
            self.image = assets['capivara_r_img']
            self.mask = pygame.mask.from_surface(self.image)


# Desenhando as vidas
class Vidas(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['vida=3']
        self.rect = self.image.get_rect()
        self.rect.x = 900
        self.rect.y = 10
        self.vidas = 3 #contador de vidas

    # Muda imagem das vidas
    def update(self):
        if self.vidas == 3:
            self.image = assets['vida=3']
        elif self.vidas == 2:
            self.image = assets['vida=2']
        else:
            self.image = assets['vida=1']


def char_change(char_choose):
    player.spritesr = []
    player.spritesl = []
    if char_choose == 1:
        player.spritesr.append(pygame.image.load('assets/img/fer_move_r-1.png').convert_alpha())
        player.spritesr.append(pygame.image.load('assets/img/fer_move_r-2.png').convert_alpha())
        player.spritesr.append(pygame.image.load('assets/img/fer_move_r-3.png').convert_alpha())
        player.spritesr.append(pygame.image.load('assets/img/fer_move_r-4.png').convert_alpha())
        player.spritesl.append(pygame.image.load('assets/img/fer_move_l-1.png').convert_alpha())
        player.spritesl.append(pygame.image.load('assets/img/fer_move_l-2.png').convert_alpha())
        player.spritesl.append(pygame.image.load('assets/img/fer_move_l-3.png').convert_alpha())
        player.spritesl.append(pygame.image.load('assets/img/fer_move_l-4.png').convert_alpha())
        assets['player_r_img'] = pygame.image.load('assets/img/fer_r.png').convert_alpha()
        assets['player_r_img'] = pygame.transform.scale(assets['player_r_img'], (PLAYER_WIDTH, PLAYER_HEIGHT))
        assets['player_l_img'] = pygame.image.load('assets/img/fer_l.png').convert_alpha()
        assets['player_l_img'] = pygame.transform.scale(assets['player_l_img'], (PLAYER_WIDTH, PLAYER_HEIGHT))
    if char_choose == 2:
        player.spritesr.append(pygame.image.load('assets/img/Marlin_move_r-1.png').convert_alpha())
        player.spritesr.append(pygame.image.load('assets/img/Marlin_move_r-2.png').convert_alpha())
        player.spritesr.append(pygame.image.load('assets/img/Marlin_move_r-3.png').convert_alpha())
        player.spritesr.append(pygame.image.load('assets/img/Marlin_move_r-4.png').convert_alpha())
        player.spritesl.append(pygame.image.load('assets/img/Marlin_move_l-1.png').convert_alpha())
        player.spritesl.append(pygame.image.load('assets/img/Marlin_move_l-2.png').convert_alpha())
        player.spritesl.append(pygame.image.load('assets/img/Marlin_move_l-3.png').convert_alpha())
        player.spritesl.append(pygame.image.load('assets/img/Marlin_move_l-4.png').convert_alpha())
        assets['player_r_img'] = pygame.image.load('assets/img/Marlin_r.png').convert_alpha()
        assets['player_r_img'] = pygame.transform.scale(assets['player_r_img'], (PLAYER_WIDTH, PLAYER_HEIGHT))
        assets['player_l_img'] = pygame.image.load('assets/img/Marlin_l.png').convert_alpha()
        assets['player_l_img'] = pygame.transform.scale(assets['player_l_img'], (PLAYER_WIDTH, PLAYER_HEIGHT))
    if char_choose == 3:
        player.spritesr.append(pygame.image.load('assets/img/guitas_move_r-1.png').convert_alpha())
        player.spritesr.append(pygame.image.load('assets/img/guitas_move_r-2.png').convert_alpha())
        player.spritesr.append(pygame.image.load('assets/img/guitas_move_r-3.png').convert_alpha())
        player.spritesr.append(pygame.image.load('assets/img/guitas_move_r-4.png').convert_alpha())
        player.spritesl.append(pygame.image.load('assets/img/guitas_move_l-1.png').convert_alpha())
        player.spritesl.append(pygame.image.load('assets/img/guitas_move_l-2.png').convert_alpha())
        player.spritesl.append(pygame.image.load('assets/img/guitas_move_l-3.png').convert_alpha())
        player.spritesl.append(pygame.image.load('assets/img/guitas_move_l-4.png').convert_alpha())
        assets['player_r_img'] = pygame.image.load('assets/img/guitas_r.png').convert_alpha()
        assets['player_r_img'] = pygame.transform.scale(assets['player_r_img'], (PLAYER_WIDTH, PLAYER_HEIGHT))
        assets['player_l_img'] = pygame.image.load('assets/img/guitas_l.png').convert_alpha()
        assets['player_l_img'] = pygame.transform.scale(assets['player_l_img'], (PLAYER_WIDTH, PLAYER_HEIGHT))
    
all_sprites = pygame.sprite.Group()
all_bolinhos = pygame.sprite.Group()
all_capivaras = pygame.sprite.Group()
all_capivaras2 = pygame.sprite.Group()
all_refri = pygame.sprite.Group()
all_capivarasmoto = pygame.sprite.Group()

groups = {}
groups['all_bolinhos'] = all_bolinhos
groups['all_capivaras'] = all_capivaras
groups['all_capivaras2'] = all_capivaras2
groups['all_refris'] = all_refri
groups['all_capivarasmoto'] = all_capivarasmoto

player = Player(assets)
bolinho = Bolinho(assets)
capivara = Capivara(assets)
vida = Vidas(assets)
capivaramoto = CapivaraMoto(assets)


for i in range(2):
    bolinho = Bolinho(assets)
    all_sprites.add(bolinho)
    all_bolinhos.add(bolinho)

for i in range(2):
    capivara = Capivara(assets)
    all_sprites.add(capivara)
    all_capivaras.add(capivara)

all_sprites.add(player)
all_sprites.add(vida)

keys_down = {}

score = 0

game = True

DONE = 0
INIT = 1
INSTRUCTIONS = 2
CHOOSE = 3
FASE1 = 4
FASE2INST = 5
FASE2 = 6
FASE3INST = 7
FASE3 = 8
GAMEWON = 9
GAMEOVER = 10

init_rect = assets['background1'].get_rect()
init_count = 0
state = INIT

pygame.mixer.music.play(loops=-1)

while state != DONE:
    clock.tick(FPS)

    if state == INIT:
            # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    state = CHOOSE

        window.fill(BLACK)
        window.blit(assets['init_img'], init_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    if state == CHOOSE:
            # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
            if event.type == pygame.KEYDOWN:
                keys_down[event.key] = True
                if event.key == pygame.K_a:
                    char_choose = 1
                    char_change(char_choose)
                    state = INSTRUCTIONS
                if event.key == pygame.K_s:
                    char_choose = 2
                    char_change(char_choose)
                    state = INSTRUCTIONS
                if event.key == pygame.K_d:
                    char_choose = 3
                    char_change(char_choose)
                    state = INSTRUCTIONS

        window.fill(BLACK)
        window.blit(assets['charchoose_img'], init_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    if state == INSTRUCTIONS:
            # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    state = FASE1

        window.fill(BLACK)
        window.blit(assets['instructions_img'], init_rect)
        player.speedx = 0
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    if state == FASE1:
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera a velocidade.
                keys_down[event.key] = True
                if event.key == pygame.K_LEFT:
                    player.wleft = True
                    player.speedx -= 10
                if event.key == pygame.K_RIGHT:
                    player.wright = True
                    player.speedx += 10
                if event.key == pygame.K_UP:
                    if player.rect.y != HEIGHT - PLAYER_HEIGHT - 70:
                        pass
                    else:
                        player.jumping()

            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera a velocidade.
                if event.key in keys_down and keys_down[event.key]:
                    if event.key == pygame.K_LEFT:
                        player.wleft = False
                        player.speedx += 10
                        player.image = assets['player_l_img'] 
                    if event.key == pygame.K_RIGHT:
                        player.wright = False
                        player.speedx -= 10
                        player.image = assets['player_r_img'] 
                    if event.key == pygame.K_UP:
                        player.speedy = 10

        hits = pygame.sprite.spritecollide(player, all_bolinhos, True, pygame.sprite.collide_mask)
        if len(hits) == 1:
            assets['eat_sound'].play()
            score += 1
            bolinho = Bolinho(assets)
            all_sprites.add(bolinho)
            all_bolinhos.add(bolinho)
            if score % 10 == 0 and score != 0:
                refri = Refri(assets)
                all_sprites.add(refri)
                all_refri.add(refri)
        elif len(hits) == 2:
            score += 2
            for i in range(2):
                assets['eat_sound'].play()
                bolinho = Bolinho(assets)
                all_sprites.add(bolinho)
                all_bolinhos.add(bolinho)


        hits = pygame.sprite.spritecollide(player, all_capivaras, True, pygame.sprite.collide_mask)
        if len(hits) == 1:
            vida.vidas -= 1
            capivara = Capivara(assets)
            all_sprites.add(capivara)
            all_capivaras.add(capivara)
        elif len(hits) == 2:
            vida.vidas -= 1
            for i in range(2):
                capivara = Capivara(assets)
                all_sprites.add(capivara)
                all_capivaras.add(capivara)

        hits = pygame.sprite.spritecollide(player, all_refri, True, pygame.sprite.collide_mask)
        if len(hits) == 1:
            if vida.vidas == 3:
                vida.vidas = 3
            else:
                vida.vidas += 1

        if vida.vidas == 0:
            state = GAMEOVER

        if score == 20:
            for i in range(2):
                capivara2 = Capivara2(assets)
                all_sprites.add(capivara2)
                all_capivaras2.add(capivara2)
            all_sprites.remove(all_capivaras)
            state = FASE2INST

            # ----- Gera saídas
        window.fill((200, 200, 200))  # Preenche com a cor branca
        window.blit(assets['background1'],(0,0))

        text_surface = assets['score_font'].render("Pontos:{:01d}".format(score), True, (0, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)

        window.blit(text_surface, text_rect)
        all_sprites.draw(window)
        all_sprites.update()

        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador

    if state == FASE2INST:
            # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.rect.x = WIDTH / 2
                    player.rect.y = HEIGHT-60
                    player.wleft = False
                    player.wright = False 
                    player.speedx = 0 
                    vida.vidas = 3            
                    state = FASE2

        window.fill(BLACK)
        window.blit(assets['instructions2_img'], init_rect)
        player.speedx = 0
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    if state == FASE2:
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera a velocidade.
                keys_down[event.key] = True
                if event.key == pygame.K_LEFT:
                    player.wleft = True
                    player.speedx -= 10
                if event.key == pygame.K_RIGHT:
                    player.wright = True
                    player.speedx += 10
                if event.key == pygame.K_UP:
                    if player.rect.y != HEIGHT - PLAYER_HEIGHT - 70:
                        pass
                    else:
                        player.jumping()

            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera a velocidade.
                if event.key in keys_down and keys_down[event.key]:
                    if event.key == pygame.K_LEFT:
                        player.wleft = False
                        player.speedx += 10
                        player.image = assets['player_l_img'] 
                    if event.key == pygame.K_RIGHT:
                        player.wright = False
                        player.speedx -= 10
                        player.image = assets['player_r_img'] 
                    if event.key == pygame.K_UP:
                        player.speedy = 10

        hits = pygame.sprite.spritecollide(player, all_bolinhos, True, pygame.sprite.collide_mask)
        if len(hits) == 1:
            assets['eat_sound'].play()
            score += 1
            bolinho = Bolinho(assets)
            all_sprites.add(bolinho)
            all_bolinhos.add(bolinho)
            if score % 10 == 0 and score != 0:
                refri = Refri(assets)
                all_sprites.add(refri)
                all_refri.add(refri)
        elif len(hits) == 2:
            score += 2
            for i in range(2):
                assets['eat_sound'].play()
                bolinho = Bolinho(assets)
                all_sprites.add(bolinho)
                all_bolinhos.add(bolinho)

        hits = pygame.sprite.spritecollide(player, all_capivaras2, True, pygame.sprite.collide_mask)
        if len(hits) == 1:
            vida.vidas -= 1
            capivara2 = Capivara2(assets)
            all_sprites.add(capivara2)
            all_capivaras2.add(capivara2)
        elif len(hits) == 2:
            vida.vidas -= 1
            for i in range(2):
                capivara2 = Capivara2(assets)
                all_sprites.add(capivara2)
                all_capivaras2.add(capivara2)

        hits = pygame.sprite.spritecollide(player, all_refri, True, pygame.sprite.collide_mask)
        if len(hits) == 1:
            if vida.vidas == 3:
                vida.vidas = 3
            else:
                vida.vidas += 1

        if vida.vidas == 0:
            state = GAMEOVER

        if score == 40:
            capivaramoto = CapivaraMoto(assets)
            all_sprites.add(capivaramoto)
            all_capivarasmoto.add(capivaramoto)
            all_sprites.remove(all_capivaras2)
            state = FASE3INST

        # ----- Gera saídas
        window.fill((200, 200, 200))  # Preenche com a cor branca
        window.blit(assets['background2'],(0,0))

        text_surface = assets['score_font'].render("Pontos:{:01d}".format(score), True, (0, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)

        window.blit(text_surface, text_rect)
        all_sprites.draw(window)
        all_sprites.update()

        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador

    if state == FASE3INST:
            # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.rect.x = WIDTH / 2
                    player.rect.y = HEIGHT-60
                    player.wleft = False
                    player.wright = False 
                    vida.vidas = 3                 
                    state = FASE3

        window.fill(BLACK)
        window.blit(assets['instructions3_img'], init_rect)
        player.speedx = 0
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    if state == FASE3:
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera a velocidade.
                keys_down[event.key] = True
                if event.key == pygame.K_LEFT:
                    player.wleft = True
                    player.speedx -= 10
                if event.key == pygame.K_RIGHT:
                    player.wright = True
                    player.speedx += 10
                if event.key == pygame.K_UP:
                    if player.rect.y != HEIGHT - PLAYER_HEIGHT - 70:
                        pass
                    else:
                        player.jumping()

            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera a velocidade.
                if event.key in keys_down and keys_down[event.key]:
                    if event.key == pygame.K_LEFT:
                        player.wleft = False
                        player.speedx += 10
                        player.image = assets['player_l_img'] 
                    if event.key == pygame.K_RIGHT:
                        player.wright = False
                        player.speedx -= 10
                        player.image = assets['player_r_img'] 
                    if event.key == pygame.K_UP:
                        player.speedy = 10

        hits = pygame.sprite.spritecollide(player, all_bolinhos, True, pygame.sprite.collide_mask)
        if len(hits) == 1:
            assets['eat_sound'].play()
            score += 1
            bolinho = Bolinho(assets)
            all_sprites.add(bolinho)
            all_bolinhos.add(bolinho)
            if score % 10 == 0 and score != 0:
                refri = Refri(assets)
                all_sprites.add(refri)
                all_refri.add(refri)
        elif len(hits) == 2:
            score += 2
            for i in range(2):
                assets['eat_sound'].play()
                bolinho = Bolinho(assets)
                all_sprites.add(bolinho)
                all_bolinhos.add(bolinho)
            if score % 10 == 0 and score != 0:
                if vida.vidas == 3:
                    vida.vidas = 3
                else:
                    vida.vidas += 1

        hits = pygame.sprite.spritecollide(player, all_capivarasmoto, True, pygame.sprite.collide_mask)
        if len(hits) == 1:
            vida.vidas -= 1
            capivaramoto = CapivaraMoto(assets)
            all_sprites.add(capivaramoto)
            all_capivarasmoto.add(capivaramoto)

        hits = pygame.sprite.spritecollide(player, all_refri, True, pygame.sprite.collide_mask)
        if len(hits) == 1:
            if vida.vidas == 3:
                vida.vidas = 3
            else:
                vida.vidas += 1

        if vida.vidas == 0:
            state = GAMEOVER


        # ----- Gera saídas
        window.fill((200, 200, 200))  # Preenche com a cor branca
        window.blit(assets['background3'],(0,0))

        text_surface = assets['score_font'].render("Pontos:{:01d}".format(score), True, (0, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)

        window.blit(text_surface, text_rect)
        all_sprites.draw(window)
        all_sprites.update()

        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador

    elif state == GAMEOVER:
        vida.vidas = 3
        player.speedx = 0
        player.wleft = False
        player.wright = False
            # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    score = 0
                    vida.vidas = 3
                    all_sprites.remove(all_capivaras)
                    all_sprites.remove(all_capivaras2)
                    all_sprites.remove(all_capivarasmoto)
                    for i in range(2):
                        capiva = Capivara(assets)
                        all_sprites.add(capivara)
                        all_capivaras.add(capivara)
                    state = CHOOSE
        window.fill(BLACK)
        window.blit(assets['telafim_img'], init_rect)

        text_surface = assets['score_font'].render("Pontos obtidos:{:01d}".format(score), True, (0, 200, 255))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  50)
        window.blit(text_surface, text_rect)

        pygame.display.flip()
pygame.quit()