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
        self.label_game_over = Label(master = self, x=ANCHO_VENTANA/2, y=20, w=400, h=150,color_border=None, text=f"GAME OVER", font="Comic Sans MS", font_size=35, font_color=C_WHITE, image_background=None)
        self.personaje = Player(master=self, x=150,y=20,speed_walk=8,speed_run=12,gravity=14,jump_power=30,frame_rate_ms=80,move_rate_ms=50,jump_height=110,p_scale=0.5,interval_time_jump=300)
        self.personaje.animation = self.personaje.die_r
        self.personaje.frame_rate_ms = 1000
        self.end_animation = False

        self.label_score_1 = Label(master = self, x=780, y=125, w=600, h=100,color_border=None, text=f"EMPTY", font="Comic Sans MS", font_size=25, font_color=C_WHITE, image_background=None)
        self.label_score_2 = Label(master = self, x=780, y=180, w=600, h=100,color_border=None, text=f"EMPTY", font="Comic Sans MS", font_size=25, font_color=C_WHITE, image_background=None)
        self.label_score_3 = Label(master = self, x=780, y=230, w=600, h=100,color_border=None, text=f"EMPTY", font="Comic Sans MS", font_size=25, font_color=C_WHITE, image_background=None)
        self.label_score_4 = Label(master = self, x=780, y=285, w=600, h=100,color_border=None, text=f"EMPTY", font="Comic Sans MS", font_size=25, font_color=C_WHITE, image_background=None)
        self.label_score_5 = Label(master = self, x=780, y=340, w=600, h=100,color_border=None, text=f"EMPTY", font="Comic Sans MS", font_size=25, font_color=C_WHITE, image_background=None)
        self.last_label_score = Label(master = self, x=200, y=20, w=600, h=120,color_border=None, text=f"", font="Comic Sans MS", font_size=25, font_color=C_WHITE, image_background=None)
        self.list_labels_score = [self.label_score_1,self.label_score_2,self.label_score_3,self.label_score_4,self.label_score_5]
        self.file_score = File('data_game')
        self.time_to_refresh = 0
        self.numbers = []
        for number in range(4):
            self.numbers.append(pygame.image.load('images\gui\Gui\\numbers\{0}.png'.format(number)))
        
        
    def update(self, lista_eventos,keys,delta_ms):          

        self.file_score.read_file()
        self.last_label_score._text = self.file_score.list_players[-1]['text']
        self.label_game_over.update()
        self.last_label_score.update()
        index = 0
        self.file_score.order_list_file()
        try:
            for label_score in self.list_labels_score:
                label_score._text = '{0}'.format(self.file_score.file_sort_players[index]['text'])
                index += 1

        except IndexError:
            print("Índice fuera de rango. No hay suficientes elementos en la lista.")
            label_score._text = ''


        for label_score in self.list_labels_score:
            label_score.update()

        if(self.personaje.frame < len(self.personaje.animation) - 1 and not self.end_animation):
            self.personaje.do_animation(delta_ms)
            print(self.personaje.frame)
        else: 
            self.end_animation = True            

        if(keys[pygame.K_SPACE]):
            self.active = False
            self.end_animation = False
            self.personaje.frame = 0
            self.set_active('form_menu_A')
        
        
    def draw(self): 
        super().draw()
        self.static_background.draw(self.surface)
        
        for label_score in self.list_labels_score:
            label_score.draw()

        self.last_label_score.draw()
        self.label_game_over.draw()
        self.personaje.draw(self.surface)