# Groupe-3-Cartable-num-rique

Pour le jeu tapatan que nous avons créé, pendant la phase de placement des pions il suffit de faire un clic gauche sur une case libre pour placer un pion. Pendant la phase de déplacement, un premier clic gauche sur une case avec un pion de la couleur du joueur dont c'est le tour sélectionne ce pion, et un deuxième clic gauche sur une case libre adjacente déplace ce pion. Un clic droit sur un pion sélectionné le désélectionne.
Toutes les informations de déplacement sont indiquées sur le plateau pendant le jeu.

Concernant les bugs, nous en avons pendant la phase de déplacement. Parfois lorsque l'on souhaite sélectionner un pion, sa couleur ne change pas (donc la sélection n'est pas faite). Il faut alors sélectionner/déselectionner un autre pion puis sélectionner le pion que l'on souhaitait bouger initialement.

Nous n'avons pas eu le temps ni le niveau de nous pencher sur les fonctionnalités avancées.
Nous pensons cependant pour la sauvegarde de partie qu'il faut écrire les informations à sauvegarder dans un fichier suite à un clic sur un bouton "sauvegarde", et récupérer les informations contenues dans ce fichier suite à un clic sur un bouton "récupérer sauvegarde".

Concernant le match nul, nous n'avons pu que le fixer à 30 tours de jeu et non après 3 occurences d'une même répartition des pions sur le plateau comme demandé.
Nous pensons qu'il aurait fallu utiliser des listes imbriquées contenant les informations des cases, mais il aurait fallu modifier l'ensemble de notre code pour cela et nous n'avions pas le temps, notre code étant alors déjà bien avancé.
