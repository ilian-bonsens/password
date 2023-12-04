import re
note = 0


def password():
    global note
    while True:
        mdp = input("Choisissez votre mot de passe : ")
        if len(mdp) < 8:
            note = -1
        elif not re.search("[a-z]", mdp):
            note = -1
        elif not re.search("[A-Z]", mdp):
            note = -1
        elif not re.search("[0-9]", mdp):
            note = -1
        elif not re.search("[*%@$!#\^]", mdp):
            note = -1
        elif re.search("\s", mdp):
            note = -1
        else:
            note = 0
            print("Mot de passe validé.")
            break
        if note == -1:
            print("Erreur : le mot de passe doit contenir au moins 8 caractères : 1 majuscule, 1 minuscule et un caractère spécial.")

password()