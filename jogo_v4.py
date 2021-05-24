# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
from config import WIDTH, HEIGHT, GAME, QUIT
# from init_screen import init_screen
from game_screen import game_screen

pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Jogo V4')

state = GAME
while state != QUIT:
    if state == GAME:
        state = game_screen(window)
    else:
        state = QUIT

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados