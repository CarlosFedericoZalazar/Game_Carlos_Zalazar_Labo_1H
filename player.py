import pygame 
from constantes import *
from auxiliar import Auxiliar
from gui_label import Label
from auxiliar_player import obtener_rectangulo
from bullet import Bullet

class Player:
    def __init__(self, master, x,y,speed_walk,speed_run,gravity,jump_power,frame_rate_ms,move_rate_ms,jump_height,p_scale=1,interval_time_jump=100) -> None:
        '''
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/walk.png",15,1,scale=p_scale)[:12]
        '''
        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles(PATH_PLAYER+ 'IDLE\_IDLE_{0}.png',0,6,flip=False,scale=p_scale)
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles(PATH_PLAYER+ 'IDLE\_IDLE_{0}.png',0,6,flip=True,scale=p_scale)
        self.jump_r = Auxiliar.getSurfaceFromSeparateFiles(PATH_PLAYER+ 'JUMP\_JUMP_{0}.png',0,6,flip=False,scale=p_scale)
        self.jump_l = Auxiliar.getSurfaceFromSeparateFiles(PATH_PLAYER+ 'JUMP\_JUMP_{0}.png',0,6,flip=True,scale=p_scale)
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles(PATH_PLAYER+ 'WALK\_WALK_{0}.png',0,6,flip=False,scale=p_scale)
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles(PATH_PLAYER+ 'WALK\_WALK_{0}.png',0,6,flip=True,scale=p_scale)
        self.hurt_l = Auxiliar.getSurfaceFromSeparateFiles(PATH_PLAYER+ 'HURT\_HURT_{0}.png',0,6,flip=False,scale=p_scale)
        self.hurt_r = Auxiliar.getSurfaceFromSeparateFiles(PATH_PLAYER+ 'HURT\_HURT_{0}.png',0,6,flip=True,scale=p_scale)
        self.shoot_r = Auxiliar.getSurfaceFromSeparateFiles(PATH_PLAYER+ 'SHOOT\_SHOOT_{0}.png',0,3,flip=False,scale=p_scale,repeat_frame=2)
        self.shoot_l = Auxiliar.getSurfaceFromSeparateFiles(PATH_PLAYER+ 'SHOOT\_SHOOT_{0}.png',0,3,flip=True,scale=p_scale,repeat_frame=2)
        self.knife_r = Auxiliar.getSurfaceFromSeparateFiles(PATH_PLAYER+ 'ATTACK\_ATTACK_{0}.png',0,6,flip=False,scale=p_scale,repeat_frame=1)
        self.knife_l = Auxiliar.getSurfaceFromSeparateFiles(PATH_PLAYER+ 'ATTACK\_ATTACK_{0}.png',0,6,flip=True,scale=p_scale,repeat_frame=1)
        self.die_r = Auxiliar.getSurfaceFromSeparateFiles(PATH_PLAYER+ 'DIE\_DIE_{0}.png',0,6,flip=False,scale=p_scale,repeat_frame=1)
        #self.impacto = Auxiliar.getSurfaceFromSeparateFiles('images\gui\Gui\IMPACTO\\'+ '{0}.png',1,8,flip=False,scale=p_scale)
        
        # MOVIMIENTO
        self.frame = 0
        self.lives = PLAYER_LIFE
        self.score = 0
        self.coins = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.gravity = 20 #gravity
        self.jump_power = 30 #jump_power
        self.animation = self.stay_r
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        self.alive = True
        self.label_score = Label(master, x=1100, y=10, w=300, h=100,color_border=None, text=f"Score: {0}", font="Comic Sans MS", font_size=30, font_color=C_WHITE, image_background='images\gui\Gui\\table_point_screen.png')
        self.label_coins = Label(master, x=1100, y=60, w=300, h=120,color_border=None, text=f"Coins: {0}", font="Comic Sans MS", font_size=35, font_color=C_WHITE, color_background=None)
        # RECTANGULO PERSONAJE
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.sides = obtener_rectangulo(self.rect)
        self.sides['bottom'].y = y + self.rect.height - GROUND_COLLIDE_H
        self.sides['bottom'].height = GROUND_COLLIDE_H        
        
        self.is_jump = False
        self.is_fall = False
        self.is_shoot = False
        self.is_knife = False
        self.atack = False
        self.time_to_shoot = 0

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height

        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0 # en base al tiempo transcurrido general
        self.interval_time_jump = interval_time_jump
        # DISPARO
        self.bullet_list = []


    def walk(self,direction, plataform_list):
        if(self.is_jump == False and self.is_fall == False):
            if(self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l)):
                self.frame = 0
                self.direction = direction
                if(direction == DIRECTION_R):
                    self.move_x = self.speed_walk
                    self.animation = self.walk_r
                else:
                    self.move_x = -self.speed_walk
                    self.animation = self.walk_l

    def shoot(self,on_off = True):
        self.is_shoot = on_off
        if(on_off == True and self.is_jump == False and self.is_fall == False):

            if(self.animation != self.shoot_r and self.animation != self.shoot_l):
                self.frame = 0
                self.is_shoot = True
                self.bullet_list.append(Bullet(self, self.rect.centerx, self.rect.centery, ANCHO_VENTANA , self.rect.centery,20,path="images\caracters\players\caballero\SHOOT\SHOOT.png",frame_rate_ms=100,move_rate_ms=20,width=20,height=20))
                if(self.direction == DIRECTION_R):
                    self.animation = self.shoot_r

                else:
                    self.animation = self.shoot_l       

    def receive_shoot(self):
        if not self.atack:            
            self.lives -= 1
        else:
            print('ATAJASTE EL CUETASO')
            self.score += 5

    def knife(self,on_off = True):
        self.is_knife = on_off
        if(on_off == True and self.is_jump == False and self.is_fall == False):
            if(self.animation != self.knife_r and self.animation != self.knife_l):
                self.frame = 0
                if(self.direction == DIRECTION_R):
                    self.animation = self.knife_r
                else:
                    self.animation = self.knife_l      

    def verify_collide(self, some_enemy, power_rebound):
        if(self.sides['right'].colliderect(some_enemy.sides['main']) or 
                self.sides['left'].colliderect(some_enemy.sides['main'])):
            if self.atack:
                some_enemy.lives -= 1
                print('LO CORTASTE TODO AL MOSNTRUO')
            else:
                self.lives -= 1
                if self.direction == DIRECTION_R:
                    self.rebound('left',power_rebound)
                else:
                    self.rebound('right',power_rebound)

            if self.direction == DIRECTION_R:
                some_enemy.rebound('right',power_rebound)
            else:
                some_enemy.rebound('left',power_rebound)
    
    def contact(self, enemy_list, boss):
        for enemy_element in  enemy_list:
            self.verify_collide(enemy_element, 60)
            # if(self.sides['right'].colliderect(enemy_element.sides['main']) or
            #       self.sides['left'].colliderect(enemy_element.sides['main'])):
            #     if self.atack:
            #         enemy_element.lives -= 1
            #         print('LO CORTASTE TODO AL MOSNTRUO')
            #     else:
            #         self.lives -= 1
            #     if self.direction == DIRECTION_R:
            #         enemy_element.rebound('right',60)
            #     else:
            #         enemy_element.rebound('left',60)
        self.verify_collide(boss, 60)



    def rebound(self, direction, power_rebound):
        """ Realiza un efecto rebote en el personaje y sus rectangulos dependiendo el parametro
        recibido (left/right).
        """ 
        auxiliar = power_rebound
        if direction == 'left':
            auxiliar *= -1
        for side in self.sides:
            self.sides[side].x += auxiliar  

    
    def jump(self,on_off = True):
        if(on_off and self.is_jump == False and self.is_fall == False):
            self.y_start_jump = self.rect.y
            if(self.direction == DIRECTION_R):
                self.move_x = int(self.move_x + 5 / 2)
                self.move_y = -self.jump_power
                self.animation = self.jump_r
            else:
                self.move_x = int(self.move_x - 5 / 2)
                self.move_y = -self.jump_power
                self.animation = self.jump_l
            self.frame = 0
            self.is_jump = True
        if(on_off == False):
            self.is_jump = False
            self.stay()

    def stay(self):
        if(self.is_knife or self.is_shoot):
            return

        if(self.animation != self.stay_r and self.animation != self.stay_l):
            if(self.direction == DIRECTION_R):
                self.animation = self.stay_r
            else:
                self.animation = self.stay_l
            self.move_x = 0
            self.move_y = 0
            self.frame = 0

    def change_x(self,delta_x):
                
        if self.rect.x >= 0 and self.rect.x <= ANCHO_VENTANA - self.rect.width :
            for side in self.sides:
                    self.sides[side].x += delta_x
        else:
            if self.rect.x < 0:
                self.rebound('right',10)
            elif self.rect.x > ANCHO_VENTANA - self.rect.width:
                self.rebound('left',10)


    def change_y(self,delta_y):
        for side in self.sides:
            self.sides[side].y += delta_y


    def do_movement(self,delta_ms,plataform_list, coin_list):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0
            if(abs(self.y_start_jump - self.rect.y) > self.jump_height and self.is_jump):                
                self.move_y = 0
          
            self.change_x(self.move_x)
            self.change_y(self.move_y)

            self.take_coin(coin_list)
            
            if(not self.is_on_plataform(plataform_list)):

                if(self.move_y == 0):
                    self.is_fall = True
                    self.change_y(self.gravity)
            else:
                if (self.is_jump): 
                    self.jump(False)
                self.is_fall = False

    def contact_trap(self, list_trap):
        for trap in  list_trap:
            if self.sides['right'].colliderect(trap.rect) or  \
                  self.sides['left'].colliderect(trap.rect):
                if self.atack:
                    self.score += ELIMINAR_TRAMPA 
                    list_trap.pop(list_trap.index(trap))
                    print('ELIMINASTE LA TRAMPA')
                else:
                    self.lives -= 1
                if self.direction == DIRECTION_R:
                    self.rebound('left',40)
                else:
                    self.rebound('right',40)
            elif self.sides['bottom'].colliderect(trap.rect):
                print('PISASTE AL BICHO')
                list_trap.pop(list_trap.index(trap))
                print('ELIMINASTE LA TRAMPA')
                self.score += ELIMINAR_TRAMPA               
                if self.direction == DIRECTION_R:
                    self.rebound('right',60)
                else:
                    self.rebound('left',60)

    def is_on_plataform(self,plataform_list):
        retorno = False
        
        if(self.rect.bottom >= GROUND_LEVEL):
            retorno = True     
        else:
            for plataforma in  plataform_list:
                if(self.sides['bottom'].colliderect(plataforma.ground_collition_rect)):
                    #print('ARRIBA DE PLATAFORMA')
                    retorno = True
                    break                 
        return retorno

    def take_coin(self, coin_list):
        for coin in coin_list:
            if(self.rect.colliderect(coin.rect)):
                self.score += coin.coin_value
                self.coins += 1
                print('AGARRASTE LA MONEDA!!!')
                print('CANTIDAD DE MONEDAS OBTENIDAS AL MOMENTO:{0}'.format(self.coins))
                coin_list.pop(coin_list.index(coin))

    def take_life(self, life_list):
        for life in life_list:
            if(self.rect.colliderect(life.rect)):
                self.lives += life.value
                life_list.pop(life_list.index(life))

    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
                #print(self.frame)
            else: 
                self.frame = 0
 
    def update(self,delta_ms,plataform_list, coins_list,life_list, enemy_list, list_trap, number_of_stars, boss):

        self.do_movement(delta_ms,plataform_list, coins_list)
        self.do_animation(delta_ms)
        self.label_score._text = 'Puntos: {0}'.format(str(self.score))
        self.label_coins._text = 'Stars: {0}/{1}'.format(self.coins, number_of_stars)
        self.contact(enemy_list, boss)
        self.contact_trap(list_trap)
        for bullet_element in self.bullet_list:
            bullet_element.update(delta_ms,plataform_list,enemy_list,self)
        self.take_life(life_list)
    
    def draw(self,screen):
        
        if(DEBUG):
            for side in self.sides:
                if side == 'bottom':
                    pygame.draw.rect(screen,color=(0,0 ,0),rect=self.sides[side])                
                elif side == 'left' or side == 'right':
                    pygame.draw.rect(screen,color=(255,0 ,0),rect=self.sides[side])
                elif side == 'top':
                    pygame.draw.rect(screen,color=(0,255 ,0),rect=self.sides[side])
                else:
                    pygame.draw.rect(screen,color=(255,255 ,0),rect=self.sides[side]) 
           
        
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
            

    def events(self,delta_ms,keys, plataform_list):
        self.tiempo_transcurrido += delta_ms

        if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
            self.walk(DIRECTION_L, plataform_list)

        if(not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]):
            self.walk(DIRECTION_R, plataform_list)

        if(not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            self.stay()
        if(keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            self.stay()  

        if(keys[pygame.K_SPACE]):
            if((self.tiempo_transcurrido - self.tiempo_last_jump) > self.interval_time_jump):
                self.jump(True)
                self.tiempo_last_jump = self.tiempo_transcurrido

        if(not keys[pygame.K_a]):
            self.shoot(False)  

        if(not keys[pygame.K_a]):
            self.atack = False
            self.knife(False)  

        if(keys[pygame.K_s] and not keys[pygame.K_a]):
            self.is_shoot = True
            #self.shoot()   
        
        if(keys[pygame.K_a] and not keys[pygame.K_s]):
            self.atack = True
            print('ATACANDO...')
            self.knife()   