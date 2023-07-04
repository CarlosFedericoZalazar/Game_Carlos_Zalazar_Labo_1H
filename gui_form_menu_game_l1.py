import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
from gui_label import Label
from player import Player
from enemigo import Enemy
from plataforma import Plataform
from background import Background
from bullet import Bullet
from coins import Coins
from timer import Timer_level


class FormGameLevel1(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        # --- GUI WIDGET --- 
        self.boton1 = Button(master=self,x=0,y=0,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.on_click_boton1,on_click_param="form_menu_B",text="BACK",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton2 = Button(master=self,x=200,y=0,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.on_click_boton1,on_click_param="form_menu_B",text="PAUSE",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton_shoot = Button(master=self,x=400,y=0,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.on_click_shoot,on_click_param="form_menu_B",text="BALA",font="Verdana",font_size=30,font_color=C_WHITE)

        #self.score_label = Label(master=self, x=1000, y=10, w=200, h=50, text=f"Score: {0}", font="Comic Sans MS", font_size=40, font_color=C_WHITE)

        self.pb_lives = ProgressBar(master=self,x=100,y=60,w=240,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Bars/Bar_Background01.png",image_progress="images/gui/set_gui_01/Comic_Border/Bars/Bar_Segment05.png",value = 5, value_max=5)
        self.widget_list = [self.boton1,self.boton2,self.pb_lives,self.boton_shoot]

        # --- GAME ELEMNTS --- 
        self.static_background = Background(x=0,y=0,width=w,height=h,path="images/locations/set_bg_01/forest/fondo_castillo.jpg")
        # --- COINS ---
        self.coin_list = []
        self.coin_list.append(Coins(master=self, x=400, y=550,value=100,frame_rate_ms=150, p_scale=0.3, delay_time_coin = 30))
        self.coin_list.append(Coins(master=self, x=600, y=550,value=150,frame_rate_ms=150, p_scale=0.3, delay_time_coin = 20))
        self.coin_list.append(Coins(master=self, x=50, y=350,value=250,frame_rate_ms=200, p_scale=0.4, delay_time_coin = 10))
        
        # TIMER
        self.minuto_juego = 3
        self.segundos_juego = 0
        self.tiempo_juego = Timer_level(master=self, x=1000, y=10, w=200, h=50, font="Comic Sans MS", font_size=50, font_color=C_WHITE, minutes=self.minuto_juego, seconds=self.segundos_juego)
        

        self.player_1 = Player(master=self, x=10,y=400,speed_walk=8,speed_run=12,gravity=14,jump_power=30,frame_rate_ms=100,move_rate_ms=50,jump_height=110,p_scale=0.1,interval_time_jump=300)

        self.enemy_list = []
        self.enemy_list.append (Enemy(x=815,y=320,speed_walk=3,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=30,jump_height=140,p_scale=0.08,interval_time_jump=300))
        self.enemy_list.append (Enemy(x=150,y=400,speed_walk=6,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,p_scale=0.08,interval_time_jump=300))

        self.plataform_list = []
        self.plataform_list.append(Plataform(x=500,y=500,width=50,height=50,type=0))
        self.plataform_list.append(Plataform(x=550,y=500,width=50,height=50,type=1))
        self.plataform_list.append(Plataform(x=600,y=500,width=50,height=50,type=2))

        self.plataform_list.append(Plataform(x=0,y=500,width=50,height=50,type=13))
        self.plataform_list.append(Plataform(x=50,y=500,width=50,height=50,type=13))
        self.plataform_list.append(Plataform(x=100,y=500,width=50,height=50,type=13))
        self.plataform_list.append(Plataform(x=150,y=500,width=50,height=50,type=14))

        #self.plataform_list.append(Plataform(x=150,y=450,width=50,height=50,type=14))  


        self.plataform_list.append(Plataform(x=400,y=500,width=50,height=50,type=12, motion=True, speed_move_x=1,speed_move_y=1, move_rate_ms=30))
        self.plataform_list.append(Plataform(x=450,y=500,width=50,height=50,type=14, motion=True, speed_move_x=1,speed_move_y=1, move_rate_ms=30))

        self.plataform_list.append(Plataform(x=750,y=550,width=50,height=50,type=12))
        self.plataform_list.append(Plataform(x=800,y=550,width=50,height=50,type=14))

        self.plataform_list.append(Plataform(x=750,y=360,width=50,height=50,type=12))
        self.plataform_list.append(Plataform(x=800,y=360,width=50,height=50,type=13))
        self.plataform_list.append(Plataform(x=850,y=360,width=50,height=50,type=13))
        self.plataform_list.append(Plataform(x=900,y=360,width=50,height=50,type=14))

        self.bullet_list = []



    def on_click_boton1(self, parametro):
        self.set_active(parametro)

    def on_click_shoot(self, parametro):
        # for enemy_element in self.enemy_list:
        #     self.bullet_list.append(Bullet(enemy_element, enemy_element.rect.centerx, enemy_element.rect.centery,self.player_1.rect.centerx,self.player_1.rect.centery,20,path="images/gui/set_gui_01/Comic_Border/Bars/Bar_Segment06.png",frame_rate_ms=100,move_rate_ms=20,width=10,height=10))
        pass
        if(self.player_1.direction == DIRECTION_R):
            self.bullet_list.append(Bullet(self.player_1, self.player_1.rect.centerx, self.player_1.rect.centery, ANCHO_VENTANA , self.player_1.rect.centery,20,path="images\caracters\players\caballero\SHOOT\SHOOT.png",frame_rate_ms=100,move_rate_ms=20,width=20,height=20))
        else:
            # Corregir la municion para que sea unico sentido!
            self.bullet_list.append(Bullet(self.player_1, self.player_1.rect.centerx, self.player_1.rect.centery, 0 , self.player_1.rect.centery,20,path="images\caracters\players\caballero\SHOOT\SHOOT.png",frame_rate_ms=100,move_rate_ms=20,width=20,height=20))
    
    

    def update(self, lista_eventos,keys,delta_ms):

        self.tiempo_juego.update(delta_ms)  # Timer del Juego

        for aux_widget in self.widget_list:
            aux_widget.update(lista_eventos)
        

        for bullet_element in self.bullet_list:
            bullet_element.update(delta_ms,self.plataform_list,self.enemy_list,self.player_1)

        for enemy_element in self.enemy_list:
            enemy_element.update(delta_ms,self.plataform_list)

        for plataform_element in self.plataform_list:
            if plataform_element.motion:
                plataform_element.update(delta_ms, self.enemy_list)
               
        
        # IMPLEMENTAR COINS
        for coin_element in self.coin_list:
            coin_element.update(delta_ms)
            coin_element.label_coin.update()

         
        
        self.player_1.events(delta_ms,keys, self.plataform_list)
        self.player_1.update(delta_ms,self.plataform_list, self.coin_list)
        
        self.pb_lives.value = self.player_1.lives

        self.player_1.label_score.update()
        # if self.player_1.score >10:
        #     #self.active = False
        #     self.set_active('form_game_L2')
             


    def draw(self): 
        super().draw()
        self.static_background.draw(self.surface)

        for aux_widget in self.widget_list:    
            aux_widget.draw()

        for plataforma in self.plataform_list:
            plataforma.draw(self.surface)

        for enemy_element in self.enemy_list:
            enemy_element.draw(self.surface)            
            if not enemy_element.alive and enemy_element.frame == 0:               
                self.enemy_list.pop(self.enemy_list.index(enemy_element))
                self.player_1.score += 100
                
        self.player_1.draw(self.surface)
        
        
        for bullet_element in self.bullet_list:
            bullet_element.draw(self.surface)
        
        for coin_element in self.coin_list:
            coin_element.draw(self.surface)
            coin_element.label_coin.draw()
        
        self.player_1.label_score.draw()

        self.tiempo_juego.lavel_timer.draw() # Timer del Juego


