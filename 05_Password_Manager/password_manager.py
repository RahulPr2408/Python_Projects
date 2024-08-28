import hashlib
import re
from cryptography.fernet import Fernet
import os

def load_key():
    if not os.path.exists("key.key"):
        write_key()  # Generate and write a new key if the file doesn't exist
    with open("key.key", "rb") as file:
        key = file.read()
    return key

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def hash_master_pwd(master_pwd):
    return hashlib.sha256(master_pwd.encode()).digest()

def is_valid_password(pwd):
    if len(pwd) < 8 or not re.search("[a-z]", pwd) or not re.search("[A-Z]", pwd) or not re.search("[0-9]", pwd) or not re.search("[!@#$%^&*(),.?\":{}|<>]", pwd):
        print("Password must be at least 8 characters long, include a mix of upper and lower case letters, contain numbers, and special characters.")
        return False
    return True

def view():
    try:
        with open("password.txt", "r") as file:
            for line in file.readlines():
                data = line.rstrip()
                user, passw = data.split("|")
                decrypted_passw = fer.decrypt(passw.encode()).decode()
                masked_passw = decrypted_passw[:2] + "*" * (len(decrypted_passw) - 4) + decrypted_passw[-2:]
                print(f"User: {user}")
                print(f"Password: {masked_passw} (Reveal: {decrypted_passw})")
    except FileNotFoundError:
        print("No passwords stored yet.")

def add():
    name = input("Account Name: ")
    while True:
        pwd = input("Password: ")
        if is_valid_password(pwd):
            break

    with open("password.txt", "a") as file:
        file.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

def get_mode():
    while True:
        mode = input("Would you like to add a new password, view existing ones (view/add), or press q to quit: ").lower()
        if mode in ["view", "add", "q"]:
            return mode
        print("Invalid mode. Please enter 'view', 'add', or 'q'.")

master_pwd = input("What is your master password? ")
key = load_key() + hash_master_pwd(master_pwd)
fer = Fernet(key)

while True:
    mode = get_mode()

    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
