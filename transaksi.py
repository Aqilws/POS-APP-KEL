from prettytable import PrettyTable
from api import get_produk_data, simpan_transaksi, get_all_transaksi, simpan_pesanan_item, get_pesanan_items
from datetime import datetime
from abc import ABC, abstractmethod

# Base class untuk item
class BaseItem(ABC):
    def __init__(self, id, nama_produk, harga):
        self.id = id
        self.nama_produk = nama_produk
        self.harga = harga
    
    @abstractmethod
    def get_harga(self):
        pass
    
    def format_harga(self, nilai):
        return f"Rp{nilai:,}"

# MenuItem mewarisi BaseItem
class MenuItem(BaseItem):
    def __init__(self, id, nama_produk, harga, diskon, harga_diskon):
        super().__init__(id, nama_produk, harga)
        self.diskon = diskon
        self.harga_diskon = harga_diskon
    
    def get_harga(self):
        return self.harga_diskon

# Base class untuk tampilan
class BaseTampilan(ABC):
    def __init__(self):
        self.table = PrettyTable()
    
    @abstractmethod
    def tampilkan(self):
        pass

# Class untuk menampilkan menu
class TampilanMenu(BaseTampilan):
    def __init__(self):
        super().__init__()
        self.table.field_names = ["ID", "Nama Produk", "Harga", "Diskon", "Harga Diskon"]
    
    def tambah_item(self, item):
        self.table.add_row([
            item.id,
            item.nama_produk,
            f"Rp{item.harga:,}",
            item.diskon,
            f"Rp{item.harga_diskon:,}"
        ])
    
    def tampilkan(self):
        print(self.table)

# Class untuk menampilkan pesanan
class TampilanPesanan(BaseTampilan):
    def __init__(self):
        super().__init__()
        self.table.field_names = ["Nama Produk", "Harga Satuan", "Jumlah", "Subtotal"]
    
    def tambah_item(self, item, jumlah, subtotal):
        self.table.add_row([
            item["nama_produk"],
            f"Rp{item['harga']:,}",
            jumlah,
            f"Rp{subtotal:,}"
        ])
    
    def tampilkan(self):
        print(self.table)

# Base class untuk pembayaran
class Pembayaran(ABC):
    @abstractmethod
    def proses(self, total):
        pass
    
    @abstractmethod
    def get_metode(self):
        pass

# Class pembayaran tunai
class PembayaranTunai(Pembayaran):
    def proses(self, total):
        return {"status": "success", "total": total}
    
    def get_metode(self):
        return "tunai"

# Class pembayaran non tunai
class PembayaranNonTunai(Pembayaran):
    def proses(self, total):
        return {"status": "success", "total": total}
    
    def get_metode(self):
        return "non tunai"

class Pesanan:
    def __init__(self):
        self.items = []
        self._tampilan = TampilanPesanan()

    def tambah_item(self, menu_item, jumlah):
        self.items.append({"nama_produk": menu_item.nama_produk, "harga": menu_item.harga, "jumlah": jumlah})

    def tampilkan(self):
        if not self.items:
            print("Belum ada pesanan.")
            return

        total = 0
        for item in self.items:
            subtotal = item["harga"] * item["jumlah"]
            total += subtotal
            self._tampilan.tambah_item(item, item["jumlah"], subtotal)
        
        self._tampilan.tampilkan()
        print(f"Total Harga: Rp{total:,}")

# Fungsi-fungsi tetap sama namun menggunakan class-class baru
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

def tampilkan_menu():
    menu = get_menu_from_api()
    tampilan = TampilanMenu()
    for item in menu:
        tampilan.tambah_item(item)
    tampilan.tampilkan()

# Inisialisasi pesanan global
pesanan = Pesanan()

# Fungsi-fungsi lainnya tetap sama
def tambah_pesanan():
    try:
        menu = get_menu_from_api()
        id_menu = input("Masukkan ID menu yang ingin dipesan: ")
        jumlah = int(input("Masukkan jumlah: "))
        item = next((m for m in menu if m.id == id_menu), None)
        if item:
            pesanan.tambah_item(item, jumlah)
            print(f"{item.nama_produk} sebanyak {jumlah} berhasil ditambahkan ke pesanan.")
        else:
            print("ID menu tidak ditemukan.")
    except ValueError:
        print("Input tidak valid. Silakan masukkan angka.")

