import hashlib, json, os, random, string
from cryptography.fernet import Fernet

# Génère une clé pour le chiffrement du fichier json avec les hashes
key = Fernet.generate_key()
cipher_suite = Fernet(key)
print(f"\nClé de chiffrement : {key.decode()}\n")

def store_password(password):
    while True:
        if not (len(password) >= 8 and any(c.islower() for c in password) and any(c.isupper() for c in password) 
                and any(c.isdigit() for c in password) and any(c in "*%@$!#^" for c in password)):
            print("\n[-] Le mot de passe ne respecte pas les conditions.\n")
            return
        
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        password_data = {'hash': hashed_password}
        file_name = 'passwords.json'

        if os.path.exists(file_name):
            with open(file_name, 'r') as file:
                data = json.load(file)
            if any(d['hash'] == hashed_password for d in data):
                print("\n[+] Ce mot de passe existe déjà.\n")
                return
            data.append(password_data)
            with open(file_name, 'w') as file:
                json.dump(data, file, indent=1)
                break
        else:
            with open(file_name, 'x') as file:
                json.dump([password_data], file, indent=1)
                break

def view_passwords():
    while True:
        securite = input("\nEntrez la clé de chiffrement : ")
        if securite == key.decode():
            file_name = 'passwords.json'
            if os.path.exists(file_name):
                with open(file_name, 'r') as file:
                    data = json.load(file)
                print("\n[+] Hash :\n")
                for password_data in data:
                    print(f"{password_data['hash']}\n")
                    break
        else:
            print("\nErreur : clé de déchiffrement incorrecte.")

def generate_password():
    while True:
        length = random.randint(8, 24)
        password = ''.join(random.choice(string.ascii_letters + string.digits + "*%@$!#^") for _ in range(length))
        if (len(password) >= 8 and any(c.islower() for c in password) and any(c.isupper() for c in password) 
            and any(c.isdigit() for c in password) and any(c in "*%@$!#^" for c in password)):
            return password

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
        password = generate_password()
        print(f"\n[+] Mot de passe généré : {password}\n")
        store_password(password)

    elif choice == '3':
        view_passwords()

    elif choice == '4':
        break
