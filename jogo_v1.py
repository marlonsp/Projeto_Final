import pygame

pygame.init()
WIDTH = 1080
HEIGHT = 607
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Jogo.v1')
teste = pygame.image.load('assets/img/player_test.png')
pygame.display.set_icon(teste)
# ----- Inicia assets
PLAYER_WIDTH = 30
PLAYER_HEIGHT = 30
font = pygame.font.SysFont(None, 48)
player_img = pygame.image.load('assets/img/player_test.png').convert_alpha()
player_img = pygame.transform.scale(player_img, (PLAYER_WIDTH, PLAYER_HEIGHT))

clock = pygame.time.Clock()
FPS = 60

class Player(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH / 2
        self.rect.y = HEIGHT / 2
        self.speedx = 0
        self.wleft = False #Verificar movimento p/ esquerda para iniciar animação
        self.wright = False #Verificar movimento p/ direita para iniciar animação
        self.wcount = 0 #Contagem p/ os frames do movimento

    def update(self):
        # Atualizando a posição
        self.rect.x += self.speedx
 
        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

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
                player.speedx -= 8
            if event.key == pygame.K_RIGHT:
                player.wright = True
                player.speedx += 8

        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key in keys_down and keys_down[event.key]:
                if event.key == pygame.K_LEFT:
                    player.speedx += 8
                if event.key == pygame.K_RIGHT:
                    player.speedx -= 8

    # ----- Gera saídas
    window.fill((200, 200, 200))  # Preenche com a cor branca
    all_sprites.draw(window)
    all_sprites.update()

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador
pygame.quit()