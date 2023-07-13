from player import Player
from constantes import *
from auxiliar import Auxiliar
from gui_progressbar import ProgressBar

class Enemy(Player):
    def __init__(self, master, x, y, speed_walk, speed_run, gravity, jump_power, frame_rate_ms, move_rate_ms, jump_height, p_scale=1, interval_time_jump=100, shoot = False, steps = 20) -> None:
        super().__init__(master, x, y, speed_walk, speed_run, gravity, jump_power, frame_rate_ms, move_rate_ms, jump_height, p_scale, interval_time_jump)
        # ANIMACIONES
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/ork_sword/WALK/WALK_00{0}.png",0,7,scale=p_scale)
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/ork_sword/WALK/WALK_00{0}.png",0,7,flip=True,scale=p_scale)
        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/ork_sword/IDLE/IDLE_00{0}.png",0,7,scale=p_scale)
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/ork_sword/IDLE/IDLE_00{0}.png",0,7,flip=True,scale=p_scale)
        self.die_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/ork_sword/DIE/DIE_00{0}.png",0,7,scale=p_scale)
        self.hurt_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/ork_sword/HURT/HURT_00{0}.png",0,7,scale=p_scale)
        self.hurt_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/ork_sword/HURT/HURT_00{0}.png",0,7,flip=True,scale=p_scale)
        # ATRIBUTOS PROPIOS DEL MONSTRUO
        self.time_hurt = 0
        self.lives = 15
        self.can_shoot = shoot
        self.steps = steps        

        self.contador = 0

        self.sides['bottom'].y = y + self.rect.height - GROUND_COLLIDE_H + 10
        self.energy_bar = ProgressBar(master=master,x=x,y=y,w=35,h=20,color_background=None,color_border=None,image_background="images\gui\Gui\Bar_Background01.png",image_progress="images\gui\Gui\Bar_Segment05.png",value = 5, value_max=15)
        self.energy_bar.value = self.lives


    def change_x(self,delta_x):
        
        if self.rect.x >= 0 and self.rect.x <= ANCHO_VENTANA - self.rect.width :
            for side in self.sides:
                self.sides[side].x += delta_x
        else:
            if self.rect.x < 0:
                for side in self.sides:
                    self.sides[side].x += 10
            elif self.rect.x > ANCHO_VENTANA - self.rect.width:
                for side in self.sides:
                    self.sides[side].x -= 10
        self.energy_bar.x =  self.sides['top'].x + 40
    
    def change_y(self,delta_y):
        
        for side in self.sides:
            self.sides[side].y += delta_y
        self.energy_bar.y =  self.sides['top'].y - 35  


    def do_movement(self,delta_ms,plataform_list):
        #super().do_movement(self,delta_ms,plataform_list)
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0

            if(not self.is_on_plataform(plataform_list)):
                if(self.move_y == 0):
                    self.is_fall = True
                    self.change_y(self.gravity)
            else:
                self.is_fall = False
                self.change_x(self.move_x)
                if self.contador <= self.steps: # CANTIDAD DE PASOS DEL MONSTRUO
                    self.move_x = -self.speed_walk
                    self.animation = self.walk_l
                    self.contador += 1 
                elif self.contador <= self.steps * 2:
                    self.move_x = self.speed_walk
                    self.animation = self.walk_r
                    self.contador += 1
                else:
                    self.contador = 0
    
    def is_on_plataform(self,plataform_list):
        retorno = False
        if self.sides['bottom'].bottom >= GROUND_LEVEL:
        #if(self.ground_collition_rect.bottom >= GROUND_LEVEL):
            retorno = True     
        else:
            for plataforma in  plataform_list:
                if(self.sides['bottom'].colliderect(plataforma.ground_collition_rect)):
                #if(self.ground_collition_rect.colliderect(plataforma.ground_collition_rect)):
                    #print('colision!!!')
                    retorno = True
                    break       
        return retorno          

    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
                #print(self.frame)
            else: 
                self.frame = 0

    def contact(self, player):
        if(self.sides['right'].colliderect(player.sides['main'])):
            self.rebound('right',10)
        if(self.sides['left'].colliderect(player.sides['main'])):
            self.rebound('left',10)

    def update(self,delta_ms,plataform_list, player):
        self.energy_bar.value = self.lives
        
        if self.animation ==  self.hurt_r and self.time_hurt <= 400:
            self.time_hurt += delta_ms
        else:
            if self.alive:
                self.do_movement(delta_ms,plataform_list)
            else:
                self.frame_rate_ms = 600
            self.do_animation(delta_ms)
            self.contact(player) 
            self.time_hurt = 0

    def receive_shoot(self):
        if self.direction == DIRECTION_L:
            self.animation = self.hurt_l
        else:
            self.animation = self.hurt_r
        self.lives -= 1
        
