import os

data_akun = {
    "admin": {"password": "admin", "role": "admin"},
    "user": {"password": "user", "role": "user"}
}

data_laundry = {}

while True:
    os.system("cls || clear")
    print("APLIKASI LAUNDRY")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilihan_awal = input("Pilih menu: ")

    if pilihan_awal == "1":
        os.system("cls || clear")
        print("LOGIN")
        username = input("Username: ")
        password = input("Password: ")

        if username in data_akun and data_akun[username]["password"] == password:
            role = data_akun[username]["role"]
            print("Login berhasil!")
            input("Silahkan tekan enter!")
            
            if role == "admin":
                while True:
                    os.system("cls || clear")
                    print("MENU ADMIN")
                    print("1. Tambah Data Laundry")
                    print("2. Lihat Data Laundry")
                    print("3. Ubah Data Laundry")
                    print("4. Hapus Data Laundry")
                    print("5. Logout")
                    pilihan_admin = input("Pilih menu: ")

                    if pilihan_admin == "1":
                        os.system("cls || clear")
                        print("Tambah Data Laundry")
                        nama = input("Nama Customer: ")
                        jenis = input("Jenis Laundry: ")
                        berat = input("Berat (kg): ")
                        if len(data_laundry) == 0:
                            id_baru = 1
                        else:
                            id_baru = max(data_laundry.keys()) + 1

                        data_laundry[id_baru] = {
                            "nama": nama,
                            "jenis": jenis,
                            "berat": berat,
                            "status": "Belum Selesai"
                            }
                        print("Data laundry berhasil ditambahkan!")
                        input("Silahkan tekan enter!")

                    elif pilihan_admin == "2":
                        os.system("cls || clear")
                        print("Data Laundry")
                        if len(data_laundry) == 0:
                            print("Data laundry belum ada.")
                        else:
                            for i in data_laundry:
                                print(f"{i}. Nama: {data_laundry[i]['nama']}, Jenis: {data_laundry[i]['jenis']}, Berat: {data_laundry[i]['berat']} kg, Status: {data_laundry[i]['status']}")
                        input("Silahkan tekan enter!")

                    elif pilihan_admin == "3":
                        os.system("cls || clear")
                        print("Ubah Data Laundry")
                        if len(data_laundry) == 0:
                            print("Data laundry belum ada.")
                            input("Silahkan tekan enter!")
                        else:
                            for i in data_laundry:
                                print(f"{i}. Nama: {data_laundry[i]['nama']}, Jenis: {data_laundry[i]['jenis']}, Berat: {data_laundry[i]['berat']} kg, Status: {data_laundry[i]['status']}")
                            ubah_id = int(input("Masukkan ID yang ingin diubah: "))
                            if ubah_id in data_laundry:
                                print("Input data yang ingin diubah saja, kosongkan jika tidak ingin diubah.")
                                nama = input("Nama baru: ")
                                jenis = input("Jenis baru: ")
                                berat = input("Berat baru: ")
                                status = input("Status (Belum Selesai/Selesai): ")

                                if nama:
                                    data_laundry[ubah_id]["nama"] = nama
                                if jenis:
                                    data_laundry[ubah_id]["jenis"] = jenis
                                if berat:
                                    data_laundry[ubah_id]["berat"] = berat
                                if status in ["Selesai", "Belum Selesai"]:
                                    data_laundry[ubah_id]["status"] = status
                                print("Data telah diubah!")
                            else:
                                print("ID tidak ditemukan.")
                            input("Silahkan tekan enter!")

                    elif pilihan_admin == "4":
                        os.system("cls || clear")
                        print("Hapus Data Laundry")
                        if len(data_laundry) == 0:
                            print("Belum ada data.")
                            input("Silahkan tekan enter!")
                        else:
                            for i in data_laundry:
                                print(f"{i}. Nama: {data_laundry[i]['nama']}, Jenis: {data_laundry[i]['jenis']}, Berat: {data_laundry[i]['berat']} kg, Status: {data_laundry[i]['status']}")
                            hapus_id = int(input("Masukkan ID yang ingin dihapus: "))
                            if hapus_id in data_laundry:
                                del data_laundry[hapus_id]
                                print("Data telah dihapus!")
                            else:
                                print("ID tidak ditemukan.")
                            input("Silahkan tekan enter!")

                    elif pilihan_admin == "5":
                        os.system("cls || clear")
                        print("Logout berhasil!")
                        input("Silahkan tekan enter!")
                        break

                    else:
                        print("Pilihan tidak ada!")
                        input("Silahkan tekan enter!")

            elif role == "user":
                while True:
                    os.system("cls || clear")
                    print("MENU USER")
                    print("1. Lihat Data Laundry")
                    print("2. Logout")
                    pilihan_user = input("Pilih menu: ")

                    if pilihan_user == "1":
                        os.system("cls || clear")
                        print("Data Laundry")
                        if len(data_laundry) == 0:
                            print("Data laundry belum ada.")
                        else:
                            for i in data_laundry:
                                print(f"{i}. Nama: {data_laundry[i]['nama']}, Jenis: {data_laundry[i]['jenis']}, Berat: {data_laundry[i]['berat']} kg, Status: {data_laundry[i]['status']}")
                        input("Silahkan tekan enter!")

                    elif pilihan_user == "2":
                        os.system("cls || clear")
                        print("Logout berhasil!")
                        input("Silahkan tekan enter!")
                        break

                    else:
                        print("Pilihan tidak valid.")
                        input("Silahkan tekan enter!")
        else:
            print("Login gagal! Username atau password salah.")
            input("Silahkan tekan enter!")

    elif pilihan_awal == "2":
        os.system("cls || clear")
        print("REGISTER")
        username = input("Buat username baru: ")
        if username in data_akun:
            print("Username sudah digunakan!")
        else:
            password = input("Masukkan password: ")
            data_akun[username] = {"password": password, "role": "user"}
            print("Register berhasil! Silakan login.")
        input("Silahkan tekan enter!")

    elif pilihan_awal == "3":
        os.system("cls || clear")
        print("Terima kasih telah menggunakan aplikasi laundry.")
        break

    else:
        print("Pilihan tidak valid.")
        input("Silahkan tekan enter!")
