import os
from transaksi import transaksi_menu
from produk_barang import produk_barang_menu
from stok_barang import stok_barang_menu
from laporan_penjualan import Laporan_Penjualan

def clear_screen():
    """Menghapus tampilan terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    print("Daftar Menu Utama")
    print("[1] Transaksi")
    print("[2] Produk/Barang")
    print("[3] Stok Barang")
    print("[4] Laporan Penjualan")
    print("[0] Keluar")

def main():
    while True:
        clear_screen()
        show_menu()
        pilihan = input("\nPilih menu: ")
        
        if pilihan == "1":
            clear_screen()
            transaksi_menu()
        elif pilihan == "2":
            clear_screen()
            produk_barang_menu()
        elif pilihan == "3":
            clear_screen()
            stok_barang_menu()
        elif pilihan == "4":
            clear_screen()
            lp.view()
            lp.select()
        elif pilihan == "0":
            clear_screen()
            print("Keluar dari aplikasi. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
    lp = Laporan_Penjualan()
