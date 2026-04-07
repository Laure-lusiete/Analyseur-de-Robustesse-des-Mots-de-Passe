import tkinter as tk
import os

LOG_FILE = "admin_alerts.log"

admin_window = None
text_box = None


def open_admin_window(parent):
    global admin_window, text_box

    # ✅ Si la fenêtre existe déjà, on met à jour seulement
    if admin_window is not None and admin_window.winfo_exists():
        refresh_logs()
        admin_window.lift()
        admin_window.focus_force()
        return

    # ✅ Création UNIQUE de la fenêtre admin
    admin_window = tk.Toplevel(parent)
    admin_window.title("Interface Administrateur – Sécurité")
    admin_window.geometry("600x400")

    tk.Label(
        admin_window,
        text="📊 Alertes de sécurité",
        font=("Arial", 12, "bold")
    ).pack(pady=10)

    text_box = tk.Text(admin_window, height=15, width=70)
    text_box.pack(pady=5)

    refresh_logs()


def refresh_logs():
    global text_box

    if text_box is None:
        return

    text_box.delete("1.0", tk.END)

    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as log:
            content = log.read()
            text_box.insert(tk.END, content or "Aucune alerte.")
    else:
        text_box.insert(tk.END, "Aucune alerte.")
