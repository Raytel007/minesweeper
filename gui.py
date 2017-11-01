from tkinter import *
import progra_2
import tkinter.messagebox
listaMinasObjetos = []#Contiene listas de cada cuadrito y su botón respectivo



def eval(valor,obj):
    print("valor",obj.x,valor)
    if valor == -5:
        pass
    if valor == -1:
        tkinter.messagebox.showwarning("Noob", "Por lo menos sabes jugar?")
        quit()
    elif valor in [1,2,3,4,5,6,7,8]:
        for x in listaMinasObjetos:
            if x.cuadro == obj:
               x.cuadro = Button(mainFrame, text=valor, fg="black", bg="#FFFFFF", width=2, height=2, font=mainFont)
               x.cuadro.grid(row=x.x,column=x.y)
    elif not valor:
        for x in listaMinasObjetos:
            if x.cuadro == obj:
               x.cuadro = Button(mainFrame, fg="black", bg="#123456", width=2, height=2, font=mainFont)
               x.cuadro.grid(row=x.x,column=x.y)
        print(obj.coordenadas_alrededor)
        for y in obj.coordenadas_alrededor:
            #progra_2.main.lista[main.lista.index(self.x) + y[0] * progra_2.main.largo + y[1]]).click(True)
            coordenada = obj.x + y[0] * progra_2.main.largo + y[1]
            print("cordenada",coordenada)
            if not progra_2.main.lista[coordenada].activo:
                eval(progra_2.main.lista[coordenada].click(True),progra_2.main.lista[coordenada])

def demostrar(obj,x,y):

    valorDelClick = progra_2.main.lista[progra_2.main.lista.index(obj)].click(True)
   # print(x)
    #print(listaMinasObjetos)
    #for x in listaMinasObjetos:
       # for y in listaMinasObjetos:
            #pass
            #print(y)
           # if y[1].mina:
           #     print("si")

    #print(progra_2.main.lista[x * progra_2.mina.y].minas_alrededor)
    if obj.mina:
        #print(x," ",y)

        for par in listaMinasObjetos:
            #print("2")
            if par.cuadro== obj:

                progra_2.main.lista[progra_2.main.lista.index(par.cuadro)].click(True)
                par.boton= Button(mainFrame, width=2, height=2, bg="#FFFFFF")
                par.boton.grid(row=x,column=y)

   # progra_2.main.lista[progra_2.main.lista.index(obj)].activado = True
    print(valorDelClick)
    eval(valorDelClick,obj) 

class minasGUI:
    def __init__(self,boton, cuadro, x, y):
        self.x = x
        self.y = y
        self.boton = boton
        self.cuadro = cuadro
    def setupObj(self):
        self.boton.bind("<Button-1>", lambda x: demostrar(self.cuadro,self.x,self.y))
        self.boton.grid(row=self.x, column=self.y)

def listo_minas():
        global listaMinasObjetos, mainFrame
        progra_2.main.ubicar_minas(0,ancho= int (textA.get()),largo=int(textL.get()),minas=int(textM.get()))

        
        progra_2.main.lista[0].alrededor_mina()
        mainFrame = Frame(root)
        mainFrame.grid()
        for objeto in progra_2.main.lista:
            rowVar = progra_2.main.lista.index(objeto)//progra_2.main.largo#la fila
            columnVar = progra_2.main.lista.index(objeto)%progra_2.main.largo#la columna
            #print(rowVar) 
            listaMinasObjetos.append(minasGUI(Button(mainFrame, width=2,height=2, bg="#000000"), objeto, rowVar, columnVar) )

            #listaMinasObjetos[-1].boton.bind("<Button-1>",lambda x: demostrar(objeto))
            listaMinasObjetos[-1].setupObj()
            #listaMinasObjetos[-1].boton.grid(row=rowVar, column=columnVar)
            global container
            containerCustom.destroy() 
            container.destroy()
            
def pedirCustom(key):
    global textA,textL,textM, containerCustom
    #tkinter.messagebox.showinfo("personalizado", "personalizado, por favor escriba las caracteristicas del juego")

    containerCustom = Frame(root)
    containerCustom.grid(row=1)

    textA = StringVar()
    labelAncho = Label(containerCustom, text = "Ancho: ", fg = mainFg, bg = mainBg, font = mainFont, width = mainWidth)
    entryAncho = Entry(containerCustom, textvariable = textA)
    textL = StringVar()
    labelLargo = Label(containerCustom, text = "Largo: ", fg = mainFg, bg = mainBg, font=mainFont, width = mainWidth)
    entryLargo = Entry(containerCustom, textvariable = textL)
    textM = StringVar()
    labelMinas = Label(containerCustom, text = "Minas: ", fg = mainFg, bg = mainBg, font = mainFont, width = mainWidth)
    entryMinas = Entry(containerCustom, textvariable=textM)

    readyButt = Button(containerCustom, text = "Ok", fg = mainFg, bg = mainBg, font = mainFont, width = mainWidth, command = listo_minas)

    readyButt.grid(row = 3, column = 0)
    labelAncho.grid(row = 0, column = 0)
    entryAncho.grid(row = 0, column = 1)
    labelLargo.grid(row = 1, column = 0)
    entryLargo.grid(row = 1, column = 1)
    labelMinas.grid(row = 2, column = 0)
    entryMinas.grid(row = 2, column = 1)

   

def Game(players, multiplayer):
    menuFrame.destroy()
    global container
    container = Frame(root, bd=10, relief="groove")# freme kja :v

    #8x8
    mode1Butt = Button(container, text = "8x8", fg = mainFg,bg = mainBg, font = mainFont, width = mainWidth, command= lambda: progra_2.main.ubicar_minas(1))
    #16x16
    mode2Butt = Button(container, text="16x16", fg=mainFg,bg=mainBg,font = mainFont, width = mainWidth, command= lambda: progra_2.main.ubicar_minas(2))
    #30x16
    mode3Butt = Button(container, text="30x16", fg=mainFg,bg=mainBg,font=mainFont,width=mainWidth, command= lambda: progra_2.main.ubicar_minas(3))
    #Custom
    mode4Butt = Button(container, text="Custom", fg=mainFg,bg=mainBg,font=mainFont,width=mainWidth)

    mode4Butt.bind("<Button-1>", pedirCustom)


    container.grid()
    mode1Butt.grid(row=0,column=0)
    mode2Butt.grid(row=0,column=1)
    mode3Butt.grid(row=1,column=0)
    mode4Butt.grid(row=1,column=1)

root = Tk()

root.title("Minesweeper")
root.configure(background="#555555")
#root.geometry("400x400")
mainFont = ("Times", 11, "bold")
mainFg = "black"
mainBg = "#FFFFFF"
mainWidth = 16 #ancho de botones
menuFrame = Frame(root, bd = 10, relief="groove")
OnePlayerL = Button(menuFrame, width=mainWidth,text="1-Player",fg=mainFg,bg=mainBg,font=mainFont,command=lambda: Game(1,False))
TwoPlayerL = Button(menuFrame, width=mainWidth,text="2-Player",fg= mainFg,bg=mainBg,font=mainFont,command=lambda: Game(2,False))
TwoPlayerM = Button(menuFrame, width=mainWidth,text="2-Player \nMultiplayer",fg=mainFg,bg=mainBg,font=mainFont,command=lambda: Game(2,True))




menuFrame.grid(row=0,column=2,sticky="E")
OnePlayerL.grid(row=0,column=0)
TwoPlayerL.grid(row=1,column=0)
TwoPlayerM.grid(row=2,column=0)


root.mainloop()
