import os
import pygame
from modules.structureClasses import MenuController
from modules.structureClasses import ManualObjects

pygame.init()
SIZEH, SIZEW = 920, 1360

min_width, min_height = 500, 800

MC = MenuController()
screen = pygame.display.set_mode([SIZEW, SIZEH], pygame.RESIZABLE, vsync=1)  # Screen properties
pygame.display.set_caption('BEASTARS')

menuBG = pygame.image.load(r'assets/Background/Preview1.png')
menuBG_obj = MC.structureBGSize(menuBG, SIZEW, SIZEH)

MO = ManualObjects()
startBtn = MO.button(50, "START", r'assets/Font/Fonstars-4Bo0p.otf')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.VIDEORESIZE:
            menuBG_obj = MC.structureBGSize(menuBG, event.w, event.h)

            # if event.w < min_width or event.h < min_height:
            #     width = max(event.w, min_width)
            #     height = max(event.h, min_height)
            #     screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

    CURRENTW, CURRENTH = pygame.display.get_window_size()

    screen = MC.setCentre(menuBG_obj, CURRENTW, CURRENTH, screen)

    startBtn['surf'].blit(startBtn['text'], startBtn['textRect']) #set text in btn surface
    screen = MC.setObjCoordIncludeScale(screen, CURRENTW, CURRENTH, startBtn['surf'], 90, 10)

    pygame.display.flip()

pygame.quit()
