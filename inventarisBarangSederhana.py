# Latihan membuat function

# Import
import os

# kamus data
funct_template = {
    "kodeBarang" : "kodeBarang",
    "nama" : "nama",
    "kategori" : "kategori",
    "stok" : "stok"
}

dataBarang = {}

# kamus function
def bersihkanLayar():
    os.system('cls')

def gerbang():
    input("Tekan enter untuk melanjutkan!!")

def header(judul):
    bersihkanLayar()
    print("="*40)
    print(f"{judul:^40}")
    print("="*40+"\n")

def menu():
    print("1. Tambah Barang")
    print("2. Lihat Barang")
    print("3. Cari Barang")
    print("4. Keluar")


def tambahBarang():
    header("Tambahkan Barang Baru")
    barang = dict.fromkeys(funct_template.keys())
    cekKode = True
    while cekKode:      
        barang["kodeBarang"] = input("Masukan kode barang\t: ")
        cekKode = False
        for data in dataBarang:
            if data == barang["kodeBarang"]:
                print("Kode barang sudah ada!")
                cekKode = True
                break
    barang["nama"] = input("Masukan nama barang\t: ")
    barang["kategori"] = input("Masukan kategori barang\t: ")
    barang["stok"] = input("Masukan stok barang\t: ")
    dataBarang.update({barang["kodeBarang"]:barang})
    gerbang()


def lihatBarang():
    header("Daftar-daftar Barang")
    if not dataBarang:
        print("Belum ada barang")
    else:
        print(f"{"Kode Barang":<15}|{"Nama":<20}|{"Kategori":<20}|{"Stok":<3}")
        print("="*64)
        for data in dataBarang:
            print(f"{dataBarang[data]["kodeBarang"]:^15}|{dataBarang[data]["nama"]:<20}|{dataBarang[data]["kategori"]:<20}|{dataBarang[data]["stok"]:^3}")
    gerbang()

def cariBarang():
    header("Daftar-daftar Barang")
    if not dataBarang:
        print("Belum ada barang")
    else:
        inputCari = input("Masukan kode barang yang ingin dicari\t: ")
        ditemukan = False
        for data in dataBarang:
            if data == inputCari:
                print(f"\n{"Kode Barang":<15}|{"Nama":<20}|{"Kategori":<20}|{"Stok":<3}")
                print("="*60)
                print(f"{dataBarang[data]["kodeBarang"]:^15}|{dataBarang[data]["nama"]:<20}|{dataBarang[data]["kategori"]:<20}|{dataBarang[data]["stok"]:^3}")
                ditemukan = True
                break
        if ditemukan == False:
            print("Barang tidak ditemukan!")
    gerbang()

# Progarm Dimulai
while True:
    header("Program Inventaris Barang")
    menu()
    inputMenu = input("\nMasukan menu\t: ")
    try:
        value = int(inputMenu)
    except ValueError:
        print("\nInput harus berupa angka!!")
        gerbang()
        continue
    inputMenu = int(inputMenu)
    match inputMenu:
        case 1:
            tambahBarang()
        case 2:
            lihatBarang()
        case 3:
            cariBarang()
        case 4:
            os.system("cls")
            print("Terima Kasih Telah Menggunakan Program Ini!!")
            break
        case _:
            print("\nHarap masukan menu dengan benar!")
            gerbang()