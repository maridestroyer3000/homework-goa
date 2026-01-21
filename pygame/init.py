import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((700, 450))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

sky_surface = pygame.image.load('pygame/bg/Cat space background (1).jpg').convert()
ground_surface = pygame.image.load('pygame/bg/Cat space background (1).jpg').convert()
text_surface = test_font.render('vampire cat', False, 'White')
char_surface = pygame.image.load('pygame/character/vampire-cat.png').convert_alpha()
char_x_pos = 600

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (280, 50))
    char_x_pos -= 10
    if char_x_pos < -1000: char_x_pos = 800
    if char_x_pos < -1000: char_x_pos = 800
    screen.blit(char_surface, (char_x_pos,0))

    # draw all our elements
    # display everything
    pygame.display.update()
    clock.tick(60)