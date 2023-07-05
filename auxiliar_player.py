import pygame

def obtener_rectangulo(principal)->dict:
    diccionario = {}
    diccionario['main'] = principal
    diccionario['bottom'] = pygame.Rect(principal.left + 30, principal.bottom -10, principal.width - 60, 15)
    diccionario['right'] = pygame.Rect(principal.right -20, principal.top+30, 5, 40)
    diccionario['left'] = pygame.Rect(principal.left +20, principal.top+30, 5, 40)
    diccionario['top'] = pygame.Rect(principal.left, principal.top + 5, principal.width, 10)
    return diccionario