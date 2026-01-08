import random

TAILLE = 4


def init_grille():
    """
    Crée une grille 4x4 initialisée avec des zéros.
    """
    return [[0] * TAILLE for _ in range(TAILLE)]# creer une liste de 4 liste


def tasser_ligne(ligne):
    """
    Déplace les nombres non nuls d’une ligne vers la gauche.
    """
    non_zeros = [x for x in ligne if x != 0]# creer une liste contenant seulement les nombre différent de zéro
    return non_zeros + [0] * (TAILLE - len(non_zeros))# ajoute des zeros vers la droite pour que la ligne fassent toujours 4


def fusion_ligne(ligne):
    """
    Fusionne les tuiles d’une ligne selon les règles du 2048.
    """
    score = 0
    ligne = tasser_ligne(ligne)
    i = 0

    while i < TAILLE - 1:
        if ligne[i] != 0 and ligne[i] == ligne[i + 1]:# verifie que la tuile n'est pas vide et qu'elle est identique à celle de droite
            ligne[i] *= 2
            score += ligne[i]
            ligne[i + 1] = 0 # supprime la tuile fusioné
            i += 2 # on empeche une double fusion
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
        nl, sc = fusion_ligne(ligne[:])# applique une fusion sur une copie de la ligne
        if nl != ligne: # si la ligne change alors valide
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
    vides = [(i, j) for i in range(TAILLE) for j in range(TAILLE) if grille[i][j] == 0]# liste de toutes les positions vides
    if not vides:
        return grille

    i, j = random.choice(vides)
    grille[i][j] = 4 if random.random() < 0.10 else 2# taux d'apparations d'un 2 ou un 4
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
            if j < TAILLE - 1 and grille[i][j] == grille[i][j + 1]:# verification fusion verticable possible
                return False
            if i < TAILLE - 1 and grille[i][j] == grille[i + 1][j]:# verifications fusion horizontable possible
                return False
    return True
