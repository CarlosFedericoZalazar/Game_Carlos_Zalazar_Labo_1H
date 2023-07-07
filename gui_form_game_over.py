import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_label import Label
from background import Background
from player import Player


class FormGameOver(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        self.static_background = Background(x=0,y=0,width=w,height=h,path="images\locations\set_bg_01\\forest\castillo.png")
        
        #self.master_surface = master_surface
        #self.tiempo_juego = Timer_level(master=self, x=1000, y=10, w=200, h=50, font="Comic Sans MS", font_size=50, font_color=C_WHITE, minutes=self.minuto_juego, seconds=self.segundos_juego)
        self.label_game_over = Label(master = self, x=ANCHO_VENTANA/2, y=ALTO_VENTANA/2, w=400, h=150,color_border=None, text=f"GAME OVER", font="Comic Sans MS", font_size=35, font_color=C_WHITE, image_background=None)
        self.personaje = Player(master=self, x=150,y=100,speed_walk=8,speed_run=12,gravity=14,jump_power=30,frame_rate_ms=100,move_rate_ms=50,jump_height=110,p_scale=0.5,interval_time_jump=300)
        self.personaje.animation = self.personaje.die_r
        self.personaje.frame_rate_ms = 1000
        self.end_animation = False
        
    def update(self, lista_eventos,keys,delta_ms):
        self.label_game_over.update()
        if(self.personaje.frame < len(self.personaje.animation) - 1 and not self.end_animation):
            self.personaje.do_animation(delta_ms)
        else: 
            self.end_animation = True
        
        
    def draw(self): 
        super().draw()
        self.static_background.draw(self.surface)
        
        self.label_game_over.draw()
        self.personaje.draw(self.surface)