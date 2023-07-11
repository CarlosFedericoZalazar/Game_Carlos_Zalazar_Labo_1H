import pygame
from auxiliar import Auxiliar
from constantes import *


class Life():
    def __init__(self, x,y,p_scale=1) -> None:        
        
        self.image_life = pygame.image.load('images\gui\Gui\\vida.png')
        self.image_life = pygame.transform.scale(self.image_life, (60,60))
        # RECTANGULO
        self.rect = self.image_life.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.value = 1
    
    def update(self,delta_ms):       
        self.do_animation(delta_ms)
        self.label_coin._text = self.change_value(delta_ms)        


    def draw(self,screen):

        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.rect)
   
        screen.blit(self.image_life,self.rect)