from schema_Personaje import Personaje
from config_Objetos import *
from config_Ubicaciones import *
from config_Nombres import *

nombre 		  = ZEEP
identificador = 6
objeto_tiene  = BATERIA
ubicacion 	  = ESTACIONAMIENTO
objeto_quiere = PISTOLA
ama 		  = []
odia 		  = [RICK]
razon_odio 	  = ["Porque le hizo darse cuenta que la razón de se existencia sólo sirve para generar la energía de su Crucero Espacial"]
razon_raptado = "Estaba dentro de la batería MicroVerso"
sabe_rapto 	  = "Desde dentro del coche se esuchó todo el rapto"
plan 		  = "Usar la Batería MicroVerso para crear un rayp laser que pulverize a -VILLANO- y así poder rescatar a -RAPTADO-"

Zeep = Personaje(nombre, identificador, objeto_tiene, ubicacion, objeto_quiere, ama, odia, razon_odio, razon_raptado, sabe_rapto, plan)

if __name__ == '__main__':
	print(Zeep)