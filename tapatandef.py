import tkinter as tk

#constantes#
LARGEUR = 600
HAUTEUR = 600
rayon = (LARGEUR+HAUTEUR)/2/20
tour = []
alternance=[]
pos=[0, 0]
pos3=[0, 0]
victoires1=[]
victoires2=[]

#Fonctions facultatives#
def fin_placement_jaune():
    canvas.itemconfigure(table[0], text="Tour du Joueur 2", fill="blue")
    tour_plus_1()

def fin_placement_bleu():
    canvas.itemconfigure(table[0], text="Tour du Joueur 1", fill="yellow")
    tour_plus_1()

def fin_mvmt_jaune():
    tour_plus_1()
    canvas.itemconfigure(table[0], text="Tour du Joueur 2", fill="blue")

def fin_mvmt_bleu():
    tour_plus_1()
    canvas.itemconfigure(table[0], text="Tour du Joueur 1", fill="yellow")

#Fonctions#
def tour_plus_1():
    global tour
    tour.append(1)
    return tour

def stop():
    global tour
    for i in range (1, 10):
        canvas.itemconfigure(table[i], fill="black")
    tour.clear()
    alternance.append(1)
    if len(victoires1)==3:
        victoires1.clear()
        victoires2.clear()
        alternance.clear()
        canvas.itemconfigure(table[0], text="JOUEUR 1 GAGNE LA PARTIE !", fill="yellow")
        canvas.itemconfigure(table[-1], text="clic gauche : nouvelle partie\n       Joueur 1 commence")
    if len(victoires2)==3:
        victoires1.clear()
        victoires2.clear()
        alternance.clear()
        canvas.itemconfigure(table[0], text="JOUEUR 2 GAGNE LA PARTIE !", fill="blue")
        canvas.itemconfigure(table[-1], text="clic gauche : nouvelle partie\n       Joueur 1 commence")
    canvas.itemconfigure(table[10], text=len(victoires1))
    canvas.itemconfigure(table[11], text=len(victoires2))
    tour = tour + alternance
    return tour, alternance

def victoire_joueur1():
    victoires1.append(1)
    canvas.itemconfigure(table[0], text="Joueur 1 gagne la manche", fill="yellow")
    if len(alternance)%2 == 0:
        canvas.itemconfigure(table[-1], text="clic gauche : nouvelle manche\n       Joueur 2 commence")
    if len(alternance)%2 == 1:
        canvas.itemconfigure(table[-1], text="clic gauche : nouvelle manche\n       Joueur 1 commence")
    stop()

def victoire_joueur2():
    victoires2.append(2)
    canvas.itemconfigure(table[0], text="Joueur 2 gagne la manche", fill="blue")
    if len(alternance)%2 == 0:
        canvas.itemconfigure(table[-1], text="clic gauche : nouvelle manche\n       Joueur 2 commence")
    if len(alternance)%2 == 1:
        canvas.itemconfigure(table[-1], text="clic gauche : nouvelle manche\n       Joueur 1 commence")
    stop()

def victoire():
    if (canvas.itemcget(table[1], 'fill')=="yellow") and (canvas.itemcget(table[2], 'fill')=="yellow") and (canvas.itemcget(table[3], 'fill')=="yellow"):
        victoire_joueur1()
    if (canvas.itemcget(table[4], 'fill')=="yellow") and (canvas.itemcget(table[5], 'fill')=="yellow") and (canvas.itemcget(table[6], 'fill')=="yellow"):
        victoire_joueur1()
    if (canvas.itemcget(table[7], 'fill')=="yellow") and (canvas.itemcget(table[8], 'fill')=="yellow") and (canvas.itemcget(table[9], 'fill')=="yellow"):
        victoire_joueur1()
    if (canvas.itemcget(table[1], 'fill')=="yellow") and (canvas.itemcget(table[4], 'fill')=="yellow") and (canvas.itemcget(table[7], 'fill')=="yellow"):
        victoire_joueur1()
    if (canvas.itemcget(table[2], 'fill')=="yellow") and (canvas.itemcget(table[5], 'fill')=="yellow") and (canvas.itemcget(table[8], 'fill')=="yellow"):
        victoire_joueur1()
    if (canvas.itemcget(table[3], 'fill')=="yellow") and (canvas.itemcget(table[6], 'fill')=="yellow") and (canvas.itemcget(table[9], 'fill')=="yellow"):
        victoire_joueur1()
    if (canvas.itemcget(table[1], 'fill')=="yellow") and (canvas.itemcget(table[5], 'fill')=="yellow") and (canvas.itemcget(table[9], 'fill')=="yellow"):
        victoire_joueur1()
    if (canvas.itemcget(table[7], 'fill')=="yellow") and (canvas.itemcget(table[5], 'fill')=="yellow") and (canvas.itemcget(table[3], 'fill')=="yellow"):
        victoire_joueur1()
    if (canvas.itemcget(table[1], 'fill')=="blue") and (canvas.itemcget(table[2], 'fill')=="blue") and (canvas.itemcget(table[3], 'fill')=="blue"):
        victoire_joueur2()
    if (canvas.itemcget(table[4], 'fill')=="blue") and (canvas.itemcget(table[5], 'fill')=="blue") and (canvas.itemcget(table[6], 'fill')=="blue"):
        victoire_joueur2()
    if (canvas.itemcget(table[7], 'fill')=="blue") and (canvas.itemcget(table[8], 'fill')=="blue") and (canvas.itemcget(table[9], 'fill')=="blue"):
        victoire_joueur2()
    if (canvas.itemcget(table[1], 'fill')=="blue") and (canvas.itemcget(table[4], 'fill')=="blue") and (canvas.itemcget(table[7], 'fill')=="blue"):
        victoire_joueur2()
    if (canvas.itemcget(table[2], 'fill')=="blue") and (canvas.itemcget(table[5], 'fill')=="blue") and (canvas.itemcget(table[8], 'fill')=="blue"):
        victoire_joueur2()
    if (canvas.itemcget(table[3], 'fill')=="blue") and (canvas.itemcget(table[6], 'fill')=="blue") and (canvas.itemcget(table[9], 'fill')=="blue"):
        victoire_joueur2()
    if (canvas.itemcget(table[1], 'fill')=="blue") and (canvas.itemcget(table[5], 'fill')=="blue") and (canvas.itemcget(table[9], 'fill')=="blue"):
        victoire_joueur2()
    if (canvas.itemcget(table[7], 'fill')=="blue") and (canvas.itemcget(table[5], 'fill')=="blue") and (canvas.itemcget(table[3], 'fill')=="blue"):
        victoire_joueur2()

def match_nul():
    if len(tour)==30:
        canvas.itemconfigure(table[0], text="manche nulle", fill="white")
        if len(alternance)%2 == 0:
            canvas.itemconfigure(table[-1], text="clic gauche : nouvelle manche\n       Joueur 2 commence")
        if len(alternance)%2 == 1:
            canvas.itemconfigure(table[-1], text="clic gauche : nouvelle manche\n       Joueur 1 commence")
        stop()

