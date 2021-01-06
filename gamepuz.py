import pygame
import os
import time
import math
pygame.init()
clock1 = pygame.time.Clock()
mousepos1 = pygame.mouse.get_pos()
screen1 = pygame.display.set_mode((800, 400))
pygame.mouse.set_visible(1)
done = False
savegame = False
x = 45
y = 45
am_to_mov = 3
colour = (55, 55, 55)
mousepressed1 = False
interact = False
testobj1 = pygame.draw.rect(screen1, (colour), (200, 200, 50, 50), 0)
testobj2 = pygame.draw.rect(screen1, (colour), (200, 300, 50, 50), 0)
testobj3 = pygame.draw.rect(screen1, (colour), (200, 100, 50, 50), 0)
testcorrect1 = pygame.draw.rect(screen1, (80, 80, 80), (350, 200, 135, 50), 0)
Correct = False
Incorrect = False
pygame.font.init()
testfont = pygame.font.SysFont('Arial', 20)
fontques = pygame.font.SysFont('Arial', 60)
testmsg = testfont.render('CORRECT', False, (255,0,0))
wrngans = testfont.render('INCORRECT', False, (255,0,0))
ans1 = testfont.render('"5x^5"', False, (255, 0, 0))
ans2 = testfont.render("25x^4", False, (255, 0, 0))
ans3 = testfont.render("x^6", False, (255, 0, 0))
ques = testfont.render("differentiate 5x^5", False, (255, 0, 0))
droptxt = testfont.render("drop answer here", False, (255, 0, 0))
diagram = 'testdiagram.PNG'

while not done:
    screen1.fill((0, 0, 0))
    circle = pygame.draw.circle(screen1, (55, 55, 55), (x, y), 20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.mouse.get_pressed():
            mousepressed1 = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
            interact = not interact
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= am_to_mov
    if pressed[pygame.K_DOWN]: y += am_to_mov
    if pressed[pygame.K_LEFT]: x -= am_to_mov
    if pressed[pygame.K_RIGHT]: x += am_to_mov

    if interact == True and testobj1.collidepoint(x, y):
        testobj1.center = circle.center
    if interact == True and testobj2.collidepoint(x, y):
        testobj2.center = circle.center
    if interact == True and testobj3.collidepoint(x, y):
        testobj3.center = circle.center
    if testobj3.collidepoint(testcorrect1.x, testcorrect1.y) and interact == False:
        Correct = True
    else:
        Correct = False
    if testobj2.collidepoint(testcorrect1.x, testcorrect1.y) and interact == False:
        Incorrect = True
    else:
        Incorrect = False
    if testobj1.collidepoint(testcorrect1.x, testcorrect1.y) and interact == False:
        Incorrect = True
    else:
        Incorrect = False
    if Correct == True:
        screen1.blit(testmsg, (250,200))
        savegame = True
    if Incorrect == True:
        screen1.blit(wrngans, (250,200))
        pygame.display.flip()
        time.sleep(5)
        done = True

    pygame.draw.rect(screen1, (55, 55, 55), testobj3)
    pygame.draw.rect(screen1, (55, 55, 55), testobj2)
    pygame.draw.rect(screen1, (55, 55, 55), testobj1)
    pygame.draw.rect(screen1, (100, 100, 100), testcorrect1)
    screen1.blit(ans3, (testobj2.x, testobj2.y))
    screen1.blit(ans1, (testobj1.x, testobj1.y))
    screen1.blit(ans2, (testobj3.x, testobj3.y))
    screen1.blit(ques, (50,50))
    screen1.blit(droptxt, (testcorrect1.x, testcorrect1.y))
    dg = pygame.image.load(os.path.join(diagram))
    screen1.blit(dg, (500,100))

    pygame.display.flip()
    clock1.tick(60)
    pygame.display.update()