from random import *
"""
0, 1, 2, 3, 4, 
5, 6, 7, 8, 9,
10,11,12,13,14,
15,16,17,18,19,
20,21,22,23,24]
"""
class partida:
    def __init__(self):
        self.lista = []
        self.largo = 0
    def ubicar_minas(self,dificultad, **customizado):  # creacion y ubicacion de la mina y lista, esto no va en esta class
        nivel = [[8,8 , 10], [16, 16, 40], [16, 30, 99]]
        print("ded")
        if dificultad:
            ancho, largo, minas = nivel[dificultad - 1][0], nivel[dificultad - 1][1], nivel[dificultad - 1][2]
        else:
            ancho = customizado["ancho"]
            largo = customizado["largo"]
            minas = customizado["minas"]
        self.largo = largo
        lista = [[]] * (largo * ancho)
        lista = list(map(lambda x: cuadro(lista.index(x)), lista))# pichudisima
        for t in range(len(lista)- 1):
            lista[t].x = t
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
        print("innit",x)
        self.x = x
        self.activo =  False # si es True se muestra al usuario, independientemente si es bandera/ bomba / vacio o un numero
        self.bandera = False 
        self.mina = False 
        self.minas_alrededor = 0
        self.coordenadas_alrededor = [] # esta va a tener las instrucciones para ir a los vecinos del cuadro
        super().__init__()
    def retornar_unos_y_ceros(self):
        return self.minas_alrededor
    def alrededor_mina(self):
        arreglo = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

        for x in main.lista:
            coordenada = main.lista.index(x)
            alrededor = arreglo.copy()
            if coordenada >= len(main.lista) - main.largo:
                alrededor.pop()
                alrededor.pop()
                alrededor.pop()
            if coordenada < main.largo:
                alrededor.pop(0)
                alrededor.pop(0)
                alrededor.pop(0)
            if coordenada % main.largo == main.largo - 1:
                alrededor.remove([0, 1])
                try:
                    alrededor.remove([-1, 1])
                except:
                    pass
                try:
                    alrededor.remove([1, 1])
                except:
                    pass
            if not coordenada % main.largo:
                alrededor.remove([0, -1])
                try:
                    alrededor.remove([-1, -1])
                except:
                    pass
                try:
                    alrededor.remove([1, -1])
                except:
                    pass
            for y in alrededor:
                if main.lista[main.lista.index(x) + y[0] * main.largo + y[1]].mina:
                    main.lista[main.lista.index(x)].minas_alrededor += 1
                    main.lista[main.lista.index(x)].coordenadas_alrededor = alrededor
    def click(self, click_derecho ):
        #derecho activa casilla
        #izquierdo pone bandera
        if click_derecho :
            if not self.activo:
                if not self.bandera:
                    self.activo = True
                    if not self.mina:
                        if not self.minas_alrededor:
                            for y in self.coordenadas_alrededor:
                                click(main.lista[main.lista.index(self.x) + y[0] * main.largo + y[1]])
                    else:
                        return True
        else:
            self.bandera = not self.bandera

        #vecino = self.lista[self.lista(index(x) ]

main = partida()
main.ubicar_minas(1)
main.lista[0].alrededor_mina()
xr = 0
while xr < 64:
    print("cs",xr)
    print(main.lista[xr].x, " ")
    if  xr % 8  == 7 :
        print("\n")
    xr += 1
def f():
    while True:
        a = int(input("efef"))
        main.lista[a].click(True)
f()
