import pygame
class escmenu:
    if ESCMENU == True:
        am_to_mv = 0
        # Button Position Variables
        test_qt_posx = 490
        test_qt_posy = 380
        test_qt2_posx = 490
        test_qt2_posy = 320
        menu_wipe_posx = 490
        menu_wipe_posy = 350
        # Bliting button text to screen
        screen.blit(menumsg3, (menu_wipe_posx, menu_wipe_posy))
        screen.blit(testmsg, (test_qt_posx, test_qt_posy))
        screen.blit(testmsg2, (test_qt2_posx + 10, test_qt2_posy))
        # Creating menu border
        tstmenu = pygame.draw.polygon(screen, (55, 1, 25), position, 5)
        # Creating button borders
        txtqtborder = pygame.draw.rect(screen, (55, 55, 55), (test_qt_posx, test_qt_posy, 90, 21), 1)
        txtqt2border = pygame.draw.rect(screen, (55, 55, 55), (test_qt2_posx, test_qt2_posy, 90, 21), 1)
        menu_wipe_border = pygame.draw.rect(screen, (55, 55, 55), (menu_wipe_posx, menu_wipe_posy, 90, 21), 1)
        # Button press occurnce
        if txtqtborder.collidepoint(mousepos) and pygame.mouse.get_pressed()[0] == 1:
            pygame.quit()
        if txtqt2border.collidepoint(mousepos) and pygame.mouse.get_pressed()[0] == 1:
            ESCMENU = False

        # if menu_wipe_border.collidepoint(mousepos) and pygame.mouse.get_pressed() [0] == 1:

    else:
        am_to_mv = 3

