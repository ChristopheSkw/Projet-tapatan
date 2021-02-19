import tkinter as tk
from random import *

racine = tk.Tk()
racine.title("couleurs")
dimensions = 256
couleur = "green"
c = tk.StringVar()

HEIGHT, WIDTH = dimensions, dimensions

def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def draw_pixel(i, j, color):
    canvas.create_rectangle (i, j, i+2, j+2, fill = color, outline = color)
    pass

def affiche_pixels_alea ():
    for i in range (0, WIDTH+1, 2):
        for j in range (0, HEIGHT+1, 2):
            color = get_color(randint(0, 255), randint(0, 255), randint(0, 255))
            draw_pixel(i, j, color)

def affiche_pixels_gris ():
    for i in range (0, WIDTH+1, 2):
        color = get_color(i, i, i)
        for j in range (0, HEIGHT+1, 2):
            draw_pixel(i, j, color)

def affiche_pixels_colorés ():
    for i in range (0, WIDTH, 2):
        for j in range (0, HEIGHT, 2):
            if c.get() == "jamaica":
                color = get_color(i, j, 0)
            if c.get() == "nokia":
                color = get_color(0, i, j)
            if c.get() == "pixel":
                color = get_color(i, 0, j)
            if c.get() == "iceland":
                color = get_color(i, j, j)
            if c.get() == "joker":
                color = get_color(j, i, j)
            if c.get() == "bosnie":
                color = get_color(i, i, j)
            draw_pixel(i, j, color)

def choix_couleur ():
    c.set (input("choisissez un thème de couleurs : nokia, pixel, jamaica, joker, bosnie, iceland >>> "))
    return c

canvas = tk.Canvas (racine, bg = "black", width = WIDTH, height = HEIGHT, relief = "sunken")
Bouton_Aleatoire = tk.Button (text = "Aléatoire", padx = 12, pady = 5, activebackground = "grey", bd = 4, command = affiche_pixels_alea)
Bouton_Degrade_Gris = tk.Button (text = "Dégradé gris", padx = 12, pady = 5, activebackground = "grey", bd = 4, command = affiche_pixels_gris)
Bouton_Degrade_2D = tk.Button (text = "Dégradé 2D", padx = 12, pady = 5, activebackground = "grey", bd = 4, command = affiche_pixels_colorés)
Bouton_Couleur = tk.Button (text = "Choix couleur", padx = 12, pady = 5, activebackground = "grey", bd = 4, command = choix_couleur)

canvas.grid(row = 0, rowspan = 4, column = 1)
Bouton_Couleur.grid(row = 0, column = 0)
Bouton_Aleatoire.grid(row = 1, column = 0)
Bouton_Degrade_Gris.grid(row = 2, column = 0)
Bouton_Degrade_2D.grid(row = 3, column = 0)

racine.mainloop()
