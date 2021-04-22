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
rayon = 20

####Fonctions

def creer_tabledejeu():
    cercle1 = canvas.create_oval((xp1-rayon, yp1-rayon),(xp1+rayon, yp1+rayon),
                                fill="black")
    cercle2 = canvas.create_oval((xp2-rayon, yp2-rayon),(xp2+rayon, yp2+rayon),
                                fill="black")
    cercle3 = canvas.create_oval((xp3-rayon, yp3-rayon),(xp3+rayon, yp3+rayon),
                                fill="black")                            
    cercle4 = canvas.create_oval((xp4-rayon, yp4-rayon), (xp4+rayon, yp4+rayon),
                                fill="black")
    cercle5 = canvas.create_oval((xp5-rayon, yp5-rayon), (xp5+rayon, yp5+rayon),
                                fill="black")
    cercle6 = canvas.create_oval((xp6-rayon, yp6-rayon),(xp6+rayon, yp6+rayon),
                                fill="black")    
    cercle7 = canvas.create_oval((xp7-rayon, yp7-rayon),(xp7+rayon, yp7+rayon),
                                fill="black")
    cercle8 = canvas.create_oval((xp8-rayon, yp8-rayon),(xp8+rayon, yp8+rayon),
                                fill="black")
    cercle9 = canvas.create_oval((xp9-rayon, yp9-rayon),(xp9+rayon, yp9+rayon),
                                fill="black") 
    ## Verticale    
    ligneV1 = canvas.create_line ((xp1,yp1),(xp7,yp7), fill="black")
    ligneV2 = canvas.create_line ((xp2,yp2),(xp8,yp8), fill="black")
    ligneV3 = canvas.create_line ((xp3,yp3),(xp9,yp9), fill="black")
    ##Horizontale
    ligneH1 = canvas.create_line ((xp1,yp1),(xp3,yp3), fill="black")
    ligneH2 = canvas.create_line ((xp4,yp4),(xp6,yp6), fill="black")
    ligneH3 = canvas.create_line ((xp7,yp7),(xp9,yp9), fill="black") 
    ##Diagonale
    ligneD1 = canvas.create_line ((xp1,yp1),(xp9,yp9), fill="black")
    ligneD2 = canvas.create_line ((xp3,yp3),(xp7,yp7), fill="black")

def placement_du_jetonJ1(event) :
    canvas.create_oval((event.x-rayon, event.y-rayon),(event.x+rayon, event.y+rayon),
                                fill="blue")
def placement_du_jetonJ2(event) :
    canvas.create_oval((event.x-rayon, event.y-rayon),(event.x+rayon, event.y+rayon),
                                fill="white")
#####################
# programme principal
racine = tk.Tk()
###Dessin de la planche
canvas = tk.Canvas(racine, bg="orange", width=700, height=700)
canvas.grid()
table = creer_tabledejeu()

####Phase 1, placement des jetons:
#######ph1 = 1
#######while ph1 > 6 :
#######    if ph1%2==1 : 
#######        TourJoueur1 = canvas.bind("<Button-1>", placement_du_jetonJ1)
#######    else :
#######        TourJoueur2 = canvas.bind("<Button-1>", placement_du_jetonJ2)
#######    ph1 = ph1 + 1
#######print ("Fin de la Phase 1 de placement")

#######ph1 = 1
#######if ph1%2==1 and ph1 < 6 :
#######    TourJoueur1 = canvas.bind("<Button-1>", placement_du_jetonJ1)
#######elif ph1%2==0 and ph1 < 6 :
#######    TourJoueur2 = canvas.bind("<Button-1>", placement_du_jetonJ2)
#######ph1 = ph1 + 1  
#######if ph1 == 6 :
#######    print ("Fin de la Phase 1 de placement")

canvas.bind("<Button-1>", placement_du_jetonJ1)
####

racine.mainloop()