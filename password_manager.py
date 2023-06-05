from cryptography.farnet import Farnet


def write_key():
    key = Farnet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    return key


key = load_key()
fer = Farnet(key)


def view():
    with open("passwords.txt", 'r') as f:
        for line in f.readline():
            date = line.rstrip()
            user, passw = data.split("|")
            print("User", user, "| Password:", fer.decrypt(passw.encode()).decode())