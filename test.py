import pygame
class variables:
    screen = pygame.display.set_mode((1400, 1050))
    #screen.blit(BackGround.image, BackGround.rect)
    done = False
    north = False
    south = False
    east = False
    west = False
    centre = True
    am_to_mv = 3
    mouseheld = False
    cx = 30
    cy = 30
    cstyle = (55,55,55)
    clock = pygame.time.Clock()
    pygame.font.init()
    pygame.init()


