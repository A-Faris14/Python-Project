# === Program Perkiraan Kecepatan Sepeda Menggunakan Interpolasi Newton Lokal ===

# import library
import os
from tabulate import tabulate
import math


# header
def header():
    print("=========================================================")
    print("<<   SISTEM METODE NUMERIK : MODE INTERPOLASI NEWTON   >>")
    print("<<      MODUL PERKIRAAN KECEPATAN SEPEDA (STRAVA)      >>")
    print("=========================================================\n")

# informasi pengguna
def info_awal():
    print("Informasi:")
    print("Program ini menggunakan metode Interpolasi Newton dengan 5 titik data.")
    print("Silakan masukkan 5 nilai jarak (km) dan 5 nilai kecepatan (km/jam) yang")
    print("mewakili data kecepatan pada jarak tertentu.\n")
    print("Pastikan jarak yang ingin Anda perkirakan berada di sekitar (tidak terlalu jauh dari)")
    print("kelima titik data tersebut, agar hasil interpolasi tetap akurat.\n")


# loop awal program
mulaiProgram = True
while mulaiProgram:
    os.system('cls')

    # summon header
    header()

    # Panggil fungsi ini setelah header utama
    info_awal()

    input("Tekan enter untuk melanjutkan...")

    os.system('cls')

    # summon header
    header()


    # Header Input
    print("\n>>=== INPUT DATA TITIK (5 TITIK DATA) ===<<")


    # kumpulan list
    data = {
        "jarakKM" : [],
        "kecepatan" : [],
        "ST-1" : [],
        "ST-2" : [],
        "ST-3" : [],
        "ST-4" : [],
    }

    print()

    # loop input jarak
    for x in range(5):
        jarakInput = float(input("Masukan daftar jarak (KM): "))
        data['jarakKM'].append(jarakInput)

    print()

    # loop input kecepatan
    for x in range(5):
        kecepatanInput = float(input("Masukkan daftar kecepatan (km/jam): "))
        data["kecepatan"].append(kecepatanInput)

    print()

    # input jarak yang ingin diperkirakan
    cekJarak = True
    while cekJarak:
        jarakPerkiraan = float(input("Masukkan jarak yang ingin diperkirakan: "))
        if jarakPerkiraan < data['jarakKM'][0] or jarakPerkiraan > data['jarakKM'][4]:
            print("Jarak Perkiraan yang anda input di luar range!\n")
        else:
            cekJarak = False

    print()

    print("Hasil anda sedang dihitung!")
    input("Tekan enter untuk melanjutkan...")

    os.system('cls')

    # Perhitungan Selisih Terbagi
    for x in range(4):
        st1 = (data["kecepatan"][x+1] - data["kecepatan"][x]) / (data["jarakKM"][x+1] - data["jarakKM"][x])
        data["ST-1"].append(st1)

    for x in range(3):
        st2 = (data["ST-1"][x+1] - data["ST-1"][x]) / (data["jarakKM"][x+2] - data["jarakKM"][x])
        data["ST-2"].append(st2)

    for x in range(2):
        st3 = (data["ST-2"][x+1] - data["ST-2"][x]) / (data["jarakKM"][x+3] - data["jarakKM"][x])
        data["ST-3"].append(st3)

    for x in range(1):
        st4 = (data["ST-3"][x+1] - data["ST-3"][x]) / (data["jarakKM"][x+4] - data["jarakKM"][x])
        data["ST-4"].append(st4)

    # summon header
    header()

    # header hasil
    print("\n>>=== TABEL SELISIH TERBAGI (DIVIDED DIFFERENCE TABLE) ===<<")

    # header untuk tabel
    headerTabel = ["x", "f(x)", "ST-1", "ST-2", "ST-3", "ST-4"]

    print()

    # Print the table with grid formatting
    print(tabulate(data, headers=headerTabel, tablefmt="grid"))


    # header hasil polinom newton
    print("\n>>=== PEMBENTUKAN POLINOM NEWTON ===<<")

    print()

    hasil = (
        data["kecepatan"][0]
        + data["ST-1"][0] * (jarakPerkiraan - data["jarakKM"][0])
        + data["ST-2"][0] * (jarakPerkiraan - data["jarakKM"][0]) * (jarakPerkiraan - data["jarakKM"][1])
        + data["ST-3"][0] * (jarakPerkiraan - data["jarakKM"][0]) * (jarakPerkiraan - data["jarakKM"][1]) * (jarakPerkiraan - data["jarakKM"][2])
        + data["ST-4"][0] * (jarakPerkiraan - data["jarakKM"][0]) * (jarakPerkiraan - data["jarakKM"][1]) * (jarakPerkiraan - data["jarakKM"][2]) * (jarakPerkiraan - data["jarakKM"][3])
    )

    print(f"P4(x) = {data["kecepatan"][0]}", )
    print(f"      + {data['ST-1'][0]:.4f} ({jarakPerkiraan} - {data['jarakKM'][0]})")
    print(f"      + {data['ST-2'][0]:.4f} ({jarakPerkiraan} - {data['jarakKM'][0]})({jarakPerkiraan} - {data['jarakKM'][1]})")
    print(f"      + {data['ST-3'][0]:.4f} ({jarakPerkiraan} - {data['jarakKM'][0]})({jarakPerkiraan} - {data['jarakKM'][1]})({jarakPerkiraan} - {data['jarakKM'][2]})")
    print(f"      + {data['ST-4'][0]:.4f} ({jarakPerkiraan} - {data['jarakKM'][0]})({jarakPerkiraan} - {data['jarakKM'][1]})({jarakPerkiraan} - {data['jarakKM'][2]})({jarakPerkiraan} - {data['jarakKM'][3]})")

    print("\n>>=== HASIL INTERPOLASI NEWTON ===<<\n")

    print(f"Kecepatan pada jarak {jarakPerkiraan:.2f} km diperkirakan = {hasil:.2f} km/jam\n")

    input("Tekan enter untuk melanjutkan...")

    os.system('cls')

    header()

    print("\n>>=== ULANGI PROGRAM? ===<<\n")

    tanya = input("Ingin mencoba perhitungan lagi? (y/t): ")

    if tanya == "t":
        mulaiProgram = False

os.system('cls')
print("\n>>=== TERIMA KASIH TELAH MENGGUNAKAN SISTEM INTERPOLASI NEWTON ===<<")
print("Semoga hasil perkiraan ini membantu Anda dalam menganalisis performa bersepeda.")
print("Sampai jumpa pada perhitungan berikutnya!\n")
