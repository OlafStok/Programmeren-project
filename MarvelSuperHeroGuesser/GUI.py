from tkinter import *
import time
import tkinter.messagebox

root = Tk()

C = Canvas(root, bg="blue", height=300, width=400 )
filename = PhotoImage(file = "superhelden.gif")
Gegeven_antwoord = StringVar()
antwoordLabel = Label(C,text = "guess")

def start_game():
    button1.lift()
    button4.lift()
    button5.lower()
    antwoord.lift()

def main_menu():
    button1.lower()
    button2.lower()
    button3.lower()
    button4.lower()
    button5.lift()
    antwoord.lower()


backgroundimg = PhotoImage(file="superhelden.gif")
backgroundlabel = Label(C, image=backgroundimg)
C.create_window(0, 0, anchor="nw", window = backgroundlabel)

C.grid()


def sluiten():
    import sys;
    sys.exit()



def geefhint():
    klik = tkinter.messagebox.askquestion("Waarschuwing", "Wil je je 1e hint gebruiken?")
    if klik == 'yes':
        label5= Label(C,text="Tekst hint 1")
        time.sleep(0.5)
        C.create_window(200,200, anchor= "n", window= label5)
        button1.lower()
        button2.lift()
def geefhint2():
    label6= Label(C,text="Tekst hint 2")
    time.sleep(0.5)
    klik2 = tkinter.messagebox.askquestion("Waarschuwing", "Wil je je 2e hint gebruiken?")
    C.create_window(200,225, anchor= "n", window = label6)
    button2.lower()
    button3.lift()
def geefhint3():
    label7= Label(C,text="Tekst hint 3")
    time.sleep(0.5)
    klik3 = tkinter.messagebox.askquestion("Waarschuwing","Wil je je 3e hint gebruiken?")
    C.create_window(200,250, anchor="n", window=label7)
    button3.lower()
def checker():
    time.sleep(0.5)
    if str(Gegeven_antwoord.get()) == antwoord:
        label3.lower()
        label2.lift()
    else:
        label3.lift()
        label2.lower()

def menuTest():
    print("Je hebt geklikt op een menu item.")

root.minsize(width=400, height=250)

#frame = Frame(root, width=400, height=250)
#frame.grid(anchor="C"

antwoordLabel = Label(C, text="Guess")


menu = Menu(root)
root.config(menu=menu)
subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_separator()
subMenu.add_command(label="Exit", command = sluiten)
subMenu.add_command(label="Exit to Main menu", command = main_menu)

button1 = Button(C, text="Hint 1", command=geefhint, fg = "blue")
button2 = Button(C, text="Hint 2", command=geefhint2, fg = "blue")
button3 = Button(C, text="Hint 3", command=geefhint3, fg = "blue")
button4 = Button(C, text="Check antwoord!", command=checker)
button5 = Button(C, text="Start game", command=start_game, fg = "blue")

antwoord=Entry(C, textvariable= Gegeven_antwoord)

label2 = Label(C, text ="Dat klopt!", fg = "green")
label3 = Label(C,text="Helaas dat klopt niet", fg= "red")

C.create_window(180,80,anchor = "w", window = button1)
C.create_window(180,80,anchor = "w", window = button2)
C.create_window(180,80, anchor = "w", window = button3)
C.create_window(150,185, anchor = "w", window = button4)
C.create_window(168, 120,anchor = "nw", window = button5)

C.create_window(139,160, anchor = "w", window = antwoord)

C.create_window(200, 129 , anchor= "n", window= label2)
C.create_window(200, 129 , anchor= "n", window= label3)

main_menu()
label2.lower()
label3.lower()


root.title("Raad de superheld")

root.mainloop()

