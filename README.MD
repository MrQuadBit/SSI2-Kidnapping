S = Sub Meta
A = Acción

Meta - Crear Episodio
	A0 - Inicializar actores
	S0 - Ejecutar Secuestro
	Si el HEROE ama al RAPTADO
		S1 - Obtener Información sobre el secuestro
		S2 - Ejecutar plan para salvar al RAPTADO
		A1 - Terminar la historia normal
	Si no ama al RAPTADO
		A2 - Terminar la historia abruptamente porque no hay una relación de amor

Sub Metas
	0 -Ejecutar Secuestro
		A3 - Traslado del VILLANO a la ubicación del RAPTADO
		A4 - Privar de la libertad al RAPTADO
		A5 - Trasladarse con el RAPTADO a la ubicación secreta
	1 - Obtener información sobre el secuestro
		Si HEROE no tiene acceso a ubicación del RAPTADO
			A6- Terminar la historia abruptamente porque no puede trasladarse
		A7 - Trasaladar al HEROE a la ubicación del INFORMANTE
		A8 - Saber qué quiere el INFORMANTE por la información (quien y a dónde se llevaron al RAPTADO)
		A9 - Conseguir el objeto que quiere el INFORMANTE
		A10 - Ejecutar intercambio entre HEROE e INFORMANTE
		A11 - Escuchar la información y el plan para salvar al RAPTADO
	2 - Ejecutar plan para salvar a la RAPTADO
		A12 - Trasladarse a la ubicación donde el VILLANO tiene al RAPTADO
		A13 - Ejecutar el plan del INFORMANTE

Acciones:
	0.-Inicializar actores
	1.-Terminar la historia normal
	2.-Terminar la historia abruptamente porque no hay una relación de amor
	3.-Traslado del VILLANO a la ubicación del RAPTADO
	4.-Privar de la libertad al RAPTADO
	5.-Trasladarse con el RAPTADO a la ubicación secreta
	6.-Terminar la historia abruptamente porque no puede trasladarse
	7.-Trasaladar al HEROE a la ubicación del INFORMANTE
	8.-Saber qué quiere el INFORMANTE por la información (quien y a dónde se llevaron al RAPTADO)
	9.-Conseguir el objeto que quiere el INFORMANTE
	10.-Ejecutar intercambio entre HEROE e INFORMANTE
	11.-Escuchar la información y el plan para salvar al RAPTADO
	12.-Trasladarse a la ubicación donde el VILLANO tiene al RAPTADO
	13.-Ejecutar el plan del INFORMANTE

Personajes:
	0.-Rick
	1.-Morty
	2.-Summer
	3.-Jerry
	4.-Beth
	5.-Hombre pajaro
	6.-Zeep
	7.-Diablo
	8.-Principe Nebulon
	9.-Hombre Mosca
	10.-Tammy

print(function.__doc__)