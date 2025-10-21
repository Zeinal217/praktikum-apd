# # # # # # # # # # # # # # Membuat set
# # # # # # # # # # # # # buah = {"apel", "jeruk", "mangga", "apel"}
# # # # # # # # # # # # # print(buah)

# # # # # # # # # # # # # angka_ganjil = {1, 3, 5, 7, 9}
# # # # # # # # # # # # # for angka in angka_ganjil:
# # # # # # # # # # # # #     print(angka)

# # # # # # # # # # # # # print("menambahkan angka 11")
# # # # # # # # # # # # # angka_ganjil.add(11)

# # # # # # # # # # # # # angka_ganjil.discard(15)
# # # # # # # # # # # # # print(angka_ganjil)
# # # # # # # # # # # # # # for angka in angka_ganjil:
# # # # # # # # # # # # # #     print(angka)

# # # # # # # # # # # # # # nama = ['dapupu', 'julpa', 'asep hedsot']
# # # # # # # # # # # # # # print(nama[1])

# # # # # # # # # # # # set_A = {1, 2, {3, 4}}
# # # # # # # # # # # # print(set_A)

# # # # # # # # # # # Daftar_buku = {
# # # # # # # # # # #     "Buku1" : "Bumi Manusia",
# # # # # # # # # # #     "Buku2" : "Laut Bercerita"
# # # # # # # # # # # }

# # # # # # # # # # # # print(Daftar_buku["Buku1"])
# # # # # # # # # # # # print(Daftar_buku)
# # # # # # # # # # # for value in Daftar_buku.items():
# # # # # # # # # # #     print(value)

# # # # # # # # # Biodata = {
# # # # # # # # #     "Nama" : "Ananda Daffa Harahap",
# # # # # # # # #     "NIM" : 2409106050,
# # # # # # # # #     "KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data", "Algoritma", "Jaringan Komputer"],
# # # # # # # # #     True : False,
# # # # # # # # #     "Social Media" : {"Instagram" : "daffahrhap"
# # # # # # # # #     }
# # # # # # # # # }

# # # # # # # # # # for i,j in Biodata.items():
# # # # # # # # # #     print(f"{i} : {j}")

# # # # # # # # # # print(f"nama saya adalah {Biodata["MAHASIGMA"]}")
# # # # # # # # # print(Biodata.get("KRS")[1:5:2])
# # # # # # # # # # print(f"Instagram : {Biodata['Social Media']['Instagram']}")
# # # # # # # # # # print(f"nama saya adalah {Biodata.get("Nama")}")

# # # # # # # # # # list_mahasiwa = dict(nama="Dapupu", Jurusan="Informatika", )
# # # # # # # # # # print(list_mahasiwa)

# # # # # # # # Nilai = {
# # # # # # # # "Matematika": 80,
# # # # # # # # "B. Indonesia": 90,
# # # # # # # # "B. Inggris": 81,
# # # # # # # # "Kimia": 78,
# # # # # # # # "Fisika": 80
# # # # # # # # }
# # # # # # # # # Tanpa menggunakan items()
# # # # # # # # # for i in Nilai:
# # # # # # # # #     print(i)

# # # # # # # # print("") # pemisah
# # # # # # # # # Menggunakan items()
# # # # # # # # for Bang_Pernan, Mba_Triya in Nilai.items():
# # # # # # # #     print(f"Nilai {Bang_Pernan} anda adalah {Mba_Triya}")

# # # # # # # Film = {
# # # # # # # "Avenger Endgame" : "Action",
# # # # # # # "Sherlock Holmes" : "Mystery",
# # # # # # # "The Conjuring" : "Horror"}
# # # # # # # #Sebelum Ditambah
# # # # # # # print(Film)
# # # # # # # Film["Godzilla"] = "Action"
# # # # # # # # Film.update({"Hours" : "Thriller"})
# # # # # # # print("")
# # # # # # # #Setelah Ditambah
# # # # # # # print("setelah ditambah") # pemisah
# # # # # # # print(Film)

# # # # # # # data = {
# # # # # # # "Nama" : "Daffa",
# # # # # # # "Umur" : 19,
# # # # # # # "Jurusan" : "Informatika"
# # # # # # # }
# # # # # # # #Sebelum Dihapus
# # # # # # # print(data)
# # # # # # # del data["Nama"]
# # # # # # # print(data)

# # # # # # data = {
# # # # # # "Nama" : "Daffa",
# # # # # # "Umur" : 19,
# # # # # # "Jurusan" : "Informatika"
# # # # # # }
# # # # # # #Sebelum Dihapus
# # # # # # print(data)
# # # # # # cache = data.pop("Nama")
# # # # # # print(data)
# # # # # # #Setelah dihapus
# # # # # # print(cache)

# # # # # data = {
# # # # # "Nama" : "Daffa",
# # # # # "Umur" : 19,
# # # # # "Jurusan" : "Informatika"
# # # # # }
# # # # # #Sebelum Dihapus
# # # # # print(data)
# # # # # data.clear()
# # # # # #Setelah dihapus
# # # # # print(data)

# # # # data = {
# # # # "Nama" : "Daffa",
# # # # "Umur" : 19,
# # # # "Jurusan" : "Informatika"
# # # # }

# # # # print("Jumlah Data = ", len(data))

# # # buku = {
# # # "Buku1" : "Bumi Manusia",
# # # "Buku2" : "Laut Bercerita"
# # # }
# # # pinjam = buku.copy()
# # # pinjam['Buku1'] = "Sapiens"
# # # print(buku)
# # # print(pinjam)
# # # # print("Dictionary yang telah disalin : ", pinjam)

# # key = "apel", "jeruk", "mangga"
# # value = "buah favorit"
# # buah = dict.fromkeys(key, value)
# # print(buah)

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81
# }
# #sebelum Setdefault
# print(Nilai)
# print("")
# #menggunakan setdefault
# print("Nilai : ", Nilai.setdefault("Kimia", 70))
# print("")
# #setelah menggunakan setdefault
# print(Nilai)

Musik = {
"The Chainsmoker" : ["All we Know", "The Paris"],
"Alan Walker" : ["Alone", "Lily"],
"Neffex" : ["Best of Me", "Memories"]
}
for penyanyi, album in Musik.items():
    print(f"Musik milik {penyanyi} adalah : ")
    for song in album:
        print(song)
    print("")