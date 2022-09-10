from schema_Personaje import Personaje
from config_Objetos import *
from config_Ubicaciones import *
from config_Nombres import *

nombre 		  = HMOSCA
identificador = 9
objeto_tiene  = ANALIZADOR
ubicacion 	  = MARTE
objeto_quiere = PISTOLA
ama 		  = []
odia 		  = [RICK]
razon_odio 	  = ["No le quiere dar la información para crear pistolas de portales"]
razon_raptado = "Estaba dentro del analizador cerebral"
sabe_rapto 	  = "Trabaja para la federación espacial y ellos patrocinaron el secuestro"
plan 		  = "Ponerle un analizador cerebral al -VILLANO- para poder encontrar a -RAPTADO- y así liberarlo de su raptor. "

HMosca = Personaje(nombre, identificador, objeto_tiene, ubicacion, objeto_quiere, ama, odia, razon_odio, razon_raptado, sabe_rapto, plan)

if __name__ == '__main__':
	print(HMosca)