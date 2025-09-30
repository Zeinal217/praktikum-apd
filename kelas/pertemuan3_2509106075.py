totalBelanja = int(input("Masukkan total belanja: "))

diskon = "Diskon 20%" if totalBelanja > 100000 else ("Diskon 10%" if totalBelanja > 50000 else "Tidak ada diskon")
print(diskon)