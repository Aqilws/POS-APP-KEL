from prettytable import PrettyTable

# Daftar pesanan sementara (dapat diubah untuk menggunakan database atau API)
pesanan = []

# Contoh daftar menu (biasanya diambil dari API)
menu = [
    {"id": 1, "nama": "Nasi Goreng", "harga": 20000},
    {"id": 2, "nama": "Mie Goreng", "harga": 18000},
    {"id": 3, "nama": "Sate Ayam", "harga": 25000},
    {"id": 4, "nama": "Es Teh", "harga": 5000},
    {"id": 5, "nama": "Es Jeruk", "harga": 7000},
]

def tampilkan_menu():
    """Menampilkan daftar menu."""
    table = PrettyTable()
    table.field_names = ["ID", "Nama Makanan", "Harga"]
    for item in menu:
        table.add_row([item["id"], item["nama"], f"Rp{item['harga']:,}"])
    print(table)

def tambah_pesanan():
    """Menambahkan item ke dalam pesanan."""
    try:
        id_menu = int(input("Masukkan ID menu yang ingin dipesan: "))
        jumlah = int(input("Masukkan jumlah: "))
        item = next((m for m in menu if m["id"] == id_menu), None)
        if item:
            pesanan.append({"nama": item["nama"], "harga": item["harga"], "jumlah": jumlah})
            print(f"{item['nama']} sebanyak {jumlah} berhasil ditambahkan ke pesanan.")
        else:
            print("ID menu tidak ditemukan.")
    except ValueError:
        print("Input tidak valid. Silakan masukkan angka.")

def tampilkan_pesanan():
    """Menampilkan daftar pesanan."""
    if not pesanan:
        print("Belum ada pesanan.")
        return

    table = PrettyTable()
    table.field_names = ["Nama Makanan", "Harga Satuan", "Jumlah", "Subtotal"]
    total = 0
    for item in pesanan:
        subtotal = item["harga"] * item["jumlah"]
        total += subtotal
        table.add_row([item["nama"], f"Rp{item['harga']:,}", item["jumlah"], f"Rp{subtotal:,}"])
    print(table)
    print(f"Total Harga: Rp{total:,}")

def transaksi_menu():
    """Menu Transaksi."""
    while True:
        print("\n=== Menu Transaksi ===")
        print("Daftar Menu:")
        tampilkan_menu()  # Menampilkan menu secara langsung
        
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
