
from tkinter import *

#fenêtre window
window = Tk()

#personnalisé la fenetre
window.title("Le Puissance 4")
window.minsize(600,800)
window.config(background='#15774B')

#créer une boîte
frame=Frame(window,bg='#15774B', bd=1, relief=SUNKEN)
frame2=Frame(window,bg='#15774B', bd=1, relief=SUNKEN)
frame3=Frame(window,bg='#15774B', bd=1, relief=SUNKEN)
global frame4
frame4=Frame(window,bg='#15774B', bd=1, relief=SUNKEN)
frame5=Frame(window,bg='#15774B', pady=10)


#Titre
label_title = Label(frame, text="Puissance 4",font=("Arial",30), bg="#15774B", fg="white")
label_title.pack()

global Tableau
Tableau=[]
global joueur
joueur=1
global nb_tours
nb_tours=0
global final
final=Label(frame5)

def final_partie(a,j):
    if a==1:
        a="Joueur "+str(j)+", vous avez gagner"
    else:
        a="Il y a match nul"

    final = Label(frame5, text=a,font=("Arial",30), bg="#15774B", fg="white")
    final.grid(row=0,column=0, sticky=W)
    frame5.pack()

def init_tableau():
    global Tableau,joueur,nb_tours
    Tableau =  [[0,0,0,0,0,0,0], #création du tableau vierge
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0]]
    nb_tours=0
    joueur=1
    final.grid_forget()
    frame5.pack_forget()



def tomber_jetons(c,joueur):#Jassim
    global Tableau
    i=5
    while (i>=0) : #On fait tomber le jeton
        if (Tableau[i][c]==0):
            Tableau[i][c]=joueur
            i = -1
        i= i-1


#afficher le tableau
def afficher_tableau():
    #frame4.pack_forget() #efface la frame 4
    for i in range(6):
        for j in range(7):
            valeur = Label(frame4, text=str(Tableau[i][j]),font=("Arial",15), bg="#15774B", fg="white", padx=20,pady=15)
            valeur.grid(row=i,column=j,sticky=W)
    frame4.pack(pady=20)#reaffiche

#Fonction de vérification de puissance 4 horizontalement
def vérification_horizontale(): #Yasmina, rien en entrée car on initialise les variables par la suite
    global Tableau
    for i in range(6): #On répéte la vérification sur les 6 lignes
        for j in range(4): #Le jeton ne peut pas être dans une colonne supérieure que la colonne 4 puisque il ne poura pas y avoir 4 jetons alignés car on dépassera du tableau
                if ((Tableau[i][j]!=0) and (Tableau[i][j]==Tableau[i][j+1]) and (Tableau[i][j]==Tableau[i][j+2]) and (Tableau[i][j]==Tableau[i][j+3])):
                    return True #Booléen indiquant que le jeton de départ est suivi directement de trois autres mêmes jetons sans cases vides
    return False #Booléen indiquant qu'il n'y a pas de même jetons alignés 4fois car au moins une condition au-dessous n'est pas respectée

def verif_verti(): #Dorian
    global Tableau
    for i in range(3):
        for j in range(7):
            a=Tableau[i][j]
            if ((a!=0) and (a==Tableau[i+1][j]) and (a==Tableau[i+2][j]) and (a==Tableau[i+3][j])):
                return True
    return False

def verif_diagonale_décroissant(): #Jules
    global Tableau
    nb_jetons=0
    for i in range(3):
        for j in range(4): #départ de toutes diagonales possibles
            for x in range(4): #décalage pour la diagonale
                if ((Tableau[i][j]!=0) and (Tableau[i][j] == Tableau[i+x][j+x])):
                    nb_jetons+=1
            if nb_jetons == 4: #condition de victoire + sortie booléen
                return True
            else:
                nb_jetons=0 #réinitialisation
    return False

def verif_diagonale_croissant(): #Jules
    global Tableau
    nb_jetons=0
    for i in range(3,6):
        for j in range(4): #départ de toutes diagonales possibles
            for x in range(4): #décalage pour la diagonale
                if ((Tableau[i][j]!=0) and (Tableau[i][j] == Tableau[i-x][j+x])):
                    nb_jetons+=1
            if nb_jetons == 4: #condition de victoire + sortie booléen
                return True
            else:
                nb_jetons=0 #réinitialisation
    return False

def verif():#Jassim
    return verif_verti() or vérification_horizontale() or verif_diagonale_décroissant() or verif_diagonale_croissant()

def rejouer():
    a=str(input("Voulez-vous rejouer ? O ou N"))
    if (a=="O" or a=="o"): #si gagner renvois un booléen
        return True
    else: #coucou
        return False




def choix_colonne(x):
    global joueur,nb_tours
    tomber_jetons(x,joueur)
    afficher_tableau()
    if verif():
        final_partie(1,joueur)
        #rejouer()
    elif nb_tours==42:
        final_partie(2,joueur)
        #rejouer()
    nb_tours+=1
    joueur = 3 - joueur


#Boutton des colonnes du tableau
boutton1 = Button(frame2,text="1",bg="white",fg="black",font=("Arial",20),padx=16,pady=10,command=lambda: choix_colonne(0))
boutton1.grid(row=0,column=0, sticky=W)
boutton2 = Button(frame2,text="2",bg="white",fg="black",font=("Arial",20),padx=16,pady=10,command=lambda: choix_colonne(1))
boutton2.grid(row=0,column=1, sticky=W)
boutton3 = Button(frame2,text="3",bg="white",fg="black",font=("Arial",20),padx=16,pady=10,command=lambda: choix_colonne(2))
boutton3.grid(row=0,column=2, sticky=W)
boutton4 = Button(frame2,text="4",bg="white",fg="black",font=("Arial",20),padx=16,pady=10,command=lambda: choix_colonne(3))
boutton4.grid(row=0,column=3, sticky=W)
boutton5 = Button(frame2,text="5",bg="white",fg="black",font=("Arial",20),padx=16,pady=10,command=lambda: choix_colonne(4))
boutton5.grid(row=0,column=4, sticky=W)
boutton6 = Button(frame2,text="6",bg="white",fg="black",font=("Arial",20),padx=16,pady=10,command=lambda: choix_colonne(5))
boutton6.grid(row=0,column=5, sticky=W)
boutton7 = Button(frame2,text="7",bg="white",fg="black",font=("Arial",20),padx=16,pady=10,command=lambda: choix_colonne(6))
boutton7.grid(row=0,column=6, sticky=W)

#boutton validé
boutton_vd = Button(frame,text="Commencer",bg="white",fg="black",font=("Arial",20),command=lambda: [init_tableau(),afficher_tableau()])
boutton_vd.pack()

#afficher fenêtre
frame.pack(pady=10)
frame2.pack()
frame3.pack()
window.mainloop()

