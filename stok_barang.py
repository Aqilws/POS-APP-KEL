def stok_barang_menu():
    print("\n=== Menu Stok Barang ===")
    print("Fitur Stok Barang masih dalam pengembangan.")

from prettytable import PrettyTable
from api import get_produk_data

class Barang:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def tampilkan_info(self):
        return f"Nama: {self.nama}, Harga: {self.harga}, Stok: {self.stok}"


class MenuItem:
    def __init__(self, id, nama_produk, harga, diskon, harga_diskon):
        self.id = id
        self.nama_produk = nama_produk
        self.harga = harga
        self.diskon = diskon
        self.harga_diskon = harga_diskon

def get_menu_from_api():
    produk_list = get_produk_data()
    menu_items = []
    for p in produk_list:
        diskon_persen = 20
        harga_diskon = p["harga"] * (100 - diskon_persen) // 100
        menu_items.append(MenuItem(
            str(p["id"]),
            p["nama"],
            p["harga"],
            f"{diskon_persen}%",
            harga_diskon
        ))
    return menu_items
class Toko:
    def __init__(self):
        self.barang_list = [
            
        ]
    

    def tambah_barang(self, barang):
        self.barang_list.append(barang)

    

    def tampilkan_barang(self):
        """Menampilkan daftar menu."""
        menu = get_menu_from_api() 
        table = PrettyTable()
        table.field_names = ["ID", "Nama Produk", "Harga", "Diskon", "Harga Diskon"]
        for item in menu:
            table.add_row([item.id, item.nama_produk, f"Rp{item.harga:,}", item.diskon, f"Rp{item.harga_diskon:,}"])
        print(table)

def produk():
    toko = Toko()
    
    while True:
        print("\n=== Menu Manajemen Produk ===")
        print("1. Tambah Barang")
        print("2. Tampilkan Barang")
        print("0. Keluar")
        pilihan = input("Pilih opsi: ")

        if pilihan == '1':
            try:
                nama = input("Masukkan nama barang: ")
                harga = float(input("Masukkan harga barang: "))
                stok = int(input("Masukkan stok barang: "))
                
                from api import produk as api_produk
                new_id = max([p["id"] for p in api_produk]) + 1
                
                new_produk = {
                    "id": new_id,
                    "nama": nama,
                    "harga": harga,
                    "stok": stok
                }
                
                api_produk.append(new_produk)
                
                barang = Barang(nama, harga, stok)
                toko.tambah_barang(barang)
                
                print("Barang berhasil ditambahkan ke sistem.")
                
            except ValueError:
                print("Input tidak valid. Pastikan harga dan stok berupa angka.")
            except Exception as e:
                print(f"Terjadi kesalahan: {str(e)}")

        elif pilihan == '2':
            toko.tampilkan_barang()

        elif pilihan == '0':
            print("Keluar dari aplikasi.")
            break

        else:
            print("Pilihan tidak valid.")
