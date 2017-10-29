from random import *
        #cantida minas , si es multijugador o no

class partida:
    def __init__(self):
        self.matriz = []
    def ubicar_minas(self,dificultad, **customizado):  # creacion y ubicacion de la mina y matriz, esto no va en esta class
        # prsado = 0 #   1    ,     2    ,     3
        nivel = [[8, 8, 10], [16, 16, 40], [16, 30, 99]]
        if dificultad:
            ancho, largo, minas = nivel[dificultad - 1][0], nivel[dificultad - 1][1], nivel[dificultad - 1][2]
        else:
            ancho = customizado["ancho"]
            largo = customizado["largo"]
            minas = customizado["minas"]
        matriz = [[]] * (largo * ancho)
        matriz = list(map(lambda x: cuadro(matriz.index(x)), matriz))
        while minas:
            x = choice(matriz)
            if not x.mina:
                matriz[matriz.index(x)].mina = True
                minas -= 1
        self.matriz = matriz
    def retornando(self):
        return self.matriz
class cuadro(partida):
    def __init__(self, x):
        self.x = x
        self.activo =  False # si es True se muestra al usuario, independientemente si es bandera/ bomba / vacio o un numero
        self.bandera = False 
        self.mina = False 
        self.minas_alrededor = 0
        super().__init__()
    def click(self, click):
        #derecho activa casilla
        #izquierdo pone bandera
        if click:
            if not self.activo:
                if not self.bandera:
                    if self.mina:
                        return "boom bitch"
                    elif self.minas_alrededor:
                        return self.minas_alrededor
                    else:
                        self.activo = True

        else:
            self.bandera = not self.bandera
    def alrededor(self):
        pass
main = partida()
