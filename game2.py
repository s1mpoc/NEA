#Initialisation
import pygame
import json
import test
screen = pygame.display.set_mode((1400, 1050))
mouseheld = False
cx = 30
cy = 30
cstyle = (55,55,55)
clock = pygame.time.Clock()
pygame.font.init()
pygame.init()
ESCMENU = False
mouseheld = False
savegame = False
loadgame = False
pygame.font.init()
testfont = pygame.font.SysFont('Arial', 15)
testmsg = testfont.render('click here to quit', False, (255,0,0))
testmsg2= testfont.render('resume game', False, (255, 0, 0))
menumsg3= testfont.render('load game', False, (255,0,0))
menumsg4= testfont.render('save game', False, (255,0,0))
position = [(484, 310), (584, 310), (584, 430), (484, 430)]
savegame = False
right = False
ri2 = False
#Background
class background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

BackGround = background('iuN1BL10V9.jpg', [0,0])

for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouseheld = not mouseheld
#JSON
js =[]
with open ("loadfiles.json", 'r') as tj:
    testfiles = json.load(tj)
print(testfiles.items())
for fileno, filename in testfiles.items():
    for x in filename:
    #js[i] = json.loads(open(str(js[i])))9
        with open (x, 'r') as tj2:
            js.append (json.load(tj2))
            if savegame == True:
                with open ("moretestdata.json", 'r') as tj3:
                    json.dump(savegame, tj3)

#with open ('loadfiles.json', 'r') as fp:
 #   jsd = json.dump(fp)

#main while loop
while not test.variables.done:
    mousepos = pygame.mouse.get_pos()
    test.variables.screen.fill((0,0,0))
    test.variables.screen.blit(BackGround.image, BackGround.rect)
    mousepressed = False
#event loop
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
    #pygame.draw.rect(screen, (55,55,55), (500, 600, 50, 50), 1)
#Creating borders
    for i in js[0]["startmenu"]["buttons"]:
        pygame.draw.rect(test.variables.screen, (55,55,55), (i["x"], i["y"], i["h"], i["w"]), 1)
    for i in js[0]["sectborder"]["positions"]:
        line = pygame.draw.line(test.variables.screen, i["bcol"], i["stpnt"], i["endpnt"], 10)
    pressed = pygame.key.get_pressed()
#Creating sprite
    circle = pygame.draw.circle(test.variables.screen, (test.variables.cstyle), (test.variables.cx, test.variables.cy), 15)
