import data
from data import akun, clear
from colorama import Fore, Style

def login(sisa_percobaan=3):
    clear()
    print("=== LOGIN ===")

    if sisa_percobaan == 0:
        print(Fore.RED + "Sisa percobaan habis. Login gagal!" + Style.RESET_ALL)
        exit()

    username = input("Username: ")
    password = input("Password: ")

    for user in akun.values():
        if user["username"] == username and user["password"] == password:
            data.role = user["role"]
            clear()
            print(Fore.GREEN + "Login berhasil!" + Style.RESET_ALL)
            return True

    print(Fore.RED + "Username/password salah!" + Style.RESET_ALL)
    return login(sisa_percobaan - 1)

def register():
    clear()
    print("=== REGISTER ===")
    username = input("Buat username baru: ")
    new_id = max(akun.keys()) + 1
    password = input("Password: ")

    akun[new_id] = {"username": username, "password": password, "role": "user"}
    print(Fore.GREEN + "Register berhasil, silakan login." + Style.RESET_ALL)
    input("Tekan Enter...")
