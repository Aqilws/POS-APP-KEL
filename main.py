import os
from transaksi import transaksi_menu
from stok_barang import produk
from laporan_penjualan import Laporan_Penjualan
from karyawan_profile import karyawanMain
from login import login, logout

def clear_screen():
    """Menghapus tampilan terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    print("Daftar Menu Utama")
    print("[1] Transaksi")
    print("[2] Produk/Barang")
    print("[3] Laporan Penjualan")
    print("[4] Profile")

    print("[0] Keluar")

def main():
    while True:
        clear_screen()
        logged_in_user = login()
        
        if logged_in_user is None:
            print("Login gagal. Program berhenti.")
            break
            
        while True:
            clear_screen()
            print(f"Selamat datang, {logged_in_user}!")
            show_menu()
            pilihan = input("\nPilih menu: ")
            
            if pilihan == "1":
                clear_screen()
                transaksi_menu(logged_in_user)
            elif pilihan == "2":
                clear_screen()
                produk()
            elif pilihan == "3":
                clear_screen()
                Laporan_Penjualan().menu()
            elif pilihan == "4":
                clear_screen()
                karyawanMain(logged_in_user)
            elif pilihan == "0":
                clear_screen()
                logout()
                break  
            else:
                print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
