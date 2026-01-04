import random 

def init_grille():
    """Retourne une grille 4x4 vide."""
    return [[0] * 4 for _ in range(4)]

def tasser_ligne(ligne):
    """Tasse les nombres positifs vers la gauche"""
    non_zero = [x for x in ligne if x != 0]
    zero = [0] * (4 - len(non_zero))
    return non_zero + zeros

def ajout_chiffre(grille):
    