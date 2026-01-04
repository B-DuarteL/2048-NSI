import random 

TAILLE = 4
def init_grille():
    return [[0]*TAILLE for _ in range(TAILLE)]
    
def tasser_ligne(ligne):
    non_zeros=[x for x in ligne if x !=0]
    return non_zeros + [0] * (TAILLE - len(non_zeros))

def fusion_ligne(ligne):
    score=0
    ligne=tasser_ligne(ligne)
    i=0
    while i <TAILLE-1:
        if ligne[i]!=0 and ligne[i]==ligne[i+1]:
            ligne[i]*=2
            score+=ligne[i]
            ligne[i+1]=0
            i+=2
        else:
            i+=1
    ligne=tasser_ligne(ligne)
    return ligne, score

def deplacement_gauche(grille):
    nouvelle=[]
    score_total=0
    change=False
    for ligne in grille:
        nl, sc=fusion_ligne(ligne[:])
        if nl != ligne:
            change=True
        nouvelle.append(nl)
        score_total+=sc
    return nouvelle, score_total, change

def deplacement_droite(grille):
    nouvelle=[]
    score_total=0
    change=False
    for ligne in grille:
        inv=list(reversed(ligne))
        nl, sc=fusion_ligne(inv)
        nl=list(reversed(nl))
        if nl != ligne:
            change=True
        nouvelle.append(nl)
        score_total += sc
    return nouvelle, score_total, change

def deplacement_haut(grille):
    nouvelle = [[0]*TAILLE for _ in range(TAILLE)]
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
    nouvelle = [[0]*TAILLE for _ in range(TAILLE)]
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
    vides = [(i, j) for i in range(TAILLE) for j in range(TAILLE) if grille[i][j] == 0]
    if not vides:
        return grille
    i, j = random.choice(vides)
    grille[i][j] = 4 if random.random() < 0.10 else 2
    return grille

def victoire(grille):
    return any(2048 in ligne for ligne in grille)

def game_over(grille):
    for i in range(TAILLE):
        for j in range(TAILLE):
            if grille[i][j] == 0:
                return False
            if j < TAILLE-1 and grille[i][j] == grille[i][j+1]:
                return False
            if i < TAILLE-1 and grille[i][j] == grille[i+1][j]:
                return False
    return True