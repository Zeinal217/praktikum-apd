# # def menu():
# #     print("=== Menu Utama ===")
# #     print("1. Tambah Data")
# #     print("2. Hapus Data")
# #     print("3. Tampilkan Data")
# #     print("4. Keluar")
# #     pilihan = input("Pilih menu (1-4): ")
# #     return pilihan

# # def tambah_data():
# #     print("Menambahkan data")
# #     print("Data berhasil ditambahkan")
    
# # def hapus_data():
# #     print("Menghapus data")
# #     print("Data berhasil dihapus")

# # def tampilkan_data():
# #     print("Menampilkan data")
# #     print("Data ditampilkan")

# # while True:
# #     pilihan = menu()
# #     if pilihan == '1':
# #         tambah_data()
# #     elif pilihan == '2':
# #         hapus_data()
# #     elif pilihan == '3':
# #         tampilkan_data()
# #     elif pilihan == '4':
# #         print("Keluar dari program")
# #         break
# #     else:
# #         print("Pilihan tidak valid, silakan coba lagi.")

# def luas_persegi_panjang(panjang, lebar, tinggi):
#     luas =  panjang * lebar * tinggi
#     print(f"Luas persegi panjang dengan panjang adalah {luas}")

# luas_persegi_panjang(10, 5, 2)


# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas

def lPersegi(sisi):
    luas = sisi * sisi
    return luas

print(lPersegi(4))