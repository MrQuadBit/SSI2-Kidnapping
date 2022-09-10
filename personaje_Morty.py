from schema_Personaje import Personaje
from config_Objetos import *
from config_Ubicaciones import *
from config_Nombres import *

nombre 		  = MORTY
identificador = 1
objeto_tiene  = CELULAR
ubicacion 	  = ESCUELA
objeto_quiere = LLAVES
ama 		  = [RICK, BETH, SUMMER]
odia 		  = [RICK, ZEEP]
razon_odio 	  = ["Siempre lo saca de la escuela y no lo deja tener una vida normal", "Le hizo pasar un mal momento y casi lo deja morir dentro del MicroVerso"]
razon_raptado = "Estaba distraido observando a Jessica"
sabe_rapto 	  = "El secuetro sucedió cerca de su escuela y toda la secundaria se enteró"
plan 		  = "Masturbarse enfrente del -VILLANO- para que cierre los ojos del acto tan asqueroso y así puedan rescatar a -RAPTADO-"

Morty = Personaje(nombre, identificador, objeto_tiene, ubicacion, objeto_quiere, ama, odia, razon_odio, razon_raptado, sabe_rapto, plan)

if __name__ == '__main__':
	print(Morty)