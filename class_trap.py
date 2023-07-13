import pygame
from auxiliar import Auxiliar
from constantes import *

class Trap():
    def __init__(self, x, y, frame_rate_ms=100, p_scale=1.2, trap_drope = False) -> None:
        self.stay_trap = Auxiliar.getSurfaceFromSeparateFiles("images\gui\Gui\TRAMPAS\{0}.png",0,7,scale=p_scale)

        self.frame = 0
        self.animation = self.stay_trap
        self.image = self.animation[self.frame]
        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_move = 60
        self.trap_drope = trap_drope
        self.tiempo_drop = 0


    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0

    def drop(self,delta_ms, plataforma_list):
        var_aux = 4
        for plataforma in plataforma_list:
            if self.rect.colliderect(plataforma.rect) or self.rect.y == GROUND_COLLIDE_H - self.rect.height:
                self.rect.y = plataforma.rect.y - self.rect.height
                #print('TRAMPA POSADA EN PLATAFORMA')
                break
        else:
            self.tiempo_drop += delta_ms
            if self.tiempo_drop >= 100:
                self.tiempo_drop = 0
                self.change_move += 2
                if self.change_move <= 250 and self.rect.x > 30:
                    var_aux *= -1
                elif self.change_move >= 500 or self.rect.x > 1370:
                    self.change_move = 0
                self.rect.x += var_aux        
                self.rect.y += 4

    def update(self, delta_ms):
        self.do_animation(delta_ms)

    def draw(self,screen):
        
        if(DEBUG):
            pygame.draw.rect(screen,color=(0,0 ,0),rect=self.rect)          
           
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)

