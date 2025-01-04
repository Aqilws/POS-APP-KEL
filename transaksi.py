from prettytable import PrettyTable
from api import simpan_transaksi, get_all_transaksi

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

menu = [
    MenuItem("71253001", "Koper Lojel Lineo Salmon S", 500000, "50%", 250000),
    MenuItem("71253002", "Koper Lojel Lineo Salmon M", 750000, "40%", 450000),
    MenuItem("71253003", "Koper Lojel Lineo Salmon L", 1000000, "30%", 700000),
    MenuItem("71254001", "Tas Selempang Eiger 18L", 300000, "20%", 240000),
    MenuItem("71254002", "Tas Backpack Eiger 25L", 400000, "15%", 340000),
    MenuItem("72251001", "Sepatu Nike Running Air Zoom", 1200000, "30%", 840000),
    MenuItem("72251002", "Sepatu Nike Basketball Lebron 19", 2000000, "20%", 1600000),
    MenuItem("72251003", "Sepatu Nike Casual Air Force 1", 1100000, "25%", 825000),
    MenuItem("73252001", "Jaket Adidas Essentials", 600000, "20%", 480000),
    MenuItem("73252002", "Jaket Adidas Performance", 750000, "25%", 562500),
    MenuItem("73252003", "Jaket Adidas Climaproof", 850000, "30%", 595000),
    MenuItem("74255001", "Kemeja Formal Levi's", 500000, "15%", 425000),
    MenuItem("74255002", "Jeans Slim Fit Levi's 501", 900000, "20%", 720000),
    MenuItem("74255003", "Jaket Denim Levi's Original", 1000000, "25%", 750000),
    MenuItem("75256001", "Jam Tangan Casio G-Shock GA-2100", 1500000, "10%", 1350000),
    MenuItem("75256002", "Jam Tangan Casio Vintage Gold", 700000, "20%", 560000),
    MenuItem("76257001", "Parfum Chanel Bleu de Chanel 100ml", 2000000, "15%", 1700000),
    MenuItem("76257002", "Parfum Chanel Coco Mademoiselle 50ml", 1800000, "10%", 1620000),
    MenuItem("77258001", "Handuk Terry Palmer Bath Towel", 150000, "30%", 105000),
    MenuItem("77258002", "Handuk Terry Palmer Face Towel", 75000, "25%", 56250),
    MenuItem("78259001", "Bantal Dakron King Size", 120000, "20%", 96000),
    MenuItem("78259002", "Guling Dakron Medium", 100000, "15%", 85000),
    MenuItem("79260001", "Panci Supra Chef's Pan 24cm", 300000, "20%", 240000),
    MenuItem("79260002", "Wajan Supra Teflon 28cm", 250000, "15%", 212500),
    MenuItem("80261001", "Kamera Canon EOS M50 Kit 15-45mm", 8000000, "10%", 7200000),
    MenuItem("80261002", "Kamera Sony Alpha a6400", 12000000, "15%", 10200000),
    MenuItem("81262001", "TV LED Samsung 43 Inch 4K UHD", 6000000, "20%", 4800000),
    MenuItem("81262002", "TV LED LG 55 Inch OLED", 15000000, "15%", 12750000),
    MenuItem("82263001", "Laptop ASUS VivoBook 14", 7500000, "10%", 6750000),
    MenuItem("82263002", "Laptop Lenovo IdeaPad 3", 8500000, "15%", 7225000),
]

pesanan = Pesanan()

def tampilkan_menu():
    """Menampilkan daftar menu."""
    table = PrettyTable()
    table.field_names = ["ID", "Nama Produk", "Harga", "Diskon", "Harga Diskon"]
    for item in menu:
        table.add_row([item.id, item.nama_produk, f"Rp{item.harga:,}", item.diskon, f"Rp{item.harga_diskon:,}"])
    print(table)

def tambah_pesanan():
    """Menambahkan item ke dalam pesanan."""
    try:
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

def menu_pembayaran():
    """Menu Pembayaran."""
    print("\n=== Menu Pembayaran ===")
    print("[1] Pembayaran Tunai")
    print("[2] Pembayaran Non Tunai")
    pilihan = input("Pilih metode pembayaran: ")
    
    total = sum(item["harga"] * item["jumlah"] for item in pesanan.items)
    
    if pilihan == "1":
        print("Pembayaran tunai dipilih.")
    elif pilihan == "2":
        print("Pembayaran non tunai dipilih.")
    else:
        print("Pilihan tidak valid.")
        return

    # Menampilkan struk pembelian
    print("\n=== Struk Pembelian ===")
    pesanan.tampilkan()
    print(f"Total Pembayaran: Rp{total:,}")

    # Simpan transaksi
    transaksi_data = {
        "items": pesanan.items,
        "total": total,
        "metode_pembayaran": pilihan
    }
    response = simpan_transaksi(transaksi_data)  # Panggil fungsi untuk menyimpan transaksi
    print(response["message"])  # Tampilkan pesan sukses

def tampilkan_transaksi():
    """Menampilkan daftar transaksi."""
    transaksi = get_all_transaksi()  # Ambil semua transaksi dari api.py
    if not transaksi:
        print("Belum ada transaksi.")
        return

    table = PrettyTable()
    table.field_names = ["No", "Items", "Total", "Metode Pembayaran"]
    for index, item in enumerate(transaksi, start=1):
        items = ", ".join([f"{i['nama_produk']} (x{i['jumlah']})" for i in item["items"]])
        table.add_row([index, items, f"Rp{item['total']:,}", item["metode_pembayaran"]])
    print(table)

def transaksi_menu():
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
            menu_pembayaran()
        elif pilihan == "5":
            tampilkan_transaksi()
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")
        input("\nTekan Enter untuk melanjutkan...")


