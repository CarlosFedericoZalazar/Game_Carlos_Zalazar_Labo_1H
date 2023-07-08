from constantes import *
import json

class File():
    def __init__(self, name='', score= 0) -> None:
        self.name = name
        self.score = score
        self.last_index = 0
        
        self.list_players = []
        self.dict_jason = DICT_FILE_JSON
        self.file_sort = []
           
    
    def read_file(self):
        file_exist = False
        try:
            with open(PATH_DATA_SCORE + '{0}.json'.format(self.name), 'r') as archivo:
                aux_jason = json.load(archivo)
                self.list_players = aux_jason[DICT_FILE_JSON]
                self.last_index = self.list_players[-1]['id']

                print('SE LEYO CORRECTAMENTE EL ARCHIVO')
                print(' INDICE: {0}'. format(self.last_index))
            file_exist = True
        except FileNotFoundError:
            print("El archivo JSON no existe.")
        return file_exist

    def new_reg_player(self,value):        
        player = {}        
        self.read_file()
        player['id'] = self.last_index + 1
        player['name'] = value
        player['score'] = 0
        player['hour'] = None        
        self.list_players.append(player)
        self.save_data()        

    def delete_last_reg(self):
        self.read_file()
        self.list_players.pop(self.list_players.index(self.list_players[-1]))
        print('IRRUPCION DEL PROGRAMA. REGISTRO ELIMINADO')
        self.save_data()

    def save_data(self):
        dict_aux = {}
        dict_aux[DICT_FILE_JSON] = self.list_players
        with open(PATH_DATA_SCORE + '{0}.json'.format(self.name), 'w') as file:
            json.dump(dict_aux, file, indent=4)
            print('SE CREO ARCHIVO JSON')

    # ORDENAMIENTO DE LA LISTA
    def sort_list(self, list_players):
        lista_de = []
        lista_iz = []
        if len(list_players) <= 1:
            return list_players
        else:
            pivot = list_players[0]
            for elemento in list_players[1:]:
                if elemento['score'] < pivot['score']:
                    lista_de.append(elemento)
                else:
                    lista_iz.append(elemento)   
    
        lista_iz = self.sort_list(lista_iz)
        lista_iz.append(pivot)
        lista_de = self.sort_list(lista_de)
        lista_iz.extend(lista_de)

        return lista_iz


#########################################################################################
'OBTENER LA HORA H:M:S'
# import datetime

# # Obtener la hora actual del sistema
# hora_actual = datetime.datetime.now().time()

# # Imprimir la hora actual
# print("Hora actual:", hora_actual)

# # Guardar la hora actual en una variable
# mi_variable = hora_actual

# # Imprimir la variable
# print("Mi variable:", mi_variable)

#-----------------------------------------------------------------------------------------
' SE ACCEDE A LOS CAMPOS DE LA HORA POR SEPARADO'
# import datetime

# hora_actual = datetime.datetime.now().time()

# # Acceder a los componentes de la hora
# hora = hora_actual.hour
# minuto = hora_actual.minute
# segundo = hora_actual.second
# microsegundo = hora_actual.microsecond

# # Imprimir los componentes individuales
# print("Hora:", hora)
# print("Minuto:", minuto)
# print("Segundo:", segundo)
# print("Microsegundo:", microsegundo)

#-------------------------------------------------------------------------------------------


        