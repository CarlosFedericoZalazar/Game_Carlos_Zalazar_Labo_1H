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
from class_file import File
from class_life import Life
from class_trap import Trap
import random
from auxiliar_player import save_data_player
from nivel import level_1

class FormGameLevel1(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)
        #dict_level_1 = level_1()
        # --- GUI WIDGET --- 
        self.boton1 = Button(master=self,x=0,y=0,w=140,h=50,color_background=None,color_border=None,image_background="images\gui\Gui\Buttom.png",on_click=self.on_click_boton1,on_click_param="form_menu_B",text="RESET",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton2 = Button(master=self,x=200,y=0,w=140,h=50,color_background=None,color_border=None,image_background="images\gui\Gui\Buttom.png",on_click=self.on_click_boton1,on_click_param="form_menu_B",text="PAUSE",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton_shoot = Button(master=self,x=400,y=0,w=140,h=50,color_background=None,color_border=None,image_background="images\gui\Gui\Buttom.png",on_click=self.on_click_shoot,on_click_param="form_menu_B",text="",font="Verdana",font_size=30,font_color=C_WHITE)
        self.restart = True
        self.pb_lives = ProgressBar(master=self,x=1100,y=80,w=240,h=50,color_background=None,color_border=None,image_background=None,image_progress="images\gui\Gui\\vida.png",value = 5, value_max=5)
        self.widget_list = [self.boton1,self.boton2,self.pb_lives,self.boton_shoot]
        # FILE GAME
        self.file_game_score = File('data_game')
        # --- GAME ELEMNTS --- 
        self.static_background = Background(x=0,y=0,width=w,height=h,path="images/locations/set_bg_01/forest/bosque_tenebroso.png")
        # --- COINS ---
        self.coin_list = []
        self.coin_list.append(Coins(master=self, x=400, y=450,value=100,frame_rate_ms=200, p_scale=0.4, delay_time_coin = 30))
        self.coin_list.append(Coins(master=self, x=1050, y=450,value=150,frame_rate_ms=200, p_scale=0.4, delay_time_coin = 20))
        self.coin_list.append(Coins(master=self, x=50, y=250,value=250,frame_rate_ms=200, p_scale=0.4, delay_time_coin = 10))
        self.coin_list.append(Coins(master=self, x=550, y=300,value=400,frame_rate_ms=200, p_scale=0.4, delay_time_coin = 10))
        self.coin_list.append(Coins(master=self, x=950, y=350,value=200,frame_rate_ms=200, p_scale=0.4, delay_time_coin = 0))
        self.coin_list.append(Coins(master=self, x=750, y=350,value=200,frame_rate_ms=200, p_scale=0.4, delay_time_coin = 0))
        self.coin_list.append(Coins(master=self, x=300, y=250,value=200,frame_rate_ms=200, p_scale=0.4, delay_time_coin = 0))
        self.number_of_stars = len(self.coin_list)
        # TIMER
        self.minuto_juego = TIME_GAME_MINUTES
        self.segundos_juego = TIME_GAME_SECONDS
        self.tiempo_juego = Timer_level(master=self, x=1000, y=10, w=200, h=50, font="Comic Sans MS", font_size=50, font_color=C_WHITE, minutes=self.minuto_juego, seconds=self.segundos_juego)
        self.time_enemy_shoot = 0
        # LIFES
        self.list_lifes = []
        self.list_lifes.append(Life(x=200,y=400))
        self.list_lifes.append(Life(x=1250,y=350))
        self.player_1 = Player(master=self, x=INIT_POSITION_PLAYER_X,y=INIT_POSITION_PLAYER_Y,speed_walk=8,speed_run=12,gravity=14,jump_power=30,frame_rate_ms=100,move_rate_ms=50,jump_height=110,p_scale=0.1,interval_time_jump=300)
        self.pb_lives.value = self.player_1.lives
        # TRAMPAS
        self.list_trap=[]
        self.list_trap.append(Trap(x=400,y=600,p_scale=1, frame_rate_ms=200))
        self.list_trap.append(Trap(x=600,y=600,p_scale=1, frame_rate_ms=200))
        # ENEMIGOS
        self.enemy_list = []
        self.enemy_list.append (Enemy(master=self,x=30,y=400,speed_walk=3,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=30,jump_height=140,p_scale=0.08,interval_time_jump=300, shoot=False, steps=20))
        #self.enemy_list.append (Enemy(master=self,x=1250,y=500,speed_walk=6,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,p_scale=0.08,interval_time_jump=300, shoot=True, steps=10))
        self.enemy_list.append (Enemy(master=self,x=700,y=100,speed_walk=6,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,p_scale=0.08,interval_time_jump=300, shoot=False, steps=50))
        self.enemy_list.append (Enemy(master=self,x=859,y=200,speed_walk=6,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,p_scale=0.08,interval_time_jump=300, shoot=False, steps=30))
        
        self.plataform_list = []

        # PLATAFORMAS
        # PLATAFORMA SUELO
        for aux in range(0,1400,50):
            self.plataform_list.append(Plataform(x=aux,y=650,width=50,height=50,type=1, style_tile='dark_forest'))        
        # PLATAFORMA 1
        self.plataform_list.append(Plataform(x=0,y=500,width=50,height=50,type=13, style_tile='dark_forest'))
        self.plataform_list.append(Plataform(x=50,y=500,width=50,height=50,type=13, style_tile='dark_forest'))
        self.plataform_list.append(Plataform(x=100,y=500,width=50,height=50,type=13, style_tile='dark_forest'))
        self.plataform_list.append(Plataform(x=150,y=500,width=50,height=50,type=13, style_tile='dark_forest'))
        self.plataform_list.append(Plataform(x=200,y=500,width=50,height=50,type=13, style_tile='dark_forest'))
        self.plataform_list.append(Plataform(x=250,y=500,width=50,height=50,type=14, style_tile='dark_forest'))
        # PLATAFORMA 2
        self.plataform_list.append(Plataform(x=350,y=550,width=50,height=50,type=12, style_tile='dark_forest'))
        self.plataform_list.append(Plataform(x=400,y=550,width=50,height=50,type=14, style_tile='dark_forest'))
        # PLATAFORMA 3
        self.plataform_list.append(Plataform(x=700,y=500,width=50,height=50,type=12, style_tile='dark_forest'))
        self.plataform_list.append(Plataform(x=750,y=500,width=50,height=50,type=13, style_tile='dark_forest'))
        self.plataform_list.append(Plataform(x=800,y=500,width=50,height=50,type=13, style_tile='dark_forest'))
        self.plataform_list.append(Plataform(x=850,y=500,width=50,height=50,type=14, style_tile='dark_forest')) 
        # PLATAFORMA 4
        self.plataform_list.append(Plataform(x=1000,y=550,width=50,height=50,type=12, style_tile='dark_forest'))
        self.plataform_list.append(Plataform(x=1050,y=550,width=50,height=50,type=14, style_tile='dark_forest'))
        # PLATAFORMA 5
        self.plataform_list.append(Plataform(x=1350,y=500,width=50,height=50,type=13, style_tile='dark_forest'))
        self.plataform_list.append(Plataform(x=1300,y=500,width=50,height=50,type=13, style_tile='dark_forest'))
        self.plataform_list.append(Plataform(x=1250,y=500,width=50,height=50,type=13, style_tile='dark_forest'))
        self.plataform_list.append(Plataform(x=1200,y=500,width=50,height=50,type=13, style_tile='dark_forest'))
        self.plataform_list.append(Plataform(x=1150,y=500,width=50,height=50,type=12, style_tile='dark_forest'))
        # PLATAFORMA 6
        self.plataform_list.append(Plataform(x=0,y=350,width=50,height=50,type=13, style_tile='dark_forest'))
        self.plataform_list.append(Plataform(x=50,y=350,width=50,height=50,type=13, style_tile='dark_forest'))
        self.plataform_list.append(Plataform(x=100,y=350,width=50,height=50,type=14, style_tile='dark_forest'))
        # PLATAFORMA 7
        self.plataform_list.append(Plataform(x=250,y=350,width=50,height=50,type=12, style_tile='dark_forest'))
        self.plataform_list.append(Plataform(x=300,y=350,width=50,height=50,type=14, style_tile='dark_forest'))
        # PLATAFORMA 8
        self.plataform_list.append(Plataform(x=400,y=400,width=50,height=50,type=12, style_tile='dark_forest'))
        self.plataform_list.append(Plataform(x=450,y=400,width=50,height=50,type=13, style_tile='dark_forest'))
        self.plataform_list.append(Plataform(x=500,y=400,width=50,height=50,type=13, style_tile='dark_forest'))
        self.plataform_list.append(Plataform(x=550,y=400,width=50,height=50,type=13, style_tile='dark_forest'))
        self.plataform_list.append(Plataform(x=600,y=400,width=50,height=50,type=14, style_tile='dark_forest'))
        # PLATAFORMA 9
        self.plataform_list.append(Plataform(x=750,y=250,width=50,height=50,type=12, style_tile='dark_forest'))
        self.plataform_list.append(Plataform(x=800,y=250,width=50,height=50,type=13, style_tile='dark_forest'))
        self.plataform_list.append(Plataform(x=850,y=250,width=50,height=50,type=13, style_tile='dark_forest'))
        self.plataform_list.append(Plataform(x=900,y=250,width=50,height=50,type=14, style_tile='dark_forest'))
        # PLATAFORMA 10
        self.plataform_list.append(Plataform(x=1350,y=350,width=50,height=50,type=13, style_tile='dark_forest'))
        self.plataform_list.append(Plataform(x=1300,y=350,width=50,height=50,type=13, style_tile='dark_forest'))
        self.plataform_list.append(Plataform(x=1250,y=350,width=50,height=50,type=13, style_tile='dark_forest'))
        self.plataform_list.append(Plataform(x=1200,y=350,width=50,height=50,type=12, style_tile='dark_forest'))
        # PLATAFORMA 11
        self.plataform_list.append(Plataform(x=400,y=250,width=50,height=50,type=12, style_tile='dark_forest'))
        self.plataform_list.append(Plataform(x=450,y=250,width=50,height=50,type=13, style_tile='dark_forest'))
        self.plataform_list.append(Plataform(x=500,y=250,width=50,height=50,type=14, style_tile='dark_forest'))


        self.bullet_list = []


    def on_click_boton1(self, parametro):
        self.set_active(parametro)

    def on_click_shoot(self, parametro):
        #for enemy_element in self.enemy_list:
             #self.bullet_list.append(Bullet(enemy_element, enemy_element.rect.centerx, enemy_element.rect.centery,self.player_1.rect.centerx,self.player_1.rect.centery,20,path="images/gui/set_gui_01/Comic_Border/Bars/Bar_Segment06.png",frame_rate_ms=100,move_rate_ms=20,width=10,height=10))
        #pass
        if(self.player_1.direction == DIRECTION_R):
            print('DISPARO HACIA LA DERECHA')
            self.bullet_list.append(Bullet(self.player_1, self.player_1.rect.centerx, self.player_1.rect.centery, ANCHO_VENTANA , self.player_1.rect.centery,20,path="images\caracters\players\caballero\SHOOT\SHOOT.png",frame_rate_ms=100,move_rate_ms=20,width=20,height=20))
        else:
            # Corregir la municion para que sea unico sentido!
            self.bullet_list.append(Bullet(self.player_1, self.player_1.rect.centerx, self.player_1.rect.centery, 0 , self.player_1.rect.centery,20,path="images\caracters\players\caballero\SHOOT\SHOOT.png",frame_rate_ms=100,move_rate_ms=20,width=20,height=20))
    
    def enemy_shoot(self, indice):   
        if self.enemy_list[indice].can_shoot and self.enemy_list[indice].alive:
            print('DISPARO DEL MONSTRUO')
            self.bullet_list.append(Bullet(self.enemy_list[indice], self.enemy_list[indice].rect.centerx, self.enemy_list[indice].rect.centery,self.player_1.rect.centerx,self.player_1.rect.centery,20,path="images\gui\Gui\Bar_Segment02.png",frame_rate_ms=200,move_rate_ms=20,width=10,height=10))

    def player_shoot(self, delta_ms):
        self.player_1.time_to_shoot += delta_ms
        if self.player_1.time_to_shoot >= 250 or self.player_1.time_to_shoot == 0:
            self.player_1.time_to_shoot = 0
            if(self.player_1.direction == DIRECTION_R):
                print('DISPARO HACIA LA DERECHA')
                self.bullet_list.append(Bullet(self.player_1, self.player_1.rect.centerx, self.player_1.rect.centery, ANCHO_VENTANA , self.player_1.rect.centery,20,path="images\caracters\players\caballero\SHOOT\SHOOT.png",frame_rate_ms=100,move_rate_ms=20,width=20,height=20))
            else:
                self.bullet_list.append(Bullet(self.player_1, self.player_1.rect.centerx, self.player_1.rect.centery, 0 , self.player_1.rect.centery,20,path="images\caracters\players\caballero\SHOOT\SHOOT.png",frame_rate_ms=100,move_rate_ms=20,width=20,height=20))
    
    def restart_all_list(self):
        self.enemy_list.clear()
        self.coin_list.clear()
        self.list_lifes.clear()

    
    def restart_game(self):
        if self.restart:
            #REINICIAMOS ENEMIGOS:
            #self.enemy_list = []            
            #self.enemy_list.append (Enemy(master=self,x=30,y=400,speed_walk=3,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=30,jump_height=140,p_scale=0.08,interval_time_jump=300, shoot=False, steps=40))
            #self.enemy_list.append (Enemy(master=self,x=500,y=500,speed_walk=6,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,p_scale=0.08,interval_time_jump=300, shoot=False, steps=10))
            #REINICIAMOS TIEMPO DE PARTIDA
            self.tiempo_juego.minutes = TIME_GAME_MINUTES
            self.tiempo_juego.seconds = TIME_GAME_SECONDS
            #REINICIAMOS AL PLAYER
            self.pb_lives.value = self.player_1.lives
            self.player_1.lives = PLAYER_LIFE
            self.player_1.score = 0
            self.player_1.rect.x = INIT_POSITION_PLAYER_X
            self.player_1.rect.y = INIT_POSITION_PLAYER_Y
            for side in self.player_1.sides:
                self.player_1.sides[side].x = INIT_POSITION_PLAYER_X
                self.player_1.sides[side].y = INIT_POSITION_PLAYER_Y
            self.player_1.sides['left'].x += 20
            self.player_1.sides['right'].x += 100 
            self.player_1.sides['bottom'].y = INIT_POSITION_PLAYER_Y + self.player_1.rect.height - GROUND_COLLIDE_H
            self.player_1.sides['bottom'].height = GROUND_COLLIDE_H
            
            #self.enemy_list.append (Enemy(master=self,x=30,y=400,speed_walk=3,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=30,jump_height=140,p_scale=0.08,interval_time_jump=300, shoot=False, steps=20))
            # self.enemy_list.append (Enemy(master=self,x=1250,y=500,speed_walk=6,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,p_scale=0.3,interval_time_jump=300, shoot=True, steps=10))
            # self.enemy_list.append (Enemy(master=self,x=700,y=100,speed_walk=6,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,p_scale=0.08,interval_time_jump=300, shoot=False, steps=50))
            # self.enemy_list.append (Enemy(master=self,x=859,y=200,speed_walk=6,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,p_scale=0.08,interval_time_jump=300, shoot=False, steps=30))
        
            self.restart = False    
    
    
    def update(self, lista_eventos,keys,delta_ms):

        self.tiempo_juego.update(delta_ms)  # Timer del Juego        
        for trap in self.list_trap:
            trap.update(delta_ms)
        self.pb_lives.value = self.player_1.lives
        
        for coin_element in self.coin_list:
            coin_element.update(delta_ms)
            coin_element.label_coin.update()

        self.pb_lives.value = self.player_1.lives
        self.player_1.label_score.update()
        self.player_1.label_coins.update() 

        for aux_widget in self.widget_list:
            aux_widget.update(lista_eventos)        

        for bullet_element in self.bullet_list:
            bullet_element.update(delta_ms,self.plataform_list,self.enemy_list,self.player_1)

        for enemy_element in self.enemy_list:
            enemy_element.update(delta_ms,self.plataform_list, self.player_1)
            enemy_element.energy_bar.update(lista_eventos)
            self.time_enemy_shoot += delta_ms
            # LOGICA DE DISPARO ALEATORIO ENEMIGO
            if self.time_enemy_shoot >= 2000:
                self.time_enemy_shoot = 0
                indice_enemigo = random.randint(0, len(self.enemy_list)-1)
                if (self.enemy_list[indice_enemigo].direction == 1 and self.player_1.direction == 0) or\
                       (self.enemy_list[indice_enemigo].direction == 0 and self.player_1.direction == 1):
                    self.enemy_shoot(indice_enemigo)

            if enemy_element.lives <= 0:
                enemy_element.animation = enemy_element.die_r
                enemy_element.alive = False
                print('LA QUEDO EL MONSTRUO')

        for plataform_element in self.plataform_list:
            if plataform_element.motion:
                plataform_element.update(delta_ms, self.enemy_list)
               
        
        # IMPLEMENTAR COINS
        
        self.player_1.events(delta_ms,keys, self.plataform_list)
        self.player_1.update(delta_ms,self.plataform_list, self.coin_list, self.list_lifes, self.enemy_list, self.list_trap, self.number_of_stars)
        
        if self.player_1.is_shoot:
            self.player_shoot(delta_ms)


        # CAMBIO DE NIVEL
        if self.player_1.coins == self.number_of_stars:
            save_data_player(self.player_1.score, self.player_1.lives)
            self.active = False
            self.set_active('form_game_L2')
        # CAMBIO A GAME OVER
        if self.player_1.lives == 0 or self.tiempo_juego.lavel_timer._text == '0:00':
            self.active = False
            self.file_game_score.add_data_reg(self.player_1.score)
            self.restart = True
            self.pb_lives.value = self.player_1.lives
            self.player_1.lives = PLAYER_LIFE
            
            #self.restart_all_list()
            #self.restart_game()
            self.set_active('form_game_over')

    def draw(self): 
        super().draw()
        self.static_background.draw(self.surface)
        for trap in self.list_trap:
            trap.draw(self.surface)

        for aux_widget in self.widget_list:    
            aux_widget.draw()

        for plataforma in self.plataform_list:
            plataforma.draw(self.surface)

        for enemy_element in self.enemy_list:
            enemy_element.draw(self.surface)
            enemy_element.energy_bar.draw()

            if not enemy_element.alive and enemy_element.frame == 0:               
                self.enemy_list.pop(self.enemy_list.index(enemy_element))
                self.player_1.score += 100
                

        for bullet_element in self.bullet_list:
            bullet_element.draw(self.surface)
        
        self.player_1.draw(self.surface)
        
        for coin_element in self.coin_list:
            coin_element.draw(self.surface)
            coin_element.label_coin.draw()
        
        self.player_1.label_score.draw()
        self.player_1.label_coins.draw()

        for life in self.list_lifes:
            life.draw(self.surface)

        self.tiempo_juego.lavel_timer.draw() # Timer del Juego


