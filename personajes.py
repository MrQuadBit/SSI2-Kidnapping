from personaje_Beth import Beth
from personaje_Diablo import Diablo
from personaje_HMosca import HMosca
from personaje_HPajaro import HPajaro
from personaje_Jerry import Jerry
from personaje_Morty import Morty
from personaje_Nebulon import Nebulon
from personaje_Rick import Rick
from personaje_Summer import Summer
from personaje_Tammy import Tammy
from personaje_Zeep import Zeep

personajes = [Rick, Morty, Summer, Jerry, Beth, HPajaro, Zeep, Diablo, Nebulon, HMosca, Tammy]

if __name__ == "__main__":
	for p in personajes:
		print(p.dameIdentificador(), p.dameNombre())