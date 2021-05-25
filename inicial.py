import pygame
import random
from os import path
from jogo_v4 import window
from config import FPS, WIDTH, HEIGHT, GAME, QUIT, IMG_DIR
BLACK = (0, 0, 0)
def tela_inicial(window):
    clock = pygame.time.Clock()
    background = pygame.image.load(path.join('assets/img/up.png'))
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
            running = False

            if event.type == pygame.KEYUP:
                state = GAME
                running = False

        window.fill(BLACK)
        window.blit(background, (0,0))
        
        pygame.display.flip()

    return state
