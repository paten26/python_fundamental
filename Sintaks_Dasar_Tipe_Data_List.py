Daftar_kopi = ["Kopken", "Janjijiwa", "Fore"]
print("Tampilkan variable daftar buku")
print(Daftar_kopi)

print("\nProses dengan for in")
for kopi in Daftar_kopi:
    print(kopi)

print("\nTampilkan daftar kopi sesuai yang dipilih")
print(Daftar_kopi[0]) #0 berarti kopi pertama
print(Daftar_kopi[2]) #2 berarti kopi ke-3

print("\nTampilkan dengan for in range")
for i in range(0, len(Daftar_kopi)): #len untuk mendefinisikan panjang suatu data
    print(Daftar_kopi[i]) #i tidak memiliki arti khusus, bisa diganti dengan apa saja

print("\nMenambahkan data")
Daftar_kopi.append("koi") #.append untuk menambahkan data "koi"
for i in range(0, len(Daftar_kopi)):
    print(Daftar_kopi[i])

print("\nClear data keseluruhan")
Daftar_kopi.clear()
for i in range(0, len(Daftar_kopi)):
    print(Daftar_kopi[i])

print("\nMengganti data")
Daftar_kopi = ["Kopken", "Janjijiwa", "Fore", "Koi"]
Daftar_kopi[3]="kapalapi"
for i in range(0, len(Daftar_kopi)):
    print(Daftar_kopi[i])

print("\nAmbil data")
Daftar_kopi = ["Kopken", "Janjijiwa", "Fore", "Koi"]
kopi = Daftar_kopi.pop(3) #.pop mengambil data, 3 berarti data ke-3
for i in range(0, len(Daftar_kopi)):
    print(Daftar_kopi[i])

print("\nTampilkan data yang diambil")
print(kopi) #menampilkan data yang tadi diambil, yaitu kapalapi

print("\nDelete salah satu data")
Daftar_kopi = ["Kopken", "Janjijiwa", "Fore", "Koi"]
del Daftar_kopi [1] #del 1 berarti menghapus data yang ke-2
for i in range(0, len(Daftar_kopi)):
    print(Daftar_kopi[i])

print("\nDelete dengan list comprehension")
Daftar_kopi = ["Kopken", "Janjijiwa", "Fore", "Koi"]
del Daftar_kopi[:] #del : berarti menghapus semua data
for i in range(0, len(Daftar_kopi)):
    print(Daftar_kopi[i])

print("\nDelete dengan list comprehension dengan start")
Daftar_kopi = ["Kopken", "Janjijiwa", "Fore", "Koi"]
del Daftar_kopi[0:1] #del 0:1 start 0, stop 1
for i in range(0, len(Daftar_kopi)):
    print(Daftar_kopi[i])