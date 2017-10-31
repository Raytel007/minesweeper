from random import *

class partida:
    def __init__(self):
        self.lista = []
        self.largo = 0

    def alrededor(self):
        arreglo = [-1, 0, 1]
        for x in self.lista:
            coordenada = self.lista.index(x)

    def ubicar_minas(self,dificultad, **customizado):  # creacion y ubicacion de la mina y lista, esto no va en esta class
        # prsado = 0 #   1    ,     2    ,     3
        nivel = [[8, 8, 10], [16, 16, 40], [16, 30, 99]]

        if dificultad:
            ancho, largo, minas = nivel[dificultad - 1][0], nivel[dificultad - 1][1], nivel[dificultad - 1][2]
        else:
            ancho = customizado["ancho"]
            largo = customizado["largo"]
            minas = customizado["minas"]
        self.largo = largo
        lista = [[]] * (largo * ancho)
        lista = list(map(lambda x: cuadro(lista.index(x)), lista))

        while minas:
            x = choice(lista)
            if not x.mina:
                lista[lista.index(x)].mina = True
                minas -= 1
        self.lista = lista

    def retornando_lista(self):
        return self.lista


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

            #vecino = self.lista[self.lista(index(x) ]
main = partida()
