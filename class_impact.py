import pygame
from auxiliar import Auxiliar

class Impact():
    def __init__(self, x, y, type, frame_rate_ms=100, p_scale=1.2) -> None:
        #self.efect = {}
        #self.efect = Auxiliar.getSurfaceFromSeparateFiles("images\efects\BLOOD\{0}.png",0,4,scale=p_scale)
        self.efect = Auxiliar.getSurfaceFromSeparateFiles("images\efects\IMPACTO\{0}.png",0,7,scale=p_scale)
        
        self.frame = 0
        self.animation = self.efect
        self.image = self.animation[self.frame]
        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.impact = False
        self.end_animation = False

    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0
                self.end_animation = True

    def update(self, delta_ms):
        self.do_animation(delta_ms)

    
    def draw(self,screen):
        screen.blit(self.image,self.rect)