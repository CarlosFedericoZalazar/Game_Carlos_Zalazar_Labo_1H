import pygame
from pygame.locals import *
import sys
from constantes import *
from gui_form import Form
from gui_form_game_over import FormGameOver
from class_file import File

from pygame.locals import *
from plataforma import Plataform


plataforma_level_1 = []

plataforma_level_1.append(Plataform(x=1000,y=550,width=50,height=50,type=12))
plataforma_level_1.append(Plataform(x=1050,y=550,width=50,height=50,type=14))

# for aux in range(0,1400,50):
#     plataforma_level_1.append(Plataform(x=aux,y=650,width=50,height=50,type=1))