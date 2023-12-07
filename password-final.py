import hashlib, json, os, random, string
from cryptography.fernet import Fernet


# Génère une clé pour ouvrir le fichier json avec les hashes
key = Fernet.generate_key()
token = Fernet(key)
print(f"\nClé de chiffrement : {key.decode()}\n")


def store_password(password): # Fonction qui stocke le mot de passe dans un fichier json
    while True:
# Vérifie si le mot de passe respecte les conditions 8 caractères, 1 minuscule, 1 majuscule, 1 chiffre, 1 caractère spécial
        if not (len(password) >= 8 and any(c.islower() for c in password) and any(c.isupper() for c in password) 
                and any(c.isdigit() for c in password) and any(c in "*%@$!#^" for c in password)):
            print("\n[-] Le mot de passe ne respecte pas les conditions.\n")
            return
        # Hash le mot de passe
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        password_data = {'hash': hashed_password}
        file_name = 'passwords.json'
# Vérifie si le fichier json existe : si oui on le charge, si non on crée une liste vide qui va accueillir
        if os.path.exists(file_name):
            with open(file_name, 'r') as file:
                data = json.load(file)
# Vérifie si le mot de passe existe déjà dans le fichier json grace au hash
            if any(d['hash'] == hashed_password for d in data):
                print("\n[+] Ce mot de passe existe déjà.\n")
                return
# Ajoute le hash du mot de passe dans le fichier json          
            data.append(password_data)
            with open(file_name, 'w') as file:
                json.dump(data, file, indent=1)
                break
        else: # Sinon, crée le fichier json et ajoute le hash du mot de passe
            with open(file_name, 'x') as file:
                json.dump([password_data], file, indent=1)
                break

def voir_passwords(): # Fonction qui affiche les hashes stockés dans le fichier json
    while True:
        securite = input("\nEntrez la clé de chiffrement : ")
# Vérifie si la clé de chiffrement est correcte
        if securite == key.decode():
            file_name = 'passwords.json'
# Vérifie si le fichier json existe : si oui on le charge, si non on crée une liste vide
            if os.path.exists(file_name):
                with open(file_name, 'r') as file:
                    data = json.load(file)
                print("\n[+] Hash :\n")
                for password_data in data:
                    print(f"{password_data['hash']}\n")
            break
        else:
            print("\nErreur : clé de déchiffrement incorrecte.")


def generer_password():
    while True:
    # Génère une longueur de mot de passe aléatoire entre 8 et 24 caractères
        length = random.randint(8, 24) 
    # Génère un mot de passe aléatoire de la longueur définie avec des lettres, chiffres, caractères spéciaux
        password = ''.join(random.choice(string.ascii_letters + string.digits + "*%@$!#^") for _ in range(length))
    # Vérifie si le mot de passe respecte les conditions
        if (len(password) >= 8 and any(c.islower() for c in password) and any(c.isupper() for c in password) 
            and any(c.isdigit() for c in password) and any(c in "*%@$!#^" for c in password)):
            return password

            # Menu
while True:
    print("1. Créer un mot de passe")
    print("2. Générer un mot de passe")
    print("3. Afficher les mot de passe")
    print("4. Quitter")
    choice = input("\nEntrez votre choix : ")

    if choice == '1':
        password = input("\nTapez votre mot de passe : ")
        store_password(password)

    elif choice == '2':
        password = generer_password()
        print(f"\n[+] Mot de passe généré : {password}\n")
        store_password(password)

    elif choice == '3':
        voir_passwords()

    elif choice == '4':
        break