def placement():
    if len(tour)%2 == 0:
        if 0<pos[0]<(3*LARGEUR/8) and 0<pos[1]<(3*HAUTEUR/8) and (canvas.itemcget(table[1], 'fill')=="black"):
            canvas.itemconfigure(table[1], fill="yellow")
            fin_placement_jaune()
        if (3*LARGEUR/8)<=pos[0]<=(5*LARGEUR/8) and 0<pos[1]<(3*HAUTEUR/8) and (canvas.itemcget(table[2], 'fill')=="black"):
            canvas.itemconfigure(table[2], fill="yellow")
            fin_placement_jaune()
        if (5*LARGEUR/8)<pos[0]<LARGEUR and 0<pos[1]<(3*HAUTEUR/8) and (canvas.itemcget(table[3], 'fill')=="black"):
            canvas.itemconfigure(table[3], fill="yellow")
            fin_placement_jaune()
        if 0<pos[0]<(3*LARGEUR/8) and (3*HAUTEUR/8)<=pos[1]<=(5*HAUTEUR/8) and (canvas.itemcget(table[4], 'fill')=="black"):
            canvas.itemconfigure(table[4], fill="yellow")
            fin_placement_jaune()
        if (3*LARGEUR/8)<=pos[0]<=(5*LARGEUR/8) and (3*HAUTEUR/8)<=pos[1]<=(5*HAUTEUR/8) and (canvas.itemcget(table[5], 'fill')=="black"):
            canvas.itemconfigure(table[5], fill="yellow")
            fin_placement_jaune()
        if (5*LARGEUR/8)<pos[0]<LARGEUR and (3*HAUTEUR/8)<=pos[1]<=(5*HAUTEUR/8) and (canvas.itemcget(table[6], 'fill')=="black"):
            canvas.itemconfigure(table[6], fill="yellow")
            fin_placement_jaune()
        if 0<pos[0]<(3*LARGEUR/8) and (5*HAUTEUR/8)<pos[1]<HAUTEUR and (canvas.itemcget(table[7], 'fill')=="black"):
            canvas.itemconfigure(table[7], fill="yellow")
            fin_placement_jaune()
        if (3*LARGEUR/8)<=pos[0]<=(5*LARGEUR/8) and (5*HAUTEUR/8)<pos[1]<HAUTEUR and (canvas.itemcget(table[8], 'fill')=="black"):
            canvas.itemconfigure(table[8], fill="yellow")
            fin_placement_jaune()
        if (5*LARGEUR/8)<pos[0]<LARGEUR and (5*HAUTEUR/8)<pos[1]<HAUTEUR and (canvas.itemcget(table[9], 'fill')=="black"):
            canvas.itemconfigure(table[9], fill="yellow")
            fin_placement_jaune()
    if len(tour)%2 == 1:
        if 0<pos[0]<(3*LARGEUR/8) and 0<pos[1]<(3*HAUTEUR/8) and (canvas.itemcget(table[1], 'fill')=="black"):
            canvas.itemconfigure(table[1], fill="blue")
            fin_placement_bleu()
        if (3*LARGEUR/8)<=pos[0]<=(5*LARGEUR/8) and 0<pos[1]<(3*HAUTEUR/8) and (canvas.itemcget(table[2], 'fill')=="black"):
            canvas.itemconfigure(table[2], fill="blue")
            fin_placement_bleu()
        if (5*LARGEUR/8)<pos[0]<LARGEUR and 0<pos[1]<(3*HAUTEUR/8) and (canvas.itemcget(table[3], 'fill')=="black"):
            canvas.itemconfigure(table[3], fill="blue")
            fin_placement_bleu()
        if 0<pos[0]<(3*LARGEUR/8) and (3*HAUTEUR/8)<=pos[1]<=(5*HAUTEUR/8) and (canvas.itemcget(table[4], 'fill')=="black"):
            canvas.itemconfigure(table[4], fill="blue")
            fin_placement_bleu()
        if (3*LARGEUR/8)<=pos[0]<=(5*LARGEUR/8) and (3*HAUTEUR/8)<=pos[1]<=(5*HAUTEUR/8) and (canvas.itemcget(table[5], 'fill')=="black"):
            canvas.itemconfigure(table[5], fill="blue")
            fin_placement_bleu()
        if (5*LARGEUR/8)<pos[0]<LARGEUR and (3*HAUTEUR/8)<=pos[1]<=(5*HAUTEUR/8) and (canvas.itemcget(table[6], 'fill')=="black"):
            canvas.itemconfigure(table[6], fill="blue")
            fin_placement_bleu()
        if 0<pos[0]<(3*LARGEUR/8) and (5*HAUTEUR/8)<pos[1]<HAUTEUR and (canvas.itemcget(table[7], 'fill')=="black"):
            canvas.itemconfigure(table[7], fill="blue")
            fin_placement_bleu()
        if (3*LARGEUR/8)<=pos[0]<=(5*LARGEUR/8) and (5*HAUTEUR/8)<pos[1]<HAUTEUR and (canvas.itemcget(table[8], 'fill')=="black"):
            canvas.itemconfigure(table[8], fill="blue")
            fin_placement_bleu()
        if (5*LARGEUR/8)<pos[0]<LARGEUR and (5*HAUTEUR/8)<pos[1]<HAUTEUR and (canvas.itemcget(table[9], 'fill')=="black"):
            canvas.itemconfigure(table[9], fill="blue")
            fin_placement_bleu()

def deplacement():
    canvas.itemconfigure(table[-1], text="    <clic gauche pour choisir un pion> \n<clic droit pour désélectionner un pion>")
    choix_jeton()
    non_choix_jeton()
    mvmt_jeton()
    victoire()
    match_nul()

