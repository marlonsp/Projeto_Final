import pygame
import os
from config import PLAYER_HEIGHT, PLAYER_WIDTH, IMG_DIR

PLAYER_LIMG = 'player_limg'
PLAYER_RIMG = 'player_rimg'
PLAYER_LWALK = 'player_lwalk'
PLAYER_RWALK = 'player_rwalk'

def load_assets():
    assets = {}
    assets[PLAYER_LIMG] = pygame.image.load('assets/img/Marlin_l.png').convert_alpha() #alterar para cada jogador
    assets[PLAYER_RIMG] = pygame.image.load('assets/img/Marlin_r.png').convert_alpha() #alterar para cada jogador
    player_lanim = []
    for i in range(4): #alterar para cada jogador
        filename = os.path.join(IMG_DIR, 'Marlin_move_l-{}.png'.format(i))
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (PLAYER_WIDTH, PLAYER_HEIGHT))
        player_lanim.append(img)
    assets[PLAYER_LWALK] = player_lanim
    player_ranim = []
    for i in range(4): #alterar para cada jogador
        filename = os.path.join(IMG_DIR, 'Marlin_move_r-{}.png'.format(i))
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (PLAYER_WIDTH, PLAYER_HEIGHT))
        player_lanim.append(img)
    assets[PLAYER_RWALK] = player_ranim