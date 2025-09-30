ukt = 600000
namaTerdaftar = "Zeinal Abidin"
nimTerdaftar = "2509106075"

nama = input("Masukkan nama: ")
nim = input("Masukkan NIM: ")

if nama == namaTerdaftar and nim == nimTerdaftar:
    print(f"""Silakan pilih opsi pembayaran UKT :
1. Lunas: Biaya administrasi 1%
2. Cicilan 2x: Biaya administrasi 5%
3. Cicilan 4x: Biaya administrasi 8%
4. Cicilan 6x: Biaya administrasi 12%""")
    opsiPembayaran = int(input("Masukkan opsi pembayaran (1-4): "))
    if opsiPembayaran == 1:
        totalBayar = ukt + (ukt * 1/100)
        print(f"""===Rincian Pembayaran===
UKT = Rp {ukt}
Biaya administrasi = Rp {ukt * 1/100}
Total bayar anda = Rp {totalBayar}""")
    elif opsiPembayaran == 2:
        totalBayar = ukt + (ukt * 5/100)
        cicilan = totalBayar / 2
        print(f"""===Rincian Pembayaran===
UKT = Rp {ukt}
Biaya administrasi = Rp {ukt * 5/100}
Total bayar anda = Rp {totalBayar}
Cicilan yang harus anda bayar 2x = Rp {cicilan}""")
    elif opsiPembayaran == 3:
        totalBayar = ukt + (ukt * 8/100)
        cicilan = totalBayar / 4
        print(f"""===Rincian Pembayaran===
UKT = Rp {ukt}
Biaya administrasi = Rp {ukt * 8/100}
Total bayar anda = Rp {totalBayar}
Cicilan yang harus anda bayar 4x = Rp {cicilan}""")
    elif opsiPembayaran == 4:
        totalBayar = ukt + (ukt * 12/100)
        cicilan = totalBayar / 6
        print(f"""===Rincian Pembayaran===
UKT = Rp {ukt}
Biaya administrasi = Rp {ukt * 12/100}
Total bayar anda = Rp {totalBayar}
Cicilan yang harus anda bayar 6x = Rp {cicilan}""")
    else:
        print("Anda tidak memilih angka 1-4.")
else:
    print("Login Gagal")