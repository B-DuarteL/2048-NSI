import random 

TAILLE = 4
def init_grille():
    return [[0]*Taille for _ in range(TAILLE)]
    
def tasser_ligne(ligne):
    non_zeros=[x for x in ligne if x !=0]
    return non_zeros+[0]*TAILE-len(non_zeros)

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