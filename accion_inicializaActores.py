from personajes import personajes
def inicializaActoresPorNombre(VILLANO, RAPTADO, HEROE, INFORMANTE):
	print("inicializaActoresPorNombre")
	actores = {}
	for p in personajes:
		if p.dameNombre() == VILLANO:
			actores["villano"] = p
		elif p.dameNombre() == RAPTADO:
			actores["raptado"] = p
		elif p.dameNombre() == HEROE:
			actores["heroe"] = p
		elif p.dameNombre() == INFORMANTE:
			actores["informante"] = p
	return actores

def inicializaActoresPorIdentificador(VILLANO, RAPTADO, HEROE, INFORMANTE):
	print(inicializaActoresPorIdentificador)
	actores = {}
	actores["villano"] = personajes[VILLANO]
	actores["raptado"] = personajes[RAPTADO]
	actores["heroe"] = personajes[HEROE]
	actores["informante"] = personajes[INFORMANTE]

	return actores