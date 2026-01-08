import random

TAILLE = 4


def init_grille():
    """
    Crée une grille 4x4 initialisée avec des zéros.
    """
    return [[0] * TAILLE for _ in range(TAILLE)]


def tasser_ligne(ligne):
    """
    Déplace les nombres non nuls d’une ligne vers la gauche.
    """
    non_zeros = [x for x in ligne if x != 0]
    return non_zeros + [0] * (TAILLE - len(non_zeros))


def fusion_ligne(ligne):
    """
    Fusionne les tuiles d’une ligne selon les règles du 2048.
    """
    score = 0
    ligne = tasser_ligne(ligne)
    i = 0

    while i < TAILLE - 1:
        if ligne[i] != 0 and ligne[i] == ligne[i + 1]:
            ligne[i] *= 2
            score += ligne[i]
            ligne[i + 1] = 0
            i += 2
        else:
            i += 1

    ligne = tasser_ligne(ligne)
    return ligne, score


def deplacement_gauche(grille):
    """
    Applique un déplacement vers la gauche à toute la grille.
    """
    nouvelle = []
    score_total = 0
    change = False

    for ligne in grille:
        nl, sc = fusion_ligne(ligne[:])
        if nl != ligne:
            change = True
        nouvelle.append(nl)
        score_total += sc

    return nouvelle, score_total, change


def deplacement_droite(grille):
    """
    Applique un déplacement vers la droite à toute la grille.
    """
    nouvelle = []
    score_total = 0
    change = False

    for ligne in grille:
        inv = list(reversed(ligne))
        nl, sc = fusion_ligne(inv)
        nl = list(reversed(nl))
        if nl != ligne:
            change = True
        nouvelle.append(nl)
        score_total += sc

    return nouvelle, score_total, change


def deplacement_haut(grille):
    """
    Applique un déplacement vers le haut à toute la grille.
    """
    nouvelle = [[0] * TAILLE for _ in range(TAILLE)]
    score_total = 0
    change = False

    for j in range(TAILLE):
        col = [grille[i][j] for i in range(TAILLE)]
        nc, sc = fusion_ligne(col)
        score_total += sc
        for i in range(TAILLE):
            nouvelle[i][j] = nc[i]
            if nouvelle[i][j] != grille[i][j]:
                change = True

    return nouvelle, score_total, change


def deplacement_bas(grille):
    """
    Applique un déplacement vers le bas à toute la grille.
    """
    nouvelle = [[0] * TAILLE for _ in range(TAILLE)]
    score_total = 0
    change = False

    for j in range(TAILLE):
        col = [grille[i][j] for i in range(TAILLE)][::-1]
        nc, sc = fusion_ligne(col)
        nc = nc[::-1]
        score_total += sc
        for i in range(TAILLE):
            nouvelle[i][j] = nc[i]
            if nouvelle[i][j] != grille[i][j]:
                change = True

    return nouvelle, score_total, change


def ajout_chiffre(grille):
    """
    Ajoute une tuile (2 ou 4) dans une case vide de la grille.
    """
    vides = [(i, j) for i in range(TAILLE) for j in range(TAILLE) if grille[i][j] == 0]
    if not vides:
        return grille

    i, j = random.choice(vides)
    grille[i][j] = 4 if random.random() < 0.10 else 2
    return grille


def victoire(grille):
    """
    Vérifie si la tuile 2048 est présente dans la grille.
    """
    return any(2048 in ligne for ligne in grille)


def game_over(grille):
    """
    Vérifie si aucun coup n’est encore possible.
    """
    for i in range(TAILLE):
        for j in range(TAILLE):
            if grille[i][j] == 0:
                return False
            if j < TAILLE - 1 and grille[i][j] == grille[i][j + 1]:
                return False
            if i < TAILLE - 1 and grille[i][j] == grille[i + 1][j]:
                return False
    return True
