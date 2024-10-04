import pygame

class MenuController:
    def __init__(self):
        pygame.init()

    def structureObjSize(self, obj, width, height): #Scale object to screen size

        original_width, original_height = obj.get_size()

        scale_factor = min(width / original_width, height / original_height)

        new_width = int(original_width * scale_factor)
        new_height = int(original_height * scale_factor)

        obj = pygame.transform.scale(obj, (new_width, new_height))

        return obj
    def setCentre(self, obj, width, height, screen, moveX=0, moveY=0):

        obj_width, obj_height = obj.get_size()
        
        screen.blit(obj, (((width - obj_width) // 2) + moveX, ((height - obj_height) // 2) + moveY))

        return screen