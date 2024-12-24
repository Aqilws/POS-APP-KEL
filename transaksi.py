from prettytable import PrettyTable

class MenuItem:
    def __init__(self, id, nama, harga):
        self.id = id
        self.nama = nama
        self.harga = harga

class Makanan(MenuItem):
    def __init__(self, id, nama, harga):
        super().__init__(id, nama, harga)

class Minuman(MenuItem):
    def __init__(self, id, nama, harga):
        super().__init__(id, nama, harga)

class Pesanan:
    def __init__(self):
        self.items = []

    def tambah_item(self, menu_item, jumlah):
        self.items.append({"nama": menu_item.nama, "harga": menu_item.harga, "jumlah": jumlah})

    def tampilkan(self):
        if not self.items:
            print("Belum ada pesanan.")
            return

        table = PrettyTable()
        table.field_names = ["Nama Makanan", "Harga Satuan", "Jumlah", "Subtotal"]
        total = 0
        for item in self.items:
            subtotal = item["harga"] * item["jumlah"]
            total += subtotal
            table.add_row([item["nama"], f"Rp{item['harga']:,}", item["jumlah"], f"Rp{subtotal:,}"])
        print(table)
        print(f"Total Harga: Rp{total:,}")

menu = [
    Makanan(1, "Nasi Goreng", 20000),
    Makanan(2, "Mie Goreng", 18000),
    Minuman(3, "Sate Ayam", 25000),
    Minuman(4, "Es Teh", 5000),
    Minuman(5, "Es Jeruk", 7000),
]

pesanan = Pesanan()

def tampilkan_menu():
    """Menampilkan daftar menu."""
    table = PrettyTable()
    table.field_names = ["ID", "Nama Makanan", "Harga"]
    for item in menu:
        table.add_row([item.id, item.nama, f"Rp{item.harga:,}"])
    print(table)

def tambah_pesanan():
    """Menambahkan item ke dalam pesanan."""
    try:
        id_menu = int(input("Masukkan ID menu yang ingin dipesan: "))
        jumlah = int(input("Masukkan jumlah: "))
        item = next((m for m in menu if m.id == id_menu), None)
        if item:
            pesanan.tambah_item(item, jumlah)
            print(f"{item.nama} sebanyak {jumlah} berhasil ditambahkan ke pesanan.")
        else:
            print("ID menu tidak ditemukan.")
    except ValueError:
        print("Input tidak valid. Silakan masukkan angka.")

def tampilkan_pesanan():
    """Menampilkan daftar pesanan."""
    pesanan.tampilkan()

def transaksi_menu():
    """Menu Transaksi."""
    while True:
        print("\n=== Menu Transaksi ===")
        print("Daftar Menu:")
        tampilkan_menu() 

        print("\n[1] Tambah Pesanan")
        print("[2] Tampilkan Pesanan")
        print("[0] Kembali ke Menu Utama")
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            tambah_pesanan()
        elif pilihan == "2":
            tampilkan_pesanan()
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")
        input("\nTekan Enter untuk melanjutkan...")
