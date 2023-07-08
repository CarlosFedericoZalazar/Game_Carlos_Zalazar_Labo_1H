import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_label import Label
from background import Background
from player import Player
from class_file import File


class FormGameOver(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        self.static_background = Background(x=0,y=0,width=w,height=h,path="images\locations\set_bg_01\\forest\castillo.png")
        
        #self.master_surface = master_surface
        #self.tiempo_juego = Timer_level(master=self, x=1000, y=10, w=200, h=50, font="Comic Sans MS", font_size=50, font_color=C_WHITE, minutes=self.minuto_juego, seconds=self.segundos_juego)
        self.label_game_over = Label(master = self, x=ANCHO_VENTANA/2, y=80, w=400, h=150,color_border=None, text=f"GAME OVER", font="Comic Sans MS", font_size=35, font_color=C_WHITE, image_background=None)
        self.personaje = Player(master=self, x=150,y=20,speed_walk=8,speed_run=12,gravity=14,jump_power=30,frame_rate_ms=80,move_rate_ms=50,jump_height=110,p_scale=0.5,interval_time_jump=300)
        self.personaje.animation = self.personaje.die_r
        self.personaje.frame_rate_ms = 1000
        self.end_animation = False

        self.label_score_1 = Label(master = self, x=ANCHO_VENTANA/2, y=200, w=400, h=150,color_border=None, text=f"1 - SCORE  COSME FULANITO", font="Comic Sans MS", font_size=20, font_color=C_WHITE, image_background=None)
        self.label_score_2 = Label(master = self, x=ANCHO_VENTANA/2, y=220, w=400, h=150,color_border=None, text=f"1 - SCORE  COSME FULANITO", font="Comic Sans MS", font_size=20, font_color=C_WHITE, image_background=None)
        self.label_score_3 = Label(master = self, x=ANCHO_VENTANA/2, y=240, w=400, h=150,color_border=None, text=f"1 - SCORE  COSME FULANITO", font="Comic Sans MS", font_size=20, font_color=C_WHITE, image_background=None)
        self.label_score_4 = Label(master = self, x=ANCHO_VENTANA/2, y=260, w=400, h=150,color_border=None, text=f"1 - SCORE  COSME FULANITO", font="Comic Sans MS", font_size=20, font_color=C_WHITE, image_background=None)
        self.label_score_5 = Label(master = self, x=ANCHO_VENTANA/2, y=280, w=400, h=150,color_border=None, text=f"1 - SCORE  COSME FULANITO", font="Comic Sans MS", font_size=20, font_color=C_WHITE, image_background=None)
        self.list_labels_score = [self.label_score_1,self.label_score_2,self.label_score_3,self.label_score_4,self.label_score_5]
        self.file_score = File('data_game')
        
    def update(self, lista_eventos,keys,delta_ms):
        
        self.file_score.read_file()
        self.label_game_over.update()

        # self.label_score_1._text = self.file_score.list_players[0]['name']
        # self.label_score_2._text = self.file_score.list_players[1]['name']
        # self.label_score_3._text = self.file_score.list_players[2]['name']
        # self.label_score_4._text = self.file_score.list_players[3]['name']
        # self.label_score_5._text = self.file_score.list_players[4]['name']

        index = 0
        try:
            for label_score in self.list_labels_score:
                label_score._text = '{0} Score: {1}'.format(self.file_score.list_players[index]['name'],
                                                            self.file_score.list_players[index]['score'])
                index += 1

        except IndexError:
            print("Índice fuera de rango. No hay suficientes elementos en la lista.")
            label_score._text = ''


        for label_score in self.list_labels_score:
            label_score.update()

        if(self.personaje.frame < len(self.personaje.animation) - 1 and not self.end_animation):
            self.personaje.do_animation(delta_ms)
        else: 
            self.end_animation = True

        
        
    def draw(self): 
        super().draw()
        self.static_background.draw(self.surface)
        
        for label_score in self.list_labels_score:
            label_score.draw()

        self.label_game_over.draw()
        self.personaje.draw(self.surface)