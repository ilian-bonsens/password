import re
import hashlib

def password():
    while True:
        mdp = input("Choisissez votre mot de passe : ")
        if len(mdp) < 8:
            print("Erreur : le mot de passe doit contenir au moins 8 caractères.")
        elif not re.search("[a-z]", mdp):
            print("Erreur : le mot de passe doit contenir au moins 1 minuscule.")
        elif not re.search("[A-Z]", mdp):
            print("Erreur : le mot de passe doit contenir au moins 1 majuscule.")
        elif not re.search("[0-9]", mdp):
            print("Erreur : le mot de passe doit contenir au moins 1 chiffre.")
        elif not re.search("[*%@$!#\\^]", mdp):
            print("Erreur : le mot de passe doit contenir au moins 1 caractère spécial.")
        elif re.search("\s", mdp):
            print("Erreur : le mot de passe ne doit pas contenir d'espaces.")
        else:
            print("Mot de passe validé.")
            hash_mdp = hashlib.sha256(mdp.encode())
            hex_dig = hash_mdp.hexdigest()
            print(f"Hash du mot de passe : {hex_dig}.")
            break

password()
