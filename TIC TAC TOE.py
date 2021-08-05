import tkinter.messagebox
from tkinter import*

root =Tk()
root.geometry("1350x750+0+0")
root.title("TIC TAC TOE")
root.configure(background="Cadet Blue")


Tops = Frame(root, bg="Cadet Blue", pady=2, width=1350, height=100, relief=RIDGE)
Tops.grid(row=0,column = 0)

lblTitle =Label(Tops, font=('arial',50,'bold'), text="ADVANCED TIC TAC TOE GAME", bd= 21, bg='Cadet Blue', fg='cornsilk', justify= CENTER)
lblTitle.grid(row=0,column = 0)

MainFrame = Frame(root, bg='Powder Blue', bd= 10, width=1350, height=600, relief=RIDGE)
MainFrame.grid(row=1,column = 0)

LeftFrame = Frame(MainFrame, bd= 10, width=750, height=500, padx=10, pady=2, bg="Cadet Blue", relief=RIDGE)
LeftFrame.pack(side=LEFT)

RightFrame = Frame(MainFrame, bd=10, width=560, height=500, padx=10, pady=2, bg="Cadet Blue", relief=RIDGE)
RightFrame.pack(side=RIGHT)

RightFrame1 = Frame(RightFrame, bd=10, width=400, height=200, padx=10, pady=2, bg="Cadet Blue", relief=RIDGE)
RightFrame1.grid(row=0,column = 0)

RightFrame2 = Frame(RightFrame, bd=10, width=400, height=200, padx=10, pady=2, bg="Cadet Blue", relief=RIDGE)
RightFrame2.grid(row=1,column = 0)

PlayerX=IntVar()
PlayerO=IntVar()

PlayerX.set(0)
PlayerO.set(0)

buttons = StringVar()
click = True

def checker(buttons):
    global click
    if buttons["text"] ==" " and click == True:
        buttons["text"] = "X"
        click = False
        scorekeeper()
    elif buttons["text"] == " " and click == False:
        buttons["text"] = "O"
        click = True
        scorekeeper()

