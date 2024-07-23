"""
SINTAKSIS DASAR
"""

#1.SEKUENSIAL
print("CONTOH SEKUENSIAL")
print("Dia levi")
print('Aku siapa?')
print("")

#2.PERCABANGAN
print("\nCONTOH PERCABANGAN IF ELSE") #\n sebagai enter memberikan spasi saat run
#Contoh soal : levi menyuruh saya membeli kopi, jika harga 1 gelas kopi Rp.5000, beli 2 gelas. jika lebih beli 1 gelas saja
harga_kopi = 6000
if harga_kopi == 5000: #if (jika), : (maka)
    print("beli 2 gelas")
else:
    print("beli 1 gelas")
print("")

#3.PENGULANGAN FOR
print("\nCONTOH PENGULANGAN DENGAN FOR")
#Contoh soal : Levi menyuruh saya meminum seluruh kopi yang ada
Jumlah_kopi = 10
Jumlah_kopi_sudah_diminum = 0

for Jumlah_kopi_sudah_diminum in range (1, Jumlah_kopi+1):
    print(f"kopi yang sudah diminum = {Jumlah_kopi_sudah_diminum} gelas")
print("")

#PENGULANGAN WHILE 1
print("\nCONTOH PENGULANGAN DENGAN WHILE 1")
#Contoh soal : Levi menyuruh saya meminum seluruh kopi yang ada
Jumlah_kopi = 10
Jumlah_kopi_sudah_diminum = 0

while Jumlah_kopi_sudah_diminum < Jumlah_kopi : #while (selama)
    Jumlah_kopi_sudah_diminum = Jumlah_kopi_sudah_diminum + 1
    print(f"kopi yang sudah diminum {Jumlah_kopi_sudah_diminum} gelas")

#PENGULANGAN WHILE 2
print("\nCONTOH PENGULANGAN DENGAN WHILE 2")
#Contoh soal : Levi menyuruh saya meminum seluruh kopi yang ada sampai habis
Jumlah_kopi = 10
Jumlah_kopi_sudah_diminum_dan_habis = 10

while Jumlah_kopi_sudah_diminum_dan_habis < Jumlah_kopi :
    Jumlah_kopi_sudah_diminum_dan_habis = Jumlah_kopi_sudah_diminum_dan_habis + 1
    if Jumlah_kopi_sudah_diminum_dan_habis == 0:
        print(f"Kopi ke {Jumlah_kopi_sudah_diminum_dan_habis} belum habis")
    else:
        Jumlah_kopi_sudah_diminum_dan_habis = Jumlah_kopi_sudah_diminum_dan_habis + 1
        print(f"Kopi ke {Jumlah_kopi_sudah_diminum_dan_habis} sudah diminum dan habis")
