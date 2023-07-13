from plataforma import Plataform

def level_1():
    dict_level = {}
    list_plataforma = []

    list_plataforma.append(Plataform(x=350,y=550,width=50,height=50,type=12))
    list_plataforma.append(Plataform(x=400,y=550,width=50,height=50,type=14))

    dict_level['plataforma'] = list_plataforma

    return dict_level