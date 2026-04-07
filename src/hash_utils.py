import hashlib
import bcrypt


# =========================
# HACHAGE MD5 (DÉMONSTRATIF)
# =========================
def hash_md5(password: str) -> str:
    """
    Génère un hash MD5 (non sécurisé).
    Usage strictement pédagogique.
    """
    return hashlib.md5(password.encode()).hexdigest()


# ==============================
# HACHAGE SHA-256 (DÉMONSTRATIF)
# ==============================
def hash_sha256(password: str) -> str:
    """
    Génère un hash SHA-256.
    Usage pédagogique (trop rapide pour les mots de passe).
    """
    return hashlib.sha256(password.encode()).hexdigest()


# ======================
# HACHAGE BCRYPT (✅ SÉCURITÉ)
# ======================
def hash_bcrypt(password: str) -> bytes:
    """
    Génère un hash bcrypt sécurisé.
    ✅ Recommandé pour les mots de passe.
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)


# ======================
# COMPARAISON PÉDAGOGIQUE
# ======================
def compare_algorithms(password: str) -> dict:
    """
    Compare les algorithmes de hachage (usage pédagogique).
    Retourne un dictionnaire avec les résultats.
    """
    return {
        "MD5": hash_md5(password),
        "SHA-256": hash_sha256(password),
        "bcrypt": hash_bcrypt(password)
    }