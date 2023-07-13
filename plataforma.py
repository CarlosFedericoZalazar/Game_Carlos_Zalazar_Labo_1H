import pygame
from constantes import *
from auxiliar import Auxiliar

class Plataform:
    def __init__(self, x, y,width, height,  type=1, motion = False, speed_move_x = 0, speed_move_y = 0, move_rate_ms=0, style_tile='castle'):
        aux_number_frame_top = 0
        if style_tile == 'forest' or style_tile == 'castle':
            aux_number_frame_top = 17
        elif style_tile == 'dark_forest':
            aux_number_frame_top = 15
   
        
        self.image_list = Auxiliar.getSurfaceFromSeparateFiles(f"images/tileset/{style_tile}/"+"{0}.png",0,aux_number_frame_top,flip=False,w=width,h=height)
        #plat_castle = self.image_list= Auxiliar.getSurfaceFromSeparateFiles(f"images/tileset/{style_tile}/{0}.png",0,15,flip=False,w=width,h=height)
        # plataformas['bosque_verde'] = plat_bosque_verde
        # plataformas['bosque_oscuro'] = plat_bosque_oscuro
        # plataformas['castle'] = plat_castle


        #self.image_list= Auxiliar.getSurfaceFromSeparateFiles("images/tileset/forest/Tiles/{0}.png",1,18,flip=False,w=width,h=height)
        self.image = self.image_list[type]
        #self.image = self.image_list[type]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(self.rect)
        self.ground_collition_rect = pygame.Rect(self.rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H + 5
        # MOVIMIENTO
        self.motion = motion
        self.speed_move_x =  speed_move_x
        self.speed_move_y = speed_move_y
        self.move_x = 0
        self.move_y = 0
        self.contador = 0
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms 

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
    
    
    
    def do_movement(self,delta_ms, enemy_list):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0


        self.change_x(self.move_x)
        if self.contador <= 300: 
            self.move_x = -self.speed_move_x            
            self.contador += 1 
        elif self.contador <= 600:
            self.move_x = self.speed_move_x            
            self.contador += 1
        else:
            self.contador = 0
        self.change_y(self.move_y)
        if self.contador <= 300: 
            self.move_y = -self.speed_move_y            
            self.contador += 1 
        elif self.contador <= 600:
            self.move_y = self.speed_move_y            
            self.contador += 1
        else:
            self.contador = 0
    
    def update(self, delta_ms, enemy_list):
        self.do_movement(delta_ms, enemy_list)
        #self.draw()