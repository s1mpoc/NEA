import pygame
from MorsifyModule import game
screen = pygame.display.set_mode((1068, 720))
testfont = pygame.font.SysFont('Helvicta', 17)
testmsg = testfont.render('click here to quit', False, (255,0,0))
mousepos = pygame.mouse.get_pos()
position = [(484, 310), (584, 310), (584, 410), (484, 410)]
class button_var:
    def escmenu(self):
            test_qt_posx = 490
            test_qt_posy = 390
            screen.blit(testmsg, (test_qt_posx, test_qt_posy))
            tstmenu = pygame.draw.polygon(screen, (55, 1, 25), position, 5)
            txtqtborder = pygame.draw.rect(screen, (55, 55, 55), (test_qt_posx, test_qt_posy, 90, 13), 1)
            if txtqtborder.collidepoint(mousepos) and pygame.mouse.get_pressed()[0] == 1:
                pygame.quit()