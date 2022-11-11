import pygame 

from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, RESET

FONT_STYLE = 'freesansbold.ttf'
black_color = (0,0,0)

def get_score_element(points):
    font = pygame.font.Font(FONT_STYLE, 22)
    text = font.render('points: ' + str(points), True, black_color)
    text_rect = text.get_rect()
    text_rect.center = (1000, 50)
    return text, text_rect              #Regresamos el texto y el rectangulo donde mostramos el texto

def get_centred_message(message, width = SCREEN_WIDTH // 2, height = SCREEN_HEIGHT // 2):
    font = pygame.font.Font(FONT_STYLE, 30)
    text = font.render(message, True, black_color)
    text_rect = text.get_rect()
    text_rect.center = (width, height)
    return text, text_rect
