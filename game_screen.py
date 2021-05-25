import pygame
from config import FPS, WIDTH, HEIGHT, PLAYER_HEIGHT, PLAYER_WIDTH
from assets import load_assets, PLAYER_RIMG, PLAYER_LIMG
from sprites import Player

def game_screen(window):
    assets = load_assets()

    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    player = Player(assets[PLAYER_RIMG])
    all_sprites.add(player)

    keys_down = {}

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
                    player.speedx += 8
                    player.image = pygame.image.load('assets/img/Marlin_l.png').convert_alpha()
                    player.image = pygame.transform.scale(assets[PLAYER_LIMG], (PLAYER_WIDTH, PLAYER_HEIGHT))
                if event.key == pygame.K_RIGHT:
                    player.wright = False
                    player.speedx -= 8
                    player.image = pygame.image.load('assets/img/Marlin_r.png').convert_alpha()
                    player.image = pygame.transform.scale(assets[PLAYER_RIMG], (PLAYER_WIDTH, PLAYER_HEIGHT))
                if event.key == pygame.K_UP:
                    player.speedy = 10

    # ----- Gera saídas
    window.fill((200, 200, 200))  # Preenche com a cor branca
    all_sprites.draw(window)
    all_sprites.update()

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador