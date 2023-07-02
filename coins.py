import pygame
from constantes import *
from auxiliar import Auxiliar
from gui_label import Label

class Coins:
    def __init__(self, master, x,y,value, frame_rate_ms,p_scale=1) -> None:
        
        
        self.coins = Auxiliar.getSurfaceFromSeparateFiles(PATH_COINS + '{0}.png',0,9,flip=False,scale=p_scale)
        
        self.coin_value = value
        self.text_value = str(self.coin_value)
        
        self.label_coin = Label(master, x - 12, y -8, w=50, h=50, color_background=None, color_border=None, text=self.text_value,font="Comic Sans MS", font_size=15, font_color=C_BLACK)

        #ANIMACION
        self.animation = self.coins
        self.frame = 0
        self.image = self.animation[self.frame]
        self.tiempo_transcurrido_animation = 0

        # RECTANGULO
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.frame_rate_ms = frame_rate_ms


    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
                #print(self.frame)
            else: 
                self.frame = 0
    
    def update(self,delta_ms):
        self.do_animation(delta_ms)

    def draw(self,screen):

        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.rect)

        self.image = self.animation[self.frame]
        
        screen.blit(self.image,self.rect)