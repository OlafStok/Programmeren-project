from datetime import date
from tkinter import *
import time
import tkinter.messagebox
from MarvelSuperHeroGuesser import Super_Wonder_Captain_Requester as requester
from MarvelSuperHeroGuesser import Super_Wonder_Captain_ScoreBoard as scoreboard



root = Tk()
root.resizable(False, False)

C = Canvas(root, bg="blue", height=300, width=400 )
filename = PhotoImage(file = "superhelden.gif")
Gegeven_antwoord = StringVar()
gegeven_naam = StringVar()
punten = 25
naam = ""

def getnewinfo():
    antwoordLabel = Label(C,text = "guess")
    informatie = requester.gethintsfromlistofcharacterwithid(requester.randomIDfromlist())
    informatie = informatie.split(";;;")
    global hint1, hint2, hint3, goede_antwoord
    hint1 = informatie[0]
    hint2 = informatie[1]
    hint3 = informatie[2]
    goede_antwoord = informatie[3]


def start_game_buttonpressed():
    global punten
    punten = 25
    start_game()

def start_game():
    button1.lift()
    button4.lift()
    button5.lower()
    antwoord.lift()
    backbutton.lift()
    scoreboardbutton.lower()
    scoreboardbuttondaily.lower()

def open_scoreboard():
    scoreboard.fillscoreboard(scoreboardlist)
    scoreboardlist.lift()
    button5.lower()
    backbutton.lift()
    scoreboardbutton.lower()
    scoreboardbuttondaily.lower()

def open_scoreboard_daily():
    scoreboard.fillscoreboarddaily(scoreboardlist)
    scoreboardlist.lift()
    button5.lower()
    backbutton.lift()
    scoreboardbutton.lower()
    scoreboardbuttondaily.lower()

backgroundimg = PhotoImage(file="superhelden.gif")
backgroundlabel = Label(C, image=backgroundimg)
C.create_window(0, 0, anchor="nw", window = backgroundlabel)
getnewinfo()
C.grid()


def sluiten():
    import sys;
    sys.exit()

def opnieuw_opstarten():
    button1.lower()
    button2.lower()
    button3.lower()
    button4.lower()
    button5.lift()
    antwoord.lower()
    label2.lower()
    label3.lower()
    label5.lower()
    label6.lower()
    label7.lower()
    scoreboardlist.lower()
    backbutton.lower()
    scoreboardbutton.lift()
    scoreboardbuttondaily.lift()
    start_game()

def uppunten():
    global punten
    punten = punten + 25

def hintpuntaftrek():
    global punten
    punten = punten-3

def slapuntenop(naam):
    with open("Scores.txt", "a") as scorefile:
        scorefile.write(str(date.today()) + ";" + str(naam) + ";" + str(punten) + "\n")

def geefhint():
    klik = tkinter.messagebox.askquestion("Waarschuwing", "Wil je je 1e hint gebruiken?")
    if klik == 'yes':
        label5.lift()
        time.sleep(0.5)
        C.create_window(200,95, anchor= "n", window= label5)
        button1.lower()
        button2.lift()
        hintpuntaftrek()

def geefhint2():
    label6.lift()
    time.sleep(0.5)
    klik2 = tkinter.messagebox.askquestion("Waarschuwing", "Wil je je 2e hint gebruiken?")
    C.create_window(200,200, anchor= "n", window = label6)
    button2.lower()
    button3.lift()
    hintpuntaftrek()

def geefhint3():
    label7.lift()
    time.sleep(0.5)
    klik3 = tkinter.messagebox.askquestion("Waarschuwing","Wil je je 3de hint gebruiken?")
    C.create_window(200,225, anchor="n", window=label7)
    button3.lower()
    hintpuntaftrek()

def checker():
    time.sleep(0.5)
    if str(Gegeven_antwoord.get()).lower() == goede_antwoord.lower():
        label3.lower()
        label2.lift()
        uppunten()
        time.sleep(3)
        getnewinfo()
        opnieuw_opstarten()
        label5.config(text=hint1)
        label6.config(text=hint2)
        label7.config(text=hint3)
    else:
        label3.lift()
        label2.lower()
        global punten
        punten = punten-1
def main_menu():
    button1.lower()
    button2.lower()
    button3.lower()
    button4.lower()
    button5.lift()
    antwoord.lower()
    label2.lower()
    label3.lower()
    label5.lower()
    label6.lower()
    label7.lower()
    scoreboardlist.lower()
    backbutton.lower()
    scoreboardbutton.lift()
    scoreboardbuttondaily.lift()
    if (punten != 25):
        slapuntenop(naam)

def naamopslaan():
    naambutton.lower()
    button5.lift()
    scoreboardbuttondaily.lift()
    scoreboardbutton.lift()
    naaminput.lower()
    global naam
    naam = str(gegeven_naam.get().replace(";", ""))

root.minsize(width=400, height=250)

#frame = Frame(root, width=400, height=250)
#frame.grid(anchor="C"

antwoordLabel = Label(C, text="Guess")


menu = Menu(root)
root.config(menu=menu)
subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New game...", command = opnieuw_opstarten)
subMenu.add_separator()
subMenu.add_command(label="Exit", command = sluiten)
subMenu.add_command(label="Exit to Main menu", command = main_menu)

button1 = Button(C, text="Hint 1", command=geefhint, fg = "blue")
button2 = Button(C, text="Hint 2", command=geefhint2, fg = "blue")
button3 = Button(C, text="Hint 3", command=geefhint3, fg = "blue")
button4 = Button(C, text="Check antwoord!", command=checker)
button5 = Button(C, text="Start game", command=start_game_buttonpressed, fg = "blue")
scoreboardbutton = Button(C, text="scoreboard", command = open_scoreboard, fg = "blue")
scoreboardbuttondaily = Button(C, text="scoreboard daily", command = open_scoreboard_daily, fg = "blue")
backbutton = Button(C, text="back", command=main_menu, fg="red")
naambutton = Button(C, text="naam opslaan", command=naamopslaan)

scoreboardlist = Listbox(C)

antwoord=Entry(C, textvariable= Gegeven_antwoord)
naaminput = Entry(C, textvariable= gegeven_naam)

label2 = Label(C, text ="Dat klopt!", fg = "green")
label3 = Label(C,text="Helaas dat klopt niet", fg= "red")
label5= Label(C,text=hint1)
label6= Label(C,text=hint2)
label7= Label(C,text=hint3)

C.create_window(180,80,anchor = "w", window = button1)
C.create_window(180,80,anchor = "w", window = button2)
C.create_window(180,80, anchor = "w", window = button3)
C.create_window(150,185, anchor = "w", window = button4)
C.create_window(168, 120,anchor = "nw", window = button5)
C.create_window(168, 150, anchor="nw", window = scoreboardbutton)
C.create_window(168, 180, anchor="nw", window = scoreboardbuttondaily)
C.create_window(180, 250, anchor="nw", window = backbutton)
C.create_window(168, 120, anchor="nw", window = naambutton)

C.create_window(139,160, anchor = "w", window = antwoord)
C.create_window(139, 220, anchor="w", window = naaminput)

C.create_window(200, 20 , anchor= "n", window= label2)
C.create_window(200, 20 , anchor= "n", window= label3)

scoreboard.fillscoreboarddaily(scoreboardlist)
C.create_window(200, 150, anchor="center", window = scoreboardlist)

main_menu()
button5.lower()
scoreboardbuttondaily.lower()
scoreboardbutton.lower()

root.title("Raad de superheld")

root.mainloop()

