from random import *
        #cantida minas , si es multijugador o no

class partida:
    def __init__(self):
        self.matriz = None
    def ubicar_minas(self,dificultad, **customizado):  # creacion y ubicacion de la mina y matriz, esto no va en esta class
        # prsado = 0 #   1    ,     2    ,     3
        nivel = [[8, 8, 10], [16, 16, 40], [16, 30, 99]]
        ancho = customizado["ancho"]
        largo = customizado["largo"]
        minas = customizado["minas"]
        while True:
            try:
                dificultad = int(dificultad)
                break
            except:
                pass
        if dificultad:
            ancho, largo, minas = nivel[dificultad - 1][0], nivel[dificultad - 1][1], nivel[dificultad - 1][2]
        else:
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
        matriz = [[]] * (largo * ancho)
        matriz = list(map(lambda x: cuadro(matriz.index(x)), matriz))
        while minas:
            x = choice(matriz)
            if x.mina:
                pass
            else:
                matriz[matriz.index(x)].mina = True
                minas -= 1
        self.matriz = matriz
    def retornando(self):
        return self.matriz

class cuadro:
    def __init__(self, x):
        self.x = x
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
main = partida()