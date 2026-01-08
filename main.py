import tkinter as tk #création interface graphique
from logique import (
    init_grille, ajout_chiffre,
    deplacement_gauche, deplacement_droite,
    deplacement_haut, deplacement_bas,
    victoire, game_over
)
#Toutes les couleurs
COULEURS = {
    0: "#cdc1b4",
    2: "#eee4da",
    4: "#ede0c8",
    8: "#f2b179",
    16: "#f59563",
    32: "#f67c5f",
    64: "#f65e3b",
    128: "#edcf72",
    256: "#edcc61",
    512: "#edc850",
    1024: "#edc53f",
    2048: "#edc22e"
}

grille = init_grille()
grille = ajout_chiffre(grille)
grille = ajout_chiffre(grille)
score = 0

fenetre = tk.Tk()
fenetre.title("2048 - NSI")
fenetre.resizable(False, False)

label_score = tk.Label(fenetre, text="Score : 0", font=("Arial", 16))
label_score.pack(pady=10)

frame_grille = tk.Frame(fenetre, bg="#bbada0", padx=10, pady=10)# taille du jeu
frame_grille.pack()

labels = [[None]*4 for _ in range(4)]
for i in range(4):
    for j in range(4):
        lbl = tk.Label(
            frame_grille,
            text="",
            width=4,
            height=2,
            font=("Arial", 24, "bold"),
            bg=COULEURS[0]
        )
        lbl.grid(row=i, column=j, padx=5, pady=5)
        labels[i][j] = lbl

label_message = tk.Label(fenetre, text="", font=("Arial", 14))
label_message.pack(pady=5)

def maj_affichage():
    for i in range(4):
        for j in range(4):
            v = grille[i][j]
            labels[i][j].config(
                text="" if v == 0 else str(v),
                bg=COULEURS.get(v, "#3c3a32")
            )
    label_score.config(text=f"Score : {score}")

def nouvelle_partie():
    global grille, score
    grille = init_grille()
    grille = ajout_chiffre(grille)
    grille = ajout_chiffre(grille)
    score = 0
    label_message.config(text="")
    maj_affichage()

def gestion_touche(event):# atribution touche et role
    global grille, score

    if event.keysym == "Left":# deplacement fléche vers la gauche
        new, gain, change = deplacement_gauche(grille)
    elif event.keysym == "Right":# deplacement fléche vers la doite
        new, gain, change = deplacement_droite(grille)
    elif event.keysym == "Up":# deplacement fléche vers le haut
        new, gain, change = deplacement_haut(grille)
    elif event.keysym == "Down":# deplacement fléche vers le bas
        new, gain, change = deplacement_bas(grille)
    else:
        return

    if change:
        grille = new
        score += gain
        ajout_chiffre(grille)
        maj_affichage()

        if victoire(grille):# affiche de la victoire
            label_message.config(text="Victoire !")
        elif game_over(grille):# affichage de la defaite
            label_message.config(text="Game Over")

btn_reset = tk.Button(fenetre, text="Nouvelle partie", command=nouvelle_partie) # button pour redémarrer une nouvelle partie
btn_reset.pack(pady=10)

fenetre.bind("<Key>", gestion_touche)

maj_affichage()
fenetre.mainloop()
