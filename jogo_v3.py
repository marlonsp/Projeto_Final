import pygame
import random

pygame.init()
WIDTH = 1080
HEIGHT = 607
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Jogo.v3')

BLACK = (0, 0, 0)

teste = pygame.image.load('assets/img/player_test.png')
pygame.display.set_icon(teste)
# ----- Inicia assets
PLAYER_WIDTH = 120
PLAYER_HEIGHT = 120
assets = {}
assets['background'] = pygame.image.load('assets/img/fundo1.png')
assets['background'] = pygame.transform.scale(assets['background'], (WIDTH, HEIGHT))
assets['init_img'] = pygame.image.load('assets/img/init_img.png')
assets['init_img'] = pygame.transform.scale(assets['init_img'], (WIDTH, HEIGHT))
assets['player_r_img'] = pygame.image.load('assets/img/fer_r.png').convert_alpha()
assets['player_r_img'] = pygame.transform.scale(assets['player_r_img'], (PLAYER_WIDTH, PLAYER_HEIGHT))
assets['player_l_img'] = pygame.image.load('assets/img/fer_l.png').convert_alpha()
assets['player_l_img'] = pygame.transform.scale(assets['player_l_img'], (PLAYER_WIDTH, PLAYER_HEIGHT))
assets['bolinho_img'] = pygame.image.load('assets/img/bolinho_caipira.png').convert_alpha()
assets['bolinho_img'] = pygame.transform.scale(assets['bolinho_img'], (60, 60))
assets["score_font"] = pygame.font.Font('assets/font/lunchds.ttf', 50)
assets['capivara_r_img'] = pygame.image.load('assets/img/capivara_r.png.png').convert_alpha()
assets['capivara_r_img'] = pygame.transform.scale(assets['player_r_img'], (PLAYER_WIDTH, PLAYER_HEIGHT))
assets['capivara_l_img'] = pygame.image.load('assets/img/capivara_l.png').convert_alpha()
assets['capivara_l_img'] = pygame.transform.scale(assets['player_l_img'], (PLAYER_WIDTH, PLAYER_HEIGHT))
clock = pygame.time.Clock()
FPS = 60

#Classes do Jogador
class Player(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.spritesl = []
        self.spritesr = []
        self.spritesr.append(pygame.image.load('assets/img/fer_move_r-1.png').convert_alpha())
        self.spritesr.append(pygame.image.load('assets/img/fer_move_r-2.png').convert_alpha())
        self.spritesr.append(pygame.image.load('assets/img/fer_move_r-3.png').convert_alpha())
        self.spritesr.append(pygame.image.load('assets/img/fer_move_r-4.png').convert_alpha())
        self.spritesl.append(pygame.image.load('assets/img/fer_move_l-1.png').convert_alpha())
        self.spritesl.append(pygame.image.load('assets/img/fer_move_l-2.png').convert_alpha())
        self.spritesl.append(pygame.image.load('assets/img/fer_move_l-3.png').convert_alpha())
        self.spritesl.append(pygame.image.load('assets/img/fer_move_l-4.png').convert_alpha())
        self.image = assets['player_l_img']
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
            if self.rect.y <= 250:
                self.jump = False
            self.rect.y -=20
 
        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT-50:
            self.rect.bottom = HEIGHT-50

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

all_sprites = pygame.sprite.Group()
all_bolinhos = pygame.sprite.Group()
groups = {}
groups['all_bolinhos'] = all_bolinhos

player = Player(assets)
bolinho = Bolinho(assets)

for i in range(2):
    bolinho = Bolinho(assets)
    all_sprites.add(bolinho)
    all_bolinhos.add(bolinho)

all_sprites.add(player)

keys_down = {}

score = 0

game = True

DONE = 0
INIT = 1
PLAYING = 2

init_rect = assets['background'].get_rect()

state = INIT

while state != DONE:
    clock.tick(FPS)

    if state == INIT:
            # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
            if event.type == pygame.KEYDOWN:
                state = PLAYING

        window.fill(BLACK)
        window.blit(assets['init_img'], init_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    if state == PLAYING:
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
                    if player.rect.y != HEIGHT - PLAYER_HEIGHT - 50:
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

        hits = pygame.sprite.spritecollide(player, all_bolinhos, True)
        if len(hits) == 1:
            score += 1
            bolinho = Bolinho(assets)
            all_sprites.add(bolinho)
            all_bolinhos.add(bolinho)
        elif len(hits) == 2:
            score += 2
            for i in range(2):
                bolinho = Bolinho(assets)
                all_sprites.add(bolinho)
                all_bolinhos.add(bolinho)
        


    # ----- Gera saídas
        window.fill((200, 200, 200))  # Preenche com a cor branca
        window.blit(assets['background'],(0,0))

        text_surface = assets['score_font'].render("Pontos:{:01d}".format(score), True, (0, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)

        window.blit(text_surface, text_rect)
        all_sprites.draw(window)
        all_sprites.update()

    # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador

    class inimigo(pygame.sprite.Sprite):
        def __init__(self, x, y, assets, end):
            pygame.sprite.Sprite.__init__(self)

            self.spritesl = []
            self.spritesr = []
            self.spritesr.append(pygame.image.load('assets/img/capivara_move_r-1.png').convert_alpha())
            self.spritesr.append(pygame.image.load('assets/img/capivara_move_r-2.png').convert_alpha())
            self.spritesr.append(pygame.image.load('assets/img/capivara_move_r-3.png').convert_alpha())
            self.spritesr.append(pygame.image.load('assets/img/capivara_move_r-4.png').convert_alpha())
            self.spritesl.append(pygame.image.load('assets/img/capivara_move_l-1.png').convert_alpha())
            self.spritesl.append(pygame.image.load('assets/img/capivara_move_l-2.png').convert_alpha())
            self.spritesl.append(pygame.image.load('assets/img/capivara_move_l-3.png').convert_alpha())
            self.spritesl.append(pygame.image.load('assets/img/capivara_move_l-4.png').convert_alpha())
            self.image = assets['capivara_l_img']
            self.mask = pygame.mask.from_surface(self.image)
            self.x = x
            self.y = y
            self.width = WIDTH
            self.height = HEIGHT
            self.end = end
            self.path = [self.x, self.end]
            self.walkCount = random.randint(1,66)
            self.vel = random.randint(-150,150)/100
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)

    def draw(self,win):
        self.move()  
        if self.walkCount + 1 >= 66:
            self.walkCount = 0
        if self.walkCount==48:
            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount //6], (self.x, self.y)
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount //6], (self.x, self.y))
                self.walkCount += 1
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
pygame.quit()