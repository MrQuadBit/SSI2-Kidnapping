from schema_Personaje import Personaje
from config_Objetos import *
from config_Ubicaciones import *
from config_Nombres import *

nombre 		  = BETH
identificador = 4
objeto_tiene  = CLON
ubicacion 	  = CASA
objeto_quiere = VACACIONES
ama 		  = [RICK, MORTY, SUMMER]
odia 		  = [RICK, JERRY]
razon_odio 	  = ["La abanonó cuando era una niña pequeña","La hizo sentir mal durante muchos años"]
razon_raptado = "Estaba ocupada haciendo Yoga"
sabe_rapto 	  = "Porque su clone estaba en el lugar del secuestro y le avisó telepaticamente a Beth"
plan 		  = "Usar al clone de Beth para seducir a -Villano- se case con él, puedan hacer una familia nueva y se olvide de -RAPTADO-"

Beth = Personaje(nombre, identificador, objeto_tiene, ubicacion, objeto_quiere, ama, odia, razon_odio, razon_raptado, sabe_rapto, plan)

if __name__ == '__main__':
	print(Beth)