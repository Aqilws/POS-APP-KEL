from prettytable import PrettyTable
from api import get_produk_data, simpan_transaksi, get_all_transaksi, simpan_pesanan_item, get_pesanan_items
from datetime import datetime

class MenuItem:
    def __init__(self, id, nama_produk, harga, diskon, harga_diskon):
        self.id = id
        self.nama_produk = nama_produk
        self.harga = harga
        self.diskon = diskon
        self.harga_diskon = harga_diskon


class Pesanan:
    def __init__(self):
        self.items = []

    def tambah_item(self, menu_item, jumlah):
        self.items.append({"nama_produk": menu_item.nama_produk, "harga": menu_item.harga, "jumlah": jumlah})

    def tampilkan(self):
        if not self.items:
            print("Belum ada pesanan.")
            return

        table = PrettyTable()
        table.field_names = ["Nama Produk", "Harga Satuan", "Jumlah", "Subtotal"]
        total = 0
        for item in self.items:
            subtotal = item["harga"] * item["jumlah"]
            total += subtotal
            table.add_row([item["nama_produk"], f"Rp{item['harga']:,}", item["jumlah"], f"Rp{subtotal:,}"])
        print(table)
        print(f"Total Harga: Rp{total:,}")

pesanan = Pesanan()

def get_menu_from_api():
    produk_list = get_produk_data()  # Menggunakan fungsi internal alih-alih endpoint Flask
    menu_items = []
    for p in produk_list:
        # Hitung harga diskon (contoh: diskon 20% untuk semua item)
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
    """Menampilkan daftar menu."""
    menu = get_menu_from_api()  # Dapatkan menu terbaru dari API
    table = PrettyTable()
    table.field_names = ["ID", "Nama Produk", "Harga", "Diskon", "Harga Diskon"]
    for item in menu:
        table.add_row([item.id, item.nama_produk, f"Rp{item.harga:,}", item.diskon, f"Rp{item.harga_diskon:,}"])
    print(table)

def tambah_pesanan():
    """Menambahkan item ke dalam pesanan."""
    try:
        menu = get_menu_from_api()  # Dapatkan menu terbaru dari API
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

def hapus_barang():
    """Menghapus barang dari pesanan."""
    tampilkan_pesanan_edit()  # Tampilkan pesanan saat ini
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
    """Mengurangi jumlah barang dalam pesanan."""
    tampilkan_pesanan_edit()  # Tampilkan pesanan saat ini
    try:
        index = int(input("Masukkan nomor barang yang ingin dikurangi: ")) - 1
        if 0 <= index < len(pesanan.items):
            jumlah_sekarang = pesanan.items[index]["jumlah"]
            jumlah_baru = int(input(f"Masukkan jumlah baru (sekarang: {jumlah_sekarang}): "))
            if 0 < jumlah_baru < jumlah_sekarang:
                pesanan.items[index]["jumlah"] = jumlah_baru
                print(f"Jumlah {pesanan.items[index]['nama_produk']} berhasil diperbarui menjadi {jumlah_baru}.")
            elif jumlah_baru == 0:
                hapus_barang()  # Jika jumlah baru 0, panggil hapus_barang
            else:
                print("Jumlah baru tidak valid.")
        else:
            print("Nomor barang tidak valid.")
    except ValueError:
        print("Input tidak valid. Silakan masukkan angka.")

def tampilkan_pesanan_edit():
    """Menampilkan daftar pesanan."""
    pesanan.tampilkan()

def tampilkan_pesanan():
    """Menampilkan daftar pesanan."""
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

def cari_barang():
    """Mencari dan menampilkan barang berdasarkan nama."""
    menu = get_menu_from_api()  # Dapatkan menu terbaru dari API
    nama_cari = input("Masukkan nama produk yang ingin dicari: ").lower()
    hasil_cari = [item for item in menu if nama_cari in item.nama_produk.lower()]
    
    if hasil_cari:
        table = PrettyTable()
        table.field_names = ["ID", "Nama Produk", "Harga", "Diskon", "Harga Diskon"]
        for item in hasil_cari:
            table.add_row([item.id, item.nama_produk, f"Rp{item.harga:,}", item.diskon, f"Rp{item.harga_diskon:,}"])
        print(table)
    else:
        print("Produk tidak ditemukan.")

def menu_pembayaran(logged_in_user):
    """Menu Pembayaran."""
    print("\n=== Menu Pembayaran ===")
    print("[1] Pembayaran Tunai")
    print("[2] Pembayaran Non Tunai")
    pilihan = input("Pilih metode pembayaran: ")
    
    if pilihan not in ["1", "2"]:
        print("Pilihan tidak valid.")
        return
        
    # Hitung total qty dan value
    total_qty = sum(item["jumlah"] for item in pesanan.items)
    total_value = sum(item["harga"] * item["jumlah"] for item in pesanan.items)
    
    # Format items sesuai kebutuhan
    items_dict = {}
    for item in pesanan.items:
        # Dapatkan product_id dari nama produk
        produk_list = get_produk_data()
        product = next((p for p in produk_list if p["nama"] == item["nama_produk"]), None)
        if product:
            items_dict[str(product["id"])] = item["jumlah"]
    
    # Buat data transaksi
    transaksi_data = {
        #note: kil list transaksi tambahin id transaksi ya untuk datanya
        "date": datetime.now().strftime("%d/%m/%y"),
        "kasir": logged_in_user,
        "items": items_dict,  # Menggunakan format dictionary untuk items
        "total_qty": total_qty,
        "total_value": total_value,
        "pay": "tunai" if pilihan == "1" else "non tunai"
    }
    
    # Tampilkan struk pembelian
    print("\n=== Struk Pembelian ===")
    pesanan.tampilkan()
    print(f"Total Pembayaran: Rp{total_value:,}")
    
    # Simpan transaksi
    response = simpan_transaksi(transaksi_data)
    print(response["message"])
    
    # Reset pesanan setelah pembayaran
    pesanan.items = []

def tampilkan_transaksi():
    """Menampilkan daftar transaksi."""
    transaksi = get_all_transaksi()  # Ambil semua transaksi dari api.py
    if not transaksi:
        print("Belum ada transaksi.")
        return

    table = PrettyTable()
    table.field_names = ["No", "Tanggal", "Kasir", "Items", "Total", "Metode Pembayaran"]
    
    for index, (trs_id, item) in enumerate(transaksi.items(), start=1):
        # Format items untuk ditampilkan
        items_list = []
        for prod_id, qty in item["items"].items():
            # Dapatkan informasi produk dari ID
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
    """Menu Transaksi."""
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


