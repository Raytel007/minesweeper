from tkinter import *
import progra_2
def Game(players, multiplayer):
    menuFrame.destroy()
    container = Frame(root, bd=10, relief="groove")# freme kja :v

    #8x8
    mode1Butt = Button(container, text = "8x8", fg = mainFg,bg = mainBg, font = mainFont, width = mainWidth, command= lambda: progra_2.ubicar_minas(1))
    #16x16
    mode2Butt = Button(container, text="16x16", fg=mainFg,bg=mainBg,font = mainFont, width = mainWidth, command= lambda: progra_2.ubicar_minas(2))
    #30x16
    mode3Butt = Button(container, text="30x16", fg=mainFg,bg=mainBg,font=mainFont,width=mainWidth, command= lambda: progra_2.ubicar_minas(3))
    #Custom
    mode4Butt = Button(container, text="Custom", fg=mainFg,bg=mainBg,font=mainFont,width=mainWidth, command= lambda: progra_2.ubicar_minas(0))


    container.grid()
    mode1Butt.grid(row=0,column=0)
    mode2Butt.grid(row=0,column=1)
    mode3Butt.grid(row=1,column=0)
    mode4Butt.grid(row=1,column=1)

root = Tk()

root.title("Minesweeper")
root.configure(background="#555555")
root.geometry("400x400")
mainFont = ("Times", 11, "bold")
mainFg = "black"
mainBg = "#FFFFFF"
mainWidth = 16 #ancho de botones
menuFrame = Frame(root, bd = 10, relief="groove")
OnePlayerL = Button(menuFrame, width=mainWidth,text="1-Player",fg=mainFg,bg=mainBg,font=mainFont,command=lambda: Game(1,False))
TwoPlayerL = Button(menuFrame, width=mainWidth,text="2-Player",fg=mainFg,bg=mainBg,font=mainFont,command=lambda: Game(2,False))
TwoPlayerM = Button(menuFrame, width=mainWidth,text="2-Player \nMultiplayer",fg=mainFg,bg=mainBg,font=mainFont,command=lambda: Game(2,True))

menuFrame.grid(row=0,column=2,sticky="E")
OnePlayerL.grid(row=0,column=0)
TwoPlayerL.grid(row=1,column=0)
TwoPlayerM.grid(row=2,column=0)


root.mainloop()
