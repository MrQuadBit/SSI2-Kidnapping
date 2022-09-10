from schema_Personaje import Personaje
from config_Objetos import *
from config_Ubicaciones import *
from config_Nombres import *

nombre 		  = TAMMY
identificador = 10
objeto_tiene  = CELULAR
ubicacion 	  = CENTRO_COMERCIAL
objeto_quiere = PISTOLA
ama 		  = [HPAJARO]
odia 		  = [RICK, SUMMER]
razon_odio 	  = ["No quiere compartir los planos para construir la pistola de portales", "Se besó con Brad en un fiesta sabiendo que a ella le gustaba"]
razon_raptado = "Estaba Squancheando en una fiesta"
sabe_rapto 	  = "Es la lider de la confederación galactica y tiene hombres de informantes que vieron el secuestro"
plan 		  = "Mandar a todos los perteneciente de la confederación galactica a atacar a -VILLANO- y mientras este se defiende rescatar a -RAPTADO-"

Tammy = Personaje(nombre, identificador, objeto_tiene, ubicacion, objeto_quiere, ama, odia, razon_odio, razon_raptado, sabe_rapto, plan)

if __name__ == '__main__':
	print(Tammy)