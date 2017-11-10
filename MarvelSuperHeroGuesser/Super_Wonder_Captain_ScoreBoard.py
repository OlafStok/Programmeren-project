from tkinter import *
from datetime import date

scores = {}
sortedscores = {}
dailynum = date.today()

def fillscoreboard(listbox):
    with open("Scores.txt", "r") as scorefile:
        tempscores = scorefile.read()
        tempscores = tempscores.split("\n")
        scores = {}
        for score in tempscores:
            try:
                score = score.split(";")
                scores[int(score[2])] = score[1]
            except:
                continue
        tempsortedscores = sorted(scores, reverse=True)
        sortedscores = tempsortedscores;
        listbox.delete(0, END)
    for score in sortedscores:
        try:
            listbox.insert(END, scores[score] + " - " + str(score))
            print("added score")
        except:
            print("added blank score")
            listbox.insert(END, 0 + " - " + "SuperWonderCaptain")
    listbox.delete(10, 999)
def fillscoreboarddaily(listbox):
    with open("Scores.txt", "r") as scorefile:
        tempscores = scorefile.read()
        tempscores = tempscores.split("\n")
        #empty scores
        scores = {}
        for score in tempscores:
                score = score.split(";")
                print(score[0] + " is date")
                print(str(dailynum) + " is today")
                if(score[0]) == str(dailynum):
                    scores[int(score[2])] = score[1]
        tempsortedscores = sorted(scores, reverse=True)
        sortedscores = tempsortedscores;
        listbox.delete(0, END)
    for score in sortedscores:
        try:
            listbox.insert(END, scores[score] + " - " + str(score))
            print("added score")
        except:
            print("added blank score (error occured)")
            listbox.insert(END, 0 + " - " + "SuperWonderCaptain")
    listbox.delete(10, 999)