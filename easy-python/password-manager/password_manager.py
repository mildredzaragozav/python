from pathlib import Path
from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    ruta_key = Path(__file__).parent / "key.key"
    ruta_key.write_bytes(key)

write_key()
'''

def load_key():
    key_path = Path(__file__).parent / "key.key"
    file = open(key_path, "rb")
    key = file.read()
    file.close()
    return key

key = load_key() 
fer = Fernet(key)
passwords_path = Path(__file__).parent / "passwords.txt"

def view():
    with open(passwords_path, 'r') as file:
        for line in file.readlines():
            data = line.rstrip()
            user, password = data.split("|")
            print(f"User: '{user}' Password: '{fer.decrypt(password.encode()).decode()}")

def add():
    account = input("Account name: ")
    pwd = input("Password: ")

    with open(passwords_path, 'a') as file:
        file.write(account + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input("Would you like to add a new password or view existing ones (view, add)? Press q to quit. ").lower()
    if mode == "q" :
        break
    elif mode == "view" :
        view() 
    elif mode == "add" : 
        add()
    else:
        print("Invalid mode")