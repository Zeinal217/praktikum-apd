pemakaian = int(input("Masukkan jumlah pemakaian listrik (dalam kWh): "))

tarif_per_kwh = 1500

if pemakaian <= 100:
    tarif_per_kwh = 1000
elif pemakaian <= 300:
    tarif_per_kwh = 1200
else:
    tarif_per_kwh = 1500

total_biaya = pemakaian * tarif_per_kwh
print("Total biaya listrik yang harus dibayar: Rp", total_biaya)