def choix_jeton():
    if len(tour)%2 == 0:
        if 0<pos[0]<(3*LARGEUR/8) and 0<pos[1]<(3*HAUTEUR/8) and (canvas.itemcget(table[1], 'fill')=="yellow") and (canvas.itemcget(table[2], 'fill')!="orange") and (canvas.itemcget(table[3], 'fill')!="orange") and (canvas.itemcget(table[4], 'fill')!="orange") and (canvas.itemcget(table[5], 'fill')!="orange") and (canvas.itemcget(table[6], 'fill')!="orange") and (canvas.itemcget(table[7], 'fill')!="orange") and (canvas.itemcget(table[8], 'fill')!="orange") and (canvas.itemcget(table[9], 'fill')!="orange"):
            canvas.itemconfigure(table[1], fill="orange")
        if (3*LARGEUR/8)<=pos[0]<=(5*LARGEUR/8) and 0<pos[1]<(3*HAUTEUR/8) and (canvas.itemcget(table[2], 'fill')=="yellow") and (canvas.itemcget(table[1], 'fill')!="orange") and (canvas.itemcget(table[3], 'fill')!="orange") and (canvas.itemcget(table[4], 'fill')!="orange") and (canvas.itemcget(table[5], 'fill')!="orange") and (canvas.itemcget(table[6], 'fill')!="orange") and (canvas.itemcget(table[7], 'fill')!="orange") and (canvas.itemcget(table[8], 'fill')!="orange") and (canvas.itemcget(table[9], 'fill')!="orange"):
            canvas.itemconfigure(table[2], fill="orange")
        if (5*LARGEUR/8)<pos[0]<LARGEUR and 0<pos[1]<(3*HAUTEUR/8) and (canvas.itemcget(table[3], 'fill')=="yellow") and (canvas.itemcget(table[2], 'fill')!="orange") and (canvas.itemcget(table[1], 'fill')!="orange") and (canvas.itemcget(table[4], 'fill')!="orange") and (canvas.itemcget(table[5], 'fill')!="orange") and (canvas.itemcget(table[6], 'fill')!="orange") and (canvas.itemcget(table[7], 'fill')!="orange") and (canvas.itemcget(table[8], 'fill')!="orange") and (canvas.itemcget(table[9], 'fill')!="orange"):
            canvas.itemconfigure(table[3], fill="orange")
        if 0<pos[0]<(3*LARGEUR/8) and (3*HAUTEUR/8)<=pos[1]<=(5*HAUTEUR/8) and (canvas.itemcget(table[4], 'fill')=="yellow") and (canvas.itemcget(table[2], 'fill')!="orange") and (canvas.itemcget(table[3], 'fill')!="orange") and (canvas.itemcget(table[1], 'fill')!="orange") and (canvas.itemcget(table[5], 'fill')!="orange") and (canvas.itemcget(table[6], 'fill')!="orange") and (canvas.itemcget(table[7], 'fill')!="orange") and (canvas.itemcget(table[8], 'fill')!="orange") and (canvas.itemcget(table[9], 'fill')!="orange"):
            canvas.itemconfigure(table[4], fill="orange")
        if (3*LARGEUR/8)<=pos[0]<=(5*LARGEUR/8) and (3*HAUTEUR/8)<=pos[1]<=(5*HAUTEUR/8) and (canvas.itemcget(table[5], 'fill')=="yellow") and (canvas.itemcget(table[2], 'fill')!="orange") and (canvas.itemcget(table[3], 'fill')!="orange") and (canvas.itemcget(table[4], 'fill')!="orange") and (canvas.itemcget(table[1], 'fill')!="orange") and (canvas.itemcget(table[6], 'fill')!="orange") and (canvas.itemcget(table[7], 'fill')!="orange") and (canvas.itemcget(table[8], 'fill')!="orange") and (canvas.itemcget(table[9], 'fill')!="orange"):
            canvas.itemconfigure(table[5], fill="orange")
        if (5*LARGEUR/8)<pos[0]<LARGEUR and (3*HAUTEUR/8)<=pos[1]<=(5*HAUTEUR/8) and (canvas.itemcget(table[6], 'fill')=="yellow") and (canvas.itemcget(table[2], 'fill')!="orange") and (canvas.itemcget(table[3], 'fill')!="orange") and (canvas.itemcget(table[4], 'fill')!="orange") and (canvas.itemcget(table[5], 'fill')!="orange") and (canvas.itemcget(table[1], 'fill')!="orange") and (canvas.itemcget(table[7], 'fill')!="orange") and (canvas.itemcget(table[8], 'fill')!="orange") and (canvas.itemcget(table[9], 'fill')!="orange"):
            canvas.itemconfigure(table[6], fill="orange")
        if 0<pos[0]<(3*LARGEUR/8) and (5*HAUTEUR/8)<pos[1]<HAUTEUR and (canvas.itemcget(table[7], 'fill')=="yellow") and (canvas.itemcget(table[2], 'fill')!="orange") and (canvas.itemcget(table[3], 'fill')!="orange") and (canvas.itemcget(table[4], 'fill')!="orange") and (canvas.itemcget(table[5], 'fill')!="orange") and (canvas.itemcget(table[6], 'fill')!="orange") and (canvas.itemcget(table[1], 'fill')!="orange") and (canvas.itemcget(table[8], 'fill')!="orange") and (canvas.itemcget(table[9], 'fill')!="orange"):
            canvas.itemconfigure(table[7], fill="orange")
        if (3*LARGEUR/8)<=pos[0]<=(5*LARGEUR/8) and (5*HAUTEUR/8)<pos[1]<HAUTEUR and (canvas.itemcget(table[8], 'fill')=="yellow") and (canvas.itemcget(table[2], 'fill')!="orange") and (canvas.itemcget(table[3], 'fill')!="orange") and (canvas.itemcget(table[4], 'fill')!="orange") and (canvas.itemcget(table[5], 'fill')!="orange") and (canvas.itemcget(table[6], 'fill')!="orange") and (canvas.itemcget(table[7], 'fill')!="orange") and (canvas.itemcget(table[1], 'fill')!="orange") and (canvas.itemcget(table[9], 'fill')!="orange"):
            canvas.itemconfigure(table[8], fill="orange")
        if (5*LARGEUR/8)<pos[0]<LARGEUR and (5*HAUTEUR/8)<pos[1]<HAUTEUR and (canvas.itemcget(table[9], 'fill')=="yellow") and (canvas.itemcget(table[2], 'fill')!="orange") and (canvas.itemcget(table[3], 'fill')!="orange") and (canvas.itemcget(table[4], 'fill')!="orange") and (canvas.itemcget(table[5], 'fill')!="orange") and (canvas.itemcget(table[6], 'fill')!="orange") and (canvas.itemcget(table[7], 'fill')!="orange") and (canvas.itemcget(table[8], 'fill')!="orange") and (canvas.itemcget(table[1], 'fill')!="orange"):
            canvas.itemconfigure(table[9], fill="orange")
    if len(tour)%2 == 1:
        if 0<pos[0]<(3*LARGEUR/8) and 0<pos[1]<(3*HAUTEUR/8) and (canvas.itemcget(table[1], 'fill')=="blue") and (canvas.itemcget(table[2], 'fill')!="light blue") and (canvas.itemcget(table[3], 'fill')!="light blue") and (canvas.itemcget(table[4], 'fill')!="light blue") and (canvas.itemcget(table[5], 'fill')!="light blue") and (canvas.itemcget(table[6], 'fill')!="light blue") and (canvas.itemcget(table[7], 'fill')!="light blue") and (canvas.itemcget(table[8], 'fill')!="light blue") and (canvas.itemcget(table[9], 'fill')!="light blue"):
            canvas.itemconfigure(table[1], fill="light blue")
        if (3*LARGEUR/8)<=pos[0]<=(5*LARGEUR/8) and 0<pos[1]<(3*HAUTEUR/8) and (canvas.itemcget(table[2], 'fill')=="blue") and (canvas.itemcget(table[1], 'fill')!="light blue") and (canvas.itemcget(table[3], 'fill')!="light blue") and (canvas.itemcget(table[4], 'fill')!="light blue") and (canvas.itemcget(table[5], 'fill')!="light blue") and (canvas.itemcget(table[6], 'fill')!="light blue") and (canvas.itemcget(table[7], 'fill')!="light blue") and (canvas.itemcget(table[8], 'fill')!="light blue") and (canvas.itemcget(table[9], 'fill')!="light blue"):
            canvas.itemconfigure(table[2], fill="light blue")
        if (5*LARGEUR/8)<pos[0]<LARGEUR and 0<pos[1]<(3*HAUTEUR/8) and (canvas.itemcget(table[3], 'fill')=="blue") and (canvas.itemcget(table[2], 'fill')!="light blue") and (canvas.itemcget(table[1], 'fill')!="light blue") and (canvas.itemcget(table[4], 'fill')!="light blue") and (canvas.itemcget(table[5], 'fill')!="light blue") and (canvas.itemcget(table[6], 'fill')!="light blue") and (canvas.itemcget(table[7], 'fill')!="light blue") and (canvas.itemcget(table[8], 'fill')!="light blue") and (canvas.itemcget(table[9], 'fill')!="light blue"):
            canvas.itemconfigure(table[3], fill="light blue")
        if 0<pos[0]<(3*LARGEUR/8) and (3*HAUTEUR/8)<=pos[1]<=(5*HAUTEUR/8) and (canvas.itemcget(table[4], 'fill')=="blue") and (canvas.itemcget(table[2], 'fill')!="light blue") and (canvas.itemcget(table[3], 'fill')!="light blue") and (canvas.itemcget(table[1], 'fill')!="light blue") and (canvas.itemcget(table[5], 'fill')!="light blue") and (canvas.itemcget(table[6], 'fill')!="light blue") and (canvas.itemcget(table[7], 'fill')!="light blue") and (canvas.itemcget(table[8], 'fill')!="light blue") and (canvas.itemcget(table[9], 'fill')!="light blue"):
            canvas.itemconfigure(table[4], fill="light blue")
        if (3*LARGEUR/8)<=pos[0]<=(5*LARGEUR/8) and (3*HAUTEUR/8)<=pos[1]<=(5*HAUTEUR/8) and (canvas.itemcget(table[5], 'fill')=="blue") and (canvas.itemcget(table[2], 'fill')!="light blue") and (canvas.itemcget(table[3], 'fill')!="light blue") and (canvas.itemcget(table[4], 'fill')!="light blue") and (canvas.itemcget(table[1], 'fill')!="light blue") and (canvas.itemcget(table[6], 'fill')!="light blue") and (canvas.itemcget(table[7], 'fill')!="light blue") and (canvas.itemcget(table[8], 'fill')!="light blue") and (canvas.itemcget(table[9], 'fill')!="light blue"):
            canvas.itemconfigure(table[5], fill="light blue")
        if (5*LARGEUR/8)<pos[0]<LARGEUR and (3*HAUTEUR/8)<=pos[1]<=(5*HAUTEUR/8) and (canvas.itemcget(table[6], 'fill')=="blue") and (canvas.itemcget(table[2], 'fill')!="light blue") and (canvas.itemcget(table[3], 'fill')!="light blue") and (canvas.itemcget(table[4], 'fill')!="light blue") and (canvas.itemcget(table[5], 'fill')!="light blue") and (canvas.itemcget(table[1], 'fill')!="light blue") and (canvas.itemcget(table[7], 'fill')!="light blue") and (canvas.itemcget(table[8], 'fill')!="light blue") and (canvas.itemcget(table[9], 'fill')!="light blue"):
            canvas.itemconfigure(table[6], fill="light blue")
        if 0<pos[0]<(3*LARGEUR/8) and (5*HAUTEUR/8)<pos[1]<HAUTEUR and (canvas.itemcget(table[7], 'fill')=="blue") and (canvas.itemcget(table[2], 'fill')!="light blue") and (canvas.itemcget(table[3], 'fill')!="light blue") and (canvas.itemcget(table[4], 'fill')!="light blue") and (canvas.itemcget(table[5], 'fill')!="light blue") and (canvas.itemcget(table[6], 'fill')!="light blue") and (canvas.itemcget(table[1], 'fill')!="light blue") and (canvas.itemcget(table[8], 'fill')!="light blue") and (canvas.itemcget(table[9], 'fill')!="light blue"):
            canvas.itemconfigure(table[7], fill="light blue")
        if (3*LARGEUR/8)<=pos[0]<=(5*LARGEUR/8) and (5*HAUTEUR/8)<pos[1]<HAUTEUR and (canvas.itemcget(table[8], 'fill')=="blue") and (canvas.itemcget(table[2], 'fill')!="light blue") and (canvas.itemcget(table[3], 'fill')!="light blue") and (canvas.itemcget(table[4], 'fill')!="light blue") and (canvas.itemcget(table[5], 'fill')!="light blue") and (canvas.itemcget(table[6], 'fill')!="light blue") and (canvas.itemcget(table[7], 'fill')!="light blue") and (canvas.itemcget(table[1], 'fill')!="light blue") and (canvas.itemcget(table[9], 'fill')!="light blue"):
            canvas.itemconfigure(table[8], fill="light blue")
        if (5*LARGEUR/8)<pos[0]<LARGEUR and (5*HAUTEUR/8)<pos[1]<HAUTEUR and (canvas.itemcget(table[9], 'fill')=="blue") and (canvas.itemcget(table[2], 'fill')!="light blue") and (canvas.itemcget(table[3], 'fill')!="light blue") and (canvas.itemcget(table[4], 'fill')!="light blue") and (canvas.itemcget(table[5], 'fill')!="light blue") and (canvas.itemcget(table[6], 'fill')!="light blue") and (canvas.itemcget(table[7], 'fill')!="light blue") and (canvas.itemcget(table[8], 'fill')!="light blue") and (canvas.itemcget(table[1], 'fill')!="light blue"):
            canvas.itemconfigure(table[9], fill="light blue")

