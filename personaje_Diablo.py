from schema_Personaje import Personaje
from config_Objetos import *
from config_Ubicaciones import *
from config_Nombres import *

nombre 		  = DIABLO
identificador = 7
objeto_tiene  = MANO
ubicacion 	  = MARTE
objeto_quiere = PISTOLA
ama 		  = []
odia 		  = [RICK, SUMMER]
razon_odio 	  = ["Le quito su trabajo haciendo objetos mágicos sin maldiciones","Le metió una putiza cuando se puso mamada"]
razon_raptado = "Estaba ocupado creando objetos mágicos con maldciones"
sabe_rapto 	  = "Llegó al infierno un testigo que murió durante el secuestro"
plan 		  = "Usar la mano del mono para pedir 2 deseos, el primero matar a -VILLANO- y segundo traer de vuelta y asalvo a -RAPTADO-"

Diablo = Personaje(nombre, identificador, objeto_tiene, ubicacion, objeto_quiere, ama, odia, razon_odio, razon_raptado, sabe_rapto, plan)

if __name__ == '__main__':
	print(Diablo)