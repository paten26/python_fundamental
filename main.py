"""
SINTAKSIS DASAR
"""

#1.SEKUENSIAL
print("Dia levi")
print('Aku siapa?')

#2.PERCABANGAN
#Contoh soal : levi menyuruh saya membeli kopi, jika harga 1 gelas kopi Rp.5000, beli 2 gelas. jika lebih beli 1 gelas saja
harga_kopi = 6000
if harga_kopi == 5000:
    print("beli 2 gelas")
else:
    print("beli 1 gelas")

#3.PENGULANGAN
#Contoh soal : Levi menyuruh saya meminum seluruh kopi yang ada
Jumlah_kopi = 10
Jumlah_kopi_sudah_diminum = 0

for Jumlah_kopi_sudah_diminum in range (1, Jumlah_kopi+1):
    print(f"kopi yang sudah diminum = {Jumlah_kopi_sudah_diminum} gelas")
