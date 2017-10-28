from tkinter import *

def Game(players, multiplayer):
    menuFrame.destroy()
    container = Frame(root, bd=10, relief="groove")

    #8x8
    mode1Butt = Button(container, text="8x8", fg=mainFg,bg=mainBg,font=mainFont,width=mainWd)
    #16x16
    mode2Butt = Button(container, text="16x16", fg=mainFg,bg=mainBg,font=mainFont,width=mainWd)
    #30x16
    mode3Butt = Button(container, text="30x16", fg=mainFg,bg=mainBg,font=mainFont,width=mainWd)
    #Custom
    mode4Butt = Button(container, text="Custom", fg=mainFg,bg=mainBg,font=mainFont,width=mainWd)


    container.grid()
    mode1Butt.grid(row=0,column=0)
    mode2Butt.grid(row=0,column=1)
    mode3Butt.grid(row=1,column=0)
    mode4Butt.grid(row=1,column=1)

root = Tk()

root.title("Minesweeper")
root.configure(background="#555555")
root.geometry("400x400+100+100")
mainFont = ("Times", 11, "bold")
mainFg = "black"
mainBg = "#FFFFFF"
mainWd = 15
menuFrame = Frame(root, bd=10, relief="groove")
OnePlayerL = Button(menuFrame, width=mainWd,text="1-Player",fg=mainFg,bg=mainBg,font=mainFont,command=lambda: Game(1,False))
TwoPlayerL = Button(menuFrame, width=mainWd,text="2-Player",fg=mainFg,bg=mainBg,font=mainFont,command=lambda: Game(2,False))
TwoPlayerM = Button(menuFrame, width=mainWd,text="2-Player \nMultiplayer",fg=mainFg,bg=mainBg,font=mainFont,command=lambda: Game(2,True))

menuFrame.grid(row=0,column=2,sticky="E")
OnePlayerL.grid(row=0,column=0)
TwoPlayerL.grid(row=1,column=0)
TwoPlayerM.grid(row=2,column=0)

root.mainloop()
