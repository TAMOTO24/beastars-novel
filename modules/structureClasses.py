import pygame

class MenuController:
    def __init__(self):
        pygame.init()

    def structureBGSize(self, obj, width, height): #Scale object to screen size

        original_width, original_height = obj.get_size()

        scale_factor = min(width / original_width, height / original_height)

        self.new_width = int(original_width * scale_factor)
        self.new_height = int(original_height * scale_factor)

        obj = pygame.transform.scale(obj, (self.new_width, self.new_height))

        return obj
    def setCentre(self, obj, width, height, screen):

        obj_width, obj_height = obj.get_size()
        
        screen.blit(obj, (((width - obj_width) // 2), ((height - obj_height) // 2)))

        return screen
    def setObjCoordIncludeScale(self, screen, width, height, obj, moveX=0, moveY=0):
        x = width - self.new_width
        y = height - self.new_height

        if moveX > 0:
            moveX =  int(self.new_width * moveX//100) # procent of width
        if moveY > 0:
            moveY =  int(self.new_height * moveY//100) # procent of height

        screen.blit(obj, (((x//2) + moveX) - obj.get_width(), ((y//2) + moveY) - obj.get_height())) # set coord 0,0 including screen scale (and add user X, Y to move on screen)

        return screen

class ManualObjects:
    def __init__(self):
        pygame.init()
    def button(self, TXTsize, text="button text", fontPath="Arial"):
        font = pygame.font.Font(fontPath, TXTsize)
        text = font.render(text, 1, (0, 0, 0))
        
        button_surface = pygame.Surface((200, 50), pygame.SRCALPHA)

        text_rect = text.get_rect(
            center=(button_surface.get_width() /2, 
            button_surface.get_height()/2))

        button_rect = pygame.Rect(125, 125, 150, 50)

        return {'text': text,'textRect' : text_rect, 'btn' : button_rect, 'surf' : button_surface}


    