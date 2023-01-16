import time

def Afficher_heures(heures, minutes, secondes, mode):

    if mode == 1:

        if heures > 12:
            heures -= 12
            print(f"{heures :0>2}:{minutes :0>2}:{secondes :0>2} PM")

        else:
            print(f"{heures :0>2}:{minutes :0>2}:{secondes :0>2} AM")
    
    else:
        print(f"{heures :0>2}:{minutes :0>2}:{secondes :0>2}")


def Alarme(alarme,heure):
    if alarme[0] == heure[0] and alarme[1] == heure[1] and alarme[2] == heure[2]:
        print("Alarm goes brrrrrrrrrrrrrrrrrrrrrrrrrrrrrr!!!!!!!!!!")


def mode_affichage():

    while True:

        try:
            mode = int(input("Mode d'affichage 24H(0) / 12H(1): "))
            if mode == 0 or mode == 1:
                return mode
        except:
            print("erreur input")


def Pause():
    input("Appuyer sur Entrée pour continuer. ")


def Horloge(heure):
    
    mode = mode_affichage()

    heures = heure[0]
    minutes = heure[1]
    secondes = heure[2]

    while True:

        Afficher_heures(heures, minutes, secondes, mode)
        Alarme((12, 59, 50),(heures, minutes, secondes))

        secondes += 1

        if secondes == 60:
            secondes = 0
            minutes += 1
            Pause()

        if minutes == 60:
            minutes = 0
            heures += 1

        if heures == 24:
            heures = 0
        
        time.sleep(1)


Horloge((12, 59, 30))