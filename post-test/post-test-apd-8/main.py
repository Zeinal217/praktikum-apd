import data
from data import clear
from auth import login, register
from crud import menu_crud

while True:
    clear()
    print("=== MENU UTAMA ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        if login():
            if data.role == "admin":
                clear()
                print("=== Menu Admin ===")
                print("1. CRUD Laundry")
                print("2. CRUD Akun")
                print("3. Logout")
                p = input("Pilih: ")
                if p == "1": menu_crud("laundry")
                elif p == "2": menu_crud("akun")
                elif p == "3": data.role = None
            elif data.role == "user":
                clear()
                print("=== Menu User ===")
                print("1. CRUD Laundry")
                print("2. Logout")
                p = input("Pilih: ")
                if p == "1": menu_crud("laundry")
                elif p == "2": data.role = None
    elif pilih == "2":
        register()
    elif pilih == "3":
        clear()
        print("Keluar...")
        exit()
