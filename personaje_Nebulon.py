from schema_Personaje import Personaje
from config_Objetos import *
from config_Ubicaciones import *
from config_Nombres import *

nombre 		  = NEBULON
identificador = 8
objeto_tiene  = EJERCITO
ubicacion 	  = MARTE
objeto_quiere = PISTOLA
ama 		  = []
odia 		  = [RICK]
razon_odio 	  = ["No le quiere dar su receta para crear concentrado de materia obscura"]
razon_raptado = "Estaba solo sin su ejercito"
sabe_rapto 	  = "Uno de sus soldados le estaba mientra sucedía el secuestro"
plan 		  = "Mandar a todo su ejercito de Zigerions para atacar a -Villano-, matarlo y posteriormente liberar y traer de vuelta al -RAPTADO-"

Nebulon = Personaje(nombre, identificador, objeto_tiene, ubicacion, objeto_quiere, ama, odia, razon_odio, razon_raptado, sabe_rapto, plan)

if __name__ == '__main__':
	print(Nebulon)