def non_choix_jeton():
    if 0<pos3[0]<(3*LARGEUR/8) and 0<pos3[1]<(3*HAUTEUR/8) and (canvas.itemcget(table[1], 'fill')=="orange"):
        canvas.itemconfigure(table[1], fill="yellow")
    if (3*LARGEUR/8)<=pos3[0]<=(5*LARGEUR/8) and 0<pos3[1]<(3*HAUTEUR/8) and (canvas.itemcget(table[2], 'fill')=="orange"):
        canvas.itemconfigure(table[2], fill="yellow")
    if (5*LARGEUR/8)<pos3[0]<LARGEUR and 0<pos3[1]<(3*HAUTEUR/8) and (canvas.itemcget(table[3], 'fill')=="orange"):
        canvas.itemconfigure(table[3], fill="yellow")
    if 0<pos3[0]<(3*LARGEUR/8) and (3*HAUTEUR/8)<=pos3[1]<=(5*HAUTEUR/8) and (canvas.itemcget(table[4], 'fill')=="orange"):
        canvas.itemconfigure(table[4], fill="yellow")
    if (3*LARGEUR/8)<=pos3[0]<=(5*LARGEUR/8) and (3*HAUTEUR/8)<=pos3[1]<=(5*HAUTEUR/8) and (canvas.itemcget(table[5], 'fill')=="orange"):
        canvas.itemconfigure(table[5], fill="yellow")
    if (5*LARGEUR/8)<pos3[0]<LARGEUR and (3*HAUTEUR/8)<=pos3[1]<=(5*HAUTEUR/8) and (canvas.itemcget(table[6], 'fill')=="orange"):
        canvas.itemconfigure(table[6], fill="yellow")
    if 0<pos3[0]<(3*LARGEUR/8) and (5*HAUTEUR/8)<pos3[1]<HAUTEUR and (canvas.itemcget(table[7], 'fill')=="orange"):
        canvas.itemconfigure(table[7], fill="yellow")
    if (3*LARGEUR/8)<=pos3[0]<=(5*LARGEUR/8) and (5*HAUTEUR/8)<pos3[1]<HAUTEUR and (canvas.itemcget(table[8], 'fill')=="orange"):
        canvas.itemconfigure(table[8], fill="yellow")
    if (5*LARGEUR/8)<pos3[0]<LARGEUR and (5*HAUTEUR/8)<pos3[1]<HAUTEUR and (canvas.itemcget(table[9], 'fill')=="orange"):
        canvas.itemconfigure(table[9], fill="yellow")
    if 0<pos3[0]<(3*LARGEUR/8) and 0<pos3[1]<(3*HAUTEUR/8) and (canvas.itemcget(table[1], 'fill')=="light blue"):
        canvas.itemconfigure(table[1], fill="blue")
    if (3*LARGEUR/8)<=pos3[0]<=(5*LARGEUR/8) and 0<pos3[1]<(3*HAUTEUR/8) and (canvas.itemcget(table[2], 'fill')=="light blue"):
        canvas.itemconfigure(table[2], fill="blue")
    if (5*LARGEUR/8)<pos3[0]<LARGEUR and 0<pos3[1]<(3*HAUTEUR/8) and (canvas.itemcget(table[3], 'fill')=="light blue"):
        canvas.itemconfigure(table[3], fill="blue")
    if 0<pos3[0]<(3*LARGEUR/8) and (3*HAUTEUR/8)<=pos3[1]<=(5*HAUTEUR/8) and (canvas.itemcget(table[4], 'fill')=="light blue"):
        canvas.itemconfigure(table[4], fill="blue")
    if (3*LARGEUR/8)<=pos3[0]<=(5*LARGEUR/8) and (3*HAUTEUR/8)<=pos3[1]<=(5*HAUTEUR/8) and (canvas.itemcget(table[5], 'fill')=="light blue"):
        canvas.itemconfigure(table[5], fill="blue")
    if (5*LARGEUR/8)<pos3[0]<LARGEUR and (3*HAUTEUR/8)<=pos3[1]<=(5*HAUTEUR/8) and (canvas.itemcget(table[6], 'fill')=="light blue"):
        canvas.itemconfigure(table[6], fill="blue")
    if 0<pos3[0]<(3*LARGEUR/8) and (5*HAUTEUR/8)<pos3[1]<HAUTEUR and (canvas.itemcget(table[7], 'fill')=="light blue"):
        canvas.itemconfigure(table[7], fill="blue")
    if (3*LARGEUR/8)<=pos3[0]<=(5*LARGEUR/8) and (5*HAUTEUR/8)<pos3[1]<HAUTEUR and (canvas.itemcget(table[8], 'fill')=="light blue"):
        canvas.itemconfigure(table[8], fill="blue")
    if (5*LARGEUR/8)<pos3[0]<LARGEUR and (5*HAUTEUR/8)<pos3[1]<HAUTEUR and (canvas.itemcget(table[9], 'fill')=="light blue"):
        canvas.itemconfigure(table[9], fill="blue")

