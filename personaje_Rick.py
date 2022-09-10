from schema_Personaje import Personaje
from config_Objetos import *
from config_Ubicaciones import *
from config_Nombres import *

nombre 		  = RICK
identificador = 0
objeto_tiene  = PISTOLA
ubicacion 	  = CASA
objeto_quiere = "cualquiera"
ama 		  = [BETH, MORTY, SUMMER]
odia 		  = TODOS_NOMBRES
razon_odio 	  = ["Él cree que todos son unos imbeciles sin excepción"]
razon_raptado = "Estaba borracho"
sabe_rapto 	  = "Es el más listo del universo"
plan 		  = "Usar la pistola para traer a -RAPTADO- de vuelta y mandar a -VILLANO- al universo -UNIVERSO-"

Rick = Personaje(nombre, identificador, objeto_tiene, ubicacion, objeto_quiere, ama, odia, razon_odio, razon_raptado, sabe_rapto, plan)

if __name__ == '__main__':
	print(Rick)