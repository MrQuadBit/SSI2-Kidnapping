class Personaje(object):
	"""docstring para Personaje"""
	__nombre	   :str  = ""
	__identificador:int  = 0
	__objeto_tiene :str  = ""
	__ubicacion	   :str  = ""
	__objeto_quiere:str  = ""
	__ama 		   :list = []
	__odia		   :list = []
	__razon_odio   :list = []
	__razon_raptado:str  = ""
	__sabe_rapto   :str  = ""
	__plan		   :str  = ""

	def __init__(self, nombre, identificador, objeto_tiene, ubicacion, objeto_quiere, ama, odia, razon_odio, razon_raptado, sabe_rapto, plan):
		self.__nombre = nombre
		self.__identificador = identificador
		self.__objeto_tiene = objeto_tiene
		self.__ubicacion = ubicacion
		self.__objeto_quiere = objeto_quiere
		self.__ama = ama
		self.__odia = odia
		self.__razon_odio = razon_odio
		self.__razon_raptado = razon_raptado
		self.__sabe_rapto = sabe_rapto
		self.__plan = plan

	def __str__(self):
		descripcion = f"""
		nombre = {self.__nombre}
		identificador = {self.__identificador}
		objeto_tiene = {self.__objeto_tiene}
		ubicacion = {self.__ubicacion}
		objeto_quiere = {self.__objeto_quiere}
		ama = {self.__ama}
		odia = {self.__odia}
		razon_odio = {self.__razon_odio}
		razon_raptado = {self.__razon_raptado}
		sabe_rapto = {self.__sabe_rapto}
		plan = {self.__plan}
		"""
		return descripcion

	def dameNombre(self):
		return self.__nombre

	def dameIdentificador(self):
		return self.__identificador

	def damePersonajesAma(self):
		return self.__ama

	def ama(self, personaje):
		personajes_ama = self.damePersonajesAma()
		return True if personaje.dameNombre() in personajes_ama else False
