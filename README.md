# Analyseur-de-Robustesse-des-Mots-de-Passe
Description

Ce projet est une application de bureau développée en Python avec Tkinter, conçue pour évaluer la robustesse des mots de passe et simuler des attaques potentielles. Il offre une interface utilisateur pour la saisie et l'analyse des mots de passe, ainsi qu'une interface administrateur pour la surveillance des alertes de sécurité. L'objectif principal est d'éduquer les utilisateurs sur les bonnes pratiques en matière de mots de passe et de fournir un outil pour tester leur sécurité.

# Fonctionnalités

1. Analyse de Robustesse des Mots de Passe
   
L'application évalue la robustesse d'un mot de passe en se basant sur les critères suivants:
• Longueur minimale : Au moins 12 caractères.
• Diversité des caractères doit contenir :
   - Des chiffres (0-9)
   - Des caractères spéciaux (ponctuation)
   - Des lettres minuscules (a-z)
   - Des lettres majuscules (A-Z)



2. Simulation d'Attaques

Pour démontrer la vulnérabilité des mots de passe faibles l'attaque par dictionnaire : 
Vérifie si le mot de passe fait partie d'une liste de mots de passe couramment utilisés (par exemple, "password", "123456", "admin", "azerty").

3. Hachage Sécurisé

Le projet inclut des utilitaires de hachage pour illustrer comment les mots de passe devraient être stockés de manière sécurisée. Bien que des fonctions de hachage comme MD5 et SHA-256 soient présentes à titre démonstratif, l'application utilise bcrypt pour le hachage des mots de passe, une méthode recommandée pour sa résistance aux attaques par force brute et par dictionnaire grâce à son coût de calcul élevé 

# Prérequis

Pour exécuter ce projet, vous aurez besoin de :

- Python 3.x (version 3.11.0rc1 utilisée lors du développement).

- Les bibliothèques Python suivantes :

    • tkinter (généralement inclus avec Python)
    • bcrypt



# Installation

1. Créer et activer un environnement virtuel (recommandé) :

    Bash
    python3 -m venv venv
    source venv/bin/activate    # Sous Linux/macOS
    venv\Scripts\activate       # Sous Windows


2. Installer les dépendances :

    Bash
    pip install bcrypt


# Utilisation

Lancer l'application :

Bash
python main.py


# Structure du Projet


Analyseur de robustesse des mots de passe/
├── admin/
│   ├── admin_gui.py          # Interface graphique de l'administrateur
│   └── admin_monitor.py      # Logique de surveillance et d'alerte de l'administrateur
├── src/
│   ├── analyzer.py           # Logique principale d'analyse de robustesse
│   ├── attack_simulator.py   # Fonctions de simulation d'attaques
│   └── hash_utils.py         # Utilitaires de hachage de mots de passe
├── user/
│   ├── user_gui.py           # Interface graphique de l'utilisateur
│   └── user_interface.py     # Logique de vérification de la robustesse (critères)
├── main.py                   # Point d'entrée de l'application
├── admin_alerts.log          # Fichier de log des alertes administrateur
├── logs/
│   └── password_analysis.txt # Journal détaillé des analyses de mots de passe
└── output/
    └── results.json          # Résultats d'analyse au format JSON


Laure LUSIETE

