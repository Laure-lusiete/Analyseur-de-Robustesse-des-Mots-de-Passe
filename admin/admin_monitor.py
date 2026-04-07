from src.attack_simulator import dictionary_attack

COMMON_PASSWORDS = [
    "password",
    "123456",
    "admin",
    "admin123",
    "azerty",
    "welcome"
]

LOG_FILE = "admin_alerts.log"


def admin_check(password: str, is_strong: bool):
    """
    Analyse la tentative utilisateur côté admin.
    """

    if is_strong:
        log_admin("✅ Bon mot de passe saisi")
        return

    # mot de passe invalide → on cherche pourquoi
    if dictionary_attack(password, COMMON_PASSWORDS):
        log_admin("⚠️ UTILISATION D'UN MOT DU DICTIONNAIRE")
    else:
        log_admin("❌ Mot de passe non conforme aux normes")


def log_admin(message: str):
    with open(LOG_FILE, "a", encoding="utf-8") as log:
        log.write(f"{message}\n")
