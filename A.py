import random
import math
import time
class Pancakes:
	def __init__(self, pancakes):
		self.pancakes = pancakes
		self.orden = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m","n", "o", "p", "q", "r", "s", "t", "u", "v","w", "x", "y", "z"]
		self.nodos = 0
	def voltear(self, posicion, pancakes):
		return pancakes[0:len(pancakes)-posicion] + pancakes[len(pancakes)-posicion:len(pancakes)][::-1]

	def h(self, nodo):
		c = 0
		if (nodo[0] != "a" and nodo[0] != "b"):
			c = 1
		for i in range(len(nodo)-1):
			if (abs(self.orden.index(nodo[i])-self.orden.index(nodo[i+1])) > 1):
				c += 1
		return c
	 
	def busqAStar(self, nodo):
		cola = [(nodo, ["0"], 0)]
		meta = self.orden[0:len(nodo)]
		nodos = 0
		while cola:
			pancakes, camino, puntuacion = cola.pop(0)
			if pancakes == meta:
				return " ".join(camino[1:])
			for i in range(2, len(nodo)+1):
				if i == int(camino[-1]):
					continue
				nodo_volt = self.voltear(i, pancakes)
				if cola and self.h(nodo_volt) <= self.h(cola[0][0]):
					cola.insert(0,(nodo_volt, camino + [str(i)], self.h(nodo_volt)))
				else:
					cola.append((nodo_volt, camino + [str(i)], self.h(nodo_volt)))
				nodos += 1


pancakes = ["a", "b", "c", "d", "e", "f", "g", "h"]#, "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
random.shuffle(pancakes)
prueba = Pancakes(pancakes)
print(f"Pancakes inicio: {pancakes}")
print(prueba.busqAStar(pancakes))



