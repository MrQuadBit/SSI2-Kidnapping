from schema_Personaje import Personaje
from config_Objetos import *
from config_Ubicaciones import *
from config_Nombres import *

nombre 		  = SUMMER
identificador = 2
objeto_tiene  = CELULAR
ubicacion 	  = CENTRO_COMERCIAL
objeto_quiere = CLON
ama 		  = [RICK, BETH, SUMMER]
odia 		  = [RICK, MORTY, TAMMY, DIABLO]
razon_odio 	  = ["Porque prefiere a Morty que a ella para sus aventuras", "Porque siempre acapara la diversión con el Abuelo Rick", "Porque es una amiga traicionera", "Sólo la uso para poder hacer crecer su tienda de objetos mágicos"]
razon_raptado = "Estaba distraida viendo tiktoks en su celular"
sabe_rapto 	  = "Vío el estatus de -VILLANO- en Twitter que decía '#RaptandoA-Raptado- #YaNoHayRespeto #jajaja #EstoyEn-UBICACION-'"
plan 		  = "Envíarle DM al -VILLANO- por Twitter y decirle que si no deja libre a -RAPTADO- publicará las fotos de su trasero que le tomaron mientras hacia el secuetro"

Summer = Personaje(nombre, identificador, objeto_tiene, ubicacion, objeto_quiere, ama, odia, razon_odio, razon_raptado, sabe_rapto, plan)

if __name__ == '__main__':
	print(Summer)