import pygame
import random
from os import path
from assets import INSTRUCTIONS2_IMG

from config import IMG_DIR, BLACK, FPS, GAME, QUIT

def init_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background = assets[INSTRUCTIONS3_IMG]
    background_rect = background.get_rect()

    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        
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

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        player.speedx = 0
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state