def mvmt_jeton():
    if (canvas.itemcget(table[1], 'fill')=="orange"):
        if (3*LARGEUR/8)<=pos[0]<=(5*LARGEUR/8) and 0<pos[1]<(3*HAUTEUR/8) and (canvas.itemcget(table[2], 'fill')=="black"):
            canvas.itemconfigure(table[1], fill="black")
            canvas.itemconfigure(table[2], fill="yellow")
            fin_mvmt_jaune()
        if (3*LARGEUR/8)<=pos[0]<=(5*LARGEUR/8) and (3*HAUTEUR/8)<=pos[1]<=(5*HAUTEUR/8) and (canvas.itemcget(table[5], 'fill')=="black"):
            canvas.itemconfigure(table[1], fill="black")
            canvas.itemconfigure(table[5], fill="yellow")
            fin_mvmt_jaune()
        if 0<pos[0]<(3*LARGEUR/8) and (3*HAUTEUR/8)<=pos[1]<=(5*HAUTEUR/8) and (canvas.itemcget(table[4], 'fill')=="black"):
            canvas.itemconfigure(table[1], fill="black")
            canvas.itemconfigure(table[4], fill="yellow")
            fin_mvmt_jaune()
    if (canvas.itemcget(table[2], 'fill')=="orange"):
        if 0<pos[0]<(3*LARGEUR/8) and 0<pos[1]<(3*HAUTEUR/8) and (canvas.itemcget(table[1], 'fill')=="black"):
            canvas.itemconfigure(table[2], fill="black")
            canvas.itemconfigure(table[1], fill="yellow")
            fin_mvmt_jaune()
        if (3*LARGEUR/8)<=pos[0]<=(5*LARGEUR/8) and (3*HAUTEUR/8)<=pos[1]<=(5*HAUTEUR/8) and (canvas.itemcget(table[5], 'fill')=="black"):
            canvas.itemconfigure(table[2], fill="black")
            canvas.itemconfigure(table[5], fill="yellow")
            fin_mvmt_jaune()
        if (5*LARGEUR/8)<pos[0]<LARGEUR and 0<pos[1]<(3*HAUTEUR/8) and (canvas.itemcget(table[3], 'fill')=="black"):
            canvas.itemconfigure(table[2], fill="black")
            canvas.itemconfigure(table[3], fill="yellow")
            fin_mvmt_jaune()
    if (canvas.itemcget(table[3], 'fill')=="orange"):
        if (3*LARGEUR/8)<=pos[0]<=(5*LARGEUR/8) and 0<pos[1]<(3*HAUTEUR/8) and (canvas.itemcget(table[2], 'fill')=="black"):
            canvas.itemconfigure(table[3], fill="black")
            canvas.itemconfigure(table[2], fill="yellow")
            fin_mvmt_jaune()
        if (3*LARGEUR/8)<=pos[0]<=(5*LARGEUR/8) and (3*HAUTEUR/8)<=pos[1]<=(5*HAUTEUR/8) and (canvas.itemcget(table[5], 'fill')=="black"):
            canvas.itemconfigure(table[3], fill="black")
            canvas.itemconfigure(table[5], fill="yellow")
            fin_mvmt_jaune()
        if (5*LARGEUR/8)<pos[0]<LARGEUR and (3*HAUTEUR/8)<=pos[1]<=(5*HAUTEUR/8) and (canvas.itemcget(table[6], 'fill')=="black"):
            canvas.itemconfigure(table[3], fill="black")
            canvas.itemconfigure(table[6], fill="yellow")
            fin_mvmt_jaune()
    if (canvas.itemcget(table[4], 'fill')=="orange"):
        if 0<pos[0]<(3*LARGEUR/8) and 0<pos[1]<(3*HAUTEUR/8) and (canvas.itemcget(table[1], 'fill')=="black"):
            canvas.itemconfigure(table[4], fill="black")
            canvas.itemconfigure(table[1], fill="yellow")
            fin_mvmt_jaune()
        if (3*LARGEUR/8)<=pos[0]<=(5*LARGEUR/8) and (3*HAUTEUR/8)<=pos[1]<=(5*HAUTEUR/8) and (canvas.itemcget(table[5], 'fill')=="black"):
            canvas.itemconfigure(table[4], fill="black")
            canvas.itemconfigure(table[5], fill="yellow")
            fin_mvmt_jaune()
        if 0<pos[0]<(3*LARGEUR/8) and (5*HAUTEUR/8)<pos[1]<HAUTEUR and (canvas.itemcget(table[7], 'fill')=="black"):
            canvas.itemconfigure(table[4], fill="black")
            canvas.itemconfigure(table[7], fill="yellow")
            fin_mvmt_jaune()
    if (canvas.itemcget(table[5], 'fill')=="orange"):
        if 0<pos[0]<(3*LARGEUR/8) and 0<pos[1]<(3*HAUTEUR/8) and (canvas.itemcget(table[1], 'fill')=="black"):
            canvas.itemconfigure(table[5], fill="black")
            canvas.itemconfigure(table[1], fill="yellow")
            fin_mvmt_jaune()
        if (3*LARGEUR/8)<=pos[0]<=(5*LARGEUR/8) and 0<pos[1]<(3*HAUTEUR/8) and (canvas.itemcget(table[2], 'fill')=="black"):
            canvas.itemconfigure(table[5], fill="black")
            canvas.itemconfigure(table[2], fill="yellow")
            fin_mvmt_jaune()
        if (5*LARGEUR/8)<pos[0]<LARGEUR and 0<pos[1]<(3*HAUTEUR/8) and (canvas.itemcget(table[3], 'fill')=="black"):
            canvas.itemconfigure(table[5], fill="black")
            canvas.itemconfigure(table[3], fill="yellow")
            fin_mvmt_jaune()
        if 0<pos[0]<(3*LARGEUR/8) and (3*HAUTEUR/8)<=pos[1]<=(5*HAUTEUR/8) and (canvas.itemcget(table[4], 'fill')=="black"):
            canvas.itemconfigure(table[5], fill="black")
            canvas.itemconfigure(table[4], fill="yellow")
            fin_mvmt_jaune()
        if (5*LARGEUR/8)<pos[0]<LARGEUR and (3*HAUTEUR/8)<=pos[1]<=(5*HAUTEUR/8) and (canvas.itemcget(table[6], 'fill')=="black"):
            canvas.itemconfigure(table[5], fill="black")
            canvas.itemconfigure(table[6], fill="yellow")
            fin_mvmt_jaune()
        if 0<pos[0]<(3*LARGEUR/8) and (5*HAUTEUR/8)<pos[1]<HAUTEUR and (canvas.itemcget(table[7], 'fill')=="black"):
            canvas.itemconfigure(table[5], fill="black")
            canvas.itemconfigure(table[7], fill="yellow")
            fin_mvmt_jaune()
        if (3*LARGEUR/8)<=pos[0]<=(5*LARGEUR/8) and (5*HAUTEUR/8)<pos[1]<HAUTEUR and (canvas.itemcget(table[8], 'fill')=="black"):
            canvas.itemconfigure(table[5], fill="black")
            canvas.itemconfigure(table[8], fill="yellow")
            fin_mvmt_jaune()
        if (5*LARGEUR/8)<pos[0]<LARGEUR and (5*HAUTEUR/8)<pos[1]<HAUTEUR and (canvas.itemcget(table[9], 'fill')=="black"):
            canvas.itemconfigure(table[5], fill="black")
            canvas.itemconfigure(table[9], fill="yellow")
            fin_mvmt_jaune()
    if (canvas.itemcget(table[6], 'fill')=="orange"):
        if (5*LARGEUR/8)<pos[0]<LARGEUR and 0<pos[1]<(3*HAUTEUR/8) and (canvas.itemcget(table[3], 'fill')=="black"):
            canvas.itemconfigure(table[6], fill="black")
            canvas.itemconfigure(table[3], fill="yellow")
            fin_mvmt_jaune()
        if (3*LARGEUR/8)<=pos[0]<=(5*LARGEUR/8) and (3*HAUTEUR/8)<=pos[1]<=(5*HAUTEUR/8) and (canvas.itemcget(table[5], 'fill')=="black"):
            canvas.itemconfigure(table[6], fill="black")
            canvas.itemconfigure(table[5], fill="yellow")
            fin_mvmt_jaune()
        if (5*LARGEUR/8)<pos[0]<LARGEUR and (5*HAUTEUR/8)<pos[1]<HAUTEUR and (canvas.itemcget(table[9], 'fill')=="black"):
            canvas.itemconfigure(table[6], fill="black")
            canvas.itemconfigure(table[9], fill="yellow")
            fin_mvmt_jaune()
    if (canvas.itemcget(table[7], 'fill')=="orange"):
        if 0<pos[0]<(3*LARGEUR/8) and (3*HAUTEUR/8)<=pos[1]<=(5*HAUTEUR/8) and (canvas.itemcget(table[4], 'fill')=="black"):
            canvas.itemconfigure(table[7], fill="black")
            canvas.itemconfigure(table[4], fill="yellow")
            fin_mvmt_jaune()
        if (3*LARGEUR/8)<=pos[0]<=(5*LARGEUR/8) and (3*HAUTEUR/8)<=pos[1]<=(5*HAUTEUR/8) and (canvas.itemcget(table[5], 'fill')=="black"):
            canvas.itemconfigure(table[7], fill="black")
            canvas.itemconfigure(table[5], fill="yellow")
            fin_mvmt_jaune()
        if (3*LARGEUR/8)<=pos[0]<=(5*LARGEUR/8) and (5*HAUTEUR/8)<pos[1]<HAUTEUR and (canvas.itemcget(table[8], 'fill')=="black"):
            canvas.itemconfigure(table[7], fill="black")
            canvas.itemconfigure(table[8], fill="yellow")
            fin_mvmt_jaune()
    if (canvas.itemcget(table[8], 'fill')=="orange"):
        if 0<pos[0]<(3*LARGEUR/8) and (5*HAUTEUR/8)<pos[1]<HAUTEUR and (canvas.itemcget(table[7], 'fill')=="black"):
            canvas.itemconfigure(table[8], fill="black")
            canvas.itemconfigure(table[7], fill="yellow")
            fin_mvmt_jaune()
        if (3*LARGEUR/8)<=pos[0]<=(5*LARGEUR/8) and (3*HAUTEUR/8)<=pos[1]<=(5*HAUTEUR/8) and (canvas.itemcget(table[5], 'fill')=="black"):
            canvas.itemconfigure(table[8], fill="black")
            canvas.itemconfigure(table[5], fill="yellow")
            fin_mvmt_jaune()
        if (5*LARGEUR/8)<pos[0]<LARGEUR and (5*HAUTEUR/8)<pos[1]<HAUTEUR and (canvas.itemcget(table[9], 'fill')=="black"):
            canvas.itemconfigure(table[8], fill="black")
            canvas.itemconfigure(table[9], fill="yellow")
            fin_mvmt_jaune()
    if (canvas.itemcget(table[9], 'fill')=="orange"):
        if (5*LARGEUR/8)<pos[0]<LARGEUR and (3*HAUTEUR/8)<=pos[1]<=(5*HAUTEUR/8) and (canvas.itemcget(table[6], 'fill')=="black"):
            canvas.itemconfigure(table[9], fill="black")
            canvas.itemconfigure(table[6], fill="yellow")
            fin_mvmt_jaune()
        if (3*LARGEUR/8)<=pos[0]<=(5*LARGEUR/8) and (3*HAUTEUR/8)<=pos[1]<=(5*HAUTEUR/8) and (canvas.itemcget(table[5], 'fill')=="black"):
            canvas.itemconfigure(table[9], fill="black")
            canvas.itemconfigure(table[5], fill="yellow")
            fin_mvmt_jaune()
        if (3*LARGEUR/8)<=pos[0]<=(5*LARGEUR/8) and (5*HAUTEUR/8)<pos[1]<HAUTEUR and (canvas.itemcget(table[8], 'fill')=="black"):
            canvas.itemconfigure(table[9], fill="black")
            canvas.itemconfigure(table[8], fill="yellow")
            fin_mvmt_jaune()
    if (canvas.itemcget(table[1], 'fill')=="light blue"):
        if (3*LARGEUR/8)<=pos[0]<=(5*LARGEUR/8) and 0<pos[1]<(3*HAUTEUR/8) and (canvas.itemcget(table[2], 'fill')=="black"):
            canvas.itemconfigure(table[1], fill="black")
            canvas.itemconfigure(table[2], fill="blue")
            fin_mvmt_bleu()
        if (3*LARGEUR/8)<=pos[0]<=(5*LARGEUR/8) and (3*HAUTEUR/8)<=pos[1]<=(5*HAUTEUR/8) and (canvas.itemcget(table[5], 'fill')=="black"):
            canvas.itemconfigure(table[1], fill="black")
            canvas.itemconfigure(table[5], fill="blue")
            fin_mvmt_bleu()
        if 0<pos[0]<(3*LARGEUR/8) and (3*HAUTEUR/8)<=pos[1]<=(5*HAUTEUR/8) and (canvas.itemcget(table[4], 'fill')=="black"):
            canvas.itemconfigure(table[1], fill="black")
            canvas.itemconfigure(table[4], fill="blue")
            fin_mvmt_bleu()
    if (canvas.itemcget(table[2], 'fill')=="light blue"):
        if 0<pos[0]<(3*LARGEUR/8) and 0<pos[1]<(3*HAUTEUR/8) and (canvas.itemcget(table[1], 'fill')=="black"):
            canvas.itemconfigure(table[2], fill="black")
            canvas.itemconfigure(table[1], fill="blue")
            fin_mvmt_bleu()
        if (3*LARGEUR/8)<=pos[0]<=(5*LARGEUR/8) and (3*HAUTEUR/8)<=pos[1]<=(5*HAUTEUR/8) and (canvas.itemcget(table[5], 'fill')=="black"):
            canvas.itemconfigure(table[2], fill="black")
            canvas.itemconfigure(table[5], fill="blue")
            fin_mvmt_bleu()
        if (5*LARGEUR/8)<pos[0]<LARGEUR and 0<pos[1]<(3*HAUTEUR/8) and (canvas.itemcget(table[3], 'fill')=="black"):
            canvas.itemconfigure(table[2], fill="black")
            canvas.itemconfigure(table[3], fill="blue")
            fin_mvmt_bleu()
    if (canvas.itemcget(table[3], 'fill')=="light blue"):
        if (3*LARGEUR/8)<=pos[0]<=(5*LARGEUR/8) and 0<pos[1]<(3*HAUTEUR/8) and (canvas.itemcget(table[2], 'fill')=="black"):
            canvas.itemconfigure(table[3], fill="black")
            canvas.itemconfigure(table[2], fill="blue")
            fin_mvmt_bleu()
        if (3*LARGEUR/8)<=pos[0]<=(5*LARGEUR/8) and (3*HAUTEUR/8)<=pos[1]<=(5*HAUTEUR/8) and (canvas.itemcget(table[5], 'fill')=="black"):
            canvas.itemconfigure(table[3], fill="black")
            canvas.itemconfigure(table[5], fill="blue")
            fin_mvmt_bleu()
        if (5*LARGEUR/8)<pos[0]<LARGEUR and (3*HAUTEUR/8)<=pos[1]<=(5*HAUTEUR/8) and (canvas.itemcget(table[6], 'fill')=="black"):
            canvas.itemconfigure(table[3], fill="black")
            canvas.itemconfigure(table[6], fill="blue")
            fin_mvmt_bleu()
    if (canvas.itemcget(table[4], 'fill')=="light blue"):
        if 0<pos[0]<(3*LARGEUR/8) and 0<pos[1]<(3*HAUTEUR/8) and (canvas.itemcget(table[1], 'fill')=="black"):
            canvas.itemconfigure(table[4], fill="black")
            canvas.itemconfigure(table[1], fill="blue")
            fin_mvmt_bleu()
        if (3*LARGEUR/8)<=pos[0]<=(5*LARGEUR/8) and (3*HAUTEUR/8)<=pos[1]<=(5*HAUTEUR/8) and (canvas.itemcget(table[5], 'fill')=="black"):
            canvas.itemconfigure(table[4], fill="black")
            canvas.itemconfigure(table[5], fill="blue")
            fin_mvmt_bleu()
        if 0<pos[0]<(3*LARGEUR/8) and (5*HAUTEUR/8)<pos[1]<HAUTEUR and (canvas.itemcget(table[7], 'fill')=="black"):
            canvas.itemconfigure(table[4], fill="black")
            canvas.itemconfigure(table[7], fill="blue")
            fin_mvmt_bleu()
    if (canvas.itemcget(table[5], 'fill')=="light blue"):
        if 0<pos[0]<(3*LARGEUR/8) and 0<pos[1]<(3*HAUTEUR/8) and (canvas.itemcget(table[1], 'fill')=="black"):
            canvas.itemconfigure(table[5], fill="black")
            canvas.itemconfigure(table[1], fill="blue")
            fin_mvmt_bleu()
        if (3*LARGEUR/8)<=pos[0]<=(5*LARGEUR/8) and 0<pos[1]<(3*HAUTEUR/8) and (canvas.itemcget(table[2], 'fill')=="black"):
            canvas.itemconfigure(table[5], fill="black")
            canvas.itemconfigure(table[2], fill="blue")
            fin_mvmt_bleu()
        if (5*LARGEUR/8)<pos[0]<LARGEUR and 0<pos[1]<(3*HAUTEUR/8) and (canvas.itemcget(table[3], 'fill')=="black"):
            canvas.itemconfigure(table[5], fill="black")
            canvas.itemconfigure(table[3], fill="blue")
            fin_mvmt_bleu()
        if 0<pos[0]<(3*LARGEUR/8) and (3*HAUTEUR/8)<=pos[1]<=(5*HAUTEUR/8) and (canvas.itemcget(table[4], 'fill')=="black"):
            canvas.itemconfigure(table[5], fill="black")
            canvas.itemconfigure(table[4], fill="blue")
            fin_mvmt_bleu()
        if (5*LARGEUR/8)<pos[0]<LARGEUR and (3*HAUTEUR/8)<=pos[1]<=(5*HAUTEUR/8) and (canvas.itemcget(table[6], 'fill')=="black"):
            canvas.itemconfigure(table[5], fill="black")
            canvas.itemconfigure(table[6], fill="blue")
            fin_mvmt_bleu()
        if 0<pos[0]<(3*LARGEUR/8) and (5*HAUTEUR/8)<pos[1]<HAUTEUR and (canvas.itemcget(table[7], 'fill')=="black"):
            canvas.itemconfigure(table[5], fill="black")
            canvas.itemconfigure(table[7], fill="blue")
            fin_mvmt_bleu()
        if (3*LARGEUR/8)<=pos[0]<=(5*LARGEUR/8) and (5*HAUTEUR/8)<pos[1]<HAUTEUR and (canvas.itemcget(table[8], 'fill')=="black"):
            canvas.itemconfigure(table[5], fill="black")
            canvas.itemconfigure(table[8], fill="blue")
            fin_mvmt_bleu()
        if (5*LARGEUR/8)<pos[0]<LARGEUR and (5*HAUTEUR/8)<pos[1]<HAUTEUR and (canvas.itemcget(table[9], 'fill')=="black"):
            canvas.itemconfigure(table[5], fill="black")
            canvas.itemconfigure(table[9], fill="blue")
            fin_mvmt_bleu()
    if (canvas.itemcget(table[6], 'fill')=="light blue"):
        if (5*LARGEUR/8)<pos[0]<LARGEUR and 0<pos[1]<(3*HAUTEUR/8) and (canvas.itemcget(table[3], 'fill')=="black"):
            canvas.itemconfigure(table[6], fill="black")
            canvas.itemconfigure(table[3], fill="blue")
            fin_mvmt_bleu()
        if (3*LARGEUR/8)<=pos[0]<=(5*LARGEUR/8) and (3*HAUTEUR/8)<=pos[1]<=(5*HAUTEUR/8) and (canvas.itemcget(table[5], 'fill')=="black"):
            canvas.itemconfigure(table[6], fill="black")
            canvas.itemconfigure(table[5], fill="blue")
            fin_mvmt_bleu()
        if (5*LARGEUR/8)<pos[0]<LARGEUR and (5*HAUTEUR/8)<pos[1]<HAUTEUR and (canvas.itemcget(table[9], 'fill')=="black"):
            canvas.itemconfigure(table[6], fill="black")
            canvas.itemconfigure(table[9], fill="blue")
            fin_mvmt_bleu()
    if (canvas.itemcget(table[7], 'fill')=="light blue"):
        if 0<pos[0]<(3*LARGEUR/8) and (3*HAUTEUR/8)<=pos[1]<=(5*HAUTEUR/8) and (canvas.itemcget(table[4], 'fill')=="black"):
            canvas.itemconfigure(table[7], fill="black")
            canvas.itemconfigure(table[4], fill="blue")
            fin_mvmt_bleu()
        if (3*LARGEUR/8)<=pos[0]<=(5*LARGEUR/8) and (3*HAUTEUR/8)<=pos[1]<=(5*HAUTEUR/8) and (canvas.itemcget(table[5], 'fill')=="black"):
            canvas.itemconfigure(table[7], fill="black")
            canvas.itemconfigure(table[5], fill="blue")
            fin_mvmt_bleu()
        if (3*LARGEUR/8)<=pos[0]<=(5*LARGEUR/8) and (5*HAUTEUR/8)<pos[1]<HAUTEUR and (canvas.itemcget(table[8], 'fill')=="black"):
            canvas.itemconfigure(table[7], fill="black")
            canvas.itemconfigure(table[8], fill="blue")
            fin_mvmt_bleu()
    if (canvas.itemcget(table[8], 'fill')=="light blue"):
        if 0<pos[0]<(3*LARGEUR/8) and (5*HAUTEUR/8)<pos[1]<HAUTEUR and (canvas.itemcget(table[7], 'fill')=="black"):
            canvas.itemconfigure(table[8], fill="black")
            canvas.itemconfigure(table[7], fill="blue")
            fin_mvmt_bleu()
        if (3*LARGEUR/8)<=pos[0]<=(5*LARGEUR/8) and (3*HAUTEUR/8)<=pos[1]<=(5*HAUTEUR/8) and (canvas.itemcget(table[5], 'fill')=="black"):
            canvas.itemconfigure(table[8], fill="black")
            canvas.itemconfigure(table[5], fill="blue")
            fin_mvmt_bleu()
        if (5*LARGEUR/8)<pos[0]<LARGEUR and (5*HAUTEUR/8)<pos[1]<HAUTEUR and (canvas.itemcget(table[9], 'fill')=="black"):
            canvas.itemconfigure(table[8], fill="black")
            canvas.itemconfigure(table[9], fill="blue")
            fin_mvmt_bleu()
    if (canvas.itemcget(table[9], 'fill')=="light blue"):
        if (5*LARGEUR/8)<pos[0]<LARGEUR and (3*HAUTEUR/8)<=pos[1]<=(5*HAUTEUR/8) and (canvas.itemcget(table[6], 'fill')=="black"):
            canvas.itemconfigure(table[9], fill="black")
            canvas.itemconfigure(table[6], fill="blue")
            fin_mvmt_bleu()
        if (3*LARGEUR/8)<=pos[0]<=(5*LARGEUR/8) and (3*HAUTEUR/8)<=pos[1]<=(5*HAUTEUR/8) and (canvas.itemcget(table[5], 'fill')=="black"):
            canvas.itemconfigure(table[9], fill="black")
            canvas.itemconfigure(table[5], fill="blue")
            fin_mvmt_bleu()
        if (3*LARGEUR/8)<=pos[0]<=(5*LARGEUR/8) and (5*HAUTEUR/8)<pos[1]<HAUTEUR and (canvas.itemcget(table[8], 'fill')=="black"):
            canvas.itemconfigure(table[9], fill="black")
            canvas.itemconfigure(table[8], fill="blue")
            fin_mvmt_bleu()

