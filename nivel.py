from plataforma import Plataform
from enemigo import Enemy
from class_trap import Trap
from coins import Coins
from class_life import Life
from constantes import *
from player import Player


def level_1(self):
    dict_level = {}
    list_plataforma = []
    enemys_list = []
    list_trampas = []
    list_coins = []
    list_vidas = []
    ## PLATAFORMAS ##
    # PLATAFORMA SUELO
    for aux in range(0,1400,50):
        list_plataforma.append(Plataform(x=aux,y=650,width=50,height=50,type=1, style_tile='dark_forest'))        
    # PLATAFORMA 1
    list_plataforma.append(Plataform(x=0,y=500,width=50,height=50,type=13, style_tile='dark_forest'))
    list_plataforma.append(Plataform(x=50,y=500,width=50,height=50,type=13, style_tile='dark_forest'))
    list_plataforma.append(Plataform(x=100,y=500,width=50,height=50,type=13, style_tile='dark_forest'))
    list_plataforma.append(Plataform(x=150,y=500,width=50,height=50,type=13, style_tile='dark_forest'))
    list_plataforma.append(Plataform(x=200,y=500,width=50,height=50,type=13, style_tile='dark_forest'))
    list_plataforma.append(Plataform(x=250,y=500,width=50,height=50,type=14, style_tile='dark_forest'))
    # PLATAFORMA 2
    list_plataforma.append(Plataform(x=350,y=550,width=50,height=50,type=12, style_tile='dark_forest'))
    list_plataforma.append(Plataform(x=400,y=550,width=50,height=50,type=14, style_tile='dark_forest'))
    # PLATAFORMA 3
    list_plataforma.append(Plataform(x=700,y=500,width=50,height=50,type=12, style_tile='dark_forest'))
    list_plataforma.append(Plataform(x=750,y=500,width=50,height=50,type=13, style_tile='dark_forest'))
    list_plataforma.append(Plataform(x=800,y=500,width=50,height=50,type=13, style_tile='dark_forest'))
    list_plataforma.append(Plataform(x=850,y=500,width=50,height=50,type=14, style_tile='dark_forest')) 
    # PLATAFORMA 4
    list_plataforma.append(Plataform(x=1000,y=550,width=50,height=50,type=12, style_tile='dark_forest'))
    list_plataforma.append(Plataform(x=1050,y=550,width=50,height=50,type=14, style_tile='dark_forest'))
    # PLATAFORMA 5
    list_plataforma.append(Plataform(x=1350,y=500,width=50,height=50,type=13, style_tile='dark_forest'))
    list_plataforma.append(Plataform(x=1300,y=500,width=50,height=50,type=13, style_tile='dark_forest'))
    list_plataforma.append(Plataform(x=1250,y=500,width=50,height=50,type=13, style_tile='dark_forest'))
    list_plataforma.append(Plataform(x=1200,y=500,width=50,height=50,type=13, style_tile='dark_forest'))
    list_plataforma.append(Plataform(x=1150,y=500,width=50,height=50,type=12, style_tile='dark_forest'))
    # PLATAFORMA 6
    list_plataforma.append(Plataform(x=0,y=350,width=50,height=50,type=13, style_tile='dark_forest'))
    list_plataforma.append(Plataform(x=50,y=350,width=50,height=50,type=13, style_tile='dark_forest'))
    list_plataforma.append(Plataform(x=100,y=350,width=50,height=50,type=14, style_tile='dark_forest'))
    # PLATAFORMA 7
    list_plataforma.append(Plataform(x=250,y=350,width=50,height=50,type=12, style_tile='dark_forest'))
    list_plataforma.append(Plataform(x=300,y=350,width=50,height=50,type=14, style_tile='dark_forest'))
    # PLATAFORMA 8
    list_plataforma.append(Plataform(x=400,y=400,width=50,height=50,type=12, style_tile='dark_forest'))
    list_plataforma.append(Plataform(x=450,y=400,width=50,height=50,type=13, style_tile='dark_forest'))
    list_plataforma.append(Plataform(x=500,y=400,width=50,height=50,type=13, style_tile='dark_forest'))
    list_plataforma.append(Plataform(x=550,y=400,width=50,height=50,type=13, style_tile='dark_forest'))
    list_plataforma.append(Plataform(x=600,y=400,width=50,height=50,type=14, style_tile='dark_forest'))
    # PLATAFORMA 9
    list_plataforma.append(Plataform(x=750,y=250,width=50,height=50,type=12, style_tile='dark_forest'))
    list_plataforma.append(Plataform(x=800,y=250,width=50,height=50,type=13, style_tile='dark_forest'))
    list_plataforma.append(Plataform(x=850,y=250,width=50,height=50,type=13, style_tile='dark_forest'))
    list_plataforma.append(Plataform(x=900,y=250,width=50,height=50,type=14, style_tile='dark_forest'))
    # PLATAFORMA 10
    list_plataforma.append(Plataform(x=1350,y=350,width=50,height=50,type=13, style_tile='dark_forest'))
    list_plataforma.append(Plataform(x=1300,y=350,width=50,height=50,type=13, style_tile='dark_forest'))
    list_plataforma.append(Plataform(x=1250,y=350,width=50,height=50,type=13, style_tile='dark_forest'))
    list_plataforma.append(Plataform(x=1200,y=350,width=50,height=50,type=12, style_tile='dark_forest'))
    # PLATAFORMA 11
    list_plataforma.append(Plataform(x=400,y=250,width=50,height=50,type=12, style_tile='dark_forest'))
    list_plataforma.append(Plataform(x=450,y=250,width=50,height=50,type=13, style_tile='dark_forest'))
    list_plataforma.append(Plataform(x=500,y=250,width=50,height=50,type=14, style_tile='dark_forest'))

    ## ENEMIGOS ##
    enemys_list.append (Enemy(master=self,x=30,y=400,speed_walk=3,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=30,jump_height=140,p_scale=0.08,interval_time_jump=300, shoot=False, steps=20))
    enemys_list.append (Enemy(master=self,x=1250,y=500,speed_walk=6,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,p_scale=0.08,interval_time_jump=300, shoot=True, steps=10))
    enemys_list.append (Enemy(master=self,x=700,y=100,speed_walk=6,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,p_scale=0.08,interval_time_jump=300, shoot=False, steps=50))
    enemys_list.append (Enemy(master=self,x=859,y=200,speed_walk=6,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,p_scale=0.08,interval_time_jump=300, shoot=False, steps=30))

    ## TRAMPAS ##
    list_trampas.append(Trap(x=400,y=600,p_scale=1, frame_rate_ms=200))
    list_trampas.append(Trap(x=600,y=600,p_scale=1, frame_rate_ms=200))

    ## COINS/ESTRELLAS ##
    list_coins.append(Coins(master=self, x=400, y=450,value=100,frame_rate_ms=200, p_scale=0.4, delay_time_coin = 30))
    list_coins.append(Coins(master=self, x=1050, y=450,value=150,frame_rate_ms=200, p_scale=0.4, delay_time_coin = 20))
    list_coins.append(Coins(master=self, x=50, y=250,value=250,frame_rate_ms=200, p_scale=0.4, delay_time_coin = 10))
    list_coins.append(Coins(master=self, x=550, y=300,value=400,frame_rate_ms=200, p_scale=0.4, delay_time_coin = 10))
    list_coins.append(Coins(master=self, x=950, y=350,value=200,frame_rate_ms=200, p_scale=0.4, delay_time_coin = 0))
    list_coins.append(Coins(master=self, x=750, y=350,value=200,frame_rate_ms=200, p_scale=0.4, delay_time_coin = 0))
    list_coins.append(Coins(master=self, x=300, y=250,value=200,frame_rate_ms=200, p_scale=0.4, delay_time_coin = 0))

    ## VIDAS ##
    list_vidas.append(Life(x=200,y=400))
    list_vidas.append(Life(x=1250,y=350))

    ## PLAYER ##
    player = Player(master=self, x=INIT_POSITION_PLAYER_X,y=INIT_POSITION_PLAYER_Y,speed_walk=8,speed_run=12,gravity=14,jump_power=30,frame_rate_ms=100,move_rate_ms=50,jump_height=110,p_scale=0.1,interval_time_jump=300)
    
    ## IMAGEN DE FONDO ##
    
    dict_level['plataforma'] = list_plataforma
    dict_level['enemigos'] = enemys_list
    dict_level['trampas'] = list_trampas
    dict_level['estrellas'] = list_coins
    dict_level['vidas'] = list_vidas
    dict_level['player'] = player
    
    return dict_level