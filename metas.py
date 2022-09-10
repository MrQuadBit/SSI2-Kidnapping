from config_Nombres import *
from acciones import acciones
from submetas import submetas
def crearEpisodio(VILLANO, RAPTADO, HEROE, INFORMANTE):
	#A0 - Inicializar actores
	actores = acciones[0](VILLANO, RAPTADO, HEROE, INFORMANTE)
	villano = actores["villano"]
	raptado = actores["raptado"]
	heroe = actores["heroe"]
	informante = actores["informante"]
	#S0 - Ejecutar Secuestro
	submetas[0]()

	#Si el HEROE ama al RAPTADO
	if heroe.ama(raptado):
		#S1 - Obtener Información sobre el secuestro
		submetas[1]()
		#S2 - Ejecutar plan para salvar al RAPTADO
		submetas[2]()
		#A1 - Terminar la historia normal
		acciones[1]()
	#Si no ama al RAPTADO
	else:
		#A2 - Terminar la historia abruptamente porque no hay una relación de amor
		acciones[2]()
