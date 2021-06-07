from os import path

# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'snd')
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'font')

# Dados gerais do jogo.
WIDTH = 1100 # Largura da tela
HEIGHT = 600 # Altura da tela
FPS = 60 # Frames por segundo

# Define tamanhos
PLAYER_WIDTH = 120
PLAYER_HEIGHT = 120

CAPIVARA_WIDTH = 120
CAPIVARA_HEIGHT = 100

CAPIVARAMOTO_WIDTH = 220
CAPIVARAMOTO_HEIGHT = 220

# Define algumas variáveis com as cores básicas
BLACK = (0, 0, 0)

# Estados para controle do fluxo da aplicação
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