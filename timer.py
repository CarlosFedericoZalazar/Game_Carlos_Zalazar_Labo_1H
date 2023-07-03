import pygame
from constantes import *

from gui_label import Label


class Timer_level():
    def __init__(self, master, x=0, y=0, w=0, h=0, color_background=None, color_border=None, image_background=None, text='0:00', font='Arial', font_size =14, font_color=C_WHITE, minutes=0, seconds=00):
        
        self.minutes = minutes
        self.seconds =seconds
        self.lavel_timer = Label(master,x=ANCHO_VENTANA / 2 - 100,y=30,w=200,h=100,color_background=None, font=font,font_size=font_size, color_border=None,text=text, font_color=C_YELLOW_2)
        self.tiempo_trascurrido = 0
        self.tiempo_cumplido = False

    def calculation(self, delta_ms):
        self.tiempo_trascurrido += delta_ms
        if self.tiempo_trascurrido >= 1000:
            self.tiempo_trascurrido = 0

            if self.minutes != 0 and self.seconds == 0:
                self.seconds = 59
                self.minutes += -1
            else:
                self.seconds += -1
                if self.seconds == 0:
                    self.tiempo_cumplido = True
                    
        print(self.seconds)
        return self.tiempo_cumplido   
    
    def formato_texto(self):
        aux_texto = ''
        
        aux_texto = '{0}:'.format(self.minutes)
        if self.seconds < 10:
            aux_texto += '0{0}'.format(self.seconds)
        else:
            aux_texto += str(self.seconds)
        #print(aux_texto)
        return aux_texto    
    
    
    def update(self, delta_ms):
        self.calculation(delta_ms)
        self.lavel_timer._text = self.formato_texto()
        self.lavel_timer.update()