def position(event):
    pos[0], pos[1]=event.x, event.y
    tour_de_jeu()

def position3(event):
    pos3[0], pos3[1]=event.x, event.y
    tour_de_jeu()

def creer_tabledejeu():
    for i in range (1, 4):
        canvas.create_line((i*LARGEUR/4), (HAUTEUR/4), (i*LARGEUR/4), (3*HAUTEUR/4))
        canvas.create_line((LARGEUR/4), (i*HAUTEUR/4), (3*LARGEUR/4), (i*HAUTEUR/4))
        canvas.create_line((LARGEUR/4), (HAUTEUR/4), (3*LARGEUR/4), (3*HAUTEUR/4))
        canvas.create_line((3*LARGEUR/4), (HAUTEUR/4), (LARGEUR/4), (3*HAUTEUR/4))
    texte = canvas.create_text(LARGEUR/2, HAUTEUR/10, fill="yellow", font=("Helvetica", 20), text="Tour du Joueur 1")
    victoiresJ1 = canvas.create_text(LARGEUR/10, HAUTEUR/10, fill="yellow", font=("Helvetica", 20), text=len(victoires1))
    victoiresJ2 = canvas.create_text(9*LARGEUR/10, HAUTEUR/10, fill="blue", font=("Helvetica", 20), text=len(victoires2))
    consignes = canvas.create_text(LARGEUR/2, 9*HAUTEUR/10, fill="white", font=("Helvetica", 20), text="<clic gauche pour placer un pion>")
    cercle1 = canvas.create_oval((LARGEUR/4)-rayon, (HAUTEUR/4)-rayon, (LARGEUR/4)+rayon, (HAUTEUR/4)+rayon, fill="black")
    cercle2 = canvas.create_oval((2*LARGEUR/4)-rayon, (HAUTEUR/4)-rayon, (2*LARGEUR/4)+rayon, (HAUTEUR/4)+rayon, fill="black")
    cercle3 = canvas.create_oval((3*LARGEUR/4)-rayon, (HAUTEUR/4)-rayon, (3*LARGEUR/4)+rayon, (HAUTEUR/4)+rayon, fill="black")
    cercle4 = canvas.create_oval((LARGEUR/4)-rayon, (2*HAUTEUR/4)-rayon, (LARGEUR/4)+rayon, (2*HAUTEUR/4)+rayon, fill="black")
    cercle5 = canvas.create_oval((2*LARGEUR/4)-rayon, (2*HAUTEUR/4)-rayon, (2*LARGEUR/4)+rayon, (2*HAUTEUR/4)+rayon, fill="black")
    cercle6 = canvas.create_oval((3*LARGEUR/4)-rayon, (2*HAUTEUR/4)-rayon, (3*LARGEUR/4)+rayon, (2*HAUTEUR/4)+rayon, fill="black")
    cercle7 = canvas.create_oval((LARGEUR/4)-rayon, (3*HAUTEUR/4)-rayon, (LARGEUR/4)+rayon, (3*HAUTEUR/4)+rayon, fill="black")
    cercle8 = canvas.create_oval((2*LARGEUR/4)-rayon, (3*HAUTEUR/4)-rayon, (2*LARGEUR/4)+rayon, (3*HAUTEUR/4)+rayon, fill="black")
    cercle9 = canvas.create_oval((3*LARGEUR/4)-rayon, (3*HAUTEUR/4)-rayon, (3*LARGEUR/4)+rayon, (3*HAUTEUR/4)+rayon, fill="black")
    return [texte, cercle1, cercle2, cercle3, cercle4, cercle5, cercle6, cercle7, cercle8, cercle9, victoiresJ1, victoiresJ2, consignes]

def tour_de_jeu():
    if len(tour) < 6 + len(alternance):
        canvas.itemconfigure(table[-1], text="<clic gauche pour placer un pion>")
        placement()
        victoire()
    if len(tour) >= 6 + len(alternance):
        deplacement()

#programme principal#
racine = tk.Tk()
racine.title("Jeu Tapatan")
canvas = tk.Canvas(racine, bg="brown", width=LARGEUR, height=HAUTEUR)
canvas.grid()

table = creer_tabledejeu()
canvas.bind('<Button-1>', position)
canvas.bind('<Button-3>', position3)

racine.mainloop()