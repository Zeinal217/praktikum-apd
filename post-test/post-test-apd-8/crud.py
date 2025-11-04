from prettytable import PrettyTable
from data import data_laundry, akun, clear
from colorama import Fore, Style

def menu_crud(tipe):
    clear()

    if tipe == "laundry":
        fields = ["nama", "jenis", "berat", "status"]
        storage = data_laundry
    else:
        fields = ["username", "password", "role"]
        storage = akun

    def id_baru():
        return 1 if len(storage) == 0 else max(storage.keys()) + 1

    def tambah_data():
        clear()
        print(f"=== Tambah Data {tipe} ===")
        new_id = id_baru()
        entry = {}

        for f in fields:
            if f == "status":
                entry[f] = "Belum selesai"
            elif f == "role":
                entry[f] = "user"
            else:
                entry[f] = input(f"Masukkan {f}: ")

        storage[new_id] = entry
        print(Fore.GREEN + "Data berhasil ditambahkan!" + Style.RESET_ALL)
        input("Tekan Enter...")

    def lihat_data():
        clear()
        if not storage:
            print(Fore.YELLOW + "Belum ada data." + Style.RESET_ALL)
            input("Tekan Enter...")
            return

        table = PrettyTable()
        table.field_names = ["ID"] + list(next(iter(storage.values())).keys())

        for key, value in storage.items():
            table.add_row([key] + list(value.values()))

        print(table)
        input("Tekan Enter...")

    def ubah_data():
        lihat_data()
        try:
            target = int(input("Masukkan ID data yang ingin diubah: "))
            if target not in storage:
                raise ValueError

            clear()
            print("Kosongkan input jika tidak ingin mengubah field.")
            for f in fields:
                new_val = input(f"{f} baru: ")
                if new_val:
                    if f == "berat":
                        new_val = float(new_val)
                    storage[target][f] = new_val

            print(Fore.GREEN + "Data berhasil diperbarui!" + Style.RESET_ALL)
        except:
            print(Fore.RED + "ID tidak ditemukan!" + Style.RESET_ALL)
        input("Tekan Enter...")

    def hapus_data():
        lihat_data()
        try:
            target = int(input("Masukkan ID yang ingin dihapus: "))
            del storage[target]
            print(Fore.GREEN + "Data berhasil dihapus!" + Style.RESET_ALL)
        except:
            print(Fore.RED + "ID tidak ditemukan!" + Style.RESET_ALL)
        input("Tekan Enter...")

    while True:
        clear()
        print(f"=== CRUD {tipe.upper()} ===")
        print("1. Tambah")
        print("2. Lihat")
        print("3. Ubah")
        print("4. Hapus")
        print("5. Kembali")
        pilihan = input("Pilih menu: ")

        if pilihan == "1": tambah_data()
        elif pilihan == "2": lihat_data()
        elif pilihan == "3": ubah_data()
        elif pilihan == "4": hapus_data()
        elif pilihan == "5": break
