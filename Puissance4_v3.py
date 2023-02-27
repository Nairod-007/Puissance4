import pygame
from time import sleep

class Puissance :

    def __init__(self,taille=60):
        self.dimension = (800, 800)
        self.ecran = pygame.display.set_mode(self.dimension)
        pygame.display.set_caption("Puissance 4")


        #Tableau
        self.tableau = [[[0,None,None], [0,None,None], [0,None,None], [0,None,None], [0,None,None], [0,None,None], [0,None,None]],
                        [[0,None,None], [0,None,None], [0,None,None], [0,None,None], [0,None,None], [0,None,None], [0,None,None]],
                        [[0,None,None], [0,None,None], [0,None,None], [0,None,None], [0,None,None], [0,None,None], [0,None,None]],
                        [[0,None,None], [0,None,None], [0,None,None], [0,None,None], [0,None,None], [0,None,None], [0,None,None]],
                        [[0,None,None], [0,None,None], [0,None,None], [0,None,None], [0,None,None], [0,None,None], [0,None,None]],
                        [[0,None,None], [0,None,None], [0,None,None], [0,None,None], [0,None,None], [0,None,None], [0,None,None]]]

        self.colonne_prise = [False for i in range(len(self.tableau[0]))]
        self.taille_case = taille #En pixel
        self.taille_tableau_witdh = len(self.tableau[0]) * self.taille_case
        self.taille_tableau_height = len(self.tableau)*self.taille_case
        self.witdh_line = 1
        self.grille_position = [180,180] #Origine en haut à gauche

        #Partie
        self.partie = True
        self.nb_tours=0
        self.joueur=1
        self.couleur = [(255,255,255),(255,0,0),(0,255,0)]
        self.ligne_win = [None, None, None, None]
        self.texte = ''

        #Jeton
        self.taille_jeton = self.taille_case-self.witdh_line #En pixel
        self.jeton_position_dessus = 50
        self.jeton_position_initial = [self.grille_position[0] + self.witdh_line,
                                       self.grille_position[1] + self.witdh_line - self.jeton_position_dessus - self.taille_jeton]
        self.jeton_position = list(self.jeton_position_initial)
        self.colonne = 0 #Donne la colonne du jeton



    def main(self):
        while self.partie:
            pygame.time.Clock().tick(5) #Permet de gérer les fps du jeu. Ici on économise nos ressources
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.partie=False # Fin de la partie
                    return False

                #Donne la direction du jeton
                if event.type == pygame.KEYDOWN:
                    print(event)
                    pygame.time.Clock().tick(60) #Change les fps pour donner un mouvement fluide
                    if event.key == pygame.K_RIGHT:
                        if self.colonne<len(self.tableau[0])-1:
                            self.colonne += 1
                            self.move_colonne_x(1)
                    if event.key == pygame.K_LEFT:
                        if self.colonne>0:
                            self.colonne -= 1
                            self.move_colonne_x(-1)
                    if event.key == pygame.K_DOWN:
                        self.tomber_jeton()
                        self.nb_tours+=1

                        if self.verif():
                            print('gagnez')
                            self.texte = 'Le Joueur {} gagne la Partie !'.format(self.joueur)
                            self.partie = False
                        elif self.nb_tours == 42:
                            print("Egalité")
                            self.texte = 'Egalité !'
                            self.partie = False

                        else:
                            self.new_jeton()

            self.actualiser()

        while True:
            pygame.time.Clock().tick(10)
            font = pygame.font.Font(None, 40)
            text = font.render(self.texte, True, (0, 0, 0), (150, 150, 150))
            textRect = text.get_rect()
            textRect.center = (self.dimension[0] // 2, self.taille_tableau_height + 230)
            self.ecran.blit(text, textRect)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return True
                    else:
                        return False
                elif event.type == pygame.QUIT:
                    return False



    def new_jeton(self):
        self.jeton_position = list(self.jeton_position_initial)
        self.colonne = 0
        self.joueur = 3 - self.joueur
        self.actualiser()


    def move_colonne_x(self,a):
        for i in range(self.taille_case):
            self.jeton_position[0] += a
            self.actualiser()
            sleep(0.005)


    def move_colonne_y(self,a):
        for j in range(a):
            if j == 0:  # Pour passer du dessus de la grille à la case du haut de la colonne
                for k in range(self.jeton_position_dessus+self.taille_jeton):
                    self.jeton_position[1] += 1
                    self.actualiser()
                    sleep(0.0015)

            for i in range(self.taille_case):
                self.jeton_position[1] += 1
                self.actualiser()
                sleep(0.0015)


    def verif_colonne_pleine(self):
        if self.colonne_prise[self.colonne] == False:
            return False
        return True


    def tomber_jeton(self):
        if not (self.verif_colonne_pleine()):
            i = 5
            c = self.colonne
            while (i >= 0):  # On fait tomber le jeton
                if (self.tableau[i][c][0] == 0):
                    if i == 0:
                        self.colonne_prise[c] = True
                    self.move_colonne_y(i)
                    self.tableau[i][c][0] = self.joueur
                    self.tableau[i][c][1] = self.jeton_position[0]
                    self.tableau[i][c][2] = self.jeton_position[1]
                    i = -1
                i -= 1

        else:
            #Affiche la colonne est pleine
            pass


    def dessin_jeton_jouer(self):
        for i in range(len(self.tableau)):
            for j in range(len(self.tableau[0])):
                if self.tableau[i][j][0] == 1:
                    position = [self.tableau[i][j][1],self.tableau[i][j][2]]
                    pygame.draw.rect(self.ecran, self.couleur[1], (position[0], position[1], self.taille_jeton, self.taille_jeton))
                elif self.tableau[i][j][0] == 2:
                    position = [self.tableau[i][j][1],self.tableau[i][j][2]]
                    pygame.draw.rect(self.ecran, self.couleur[2], (position[0], position[1], self.taille_jeton, self.taille_jeton))


    def dessin_grille(self):
        longueur_horizon = self.grille_position[1] + self.taille_tableau_witdh
        longueur_verti = self.grille_position[0] + self.taille_tableau_height

        for j in range(self.grille_position[1], self.grille_position[1]+(len(self.tableau)+1)*self.taille_case, self.taille_case):
            pygame.draw.line(self.ecran, (0, 0, 0), (self.grille_position[0], j), (longueur_horizon, j),self.witdh_line)

        for i in range(self.grille_position[0], self.grille_position[0]+(len(self.tableau[0])+1)*self.taille_case, self.taille_case):
            pygame.draw.line(self.ecran, (0, 0, 0), (i, self.grille_position[1]), (i, longueur_verti),self.witdh_line)


    def dessin_jeton(self):
        pygame.draw.rect(self.ecran, self.couleur[self.joueur],(self.jeton_position[0], self.jeton_position[1], self.taille_jeton, self.taille_jeton))


    #Vérification

    def verif_verti(self):
        for i in range(len(self.tableau)-3):
            for j in range(len(self.tableau[0])):
                a = self.tableau[i][j][0]

                if ((a != 0) and (a == self.tableau[i+1][j][0]) and (a == self.tableau[i+2][j][0]) and (a == self.tableau[i+3][j][0])):
                    self.ligne_win = [self.tableau[i][j][1], self.tableau[i][j][2],self.tableau[i+3][j][1],self.tableau[i+3][j][2]]
                    return True
        return False


    def vérification_horizontale(self):
        for i in range(len(self.tableau)):
            for j in range(len(self.tableau[0])-3):
                a = self.tableau[i][j][0]
                if ((a!=0) and (a == self.tableau[i][j + 1][0]) and (a == self.tableau[i][j + 2][0]) and (a == self.tableau[i][j + 3][0])):
                    self.ligne_win = [self.tableau[i][j][1], self.tableau[i][j][2],self.tableau[i][j + 3][1], self.tableau[i][j + 3][2]]
                    return True
        return False

    def verif_diagonale_croissant(self):
        for i in range(3,len(self.tableau)):
            for j in range(len(self.tableau[0])-4):
                a = self.tableau[i][j][0]
                if ((a!=0) and (a==self.tableau[i-1][j+1][0]) and (a==self.tableau[i-2][j+2][0]) and (a==self.tableau[i-3][j+3][0])):
                    self.ligne_win = [self.tableau[i][j][1], self.tableau[i][j][2],self.tableau[i-3][j+3][1], self.tableau[i-3][j+3][2]]
                    return True
        return False


    def verif_diagonale_décroissant(self):
        for i in range(len(self.tableau)-3):
            for j in range(len(self.tableau[0]) - 3):
                a = self.tableau[i][j][0]
                if ((a != 0) and (a == self.tableau[i + 1][j + 1][0]) and (a == self.tableau[i + 2][j + 2][0]) and (a == self.tableau[i + 3][j + 3][0])):
                    self.ligne_win = [self.tableau[i][j][1], self.tableau[i][j][2],self.tableau[i + 3][j + 3][1], self.tableau[i + 3][j + 3][2]]
                    return True
        return False


    def verif(self):  # Jassim
        if self.verif_verti() or self.vérification_horizontale() or self.verif_diagonale_décroissant() or self.verif_diagonale_croissant():
            return True

    def ligne(self):
        if self.ligne_win[0] != None:
            a = (self.ligne_win[0] + self.taille_jeton // 2, self.ligne_win[1] + self.taille_jeton // 2)
            b = (self.ligne_win[2] + self.taille_jeton // 2, self.ligne_win[3] + self.taille_jeton // 2)
            pygame.draw.line(self.ecran, (0, 0, 0), a, b, self.witdh_line + 5)

    def actualiser(self):
        self.ecran.fill((255, 255, 255))  # attribut la couleur noir à l'écran
        self.dessin_jeton()
        self.dessin_jeton_jouer()
        self.dessin_grille()
        self.ligne()
        pygame.display.flip()



if __name__ == '__main__':
    pygame.init()
    a = True
    while a:
        a = Puissance().main()
    pygame.quit()