import pygame
from auxiliar import Auxiliar
from constantes import *

class Trap():
    def __init__(self, x, y, frame_rate_ms=100, p_scale=1.2) -> None:
        self.stay_trap = Auxiliar.getSurfaceFromSeparateFiles("images\gui\Gui\TRAMPAS\{0}.png",0,7,scale=p_scale)

        self.frame = 0
        self.animation = self.stay_trap
        self.image = self.animation[self.frame]
        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0

    def update(self, delta_ms):
        self.do_animation(delta_ms)

    def draw(self,screen):
        
        if(DEBUG):
            pygame.draw.rect(screen,color=(0,0 ,0),rect=self.rect)          
           
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)

