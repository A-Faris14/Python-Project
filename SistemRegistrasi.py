# Sistem Registrasi dan Verifikasi Akun Sederhana

# clear screen
import os
os.system('cls')

# Pembukaan
print("====SELAMAT DATANG====")

# input data
nama = input("Masukan nama : ")
usia = input("Masukan usia : ")
email = input("Masukan email : ")
kata_Sandi = input("Masukan kata sandi : ")

## Validasi input

# Validasi email

if "@" not in email: 
    print("\n" + "Peringatan".center(22,"="))
    print("Email tidak valid!")
    print("Email harus mengandung char '@'")
    exit()

if "." not in email.split("@")[1]:
    print("\n" + "Peringatan".center(22,"="))
    print("Email tidak valid!")
    print("Email harus mengandung char '.' setelah char '@'")
    exit()

if " " in email:
    print("\n" + "Peringatan".center(22,"="))
    print("Email tidak valid!")
    print("Email tidak boleh mengandung char spasi")
    exit()

if email.startswith("@") or email.startswith(".") or email.endswith("@") or email.endswith("."):
    print("\n" + "Peringatan".center(20,"="))
    print("Email tidak valid!")
    print("Email tidak boleh dimulai atau diakhiri dengan char '@' dan '.'")
    exit()

# Validasi usia

try:
    int(usia)
except ValueError:
    print("\n" + "Peringatan".center(20,"="))
    print("Usia tidak valid!")
    print("Usia harus angka!")
    exit()

usia = int(usia)

if usia < 13:
    print("\n" + "Peringatan".center(20,"="))
    print("Usia tidak valid!")
    print("Usia minimal 13 tahun")
    exit()

# Validasi kata sandi

if len(kata_Sandi) < 6:
    print("\n" + "Peringatan".center(20,"="))
    print("Kata sandi tidak valid!")
    print("Kata sandi minimal 6 karakter")
    exit()

if kata_Sandi.isalpha() or kata_Sandi.isdecimal():
    print("\n" + "Peringatan".center(20,"="))
    print("Kata sandi tidak valid!")
    print("Kata sandi harus terdiri dari huruf dan angka")
    exit()

import random

id_User = f"USR{nama.upper()[0]}{random.randrange(000,999)}"

print("\n" + "AKUN ANDA".center(22,"="))
print("Nama =", nama)
print("Email =", email)
print("Usia =", usia)
print("ID =", id_User)