def menu_pembayaran(logged_in_user):
    print("\n=== Menu Pembayaran ===")
    print("[1] Pembayaran Tunai")
    print("[2] Pembayaran Non Tunai")
    pilihan = input("Pilih metode pembayaran: ")
    
    if pilihan not in ["1", "2"]:
        print("Pilihan tidak valid.")
        return
    
    # Gunakan polymorphism untuk pembayaran
    pembayaran = PembayaranTunai() if pilihan == "1" else PembayaranNonTunai()
    
    total_qty = sum(item["jumlah"] for item in pesanan.items)
    total_value = sum(item["harga"] * item["jumlah"] for item in pesanan.items)
    
    # Proses pembayaran
    hasil_pembayaran = pembayaran.proses(total_value)
    
    if hasil_pembayaran["status"] == "success":
        items_dict = {}
        for item in pesanan.items:
            produk_list = get_produk_data()
            product = next((p for p in produk_list if p["nama"] == item["nama_produk"]), None)
            if product:
                items_dict[str(product["id"])] = item["jumlah"]
        
        transaksi_data = {
            "date": datetime.now().strftime("%d/%m/%y"),
            "kasir": logged_in_user,
            "items": items_dict,
            "total_qty": total_qty,
            "total_value": total_value,
            "pay": pembayaran.get_metode()
        }
        
        print("\n=== Struk Pembelian ===")
        pesanan.tampilkan()
        print(f"Total Pembayaran: Rp{total_value:,}")
        
        response = simpan_transaksi(transaksi_data)
        print(response["message"])
        
        pesanan.items = []

# Fungsi-fungsi lainnya tetap sama seperti sebelumnya
def tampilkan_pesanan_edit():
    pesanan.tampilkan()

def tampilkan_pesanan():
    pesanan.tampilkan()
    print("\n[1] Hapus Barang")
    print("[2] Kurangi Jumlah Barang")
    print("[0] Kembali")
    pilihan = input("Pilih opsi: ")
    
    if pilihan == "1":
        hapus_barang()
    elif pilihan == "2":
        kurangi_barang()
    elif pilihan == "0":
        return
    else:
        print("Pilihan tidak valid.")

def hapus_barang():
    tampilkan_pesanan_edit()
    try:
        index = int(input("Masukkan nomor barang yang ingin dihapus: ")) - 1
        if 0 <= index < len(pesanan.items):
            removed_item = pesanan.items.pop(index)
            print(f"{removed_item['nama_produk']} berhasil dihapus dari pesanan.")
        else:
            print("Nomor barang tidak valid.")
    except ValueError:
        print("Input tidak valid. Silakan masukkan angka.")

def kurangi_barang():
    tampilkan_pesanan_edit()
    try:
        index = int(input("Masukkan nomor barang yang ingin dikurangi: ")) - 1
        if 0 <= index < len(pesanan.items):
            jumlah_sekarang = pesanan.items[index]["jumlah"]
            jumlah_baru = int(input(f"Masukkan jumlah baru (sekarang: {jumlah_sekarang}): "))
            if 0 < jumlah_baru < jumlah_sekarang:
                pesanan.items[index]["jumlah"] = jumlah_baru
                print(f"Jumlah {pesanan.items[index]['nama_produk']} berhasil diperbarui menjadi {jumlah_baru}.")
            elif jumlah_baru == 0:
                hapus_barang()
            else:
                print("Jumlah baru tidak valid.")
        else:
            print("Nomor barang tidak valid.")
    except ValueError:
        print("Input tidak valid. Silakan masukkan angka.")

def cari_barang():
    menu = get_menu_from_api()
    nama_cari = input("Masukkan nama produk yang ingin dicari: ").lower()
    hasil_cari = [item for item in menu if nama_cari in item.nama_produk.lower()]
    
    if hasil_cari:
        tampilan = TampilanMenu()
        for item in hasil_cari:
            tampilan.tambah_item(item)
        tampilan.tampilkan()
    else:
        print("Produk tidak ditemukan.")

def tampilkan_transaksi():
    transaksi = get_all_transaksi()
    if not transaksi:
        print("Belum ada transaksi.")
        return

    table = PrettyTable()
    table.field_names = ["No", "Tanggal", "Kasir", "Items", "Total", "Metode Pembayaran"]
    
    for index, (trs_id, item) in enumerate(transaksi.items(), start=1):
        items_list = []
        for prod_id, qty in item["items"].items():
            produk_list = get_produk_data()
            produk = next((p for p in produk_list if str(p["id"]) == prod_id), None)
            if produk:
                items_list.append(f"{produk['nama']} (x{qty})")
        
        items_str = ", ".join(items_list)
        
        table.add_row([
            index,
            item["date"],
            item["kasir"],
            items_str,
            f"Rp{item['total_value']:,}",
            item["pay"]
        ])
    print(table)

def transaksi_menu(logged_in_user):
    while True:
        print("\n=== Menu Transaksi ===")
        print("Daftar Menu:")
        tampilkan_menu()
        
        print("\n[1] Tambah Pesanan")
        print("[2] Tampilkan Pesanan")
        print("[3] Cari Barang")
        print("[4] Menu Pembayaran")
        print("[5] Lihat Transaksi")
        print("[0] Kembali ke Menu Utama")
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            tambah_pesanan()
        elif pilihan == "2":
            tampilkan_pesanan()
        elif pilihan == "3":
            cari_barang()
        elif pilihan == "4":
            menu_pembayaran(logged_in_user)
        elif pilihan == "5":
            tampilkan_transaksi()
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")
        input("\nTekan Enter untuk melanjutkan...")
