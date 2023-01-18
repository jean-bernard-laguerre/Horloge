from tkinter import *
from tkinter import ttk

fenetre = Tk()
fenetre.title("Horloge")

heures = 0
minutes = 0
secondes = 0

en_cours = False
mode_heure = 0


def Afficher_heures(heures, minutes, secondes):

    global mode_heure

    if mode_heure == 1:

        if heures > 12:

            horloge.config(text = f"{heures - 12 :0>2}:{minutes :0>2}:{secondes :0>2} PM")

        else:
            horloge.config(text = f"{heures :0>2}:{minutes :0>2}:{secondes :0>2} AM")
    
    else:
        horloge.config(text = f"{heures :0>2}:{minutes :0>2}:{secondes :0>2}")


def Pause():
    global en_cours

    if en_cours:
        btn_demarrer.config(text="Demarrer", bg="green")
        en_cours = False
        
    else:
        en_cours = True
        btn_demarrer.config(text="Arreter", bg="red")
        Horloge()


def Mode_affichage():
    global mode_heure

    if mode_heure == 0:
        mode_heure = 1
        btn_mode.config(text="format: 24H")
        
        
    else:
        mode_heure = 0
        btn_mode.config(text="format: 12H")


def Regler():

    global heures
    global minutes
    global secondes

    try:
        heures = int(Hrs.get())
        minutes = int(Min.get())
        secondes = int(Sec.get())

    except:
        print("erreur")


def Alarme():
    pass


def Horloge():

    global en_cours
    global heures
    global minutes
    global secondes


    Afficher_heures(heures, minutes, secondes)

    secondes += 1

    if secondes >= 60:
            secondes = 0
            minutes += 1

    if minutes >= 60:
            minutes = 0
            heures += 1

    if heures >= 24:
            heures = 0
    
    if en_cours:
        horloge.after(1000, Horloge)


horloge = Label(fenetre, text= "00:00:00", font=('Arial', 18), bg="black", fg="white")
horloge.pack(fill="both", expand="yes")

boutons = Frame(fenetre)
boutons.pack()
btn_demarrer = Button(boutons, text="Demarrer", bg="green", command= Pause, width=15)
btn_demarrer.grid(row=0, column=0)
btn_mode = Button(boutons, text="format: 24H", command= Mode_affichage, width=15)
btn_mode.grid(row=0, column=2)

btn_regler = Button(boutons, text="Regler", command= Regler, width=15)
btn_regler.grid(row=1, column=0)
btn_alarme = Button(boutons, text="Alarme", command= Alarme, width=15)
btn_alarme.grid(row=1, column=2)

hr_select = Frame(fenetre, width= 30)
hr_select.pack()

Hrs = Spinbox(hr_select, from_=0, to=23, width=10)
Min= Spinbox(hr_select, from_=0, to=59, width=10)
Sec = Spinbox(hr_select, from_=0, to=59, width=10)

Hrs.grid(row=3, column=0)
Min.grid(row=3, column=1)
Sec.grid(row=3, column=2)

fenetre.mainloop()
