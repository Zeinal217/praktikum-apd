import os

data_akun = [
    ["admin", "admin", "admin"],
    ["user", "user", "user"]
]

data_laundry = []

while True:
    os.system("cls || clear")
    print("Selamat Datang di Aplikasi Laundry, Silahkan Pilih Menu:")
    print("1. Login")
    print("2. Keluar")
    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        os.system("cls || clear")
        print("Login")
        user = input("Username: ")
        pw = input("Password: ")

        login_berhasil = False
        role = ""

        for a in data_akun:
            if user == a[0] and pw == a[1]:
                login_berhasil = True
                role = a[2]
                break

        if not login_berhasil:
            print("Login gagal")
            input("Silahkan tekan enter!")
        else:
            print("Berhasil Login sebagai ", role)
            input("Silahkan tekan enter!")

            while True:
                os.system("cls || clear")
                print("Menu ", role)
                print("1. Tambah Data Laundry")
                print("2. Lihat Data Laundry")
                print("3. Ubah Data Laundry")
                print("4. Hapus Data Laundry")
                print("5. Logout")
                pilihan_menu = input("Masukkan pilihan menu: ")

                if pilihan_menu == "1":
                    os.system("cls || clear")
                    print("Tambah Data Laundry")
                    nama = input("Nama Customer: ")
                    jenis = input("Jenis laundry: ")
                    berat = float(input("Berat (kg): "))
                    status = "Belum Selesai"
                    data_laundry.append([nama, jenis, berat, status])
                    print("Data laundry berhasil ditambahkan!")
                    input("Silahkan tekan enter!")

                elif pilihan_menu == "2":
                    os.system("cls || clear")
                    print("Data Laundry")
                    if len(data_laundry) == 0:
                        print("Data laundry belum ada.")
                    else:
                        for i in range(len(data_laundry)):
                            print(f"{i+1}. Nama: {data_laundry[i][0]}, Jenis: {data_laundry[i][1]}, Berat: {data_laundry[i][2]} kg, Status: {data_laundry[i][3]}")
                    input("Silahkan tekan enter!")

                elif pilihan_menu == "3":
                    os.system("cls || clear")
                    print("Ubah Data Laundry")
                    if len(data_laundry) == 0:
                        print("Data laundry belum ada.")
                        input("Silahkan tekan enter!")
                    else:
                        for i in range(len(data_laundry)):
                            print(f"{i+1}. Nama: {data_laundry[i][0]}, Jenis: {data_laundry[i][1]}, Berat: {data_laundry[i][2]} kg, Status: {data_laundry[i][3]}")
                        nomor_data_laundry = int(input("Masukkan nomor data yang ingin diubah: ")) - 1
                        if 0 <= nomor_data_laundry < len(data_laundry):
                            print("Input data yang ingin diubah saja, kosongkan jika tidak ingin diubah.")
                            nama = input("Nama Customer: ")
                            jenis = input("Jenis laundry: ")
                            berat_input = input("Berat (kg): ")
                            status = input("Status (Belum Selesai/Selesai): ")

                            if nama:
                                data_laundry[nomor_data_laundry][0] = nama
                            if jenis:
                                data_laundry[nomor_data_laundry][1] = jenis
                            if berat_input:
                                data_laundry[nomor_data_laundry][2] = float(berat_input)
                            if status in ["Belum Selesai", "Selesai"]:
                                data_laundry[nomor_data_laundry][3] = status

                            print("Data laundry berhasil diubah!")
                        else:
                            print("Nomor data tidak valid.")
                        input("Silahkan tekan enter!")

                elif pilihan_menu == "4":
                    os.system("cls || clear")
                    print("Hapus Data Laundry")
                    if len(data_laundry) == 0:
                        print("Data laundry belum ada.")
                        input("Silahkan tekan enter!")
                    else:
                        for i in range(len(data_laundry)):
                            print(f"{i+1}. Nama: {data_laundry[i][0]}, Jenis: {data_laundry[i][1]}, Berat: {data_laundry[i][2]} kg, Status: {data_laundry[i][3]}")
                        nomor_data_laundry = int(input("Masukkan nomor data yang ingin dihapus: "))
                        if 0 <= nomor_data_laundry <= len(data_laundry):
                            del data_laundry[nomor_data_laundry-1]
                            print("Data laundry berhasil dihapus!")
                        else:
                            print("Nomor data tidak valid.")
                        input("Silahkan tekan enter!")

                elif pilihan_menu == "5":
                    os.system("cls || clear")
                    print("Logout berhasil!")
                    input("Silahkan tekan enter!")
                    break

                else:
                    print("Pilihan menu tidak valid.")
                    input("Silahkan tekan enter!")

    elif pilihan == "2":
        os.system("cls || clear")
        print("Terima kasih telah menggunakan aplikasi laundry!")
        break

    else:
        print("Pilihan tidak valid.")
        input("Silahkan tekan enter!")