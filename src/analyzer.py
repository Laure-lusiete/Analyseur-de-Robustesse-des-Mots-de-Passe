import os
import json
from datetime import datetime

from user.user_interface import check_password_strength
from src.hash_utils import hash_bcrypt
from src.attack_simulator import dictionary_attack, bruteforce_simulation

COMMON_PASSWORDS = [
    "password", "123456", "admin", "admin123", "azerty", "welcome"
]

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "password_analysis.txt")

OUTPUT_DIR = "output"
JSON_FILE = os.path.join(OUTPUT_DIR, "results.json")


def run_analysis(password: str) -> dict:
    os.makedirs(LOG_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    is_strong = check_password_strength(password)
    score = 80 if is_strong else 30

    dict_attack = dictionary_attack(password, COMMON_PASSWORDS)
    brute_attack = bruteforce_simulation(password, max_length=4)

    hash_bcrypt(password)

    result = {
        "date": datetime.now().isoformat(),
        "is_strong": is_strong,
        "strength": "Fort" if is_strong else "Faible",
        "score": score,
        "dictionary_attack": dict_attack,
        "hash_algorithm": "bcrypt",
        "cracked": dict_attack or brute_attack
    }

    write_txt_log(result)
    write_json_log(result)
    return result


def write_txt_log(r: dict):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write("===== ANALYSE DE ROBUSTESSE =====\n")
        f.write(f"Date : {r['date']}\n")
        f.write(f"Robustesse : {r['strength']}\n")
        f.write(f"Score : {r['score']}\n")

        if r["dictionary_attack"]:
            f.write("⚠️ Utilisation d'un mot du dictionnaire\n")

        if r["cracked"]:
            f.write("❌ Mot de passe cassé par simulation\n")
        else:
            f.write("✅ Mot de passe non cassé\n")

        f.write("=" * 40 + "\n\n")


def write_json_log(result: dict):
    data = []

    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []

    data.append(result)

    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
