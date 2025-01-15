from api import  get_karyawan_data
from login import login, logout
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_profile(username):
    karyawan = next((k for k in get_karyawan_data() if k["Username"] == username), None)
    if karyawan:
        print("\n=== Profil Karyawan ===")
        print(f"Nama Karyawan : {karyawan['Nama_Karyawan']}")
        print(f"Tanggal Lahir : {karyawan['Tanggal_Lahir']}")
        print(f"Posisi Jabatan: {karyawan['Posisi_Jabatan']}")
        print(f"Username      : {karyawan['Username']}")
    else:
        print("\nData karyawan tidak ditemukan!")

def karyawanMain(username):
    while True:
        print("\n=== Menu Karyawan ===")
        print("1. Lihat Profil")
        print("2. Ubah Akun")
        print("0. Keluar")
        sub_pilihan = input("Pilih menu: ")

        if sub_pilihan == "1":
            clear_screen()
            show_profile(username)
        elif sub_pilihan == "2":
            clear_screen()
            logout()
            break  
        elif sub_pilihan == "0":
            clear_screen()
            print("\nLogout berhasil!")
            break
        else:
            print("\nPilihan tidak valid!")