# def stok_barang_menu():
#     print("\n=== Menu Stok Barang ===")
#     # Tambahkan logika stok barang di sini
#     print("Fitur Stok Barang masih dalam pengembangan.")

# from prettytable import PrettyTable

# class Barang:
#     def __init__(self, nama, harga, stok):
#         self.nama = nama
#         self.harga = harga
#         self.stok = stok

#     def tampilkan_info(self):
#         return f"Nama: {self.nama}, Harga: {self.harga}, Stok: {self.stok}"

# class BarangElektronik(Barang):
#     def __init__(self, nama, harga, stok, garansi):
#         super().__init__(nama, harga, stok)
#         self.garansi = garansi

#     def tampilkan_info(self):
#         return f"{super().tampilkan_info()}, Garansi: {self.garansi} tahun"

# class BarangPakaian(Barang):
#     def __init__(self, nama, harga, stok, ukuran):
#         super().__init__(nama, harga, stok)
#         self.ukuran = ukuran

#     def tampilkan_info(self):
#         return f"{super().tampilkan_info()}, Ukuran: {self.ukuran}"

# class Toko:
#     def __init__(self):
#         self.barang_list = []

#     def tambah_barang(self, barang):
#         self.barang_list.append(barang)

#     def tampilkan_barang(self):
#         tabel = PrettyTable()
#         tabel.field_names = ["Nama", "Harga", "Stok", "Tipe"]
#         for barang in self.barang_list:
#             tipe = barang.__class__.__name__
#             tabel.add_row([barang.nama, barang.harga, barang.stok, tipe])
#         print(tabel)

# def main():
#     toko = Toko()
    
#     while True:
#         print("1. Tambah Barang")
#         print("2. Tampilkan Barang")
#         print("3. Keluar")
#         pilihan = input("Pilih opsi: ")

#         if pilihan == '1':
#             nama = input("Masukkan nama barang: ")
#             harga = float(input("Masukkan harga barang: "))
#             stok = int(input("Masukkan stok barang: "))
#             tipe_barang = input("Masukkan tipe barang (elektronik/pakaian): ")

#             if tipe_barang.lower() == 'elektronik':
#                 garansi = int(input("Masukkan masa garansi (tahun): "))
#                 barang = BarangElektronik(nama, harga, stok, garansi)
#             elif tipe_barang.lower() == 'pakaian':
#                 ukuran = input("Masukkan ukuran pakaian: ")
#                 barang = BarangPakaian(nama, harga, stok, ukuran)
#             else:
#                 print("Tipe barang tidak valid.")
#                 continue

#             toko.tambah_barang(barang)
#             print("Barang berhasil ditambahkan.")

#         elif pilihan == '2':
#             toko.tampilkan_barang()

#         elif pilihan == '3':
#             print("Keluar dari aplikasi.")
#             break

#         else:
#             print("Pilihan tidak valid.")

# if __name__ == "__main__":
#     main()

