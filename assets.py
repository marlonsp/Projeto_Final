from jogo_v10 import INSTRUCTIONS
import pygame
import os
from config import WIDTH, HEIGHT, PLAYER_HEIGHT, PLAYER_WIDTH, CAPIVARA_HEIGHT, CAPIVARAMOTO_WIDTH
    
BACKGROUND1 = 'background1'
BACKGROUND2 = 'background2'
BACKGROUND3 = 'background3'
CHARCHOOSE_IMG = 'charchoose_img'
INIT_IMG = 'init_img'
TELAFIM_IMG = 'telafim_img'
TELAWIN_IMG = 'telawin_img'
INSTRUCTIONS_IMG = 'instructions_img'
INSTRUCTIONS2_IMG = 'instructions2_img'
INSTRUCTIONS3_IMG = 'instructions3_img'
PLAYER_R_IMG = 'player_r_img'
PLAYER_L_IMG = 'player_l_img'
BOLINHO_IMG = 'bolinho_img'
REFRI_IMG = 'refri_img'
CAPIVARA_R_IMG = 'capivara_r_img'
CAPIVARA_L_IMG = 'capivara_l_img'
CAPIVARAMOTO_R_IMG = 'capivaramoto_r_img'
VIDA3 = 'vida=3'
VIDA2 = 'vida=2'
VIDA1 = 'vida=1'
EAT_SOUND = 'eat_sound'
HIT_SOUND = 'hit_sound'
DRINK_SOUND = 'drink_sound'
SAX_SOUND = 'sax_sound'
SCORE_FONT = 'score_font'

def load_assets():
    assets = {}
    assets[BACKGROUND1] = pygame.image.load(os.path.join(IMG_DIR, 'fundo1.png'))
    assets[BACKGROUND1] = pygame.transform.scale(assets['background1'], (WIDTH, HEIGHT))
    assets[BACKGROUND2] = pygame.image.load(os.path.join(IMG_DIR, 'fundo2.png'))
    assets[BACKGROUND2] = pygame.transform.scale(assets['background2'], (WIDTH, HEIGHT))
    assets[BACKGROUND3] = pygame.image.load(os.path.join(IMG_DIR, 'fundo3.png'))
    assets[BACKGROUND3] = pygame.transform.scale(assets['background3'], (WIDTH, HEIGHT))
    assets[CHARCHOOSE_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'char_choose.png')
    assets[CHARCHOOSE_IMG] = pygame.transform.scale(assets['charchoose_img'], (WIDTH, HEIGHT))
    assets[INIT_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'init_img.png'))
    assets[INIT_IMG] = pygame.transform.scale(assets['init_img'], (WIDTH, HEIGHT))
    assets[TELAFIM_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'telafim_img.png')
    assets[TELAFIM_IMG] = pygame.transform.scale(assets['telafim_img'], (WIDTH, HEIGHT))
    assets[TELAWIN_IMG ] = pygame.image.load(os.path.join(IMG_DIR, 'vitoria.png'))
    assets[TELAWIN_IMG ] = pygame.transform.scale(assets['telawin_img'], (WIDTH, HEIGHT))
    assets[INSTRUCTIONS_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'instructions_img.png')
    assets[INSTRUCTIONS_IMG] = pygame.transform.scale(assets['instructions_img'], (WIDTH, HEIGHT))
    assets[INSTRUCTIONS2_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'fase2start.png'))
    assets[INSTRUCTIONS2_IMG] = pygame.transform.scale(assets['instructions2_img'], (WIDTH, HEIGHT))
    assets[INSTRUCTIONS3_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'fase3start.png'))
    assets[INSTRUCTIONS3_IMG] = pygame.transform.scale(assets['instructions3_img'], (WIDTH, HEIGHT))
    assets[PLAYER_R_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'guitas_r.png')).convert_alpha()
    assets[PLAYER_R_IMG] = pygame.transform.scale(assets['player_r_img'], (PLAYER_WIDTH, PLAYER_HEIGHT))
    assets[PLAYER_L_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'guitas_l.png')).convert_alpha()
    assets[PLAYER_L_IMG] = pygame.transform.scale(assets['player_l_img'], (PLAYER_WIDTH, PLAYER_HEIGHT))
    assets[BOLINHO_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'bolinho_caipira.png')).convert_alpha()
    assets[BOLINHO_IMG] = pygame.transform.scale(assets['bolinho_img'], (60, 60))
    assets[REFRI_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'refri.png')).convert_alpha()
    assets[REFRI_IMG] = pygame.transform.scale(assets['refri_img'], (60, 60))
    assets[SCORE_FONT] = pygame.font.Font(os.path.join('lunchds.ttf', 50))
    assets[CAPIVARA_R_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'capivara_move_r-1.png')).convert_alpha()
    assets[CAPIVARA_R_IMG] = pygame.transform.scale(assets['capivara_r_img'], (CAPIVARA_WIDTH, CAPIVARA_HEIGHT))
    assets[CAPIVARA_L_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'capivara_move_l-1.png')).convert_alpha()
    assets[CAPIVARA_L_IMG] = pygame.transform.scale(assets['capivara_l_img'], (CAPIVARA_WIDTH, CAPIVARA_HEIGHT))
    assets[CAPIVARAMOTO_R_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'capivara_moto_r-1.png')).convert_alpha()
    assets[CAPIVARAMOTO_R_IMG] = pygame.transform.scale(assets['capivaramoto_r_img'], (CAPIVARA_WIDTH, CAPIVARA_HEIGHT))
    assets[VIDA3] = pygame.image.load(os.path.join(IMG_DIR, 'vida1.png')).convert_alpha()
    assets[VIDA3] = pygame.transform.scale(assets['vida=3'], (200, 200))
    assets[VIDA2] = pygame.image.load(os.path.join(IMG_DIR, 'vida2.png')).convert_alpha()
    assets[VIDA2] = pygame.transform.scale(assets['vida=2'], (200, 200))
    assets[VIDA1] = pygame.image.load(os.path.join(IMG_DIR, 'vida3.png')).convert_alpha()
    assets[VIDA1] = pygame.transform.scale(assets['vida=1'], (200, 200))
    assets[EAT_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'eat_snd.mp3'))
    assets[HIT_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'hit.wav'))
    pygame.mixer.Sound.set_volume(assets['hit_sound'], 0.7)
    assets[DRINK_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'drink_snd.wav'))
    pygame.mixer.Sound.set_volume(assets['drink_sound'], 0.2)
    assets[SAX_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'gameover.mp3'))
    pygame.mixer.music.load('assets/snd/prnp_sndtrack.mp3')
    pygame.mixer.music.set_volume(0.2)