def scorekeeper():
    if(button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X"):
        button1.configure(background="Powder Blue")
        button2.configure(background="Powder Blue")
        button3.configure(background="Powder Blue")
        n = float(PlayerX.get() )
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("RESULT", "PLAYER X WON THE GAME \n \nPLAYER O BETTER LUCK NEXT TIME")
    
    if(button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X"):
        button4.configure(background="Light Green")
        button5.configure(background="Light Green")
        button6.configure(background="Light Green")
        n = float(PlayerX.get() )
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("RESULT", "PLAYER X WON THE GAME \n \nPLAYER O BETTER LUCK NEXT TIME")

    if(button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X"):
        button7.configure(background="Orange")
        button8.configure(background="Orange")
        button9.configure(background="Orange")
        n = float(PlayerX.get() )
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("RESULT", "PLAYER X WON THE GAME \n \nPLAYER O BETTER LUCK NEXT TIME")

    if(button3["text"]=="X" and button5["text"]=="X" and button7["text"]=="X"):
        button3.configure(background="Blue")
        button5.configure(background="Blue")
        button7.configure(background="Blue")
        n = float(PlayerX.get() )
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("RESULT", "PLAYER X WON THE GAME \n \nPLAYER O BETTER LUCK NEXT TIME")

    if(button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X"):
        button1.configure(background="Red")
        button5.configure(background="Red")
        button9.configure(background="Red")
        n = float(PlayerX.get() )
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("RESULT", "PLAYER X WON THE GAME \n \nPLAYER O BETTER LUCK NEXT TIME")

    if(button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X"):
        button1.configure(background="Yellow")
        button4.configure(background="Yellow")
        button7.configure(background="Yellow")
        n = float(PlayerX.get() )
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("RESULT", "PLAYER X WON THE GAME \n \nPLAYER O BETTER LUCK NEXT TIME")

    if(button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X"):
        button2.configure(background="Pink")
        button5.configure(background="Pink")
        button8.configure(background="Pink")
        n = float(PlayerX.get() )
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("RESULT", "PLAYER X WON THE GAME \n \nPLAYER O BETTER LUCK NEXT TIME")

    if(button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X"):
        button3.configure(background="Aqua")
        button6.configure(background="Aqua")
        button9.configure(background="Aqua")
        n = float(PlayerX.get() )
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("RESULT", "PLAYER X WON THE GAME \n \nPLAYER O BETTER LUCK NEXT TIME")


    if(button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O"):
        button1.configure(background="Peach puff")
        button2.configure(background="Peach puff")
        button3.configure(background="Peach puff")
        n = float(PlayerO.get() )
        score = (n+1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("RESULT", "PLAYER O WON THE GAME \n \nPLAYER X BETTER LUCK NEXT TIME")
    
    if(button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O"):
        button4.configure(background="Grey")
        button5.configure(background="Grey")
        button6.configure(background="Grey")
        n = float(PlayerO.get() )
        score = (n+1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("RESULT", "PLAYER O WON THE GAME \n \nPLAYER X BETTER LUCK NEXT TIME")

    if(button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O"):
        button7.configure(background="Blanched ALmond")
        button8.configure(background="Blanched ALmond")
        button9.configure(background="Blanched ALmond")
        n = float(PlayerO.get() )
        score = (n+1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("RESULT", "PLAYER O WON THE GAME \n \nPLAYER X BETTER LUCK NEXT TIME")

    if(button3["text"]=="O" and button5["text"]=="O" and button7["text"]=="O"):
        button3.configure(background="Dark khaki")
        button5.configure(background="Dark khaki")
        button7.configure(background="Dark khaki")
        n = float(PlayerO.get() )
        score = (n+1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("RESULT", "PLAYER O WON THE GAME \n \nPLAYER X BETTER LUCK NEXT TIME")

    if(button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O"):
        button1.configure(background="Sandy brown")
        button5.configure(background="Sandy brown")
        button9.configure(background="Sandy brown")
        n = float(PlayerO.get() )
        score = (n+1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("RESULT", "PLAYER O WON THE GAME \n \nPLAYER X BETTER LUCK NEXT TIME")

    if(button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O"):
        button1.configure(background="violet")
        button4.configure(background="violet")
        button7.configure(background="violet")
        n = float(PlayerO.get() )
        score = (n+1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("RESULT", "PLAYER O WON THE GAME \n \nPLAYER X BETTER LUCK NEXT TIME")

    if(button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O"):
        button2.configure(background="MistyRose2")
        button5.configure(background="MistyRose2")
        button8.configure(background="MistyRose2")
        n = float(PlayerO.get() )
        score = (n+1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("RESULT", "PLAYER O WON THE GAME \n \nPLAYER X BETTER LUCK NEXT TIME")

    if(button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O"):
        button3.configure(background="Rosy brown")
        button6.configure(background="Rosy brown")
        button9.configure(background="Rosy brown")
        n = float(PlayerO.get() )
        score = (n+1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("RESULT", "PLAYER O WON THE GAME \n \nPLAYER X BETTER LUCK NEXT TIME")


def Reset():
    button1["text"]=" "
    button2["text"]=" "
    button3["text"]=" "
    button4["text"]=" "
    button5["text"]=" "
    button6["text"]=" "
    button7["text"]=" "
    button8["text"]=" "
    button9["text"]=" "

    button1.configure(background="Gainsboro")
    button2.configure(background="Gainsboro")
    button3.configure(background="Gainsboro")
    button4.configure(background="Gainsboro")
    button5.configure(background="Gainsboro")
    button6.configure(background="Gainsboro")
    button7.configure(background="Gainsboro")
    button8.configure(background="Gainsboro")
    button9.configure(background="Gainsboro")

def NewGame():
    Reset()
    PlayerX.set(0)
    PlayerO.set(0)

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx PLAYER X AND O xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

lblPlayerX =Label(RightFrame1, font=('arial',40,'bold'), text="Player X :", padx=2, pady=2, bg='Cadet Blue')
lblPlayerX.grid(row=0, column = 0, sticky=W)

txtPlayerX= Entry(RightFrame1, font=('arial',40,'bold'), bd=2, fg="black", textvariable= PlayerX, width=14, 
                    justify= LEFT).grid(row=0, column= 1)

lblPlayerO =Label(RightFrame1, font=('arial',40,'bold'), text="Player O :", padx=2, pady=2, bg='Cadet Blue')
lblPlayerO.grid(row=1, column = 0, sticky=W)

txtPlayerO= Entry(RightFrame1, font=('arial',40,'bold'), bd=2, fg="black", textvariable= PlayerO, width=14, 
                    justify= LEFT).grid(row=1, column= 1)

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx BUTTON RESET AND NEW GAME xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

btnReset = Button(RightFrame2, text="RESET", font=('Times',40,'bold'), height= 1, width=20, bg="Gainsboro", command= Reset)
btnReset.grid(row=0, column=0, padx=6, pady=11)

btnNewGame = Button(RightFrame2, text="NEW GAME", font=('Times',40,'bold'), height= 1, width=20, bg="Gainsboro", command= NewGame)
btnNewGame.grid(row=1, column=0, padx=6, pady=10)

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx BUTTONS OF X AND O xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

button1 = Button(LeftFrame, text=" ", font=('Times',26,'bold'), height= 3, width=8, bg="Gainsboro", command=lambda:checker(button1))
button1.grid(row=1, column=0, sticky = S+N+E+W)

button2 = Button(LeftFrame, text=" ", font=('Times',26,'bold'), height= 3, width=8, bg="Gainsboro", command=lambda:checker(button2))
button2.grid(row=1, column=1, sticky = S+N+E+W)

button3 = Button(LeftFrame, text=" ", font=('Times',26,'bold'), height= 3, width=8, bg="Gainsboro", command=lambda:checker(button3))
button3.grid(row=1, column=2, sticky = S+N+E+W)

button4 = Button(LeftFrame, text=" ", font=('Times',26,'bold'), height= 3, width=8, bg="Gainsboro", command=lambda:checker(button4))
button4.grid(row=2, column=0, sticky = S+N+E+W)

button5 = Button(LeftFrame, text=" ", font=('Times',26,'bold'), height= 3, width=8, bg="Gainsboro", command=lambda:checker(button5))
button5.grid(row=2, column=1, sticky = S+N+E+W)

button6 = Button(LeftFrame, text=" ", font=('Times',26,'bold'), height= 3, width=8, bg="Gainsboro", command=lambda:checker(button6))
button6.grid(row=2, column=2, sticky = S+N+E+W)

button7 = Button(LeftFrame, text=" ", font=('Times',26,'bold'), height= 3, width=8, bg="Gainsboro", command=lambda:checker(button7))
button7.grid(row=3, column=0, sticky = S+N+E+W)

button8 = Button(LeftFrame, text=" ", font=('Times',26,'bold'), height= 3, width=8, bg="Gainsboro", command=lambda:checker(button8))
button8.grid(row=3, column=1, sticky = S+N+E+W)

button9 = Button(LeftFrame, text=" ", font=('Times',26,'bold'), height= 3, width=8, bg="Gainsboro", command=lambda:checker(button9))
button9.grid(row=3, column=2, sticky = S+N+E+W)

root.mainloop()
