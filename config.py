from jogo_v3 import FPS
from os import path

IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')

#dimensões da tela
WIDTH = 1080
HEIGHT = 607
FPS = 60

#dimensões player
PLAYER_WIDTH = 30
PLAYER_HEIGHT = 30

# Estados para controle do fluxo da aplicação
# INIT = 0
GAME = 1
QUIT = 2