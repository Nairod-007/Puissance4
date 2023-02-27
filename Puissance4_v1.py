
global Tableau
Tableau=[]

def tableau():#Dieudonné
    global Tableau
    Tableau = [[0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0]]

def afficher_tableau():
    global Tableau
    print('\n')
    print('     | ',end='')
    for i in range(7): #Affichage des colonnes
        print(i+1,end=' | ')
    print('')

    print('     -----------------------------')
    print('')
    for i in range(6): #Affichage du tableau et du cadriage
        print('     | ',end='')
        for j in range(7):
            print(Tableau[i][j], end=" | ")
        print('')
        print('     -----------------------------')


def demander_colonne():#Rémi
    c=input("choisissez une colonne pour jouer entre 1 et 7 : ")
    return c

def verif_jeton(c): #Rémi
    global Tableau
    try:
        c=int(c)
    except ValueError:
        return False

    if ( c < 1 ) or ( c > 7): #Si c'est un nombre correct et 'qu'il est possible de jouer'
        return False

    if (Tableau[0][c-1]==1 or Tableau[0][c-1]==2):
        return False

    return True

def tomber_jetons(c,joueur):#Jassim
    global Tableau
    i=5
    while (i>=0) : #On fait tomber le jeton
        if (Tableau[i][c]==0):
            Tableau[i][c]=joueur
            i = -1
        i= i-1

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

def partie():#Maël
    joueur=1
    nb_tour=1
    tableau()

    while True:

        c=demander_colonne()
        while verif_jeton(c)==False:
            print("Rentrez un nombre ou choisisez une autre colonne")
            c=demander_colonne()
        c=int(c)-1
        tomber_jetons(c,joueur)

        afficher_tableau()

        if nb_tour>6:
            if nb_tour==42 or verif()==True:
                print('Le joueur',joueur,'a gagné la partie')
                a=str(input("Voulez-vous rejouer ? O ou N : "))
                if (a=="O" or a=="o"):
                    return True
                else:
                    return False
        nb_tour+=1
        joueur=3-joueur


while partie():
    partie()

#PS: Construction/assemblage + correction + optimisation fait par Rémi et Dorian