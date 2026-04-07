import tkinter as tk
from tkinter import messagebox

from user.user_interface import check_password_strength
from admin.admin_monitor import admin_check
from admin.admin_gui import open_admin_window
from src.analyzer import run_analysis          # 🔹 AJOUT
# from src.hash_utils import hash_bcrypt        # ❌ plus nécessaire ici


def submit_password():
    password = entry.get()

    # 🔹 ANALYSE CENTRALISÉE
    analysis = run_analysis(password)

    # Résultat de robustesse
    is_strong = analysis["is_strong"]

    # ✅ admin informé TOUJOURS
    admin_check(password, is_strong)
    open_admin_window(window)

    if not is_strong:
        messagebox.showerror(
            "Mot de passe invalide",
            "Mot de passe non conforme.\n\n"
            "✅ Au moins 12 caractères\n"
            "✅ Majuscules, minuscules\n"
            "✅ Chiffres et symboles\n"
            "❌ Mot de passe détecté par l'administrateur"
        )
        return

    messagebox.showinfo(
        "Succès",
        "✅ Bon mot de passe saisi.\n"
        "Analyse terminée avec succès."
    )


# =======================
# FENÊTRE UTILISATEUR
# =======================
window = tk.Tk()
window.title("Interface Utilisateur")
window.geometry("400x250")

tk.Label(
    window,
    text="Entrez votre mot de passe :",
    font=("Arial", 12)
).pack(pady=10)

entry = tk.Entry(window, show="*", width=30)
entry.pack(pady=5)

tk.Button(
    window,
    text="Valider",
    command=submit_password
).pack(pady=15)
