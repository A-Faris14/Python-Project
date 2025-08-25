# Aplikasi Manajemen Tugas Harian (Daily Task Manager)

## import library
# clear screen
import os
# table
from tabulate import tabulate
# time
import datetime as dt

# increment index dict tugas
index_tugas = 0

# dict tugas
tugas = {}

# pengulangan program
while True:
    # clear screen
    os.system('cls')

    # Tampilan Menu Utama
    print("===== MENU TO-DO LIST =====")
    print("1. Tambah Tugas")
    print("2. Hapus Tugas")
    print("3. Tandai Tugas Selesai")
    print("4. Lihat Semua Tugas")
    print("5. Keluar")
    print("===========================")

    input_menu = int(input("Pilih Menu : "))


    # Menu 1 : Tambah Tugas
    while input_menu == 1:
        # clear screen
        os.system('cls')

        # header menu
        print("========== TAMBAH TUGAS ==========")

        judul = input("Masukkan Judul Tugas\t\t: ")
        kategori = input("Masukkan Kategori\t\t: ")
        deadline = input("Masukkan deadline (dd-mm-yyyy)\t: ")
        
        # merubah deadline menjadi date
        datetime_object = dt.datetime.strptime(deadline, "%d-%m-%Y")
        date_object = datetime_object.date()
        date_object = date_object.strftime("%d-%m-%Y")

        # # pengecekan index tugas
        # if tugas[index_tugas]
        # list tugas
        tugas[index_tugas] = {
            "judul": judul,
            "kategori": kategori,
            "deadline": date_object,
            "status": "Belum selesai"
        }

        # indext tugas increment
        index_tugas += 1
        break

    
    # Menu 2 : Hapus Tugas
    while input_menu == 2:
        print(" List Tugas ".center(20, "="))
        print("="*64)
        headers = ["Judul", "Kategori", "Deadline", "Status"]
        print(f"{headers[0]:<15}|{headers[1]:<15}|{headers[2]:<15}|{headers[3]:<15}|")
        print("="*64)
        for i in range(0,len(tugas)):
            print(f"{i + 1}. {tugas[i]["judul"]:<15}|{tugas[i]["kategori"]:<15}|{str(tugas[i]["deadline"]):<15}|{tugas[i]["status"]:<15}|")
        hapus = int(input("\nMasukkan nomor tugas yang ingin anda hapus : "))
        del tugas[hapus - 1]
        print("\nTugas sudah berhasil dihapus")
        input("Tekan Enter untuk melanjutkan...")
        break

    # Menu 3 : Tandai Tugas Selesai
    while input_menu == 3:
        print(" List Tugas ".center(20, "="))
        for i in range(0,len(tugas)):
            if tugas[i]["status"] == "Belum selesai":
                print(f"{i + 1}. {tugas[i]["judul"]}\t{tugas[i]["kategori"]}\t{tugas[i]["deadline"]}\t{tugas[i]["status"]}")
        selesai = int(input("\nMasukkan nomor tugas yang ingin ditandai selesai : "))
        tugas[selesai - 1]["status"] = "Selesai"
        print("\nTugas berhasil ditandai selesai")
        input("Tekan Enter untuk melanjutkan...")
        break

    # Menu 4 : Lihat Semua Tugas
    while input_menu == 4:
        print(" List Tugas ".center(20, "="))
        print("="*64)
        headers = ["Judul", "Kategori", "Deadline", "Status"]
        print(f"{headers[0]:<15}|{headers[1]:<15}|{headers[2]:<15}|{headers[3]:<15}|")
        print("="*64)
        for i in range(0,len(tugas)):
                print(f"{tugas[i]["judul"]:<15}|{tugas[i]["kategori"]:<15}|{str(tugas[i]["deadline"]):<15}|{tugas[i]["status"]:<15}|")
        input("Tekan Enter untuk melanjutkan...")
        break

    if input_menu == 5:
        break


# ucapan terima kasih
print("\n==========================================")
print("Terima kasih sudah menggunakan program ini")
print("==========================================")