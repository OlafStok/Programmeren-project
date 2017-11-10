from tkinter import *
import time
import tkinter.messagebox




def sluiten():
    import sys;
    sys.exit()


def naar_menu():
    topframe.grid_forget()
    middleframe.grid_forget()
    bottomframe.grid_forget()
    statusframe.grid_forget()
    menuframe.grid()



def start_game():
    print("Starting the game")
    topframe.grid()
    middleframe.grid()
    bottomframe.grid()
    statusframe.grid()
    menuframe.grid_forget()


def geefhint():
    klik = tkinter.messagebox.askquestion("Waarschuwing", "Wil je je 1e hint gebruiken?")
    if klik == 'yes':
        label5= Label(bottomframe,text="Tekst hint 1")
        time.sleep(0.5)
        label5.grid()
def geefhint2():
    label6= Label(bottomframe,text="Tekst hint 2")
    time.sleep(0.5)
    klik2 = tkinter.messagebox.askquestion("Waarschuwing", "Wil je je 2e hint gebruiken?")
    label6.grid()
def geefhint3():
    label7= Label(bottomframe,text="Tekst hint 3")
    time.sleep(0.5)
    klik3 = tkinter.messagebox.askquestion("Waarschuwing","Er WorD EeN ViRUs GEinStAleeRd")
    label7.grid()
def checker():
    time.sleep(0.5)
    if str(antwoord1.get()) == "batman":
        label2 = Label(bottomframe,text="Dat klopt!")
        label2.grid()
    else:
        label3 = Label(bottomframe,text="Helaas dat klopt niet")
        label3.grid()
def menuTest():
    print("Je hebt geklikt op een menu item.")



root = Tk()


topframe=Frame(root)
topframe.grid()
middleframe=Frame(root, width=400, height=250)
middleframe.grid()
bottomframe=Frame(root, width=400, height=250)
bottomframe.grid()
statusframe = Frame(root, width=400, height=250)
statusframe.grid()
menuframe=Frame(root, width=400, height=250)
menuframe.grid()
naar_menu()
root.minsize(width=400, height=250)

#frame = Frame(root, width=400, height=250)
#frame.grid()

antwoord1=StringVar()

antwoordLabel = Label(middleframe, text="Guess")


menu = Menu(root)
root.config(menu=menu)
subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New game...", command = menuTest)
subMenu.add_command(label="Save game...", command = menuTest)
subMenu.add_command(label="Continue game...", command=menuTest)
subMenu.add_separator()
subMenu.add_command(label="Exit", command = sluiten)
subMenu.add_command(label="Exit to Main menu", command = naar_menu)


button5 = Button(menuframe, text="Start game", command=start_game(), fg = "blue")
button5.grid(row = 0, column= 2)

button1 = Button(topframe, text="Hint 1", command=geefhint, fg = "blue")
button1.grid()
button2 = Button(topframe, text="Hint 2", command=geefhint2, fg = "blue")
button2.grid(row = 0, column = 1)
button3 = Button(topframe, text="Hint 3", command=geefhint3, fg = "blue")
button3.grid(row =0 ,column = 2)



antwoordLabel.grid(row = 0)

antwoord=Entry(middleframe, textvariable=antwoord1)
antwoord.grid(row=0, column=1)
button4 = Button(bottomframe, text="Check antwoord!", command=checker)
button4.grid()
label1 = Label(middleframe, text=antwoord1.get())
label1.grid()

status = Label(statusframe,text="Wachtend op een input...", bd=1, relief=SUNKEN, anchor=W)
status.grid()





root.title("Raad de superheld")
root.mainloop()

