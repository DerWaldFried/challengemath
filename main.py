import time
import json
import random
import os
from timer import Timer

# Globale Variablen
global score
global nextgame
global sec

#Variablen Bestimmung
score = 0
nextgame = 0

#Highscore schreiben
def hscore_w(name, score):
    #Schreiben von der Variable gname und score in die highscore.json
    file = open(os.path.dirname(__file__) + "/highscore/highscore.json", "w")
    #Schreibe Highscore mit name und score in die Json
    highscore = {
        "name": name,
        "score": score
    }
    json.dump(highscore, file)
    file.close()


#Highscore lesen
def hscore_r():
    pass


#Funktion zur Berechnung der Randomisierten Aufgaben
def rberechnung():
        global x 
        x = random.randint(0, 100)
        global y
        y = random.randint(0, 100)
        global result
        global operator
        
        operation = random.randint(1, 3)
        
        if operation == 1:
            result = x + y
            operator = "+"
        elif operation == 2:
            result = x - y
            operator = "-"
        elif operation == 3:
            result = x * y
            operator = "*"
        else:
            result = x / y
            operator = "/"

def ausgang():
    ex = input("Wollen sie das Spiel wirklich beenden? y/n")
    if ex.lower() == "y":
        exit()
    else:
        aufgabe()

#Funktion zur Berechnung der Zeit und Erfüllung der aufgabe
def aufgabe():
    lauf = 1
    
    while lauf == 1:
        rberechnung()
        
        t = Timer()
        
        t.start()
        print("Bitte rechnen Sie die folgende Aufgabe:")
        print("{} {} {} = ?".format(x, operator, y))
            
        user_result = float(input("Ihre Antwort: "))
        
        global sec
        
        if user_result == result:
            print("Richtig!")
            sec = t.stop()
            print(sec)
            hscore_w(gname, sec)
            weiter = input("Weiter? (y/n) ")
            if weiter == "y":
                lauf = 1
            else:
                lauf = 0
                exit()
        else:
            print("Falsch. Die richtige Antwort ist: {}".format(result))
            sec = t.stop()
            print(sec)
            hscore_r()

# Hauptfunktion (Startpunkt)
def main():
    global gname
    print("Kopfsatz Junkee")
    print("-----------------------------------------------------------------------")
    print("Sie erhalten Random eine mathematische Aufgabe, die sie dann lösen müssen. ")
    print("Falls sie die Aufgabe nicht gelöst haben, verlieren sie.")
    print("-----------------------------------------------------------------------")
    gname = input("Geben Sie Ihren Spielernamen ein: ")
    aufgabe()

if __name__ == "__main__":
    main()