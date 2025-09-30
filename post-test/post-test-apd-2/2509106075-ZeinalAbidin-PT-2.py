nama = input("Masukkan nama lengkap: ")
nim = int(input("Masukkan NIM: "))

harga = int(input("Masukkan harga menu: "))

pajakPecelLele = harga * (5/100)
pajakMieAyam = harga * (8/100)
pajakNasiPadang = harga * (10/100)

hargaPecelLele = harga + pajakPecelLele
hargaMieAyam = harga  + pajakMieAyam
hargaNasiPadang = harga + pajakNasiPadang

print(f"Mahasiswa atas nama {nama} dan NIM {nim} ingin membeli makanan dengan harga Rp {harga}")

print(f"-------------------------------------------------")
print(f"|    Menu     | Harga Awal | Pajak | Harga      |")
print(f"-------------------------------------------------")
print(f"| Pecel Lele  | {harga}      | 5 %   | {hargaPecelLele}    |")
print(f"| Mie Ayam    | {harga}      | 8 %   | {hargaMieAyam}    |")
print(f"| Nasi Padang | {harga}      | 10 %  | {hargaNasiPadang}    |")
print(f"-------------------------------------------------")

pesanPecelLele = int(input("Input jumlah pemesanan pecel lele: "))
pesanMieAyam = int(input("Input jumlah pemesanan Mie Ayam: "))
pesanNasiPadang = int(input("Input jumlah pemesanan Nasi Padang: "))

totalHargaPecelLele = hargaPecelLele * pesanPecelLele
totalHargaMieAyam = hargaMieAyam * pesanMieAyam
totalHargaNasiPadang = hargaNasiPadang * pesanNasiPadang

grandTotal = totalHargaMieAyam + totalHargaPecelLele + totalHargaNasiPadang

print("Deskripsi Pembelian: ")
print(f"Pecel lele {pesanPecelLele} = Rp {totalHargaPecelLele}")
print(f"Mie ayam {pesanMieAyam} = Rp {totalHargaMieAyam}")
print(f"Nasi padang {pesanNasiPadang} = Rp {totalHargaNasiPadang}")
print(f"Harga yang harus di bayar = Rp {grandTotal}")