from schema_Personaje import Personaje
from config_Objetos import *
from config_Ubicaciones import *
from config_Nombres import *

nombre 		  = HPAJARO
identificador = 5
objeto_tiene  = HUEVO
ubicacion 	  = MARTE
objeto_quiere = COMPA
ama 		  = [TAMMY]
odia 		  = [RICK]
razon_odio 	  = ["No quiso vincular su alma y volverse su compañero espiritual"]
razon_raptado = "Estaba en una fiesta buscando compañero espiritual"
sabe_rapto 	  = "Dentro de una de sus platicas en busqueda de compañero espiritual escuchó sobre el secuestro"
plan 		  = "Intercambiar con el -VILLANO- el Huevo de oro por el -RAPTADO-, ya que el -VILLANO- ama el oro"

HPajaro = Personaje(nombre, identificador, objeto_tiene, ubicacion, objeto_quiere, ama, odia, razon_odio, razon_raptado, sabe_rapto, plan)

if __name__ == '__main__':
	print(HPajaro)