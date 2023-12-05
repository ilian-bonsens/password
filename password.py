import re, hashlib, json, os

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
            print(f"Hash du mot de passe (NE JAMAIS LE PARTAGER): {hex_dig}.")
#verifie si le fichier json existe : si oui on le charge, si non on cree une liste vide qui va accueillir
    #les data a ajouter au fichier json qui va etre cree
        if not os.path.exists('save.json'):
            data = []
        else:
            with open('save.json', 'r') as file:
                data = json.load(file)
        ligne = {'mot de passe' : mdp, 'hash' : hex_dig}
        data.append(ligne)
        with open('save.json', 'w') as file:
            json.dump(data, file, indent=1)
            break

password()
