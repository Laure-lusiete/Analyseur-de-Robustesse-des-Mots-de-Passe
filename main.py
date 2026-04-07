"""
main.py
-------
Point d'entrée principal de l'application.
Lance l'interface utilisateur Tkinter.
"""

from user.user_gui import window


def main():
    # La fenêtre Tkinter est lancée automatiquement
    # grâce à window.mainloop() dans user_gui.py
    window.mainloop()


if __name__ == "__main__":
    main()