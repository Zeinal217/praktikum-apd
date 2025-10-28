import os

akun = {
    1: {"username": "admin", "password": "admin", "role": "admin"},
    2: {"username": "user", "password": "user", "role": "user"},
}
data_laundry = {}
role = None

def clear():
    os.system("cls || clear")

def cek_login(username, password, akun):
    for i in akun.values():
        if i["username"] == username and i["password"] == password:
            return i["role"]
    return None

def login(sisa_percobaan=3):
    global role
    if sisa_percobaan == 0:
        print("Sisa percobaan habis. Login Gagal!")
        exit()
    username = input("Input Username: ")
    password = input("Input Password: ")
    hasil = cek_login(username, password, akun)
    if hasil:
        role = hasil
        clear()
        print("Login berhasil!")
        return True
    print("Username atau password salah.")
    return login(sisa_percobaan - 1)

def id_baru(nama):
    if len(nama) == 0:
        return  1
    else:
        return  max(nama.keys()) + 1

def register():
        clear()
        print("REGISTER")
        username = input("Buat username baru: ")
        if username in akun:
            print("Username sudah digunakan!")
        else:
            password = input("Masukkan password: ")
            akun[username] = {"password": password, "role": "user"}
            print("Register berhasil! Silakan login.")
        input("Silahkan tekan enter!")

def role_awal():
    return "user"

def status_awal():
    return "Belum selesai"

def tambah_data(nama, isi):
    try:
        id = id_baru(nama)
        data_baru = {}
        for f in isi:
            if f == "berat":
                data_baru[f] = input(f"Masukkan {f} (kg) : ")
            elif f == "status":
                data_baru[f] = status_awal()
            elif f == "role":
                data_baru[f] = role_awal()
            else:
                data_baru[f] = input(f"Masukkan {f}: ")
        nama[id] = data_baru
        print("Data berhasil ditambahkan!")
    except Exception as e:
        print(f"Ada error: {e}")

def lihat_data(nama):
    if not nama:
        print("Belum ada data.")
        return
    for key, value in nama.items():
        print(f"ID {key}:{value}")
    print()

def ubah_data(nama, isi):
    try:
        lihat_data(nama)
        id_data = int(input("Masukkan ID data yang ingin diubah: "))
        if id_data not in nama:
            raise Exception("ID tidak ditemukan.")
        print("Input data yang ingin diubah saja, kosongkan jika tidak ingin diubah.")
        for f in isi:
            if f == "role":
                print("Role tidak bisa diubah")
            else:
                nilai = input(f"Masukkan {f} baru: ")
                if nilai:
                    if f == "berat":
                        nilai = float(nilai)
                    nama[id_data][f] = nilai
        print("Data berhasil diperbarui!")
    except Exception as e:
        print(f"Ada error: {e}")

def hapus_data(nama):
    try:
        lihat_data(nama)
        id_data = int(input("Masukkan ID data yang ingin dihapus: "))
        if id_data not in nama:
            raise Exception("ID tidak ditemukan.")
        del nama[id_data]
        print("Data berhasil dihapus!")
    except Exception as e:
        print(f"Ada error: {e}")

def menu_crud(tipe):
    if tipe == "laundry":
        isi = ["nama", "jenis", "berat", "status"]
        nama = data_laundry
    elif tipe == "akun":
        isi = ["username", "password", "role"]
        nama = akun

    print(f"=== CRUD {tipe} ===")
    print("1. Tambah Data")
    print("2. Lihat Data")
    print("3. Ubah Data")
    print("4. Hapus Data")
    print("5. Kembali")
    menu = input("Pilih menu: ")

    if menu == "1":
        tambah_data(nama, isi)
    elif menu == "2":
        lihat_data(nama)
    elif menu == "3":
        ubah_data(nama, isi)
    elif menu == "4":
        hapus_data(nama)
    elif menu == "5":
        return

    menu_crud(tipe)

while True:
    clear()
    print("=== MENU UTAMA ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        if login():
            if role == "admin":
                print(f"=== Menu {role} ===")
                print("1. CRUD Laundry")
                print("2. CRUD Akun")
                print("3. Logout")
                pilihan = input("Pilih menu: ")
                if pilihan == "1":
                    menu_crud("laundry")
                elif pilihan == "2":
                    menu_crud("akun")
                elif pilihan == "3":
                    print("Logout berhasil.")
                    role = None
                    break

            elif role == "user":
                print(f"=== Menu {role} ===")
                print("1. CRUD Laundry")
                print("2. Logout")
                pilihan = input("Pilih menu: ")
                if pilihan == "1":
                    menu_crud("laundry")
                elif pilihan == "2":
                    print("Logout berhasil.")
                    role = None
                    break

    elif pilihan == "2":
        register()

    elif pilihan == "3":
        print("Anda telah Keluar")
        exit()

    else:
        print("Pilihan tidak valid")