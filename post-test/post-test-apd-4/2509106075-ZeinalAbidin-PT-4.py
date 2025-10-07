nama = "Zeinal Abidin"
nim = 2509106075

batasLogin = 3

for i in range(batasLogin):
    username = input("Masukkan Username: ")
    password = int(input("Masukkan Password: "))

    if username == nama and password == nim:
        print("Login berhasil! Selamat datang di Toko Furniture Infordeh")
        break
    else:
        sisaPercobaan = batasLogin - (i + 1)
        if sisaPercobaan > 0:
            print(f"Login gagal! Sisa percobaan: {sisaPercobaan}")
        else:
            print("Sisa percobaan habis, anda gagal login!")
            exit()

while True:
    print("Silahkan pilih opsi furniture berikut:")
    print("1. Sofa dengan harga per unit Rp. 500.000.")
    print("2. Meja Belajar dengan harga per unit Rp. 250.000.")
    print("3. Rak Lemari dengan harga per unit Rp. 150.000.")
    print("4. Keluar.")

    pilihanFurniture = int(input("Silhkan pilih funitur (Masukkan angka 1-4):"))

    if pilihanFurniture == 1:
        namaFurniture = "Sofa"
        hargaPerUnit = 500000
    elif pilihanFurniture == 2:
        namaFurniture = "Meja Belajar"
        hargaPerUnit = 250000
    elif pilihanFurniture == 3:
        namaFurniture = "Rak Lemari"
        hargaPerUnit = 150000
    elif pilihanFurniture == 4:
        print("Terimakasih sudah berbelanja di Toko Furniture Infordeh")
        break
    else:
        print("Input angka 1-4!")
        continue

    jumlah = int(input("Masukkan jumlah yang ingin dibeli:"))

    totalHarga = 0
    for i in range(jumlah):
        totalHarga += hargaPerUnit

    if totalHarga >= 700000:
        diskon = totalHarga * (20 / 100)
        totalHarga -= diskon
        bonus = "Diskon 20%"
    elif totalHarga >= 500000:
        diskon = totalHarga * (8 / 100)
        totalHarga -= diskon
        bonus = "Diskon 8%"
    elif totalHarga >= 150000:
        bonus ="Kitchen Set"

    print("====Struk Pembelian====")
    print(f"Nama Furniture  : {namaFurniture}")
    print(f"Jumlah          : {jumlah}")
    print(f"Total Harga     : Rp {totalHarga}")
    print(f"Bonus/diskon    : {bonus}")