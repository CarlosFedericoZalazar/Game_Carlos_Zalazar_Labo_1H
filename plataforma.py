import pygame
from constantes import *
from auxiliar import Auxiliar


class Plataform:
    def __init__(self, x, y,width, height,  type=1, motion = False, speed_move = 0):
        plataformas = {}
        plat_bosque = self.image_list= Auxiliar.getSurfaceFromSeparateFiles("images/tileset/forest/Tiles/{0}.png",1,18,flip=False,w=width,h=height)
        plataformas['bosque'] = plat_bosque


        #self.image_list= Auxiliar.getSurfaceFromSeparateFiles("images/tileset/forest/Tiles/{0}.png",1,18,flip=False,w=width,h=height)
        self.image = plataformas['bosque'][type]
        #self.image = self.image_list[type]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(self.rect)
        self.ground_collition_rect = pygame.Rect(self.rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        # MOVIMIENTO
        self.speed_move =  speed_move
        self.move_x = 0
        self.move_y = 0
        self.contador = 0
        self.tiempo_transcurrido_move = 0 

    def draw(self,screen):
        screen.blit(self.image,self.rect)
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
        
    
    def change_x(self,delta_x):

        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.ground_collition_rect.x += delta_x


    def change_y(self,delta_y):
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y
    
    
    
    def do_movement(self,delta_ms,plataform_list):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0


        self.change_x(self.move_x)
        if self.contador <= 40: # CANTIDAD DE PASOS DEL MONSTRUO
            self.move_x = -self.speed_move            
            self.contador += 1 
        elif self.contador <= 80:
            self.move_x = self.speed_move            
            self.contador += 1
        else:
            self.contador = 0