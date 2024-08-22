from cryptography.fernet import Fernet

def load_key():
  file = open("key.key", "rb")
  key = file.read()
  file.close()
  return key

def write_key():
  key = Fernet.generate_key()
  with open("key.key", "wb") as key_file:
    key_file.write(key)

master_pwd = input("What is your master password ? ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

mode = input("Would you like to add a new password or view existing ones (view/add) ? or press q to quit. ").lower()

def view():
  with open("password.txt", "r") as file:
    for line in file.readlines():
      data = line.rstrip()
      user, passw = data.split("|")
      print(f"User: {user}")
      print(f"Password: {fer.decrypt(passw.encode()).decode()}")

def add():
  name = input("Account Name: ")
  pwd = input("Password: ")

  with open("password.txt", "a") as file:
    file.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
  if mode == "q":
    break

  if mode == "view":
    view()
  elif mode == "add":
    add()
  else:
    print("Invalid mode.")
    continue

