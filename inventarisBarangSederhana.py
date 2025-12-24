# Program inventaris barang sederhana

# import
import os
from tabulate import tabulate

# kumpulan data
dataKodeBarang = [
    ("A001", "Elektronik"),
    ("A002", "Furnitur"),
    ("A003", "Perkakas")
]

dataBarang = {
    "Kode" : [],
    "Nama" : [],
    "Kategori" : [],
    "Stok" : []
}

mulaiProgram = True

while mulaiProgram:
    # header program
    os.system('cls')
    print("="*30)
    print("\tSelamat Datang")
    print("di Program Inventaris Barang")
    print("="*30)

    print("""
1. Tambah Barang
2. Lihat Barang
3. Tampilkan Kategori
4. Cari Barang
5. Keluar
    """)

    inputMenu = input("Pilih menu\t: ")
    try:
        value = int(inputMenu)
    except ValueError:
        print("\nInput harus berupa angka")
        input("Tekan enter untuk melanjutkan!")
        continue

    inputMenu = int(inputMenu)

    match inputMenu:
        case 1:
            os.system('cls')
            print("======= Tambah Barang =======")
            print("\nKategori barang yang ada:")
            print(tabulate(dataKodeBarang, headers=("Kode Barang", "Kategori"), tablefmt="grid"))

            tambah = True
            while tambah:
                dataBarang["Kode"].append(input("Masukan kode barang\t: "))
                dataBarang["Nama"].append(input("Masukan Nama barang\t: "))
                dataBarang["Kategori"].append(input("Masukan Kategori barang\t: "))
                dataBarang["Stok"].append(input("Masukan Stok barang\t: "))

                tambahLagi = input("Ingin menambah data barang lagi? (y/t)\t: ")
                if tambahLagi == "t":
                    tambah = False
                elif tambahLagi == "y":
                    tambah = True
                else:
                    print("Masukan input yang benar!!\n")
                    tambah = True
        case 2: 
            os.system('cls')
            print(f"{"="*14} Daftar Barang {"="*14}")
            if not all(dataBarang.values()):
                print("\nBarang belum ada")
                input("Tekan enter untuk melanjutkan!")
            else:
                print(f"{"Kode":<5} {"Nama":<15} {"Kategori":<15} {"Stok":^3}")
                print("-"*43)
                for x in range(len(dataBarang["Kode"])):
                    Kode = dataBarang["Kode"][x]
                    Nama = dataBarang["Nama"][x]
                    Kategori = dataBarang["Kategori"][x]
                    Stok = dataBarang["Stok"][x]
                    print(f"{Kode:<5} {Nama:<15} {Kategori:<15} {Stok:^3}")
                input("\nTekan enter untuk melanjutkan!")
        case 3: 
            os.system('cls')
            print("======= Kategori Barang =======")
            print(tabulate(dataKodeBarang, headers=("Kode Barang", "Kategori"), tablefmt="grid"))
            input("Tekan enter untuk melanjutkan!")
        case 5:
            os.system('cls')
            print("=========== Sampai jumpa lagi ===========")
            print("Terima kasih telah menggunakan program ini")
            mulaiProgram = False
        case _:
            print("\nHarap masukan menu yang tersedia!")
            input("Tekan enter untuk melanjutkan!")