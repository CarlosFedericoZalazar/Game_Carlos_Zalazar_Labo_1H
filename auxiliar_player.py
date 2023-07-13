import pygame
import json
import os
from constantes import PLAYER_LIFE

def obtener_rectangulo(principal)->dict:
    diccionario = {}
    diccionario['main'] = principal
    diccionario['bottom'] = pygame.Rect(principal.left + 30, principal.bottom -10, principal.width - 60, 15)
    diccionario['right'] = pygame.Rect(principal.right -20, principal.top+30, 10, 40)
    diccionario['left'] = pygame.Rect(principal.left +20, principal.top+30, 10, 40)
    diccionario['top'] = pygame.Rect(principal.left, principal.top + 5, principal.width, 10)
    return diccionario

def read_auxiliar_file_player():
    aux_jason = {}
    aux_jason['score'] = 0
    aux_jason['lifes'] = PLAYER_LIFE
    print('VINE A TRATAR DE LEER EL ARCHIVO')
    try:
        with open('auxiliar_file_player.json', 'r') as archivo:
            aux_jason = json.load(archivo)
            print('SE LEYO CORRECTAMENTE EL ARCHIVO AUXILIAR_PLAYER! EL QUE VAAAA!!!')
    except FileNotFoundError:
            print("El archivo JSON no existe.")
    print(f'ESTO ES LO QUE LEI --> {aux_jason}')
    return aux_jason

def save_file_auxiliar_player(dict_player):
    with open('auxiliar_file_player.json', 'w') as file:
        json.dump(dict_player, file, indent=4)
        print('SE CREO ARCHIVO JSON AUXILIAR_PLAYER')

def save_data_player(score, lifes):
    info_player = {}
    print('SE INGRESARON VALORES SCORE Y LIFES')
    info_player['score'] = score
    info_player['lifes'] = lifes
    save_file_auxiliar_player(info_player)



def delete_file_auxiliar_player():
    nombre_archivo = "auxiliar_file_player.json"

    # Comprobamos si el archivo existe antes de eliminarlo
    if os.path.exists(nombre_archivo):
        os.remove(nombre_archivo)
        print(f"El archivo {nombre_archivo} ha sido eliminado.")
    else:
        print(f"El archivo {nombre_archivo} no existe.")
