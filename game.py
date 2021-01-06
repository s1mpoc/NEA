import pygame
pygame.font.init()
testfont = pygame.font.SysFont('Arial', 15)
testmsg = testfont.render('click here to quit', False, (255,0,0))
testmsg2= testfont.render('resume game', False, (255, 0, 0))
menumsg3= testfont.render('load game', False, (255,0,0))
menumsg4= testfont.render('save game', False, (255,0,0))
pygame.init()
screen = pygame.display.set_mode((1068, 720))
done = False
is_blue = True
ESCMENU = False
mouseheld = False
savegame = False
loadgame = False
am_to_mv = 3
x = 30
y = 30
position = [(484, 310), (584, 310), (584, 430), (484, 430)]
clock = pygame.time.Clock()
pygame.mouse.set_visible(1)
maingameon = True

while not done:
    mousepressed = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue
        if event.type == pygame.mouse.get_pressed():
            mousepressed = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            ESCMENU = not ESCMENU
            print(ESCMENU)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseheld = not mouseheld
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= am_to_mv
    if pressed[pygame.K_DOWN]: y += am_to_mv
    if pressed[pygame.K_LEFT]: x -= am_to_mv
    if pressed[pygame.K_RIGHT]: x += am_to_mv
    screen.fill((0, 0, 0))
    if is_blue:
        color = (0, 128, 255)
    else:
        color = (255, 100, 0)
    circle = pygame.draw.circle(screen, color, (x, y), 20)
    circlecollisiontest = pygame.draw.rect(screen, color, (200, 200, 50,50),5)
    circlecollisiontest2 = pygame.draw.rect(screen, color, (200, 400, 50,50),5)
    circlecollisiontest3 = pygame.draw.rect(screen, color, (200, 600, 50,50),60)
    mousepos = pygame.mouse.get_pos()
    if circle.collidepoint(mousepos):
        circle = pygame.draw.circle(screen, (55, 1, 25), (x, y), 20)
    if circle.collidepoint(mousepos) and mouseheld == True:
        (x, y) = mousepos
    if circlecollisiontest.collidepoint(x, y):
        print("success")
    if circlecollisiontest2.collidepoint(x, y):
        print("wrong answer")
    if circlecollisiontest3.collidepoint(x, y):
        print("wrong anwer")
    if ESCMENU == True:
        am_to_mv = 0
        test_qt_posx = 490
        test_qt_posy = 380
        test_qt2_posx = 490
        test_qt2_posy = 320
        menu_wipe_posx = 490
        menu_wipe_posy = 350
        screen.blit(menumsg3, (menu_wipe_posx, menu_wipe_posy))
        screen.blit(testmsg, (test_qt_posx, test_qt_posy))
        screen.blit(testmsg2, (test_qt2_posx, test_qt2_posy))
        screen.blit(menumsg4, (test_qt2_posx, test_qt2_posy + 85))
        tstmenu = pygame.draw.polygon(screen, (55, 1, 25), position , 5)
        txtqtborder = pygame.draw.rect(screen, (55, 55, 55), (test_qt_posx, test_qt_posy, 90, 21), 1)
        txtqt2border = pygame.draw.rect(screen, (55, 55, 55), (test_qt2_posx, test_qt2_posy, 90, 21), 1)
        menu_wipe_border = pygame.draw.rect(screen, (55, 55, 55), (menu_wipe_posx, menu_wipe_posy, 90, 21), 1)
        menumsg4border = pygame.draw.rect(screen, (55,55,55), (test_qt2_posx, test_qt2_posy + 85, 90, 21), 1)
        if txtqtborder.collidepoint(mousepos) and pygame.mouse.get_pressed()[0] == 1:
            pygame.quit()
        if txtqt2border.collidepoint(mousepos) and pygame.mouse.get_pressed() [0] == 1:
            ESCMENU = False
        if menumsg4border.collidepoint(mousepos) and pygame.mouse.get_pressed() [0] == 1:
            savegame = True
        if menu_wipe_border.collidepoint(mousepos) and pygame.mouse.get_pressed() [0] == 1:
            print("test")

        #if menu_wipe_border.collidepoint(mousepos) and mousepressed == True:
            #print("test")
    else:
        am_to_mv = 3
    pygame.display.flip()
    clock.tick(60)