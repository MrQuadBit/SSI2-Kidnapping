from schema_Personaje import Personaje
from config_Objetos import *
from config_Ubicaciones import *
from config_Nombres import *

nombre 		  = JERRY
identificador = 3
objeto_tiene  = LLAVES
ubicacion 	  = CASA
objeto_quiere = PUERTA
ama 		  = [BETH, MORTY, SUMMER]
odia 		  = [RICK]
razon_odio 	  = ["Acapara la atención de su familia"]
razon_raptado = "Es muy debil y tonto"
sabe_rapto 	  = "Estaba estaba escondido observando todo mientras el rapto ocurría"
plan 		  = "Hacer una replica del titanic y así undir al barco junto con -VILLANO-, para poder subir a -RAPTADO- en una puerta y poderle salvar"

Jerry = Personaje(nombre, identificador, objeto_tiene, ubicacion, objeto_quiere, ama, odia, razon_odio, razon_raptado, sabe_rapto, plan)

if __name__ == '__main__':
	print(Jerry)