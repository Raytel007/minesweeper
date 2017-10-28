"""		#cantidad de minas , si es multijugador o no
def Partida(nivel, multi):
	coordena = input("el mouse")
			
class cuadro(inicio):
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.activo =  False # si es True se muestra al usuario, independientemente si es bandera/ bomba / vacio o un numero
		self.bandera = False 
		self.mina = False 
		self.minas_alrededor = 0
		
	def click(self, jugador):
		if not self.activo:
			if not self.bandera:
				if self.mina:
					return "boom bitch" 
				elif self.minas_alrededor:
					return self.minas_alrededor
				else:
					pass
"""
def ubicar_minas(): # creacion y ubicacion de la mina y matriz, esto no va en esta clas
		nivel = [[8,8,10],[16,16,40],[16,30,99]]
		dificultad = input("digite: 0 ")
		while True:
			try:
				dificultad = int(dificultad)
				break
			except:
				pass
		if dificultad:
			ancho,largo,minas = nivel[dificultad][0],nivel[dificultad][1],nivel[dificultad][2]
		else:
			matriz = []
			while True:
				ancho = input()
				largo = input()
				minas = input()
				try:
					ancho = int(ancho)
					largo = int(largo)
					minas = int(minas)
					if ancho >= 5 and ancho <= 20 and largo >= 5 and largo <= 20 and minas >= 1 and minas < largo * ancho:
						break
				except:
					pass
		matriz = [[[]] * largo] * ancho
		for x in range(ancho):
			print(matriz[x])
			
		
ubicar_minas()
