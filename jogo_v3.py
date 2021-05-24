import pygame

pygame.init()
WIDTH = 1080
HEIGHT = 607
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Jogo.v3')
teste = pygame.image.load('assets/img/player_test.png')
pygame.display.set_icon(teste)
# ----- Inicia assets
PLAYER_WIDTH = 30
PLAYER_HEIGHT = 30
font = pygame.font.SysFont(None, 48)
player_img = pygame.image.load('assets/img/Marlin_r.png').convert_alpha()
player_img = pygame.transform.scale(player_img, (PLAYER_WIDTH, PLAYER_HEIGHT))

clock = pygame.time.Clock()
FPS = 60

class Player(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.spritesl = []
        self.spritesr = []
        self.spritesr.append(pygame.image.load('assets/img/Marlin_move_r-1.png').convert_alpha())
        self.spritesr.append(pygame.image.load('assets/img/Marlin_move_r-2.png').convert_alpha())
        self.spritesr.append(pygame.image.load('assets/img/Marlin_move_r-3.png').convert_alpha())
        self.spritesr.append(pygame.image.load('assets/img/Marlin_move_r-4.png').convert_alpha())
        self.spritesl.append(pygame.image.load('assets/img/Marlin_move_l-1.png').convert_alpha())
        self.spritesl.append(pygame.image.load('assets/img/Marlin_move_l-2.png').convert_alpha())
        self.spritesl.append(pygame.image.load('assets/img/Marlin_move_l-3.png').convert_alpha())
        self.spritesl.append(pygame.image.load('assets/img/Marlin_move_l-4.png').convert_alpha())
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH / 2
        self.rect.y = HEIGHT / 2
        self.speedx = 0
        self.speedy = 10
        self.wleft = False #Verificar movimento p/ esquerda para iniciar animação
        self.wright = False #Verificar movimento p/ direita para iniciar animação
        self.wcount = 0 #Contagem p/ os frames do movimento
        self.jump = False #Verificr se está pulando

    def update(self):
        #imagem parado
        if self.wright and self.wleft:
            self.image = player_img
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
                self.image = player_img

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

# class (pygame.sprite.Sprite):

all_sprites = pygame.sprite.Group()
player = Player(player_img)
all_sprites.add(player)
keys_down = {}

game = True

while game:
    clock.tick(FPS)
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            keys_down[event.key] = True
            if event.key == pygame.K_LEFT:
                player.wleft = True
                player.speedx -= 16
            if event.key == pygame.K_RIGHT:
                player.wright = True
                player.speedx += 16
            if event.key == pygame.K_UP:
                if player.rect.y != HEIGHT - PLAYER_HEIGHT:
                    pass
                else:
                    player.jumping()

        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key in keys_down and keys_down[event.key]:
                if event.key == pygame.K_LEFT:
                    player.wleft = False
                    player.speedx += 16
                    player_img = pygame.image.load('assets/img/Marlin_l.png').convert_alpha()
                    player_img = pygame.transform.scale(player_img, (PLAYER_WIDTH, PLAYER_HEIGHT))
                if event.key == pygame.K_RIGHT:
                    player.wright = False
                    player.speedx -= 16
                    player_img = pygame.image.load('assets/img/Marlin_r.png').convert_alpha()
                    player_img = pygame.transform.scale(player_img, (PLAYER_WIDTH, PLAYER_HEIGHT))
                if event.key == pygame.K_UP:
                    player.speedy = 10

    # ----- Gera saídas
    window.fill((200, 200, 200))  # Preenche com a cor branca
    all_sprites.draw(window)
    all_sprites.update()

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador
pygame.quit()