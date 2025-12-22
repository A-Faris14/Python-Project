# Program List Buku

# import
import os
from tabulate import tabulate


# kumpulan data
inputBuku =[]
listBuku = []
headerTable = ["Judul", "Penulis", "Tahun Terbit"]

while True:
    os.system('cls')
    # Header program
    print("==================")
    print("Program List Buku")
    print("==================")

    # menu awal
    print("""
1. Tambah buku baru
2. Update buku
3. Delete buku
4. Lihat list buku
5. Keluar
    """)

    while True:
        inputMenu = (input("Pilih menu\t: "))
        try:
            value = int(inputMenu)
            break
        except:
            print("Masukan input dengan benar!!")
            input("Tekan enter untuk melanjutkan!")

    match inputMenu:
        case 1:
            inputBukuBool = True
            while inputBukuBool:
                os.system('cls')
                print("=== Masukan Data Buku ===")
                inputJudul = input("Judul buku\t: ")
                inputPenulis = input("Nama penulis\t: ")
                inputTahun = input("Tahun terbit\t: ")

                inputBuku = [inputJudul, inputPenulis, inputTahun]
                listBuku.append(inputBuku)

                tambahBool = True
                while tambahBool:
                    inputLagi = input("Tambah buku lagi? (y/t)\t: ")
                    if inputLagi == "t":
                        tambahBool = False
                        inputBukuBool = False
                    elif inputLagi == "y":
                        break
                    else:
                        print("Masukan input dengan benar!\n")
                        continue
        case 4:
            os.system('cls')
            print("==== Daftar Buku ====")
            if len(listBuku) == 0:
                print("Buku masih kosong")
                input("Tekan enter untuk melanjutkan!")
            else:
                print(tabulate(listBuku, headers=headerTable,   tablefmt="grid"))
                input("Tekan enter untuk melanjutkan!")
        case 5:
            os.system('cls')
            print("==== Terima kasih telah menggunakan program ini ====")
            break
        case _:
            print("Masukan input dengan benar!!")
            input("Tekan enter untuk melanjutkan!")
