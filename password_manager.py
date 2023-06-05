from cryptography.fernet import Fernet

def write_key():
    key = write_key.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    return key


key = load_key()
write_key(key)


def view():
    with open("passwords.txt", 'r') as f:
        for line in f.readline():
            date = line.rstrip()
            user, passw = data.split("|")
            print("User", user, "| Password:", fer.decrypt(passw.encode()).decode())


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("password.txt", "a") as f:
        f.write(name + "|" + fer.encrypd(pwd.encode()).decode() + "\n")


while True:
    mode = input("Would you like to add a password or view existing ones (view, add) or pres q to quit?").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid input. Try again 'add', 'view' or 'q' to quit")
        continue