#Border collision
    '''if test.variables.cx + test.variables.am_to_mv == circle.colliderect(line) and pressed[pygame.K_RIGHT]:
        test.variables.cx = test.variables.cx
    else:
        if pressed[pygame.K_DOWN]: test.variables.cy += test.variables.am_to_mv

    if test.variables.cx - test.variables.am_to_mv == circle.colliderect(line) and pressed[pygame.K_UP]:
        test.variables.cx = test.variables.cx
    else:
        if pressed[pygame.K_UP]: test.variables.cy -= test.variables.am_to_mv

    if test.variables.cy + test.variables.am_to_mv == circle.colliderect(line) and pressed[pygame.K_DOWN]:
        test.variables.cy = test.variables.cy
    else:
        if pressed[pygame.K_RIGHT]: test.variables.cx += test.variables.am_to_mv

    if test.variables.cy - test.variables.am_to_mv == circle.colliderect(line) and pressed[pygame.K_LEFT]:
        print("test")
        test.variables.cy = test.variables.cy -3
    else:
        if pressed[pygame.K_LEFT]: test.variables.cx -= test.variables.am_to_mv'''
    if 20 <= test.variables.cx <= 1400 and 1042 <= test.variables.cy + 1 <= 1045 and pressed[pygame.K_DOWN]:
        test.variables.cy = test.variables.cy
    else:
        if pressed[pygame.K_DOWN]: test.variables.cy += test.variables.am_to_mv

    if 20 <= test.variables.cx <= 1400 and 25 <= test.variables.cy + 1 <= 27 and pressed[pygame.K_UP]:
        test.variables.cy = test.variables.cy
    else:
        if pressed[pygame.K_UP]: test.variables.cy -= test.variables.am_to_mv

    if 10 <= test.variables.cx <= 15 and 10 <= test.variables.cy + 1 <= 1050 and pressed[pygame.K_LEFT]:
        test.variables.cy = test.variables.cy
    else:
        if pressed[pygame.K_LEFT]: test.variables.cx -= test.variables.am_to_mv

    if 1300 <= test.variables.cx <= 1350 and 10 <= test.variables.cy + 1 <= 1050 and pressed[pygame.K_RIGHT]:
        test.variables.cy = test.variables.cy
    else:
        if pressed[pygame.K_RIGHT]: test.variables.cx += test.variables.am_to_mv


    print(test.variables.cx,test.variables.cy)

    if ESCMENU == True:
    #Button Position Variables
        test_qt_posx = 490
        test_qt_posy = 380
        test_qt2_posx = 490
        test_qt2_posy = 320
        menu_wipe_posx = 490
        menu_wipe_posy = 350
    #Bliting button text to screen
        screen.blit(menumsg3, (menu_wipe_posx, menu_wipe_posy))
        screen.blit(testmsg, (test_qt_posx, test_qt_posy))
        screen.blit(testmsg2, (test_qt2_posx, test_qt2_posy))
        screen.blit(menumsg4, (test_qt2_posx, test_qt2_posy + 85))
    #Creating menu border
        tstmenu = pygame.draw.polygon(screen, (55, 1, 25), position , 5)
    #Creating button borders
        txtqtborder = pygame.draw.rect(screen, (55, 55, 55), (test_qt_posx, test_qt_posy, 90, 21), 1)
        txtqt2border = pygame.draw.rect(screen, (55, 55, 55), (test_qt2_posx, test_qt2_posy, 90, 21), 1)
        menu_wipe_border = pygame.draw.rect(screen, (55, 55, 55), (menu_wipe_posx, menu_wipe_posy, 90, 21), 1)
        menumsg4border = pygame.draw.rect(screen, (55,55,55), (test_qt2_posx, test_qt2_posy + 85, 90, 21), 1)
    #Button press interaction
        if txtqtborder.collidepoint(mousepos) and pygame.mouse.get_pressed()[0] == 1:
            pygame.QUIT()
        if txtqt2border.collidepoint(mousepos) and pygame.mouse.get_pressed() [0] == 1:
            ESCMENU = False
        if menumsg4border.collidepoint(mousepos) and pygame.mouse.get_pressed() [0] == 1:
            savegame = True
        if menu_wipe_border.collidepoint(mousepos) and pygame.mouse.get_pressed() [0] == 1:
            loadgame = True
    pygame.display.flip()
    test.variables.clock.tick(60)

#print(mousepos)
"awp neo noir min wear,ak wasteland reble ft, the empress ft, awp wildfire ft, the emperor mw"
#Load settings (JSON)

#Start menu
#while startmenu == True:
	#New game
	#Load game
	#Settings
#Quit

#Def savegame
	#Check current variable and boolean values
	#Compare to JSON file variable and boolean values
	#Replace values that are outdated

#Def loadgame
	#Show Save game list
	#Select save game
	#Load coresponding JSON file
	#Load start game

#Def New game
	#Load start game

#Def Settings
	#Display current settings
	#Get setting updates
	#Validate setting updates
	#Save setting updates

#Def Start Game
	#Start main loop
	 	#Draw background
		#Draw player
		#Draw interactable objects
		#Loop for pygame events
			#Movement
				#Player collide
			#Interact
				#Mouse down
				#Mouse collide
				#Keydown
					#Escape menu
					#Save Menu
					#Questions/puzzles
		#Update Display
	#End main loop
