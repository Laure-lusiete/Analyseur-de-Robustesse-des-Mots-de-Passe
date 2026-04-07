import string

def check_password_strength(mdp: str) -> bool:
    chiffre = False
    special = False
    minuscule = False
    majuscule = False

    for caractere in mdp:
        if caractere in "0123456789":
            chiffre = True
        if caractere in string.punctuation:
            special = True
        if caractere in "abcdefghijklmnopqrstuvwxyz":
            minuscule = True
        if caractere in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            majuscule = True

    return len(mdp) >= 12 and chiffre and special and minuscule and majuscule