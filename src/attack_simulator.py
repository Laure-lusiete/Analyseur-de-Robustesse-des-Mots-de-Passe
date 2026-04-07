import itertools
import string


# ===================================================
# ATTAQUE PAR DICTIONNAIRE (comparaison directe)
# ===================================================
def dictionary_attack(password: str, dictionary: list) -> bool:
    """
    Simulation d'une attaque par dictionnaire.
    """
    for word in dictionary:
        if word == password:
            return True
    return False


# ===================================================
# BRUTE FORCE LIMITÉE
# ===================================================
def bruteforce_simulation(password: str, max_length: int) -> bool:
    """
    Simulation brute force limitée (usage pédagogique).
    """
    alphabet = string.ascii_lowercase + string.digits

    for length in range(1, max_length + 1):
        for attempt in itertools.product(alphabet, repeat=length):
            if "".join(attempt) == password:
                return True
    return False