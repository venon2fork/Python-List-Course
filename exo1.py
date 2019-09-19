import os
import json

ch = os.path.dirname(__file__)
dsliste = os.path.join(ch, "liste_de_Course.json")
if os.path.exists(dsliste):
    with open(dsliste,"r")as f:
        listeCourse=json.load(f)
else:
    listeCourse=[]


affiche= """
++++++++++++++++++++++++++++++++++
+++++++++++   MENU      ++++++++++
++++++++++++++++++++++++++++++++++
\t 1: Ajouter 
\t 2: Enlever
\t 3: Afficher
\t 4: Effacer
\t 5: Quitter
++++++++++++++++++++++++++++++++++
"""

option = 0
while option != 5:
    print(affiche)
    option = int(input("Choississez un menu : "))
    if option == 1:
        ajouterListe = input("Entrer la valeur a ajouter :")
        listeCourse.append(ajouterListe)
    elif option == 2:
        enlever_de_la_Liste = input("Entrer la valeur a ajouter :")
        if enlever_de_la_Liste in listeCourse:
            listeCourse.remove(enlever_de_la_Liste)
        else:
            print("\n")
            print(f"++ la valeur =>\"{enlever_de_la_Liste}\"<= n'existe pas ++ \n => Retour au Menu Principale")
    elif option == 3:
        print("\n".join(listeCourse))
    elif option == 4:
        print("ATTENTION VOTRE LISTE DE COURSE VA T'ETRE EFFACER")
        efliste= "N"
        while efliste != "O":
            efface_liste = input("O/N :")
            print(efface_liste.lower())
            if efface_liste.lower() == "o" or efface_liste.lower() == "n":
                for i in listeCourse:
                    listeCourse.remove(i)
                break
            elif efface_liste.lower == "n":
                efliste= "0"
with open(dsliste, "w") as f:
    json.dump(listeCourse,f,indent=4)


    
    
    