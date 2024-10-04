import os
import pygame
from modules.structureClasses import MenuController

pygame.init()
SIZEH, SIZEW = 920, 1360

mc = MenuController()
screen = pygame.display.set_mode([SIZEW, SIZEH], pygame.RESIZABLE, vsync=1)  # Screen properties
pygame.display.set_caption('BEASTARS')

menuBG = pygame.image.load(r'assets/Background/Preview1.png')
menuBG = mc.structureObjSize(menuBG, SIZEW, SIZEH)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.VIDEORESIZE:
            menuBG = mc.structureObjSize(menuBG, event.w, event.h)

    CURRENTW, CURRENTH = pygame.display.get_window_size()

    screen = mc.setCentre(menuBG, CURRENTW, CURRENTH, screen)

    pygame.display.flip()

pygame.quit()
