from prettytable import PrettyTable
import os
from api import get_produk_data, get_all_transaksi

class Laporan_Penjualan:
    """
    Kelas untuk mengelola laporan penjualan,
    
    cara menggunakannya. panggil metode .menu() untuk menampilkan menu utama dari Laporan Penjualan
    """

    def __init__(self):
        self.product_id = str
        self.transaction_id = str
        # Konversi data dari API ke format yang dibutuhkan
        self.products = self._convert_products_from_api()
        self.transactions = self._convert_transactions_from_api()
    
    def _convert_products_from_api(self):
        """Mengkonversi data produk dari API ke format yang dibutuhkan"""
        products_data = {}
        api_products = get_produk_data()
        
        for product in api_products:
            # Hitung diskon (20% untuk semua produk sebagai contoh)
            diskon_persen = 20
            harga_diskon = product["harga"] * (100 - diskon_persen) // 100
            
            products_data[str(product["id"])] = [
                product["nama"],           # Nama barang
                product["harga"],          # Harga Normal
                f"{diskon_persen}%",       # Diskon
                harga_diskon               # Harga setelah diskon
            ]
        
        return products_data
    
    def _convert_transactions_from_api(self):
        """Mengkonversi data transaksi dari API ke format yang dibutuhkan"""
        return get_all_transaksi()
    
    def clear_screen(self):
        """
        metode untuk membersihkan text yang ada pada terminal
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def menu(self, values=[]):
        """
        metode untuk menampilkan menu utama dari class Laporan Penjualan.

        cara menggunakannya,
        jika ingin menampilkan beberapa data laporan tertentu cukup panggil metode ini dengan mengisi parameter values=[] datanya bertipe list.

        jika ingin menampilkan semua datanya cukup panggil metode-nya saja .menu()
        """

        if len(values) > 0 :
            datas = values 
        else:
            datas = self.transactions
        
        tSales = sum(self.transactions[trs_id]["total_value"] for trs_id in datas)
        tQty = sum(self.transactions[trs_id]["total_qty"] for trs_id in datas)

        table = PrettyTable()
        table.title = ("TRANSAKSI")
        table.field_names = ["No", "Tanggal", "ID", "Kasir", "Banyaknya", "Total Bayar", "Metode Pembayaran"]
        table.align["Kasir"] = 'l'
        table.align["Total Value"] = 'r'
        no = 1
        for trs_id in datas:
            table.add_row([
                no, # Nomor urut
                self.transactions[trs_id]["date"], # Tanggal
                trs_id, # Transaction ID
                self.transactions[trs_id]['kasir'], # Kasir
                self.transactions[trs_id]['total_qty'], # qty
                f"{self.transactions[trs_id]['total_value']:,}", # total
                f"{self.transactions[trs_id]['pay']}", # Metode pembayaran
            ])
            no += 1

        self.clear_screen()
        print(f"Total Sales : {tSales:,}")
        print(f"Total Qty   : {tQty:,}")
        print(table)

        self.results = self.search_transaction()
                
        if self.results == '': # Kembali ke menu utama
            return
        
        elif len(self.results) == 1: # Lanjut ke submenu
            self.clear_screen()
            self.transaction_id = self.results[0]
            self.select()
        elif len(self.results) > 1:
            pass

        else :
            self.clear_screen()
            input("Laporan penjualan tidak ditemukan...")

        """
        jika stiap pilihan/aksi selesai dijalankan, maka akan otomatis kembali untuk menampilkan metode .menu()
        """
        if len(self.results) > 1:
            self.clear_screen()
            self.menu(values=self.results)
        else:
            self.menu()
    
    def detail(self):
        """
        metode untuk menampilkan detail dari transaksi dengan id tertentu. untuk data yang ingin ditampikan diambil dari atribut self.transaction_id

        cara meanggunaknnya,
        1. set data yang ingin di tampikan ke atribut self.transaction_id
        2. panggil metodenya .detail()
        """
        
        table = PrettyTable()
        table.title = "DETAIL INFORMASI"
        table.field_names = ["No", "Product ID", "Nama Produk", "Harga Normal", "Diskon", "Harga Jual", "Banyaknya", "Jumlah`"]
        table.align["Nama Produk"] = 'l'
        table.align["Harga Normal"] = 'r'
        table.align["Harga Jual"] = 'r'
        table.align["Sub-Total"] = 'r'
        no = 1
        for prd_id in self.transactions[self.transaction_id]["items"]:
            table.add_row([
                no, # Nomor urut,
                prd_id, # Product ID
                self.products[prd_id][0], # nama produk
                f"{self.products[prd_id][1]:,}", # Harga Normal / Harga normal
                self.products[prd_id][2], # Diskon
                f"{self.products[prd_id][3]:,}", # Harga Jual / harga setelah diskon
                self.transactions[self.transaction_id]["items"][prd_id], # qty
                f"{int(self.products[prd_id][3]) * self.transactions[self.transaction_id]["items"][prd_id]:,}", # total value / uang
            ])
            no += 1
        
        self.clear_screen()
        print(f"\nID Transaksi      : {self.transaction_id}")
        print(f"Tanggal           : {self.transactions[self.transaction_id]["date"]}")
        print(f"Kasir             : {self.transactions[self.transaction_id]["kasir"]}")
        print(f"Banyaknya (pcs)   : {self.transactions[self.transaction_id]["total_qty"]}")
        print(f"Total Bayar (Rp)  : {self.transactions[self.transaction_id]["total_value"]:,}" )
        print(f"Metode Pembayaran : {self.transactions[self.transaction_id]["pay"]}")
        print(table)

    def delete(self):
        """
        metode untuk menghapus transaksi berdasarkan id tertentu. ID di ambil dari atribut self.transaction_id

        cara menggunakannyacara meanggunaknnya,
        1. set data yang ingin di tampikan ke atribut self.transaction_id
        2. panggil metodenya .detail()
        """
        if self.transaction_id in self.transactions:
            while True:
                self.clear_screen()
                self.detail()
                action = input("\nApakah anda yakin ingin menghapus Laporan tersebut? y/t: ").lower()
                if action == "y":
                    self.transactions.pop(self.transaction_id)
                    if not self.transaction_id in self.transactions:
                        self.clear_screen()
                        input("Berhasil. Laporan telah dihapus...")
                    else:
                        self.clear_screen()
                        input("Gagal...")
                    # self.menu()
                    break
                elif action == 't':
                    # self.menu()
                    break
                else:
                    self.clear_screen()
                    input("Harap masukan printah Y atau T")
                    self.clear_screen()

        else:
            input("ID tidak ditemukan....")

    def delete_item(self):
        """
        Metode untuk menghapus item yang ada ditransaksi/laporan penjualan
        """
        if self.transaction_id in self.transactions and self.product_id in self.transactions[self.transaction_id]["items"]:
            action = input("Apakah anda yakin ingin menghapus item tersebut? y/t: ")
            match action:
                case 'y':
                    self.transactions[self.transaction_id]["items"].pop(self.product_id)
                
                case 't':
                    return
                
                case _:
                    self.clear_screen()
                    input("Harap masukan printah Y atau T....")
                    self.clear_screen()
                    self.detail()
                    self.delete_item()

            if not self.product_id in self.transactions[self.transaction_id]["items"]:
                self.clear_screen()
                input("Item berhasi diapus...")
            else:
                self.clear_screen()
                input("Item Gagal diapus...")
        else:
            self.clear_screen()
            input("ID Tidak ditemukan...")
            self.clear_screen()

    def search_transaction(self):
        """
        Metode untuk mencari transaksi berdasarkan ID, Nama Kasir, Tanggal, dan Metode Pembayaran.
        
        cara menggunakanya, cukup panggil metode-nya .search_transaction()
        """

        print("\nCari transaksi")
        print("0 -> Kembali")
        query = input("\nCari: ").lower()
        self.results = []

        if query == '0':
            return ''

        else:                
            # Cari berdasarkan transaction ID
            for trs_id in self.transactions:
                if query == trs_id:
                    self.results.append(trs_id)

            # jika cari dengan ID tidak ditemukan, maka akan dicari dengan mencocokkan nama kasir, metode pembayran, tanggal
            if self.results == []:
                for trs_id in self.transactions:
                    if query in self.transactions[trs_id]["kasir"].lower() or query in self.transactions[trs_id]["pay"].lower() or query in self.transactions[trs_id]["date"]:
                        self.results.append(trs_id)

            return self.results

    def search_product(self):
        """Metode untuk mencari barang/produk yang ada di daftar produk"""
        
        results = []
        print("0 -> Batal\n")
        qeury = input("Cari Produk: ").lower().strip()

        if qeury == '0': return 'batal'
        elif qeury == '': return 'skip'

        # Cari berdasarkan ID
        for product_id, value in self.products.items():
            if qeury in product_id or qeury in value[0].lower():
                results.append(product_id)
            
        return results

    def edit(self):
        """
        Metode untuk merubah data yang ada didalam laporan
        """

        old_data = self.transactions[self.transaction_id]["items"][self.product_id]
        print("\n0 -> Batal")
        print(f"Jumlah sebelumnya : {self.transactions[self.transaction_id]["items"][self.product_id]}")
        
        try:
            new_qty = int(input("Masukan Jumlah yang baru: "))
            if new_qty == '0' or new_qty == '':
                return

            self.transactions[self.transaction_id]["items"][self.product_id] = new_qty
            new_data = self.transactions[self.transaction_id]["items"][self.product_id]

            self.clear_screen()
            if old_data != new_data:
                input("Berhasil diubah...")
            else:
                input("Gagal diubah...")

        except:
            self.clear_screen()
            input("Harap masukan angka...")
            self.clear_screen()
            self.detail()
            self.edit()

    def add_item(self):
        """
        Metode untuk menambahkan item/barang ke Laporan Penjualan
        """

        table = PrettyTable()
        table.title = "Tambah Barang ke laporan Transaksi"
        table.field_names = ["ID Produk", "Nama Produk", "Harga", "Diskon", "Harga Promo"]
        while True:
            print("\nTambah Barang ke Transaksi")
            new_items = self.search_product()
            qty = int
            
            if new_items == 'batal':
                break
            elif new_items == 'skip':
                self.clear_screen()
                continue
            elif new_items == []:
                self.clear_screen()
                input("Produk tidak ditemukan...")
                self.clear_screen()
                continue
            elif len(new_items) > 1:
                for prd_id in new_items:
                    table.add_row([
                        prd_id,
                        self.products[prd_id][0],
                        self.products[prd_id][1],
                        self.products[prd_id][2],
                        self.products[prd_id][3],
                                ])
                
                self.clear_screen()
                print("Produk ditemukan lebih dari 1. Coba cari berdasarkan ID Produknya..\n")
                print(table)
                table.clear_rows()
            elif len(new_items) == 1:
                table.add_row([
                    new_items[0],
                    self.products[new_items[0]][0],
                    self.products[new_items[0]][1],
                    self.products[new_items[0]][2],
                    self.products[new_items[0]][3],
                ])
                self.clear_screen()
                print(table)
                while True:
                    try:
                        print("\n0 -> Batal")
                        qty = int(input("Banyaknya (pcs): "))
                        if qty == 0:
                            return
                        break 
                    except:
                        self.clear_screen()
                        input("Hanya boleh memasukan angka...")
                        self.clear_screen()
                        print(table)

                while True:
                    decision = input("\nTambahkan barang tersebut? y/t: ").lower().strip()
                    if decision == 'y':
                        self.transactions[self.transaction_id]["items"] = {new_items[0]: qty}
                        input(self.transactions[self.transaction_id]["items"][new_items[0]])
                        # baru sampai sini. tugas selanjutnya memastikan bahwa item yang ditambahkan benar
                        break
                    elif decision == 't':
                        break
                
                break
        
    def select(self):
        while True:
            self.detail()
            print("\nMenu Transaksi")
            print("[1] Hapus")
            print("[2] Ubah")
            print("[3] Cari")
            print("[0] Kembali")
            selectd = input("\nPilihan: ")

            match selectd:
                case '0': # Kembali
                    break
                
                case '1': # Hapus Transaksi
                    self.delete()
                    break

                case '2': # Ubah Transaksi
                    while True:
                        self.detail()
                        print("\nUbah Transaksi")
                        print("[1] Ganti jumlah Barang")
                        print("[2] Tambah Barang")
                        print("[3] Hapus Barang")
                        print("[0] Batal")
                        selectd = input("\nMasukan pilihan: ")
                        start = True

                        # Validasi id product
                        if selectd == '1' or selectd == '3':  
                            while True:
                                self.clear_screen()
                                self.detail()
                                print("\nProses Ganti jumlah Barang") if selectd == '1' else print("\nProses Hapus Barang")
                                print("0 -> Batal")
                                self.product_id = input("\nMasukan ID Produk: ")

                                if self.product_id in self.products:
                                    break
                                elif self.product_id == '0':
                                    start = False
                                    break
                                else:
                                    self.clear_screen()
                                    input("ID Product tidak ditemukan...")
                                    self.detail()
                                    # note benerin bug ketika kembali dari input id
                                    
                        if start:
                            match selectd:
                                case '0': # kembali
                                    break
                                
                                case '1': # ubah jumlah
                                    self.edit()
                                
                                case '2': # Tambah Item
                                    self.add_item()

                                case '3': # Hapus Item
                                    self.delete_item()
                                
                                case _:
                                    self.clear_screen()
                                    input("Pilihan tidak ada...")
                                    self.clear_screen()
                
                case '3': # Cari Transaksi lain
                    self.results = self.search_transaction()
                    break

                case _:
                    self.clear_screen()
                    input("Pilihan tidak ada...")
                    self.clear_screen()

# Laporan_Penjualan().menu()