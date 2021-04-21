import tkinter as tk
##################
LARGEUR = 700
HAUTEUR = 700
###################
xp1, yp1 = LARGEUR // 7, HAUTEUR // 7
xp2, yp2 = LARGEUR // 2, HAUTEUR // 7
xp3, yp3 = (LARGEUR // 7)*6, HAUTEUR // 7
xp4, yp4 = LARGEUR // 7, HAUTEUR // 2
xp5, yp5 = LARGEUR // 2, HAUTEUR // 2
xp6, yp6 = (LARGEUR // 7)*6, HAUTEUR // 2
xp7, yp7 =  LARGEUR // 7, (HAUTEUR // 7)*6
xp8, yp8 = LARGEUR // 2, (HAUTEUR // 7)*6
xp9, yp9 = (LARGEUR // 7)*6, (HAUTEUR // 7)*6

# Fonctions
def creer_tabledejeu():
    rayon = 20
    cercle = canvas.create_oval((xp1-rayon, yp1-rayon),(xp1+rayon, yp1+rayon),
                                fill="black")
    cercle = canvas.create_oval((xp2-rayon, yp2-rayon),(xp2+rayon, yp2+rayon),
                                fill="black")
    cercle = canvas.create_oval((xp3-rayon, yp3-rayon),(xp3+rayon, yp3+rayon),
                                fill="black")                            
    cercle = canvas.create_oval((xp4-rayon, yp4-rayon), (xp4+rayon, yp4+rayon),
                                fill="black")
    cercle = canvas.create_oval((xp5-rayon, yp5-rayon), (xp5+rayon, yp5+rayon),
                                fill="black")
    cercle = canvas.create_oval((xp6-rayon, yp6-rayon),(xp6+rayon, yp6+rayon),
                                fill="black")    
    cercle = canvas.create_oval((xp7-rayon, yp7-rayon),(xp7+rayon, yp7+rayon),
                                fill="black")
    cercle = canvas.create_oval((xp8-rayon, yp8-rayon),(xp8+rayon, yp8+rayon),
                                fill="black")
 
    cercle = canvas.create_oval((xp9-rayon, yp9-rayon),(xp9+rayon, yp9+rayon),
                                fill="black") 

def creer_traitvertical() : 

    ligne = canvas.create_line ((xp1,yp1),(xp7,yp7), fill="black")
    ligne = canvas.create_line ((xp2,yp2),(xp8,yp8), fill="black")
    ligne = canvas.create_line ((xp3,yp3),(xp9,yp9), fill="black")

def creer_traithorizontal() :
    
    ligne = canvas.create_line ((xp1,yp1),(xp3,yp3), fill="black")
    ligne = canvas.create_line ((xp4,yp4),(xp6,yp6), fill="black")
    ligne = canvas.create_line ((xp7,yp7),(xp9,yp9), fill="black") 

def creer_traitdiagonal() :

    ligne = canvas.create_line ((xp1,yp1),(xp9,yp9), fill="black")
    ligne = canvas.create_line ((xp3,yp3),(xp7,yp7), fill="black")

#####################
# programme principal
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="orange", width=700, height=700)
canvas.grid()
trait1 = creer_traitvertical()
trait2 = creer_traithorizontal()
trait3 = creer_traitdiagonal()
table = creer_tabledejeu()
racine.mainloop()

####test pour le commit2