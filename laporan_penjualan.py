from prettytable import PrettyTable
import os

"""
tugas
1. selesaikan metode edit
    --- prosess buatkan metode untuk menambahkan barang pada laporan transaksi
2. benerin bug untuk total value harus menyesuaikan ketika ada perubahan qty
3. 
4. 
6. 
"""

class Laporan_Penjualan:
    """
    Kelas untuk mengelola laporan penjualan,
    
    cara menggunakannya. panggil metode .menu() untuk menampilkan menu utama dari Laporan Penjualan
    """

    def __init__(self):
        self.product_id = str
        self.transaction_id = str
        self.products = {
            # Format ID product: Nama barang, Harga Normal, Diskon, Harga setelah diskon
            "71253001": ["Koper Lojel Lineo Salmon S", 500000, "50%", 250000],
            "71253002": ["Koper Lojel Lineo Salmon M", 750000, "40%", 450000],
            "71253003": ["Koper Lojel Lineo Salmon L", 1000000, "30%", 700000],
            "71254001": ["Tas Selempang Eiger 18L", 300000, "20%", 240000],
            "71254002": ["Tas Backpack Eiger 25L", 400000, "15%", 340000],
            "72251001": ["Sepatu Nike Running Air Zoom", 1200000, "30%", 840000],
            "72251002": ["Sepatu Nike Basketball Lebron 19", 2000000, "20%", 1600000],
            "72251003": ["Sepatu Nike Casual Air Force 1", 1100000, "25%", 825000],
            "73252001": ["Jaket Adidas Essentials", 600000, "20%", 480000],
            "73252002": ["Jaket Adidas Performance", 750000, "25%", 562500],
            "73252003": ["Jaket Adidas Climaproof", 850000, "30%", 595000],
            "74255001": ["Kemeja Formal Levi's", 500000, "15%", 425000],
            "74255002": ["Jeans Slim Fit Levi's 501", 900000, "20%", 720000],
            "74255003": ["Jaket Denim Levi's Original", 1000000, "25%", 750000],
            "75256001": ["Jam Tangan Casio G-Shock GA-2100", 1500000, "10%", 1350000],
            "75256002": ["Jam Tangan Casio Vintage Gold", 700000, "20%", 560000],
            "76257001": ["Parfum Chanel Bleu de Chanel 100ml", 2000000, "15%", 1700000],
            "76257002": ["Parfum Chanel Coco Mademoiselle 50ml", 1800000, "10%", 1620000],
            "77258001": ["Handuk Terry Palmer Bath Towel", 150000, "30%", 105000],
            "77258002": ["Handuk Terry Palmer Face Towel", 75000, "25%", 56250],
            "78259001": ["Bantal Dakron King Size", 120000, "20%", 96000],
            "78259002": ["Guling Dakron Medium", 100000, "15%", 85000],
            "79260001": ["Panci Supra Chef's Pan 24cm", 300000, "20%", 240000],
            "79260002": ["Wajan Supra Teflon 28cm", 250000, "15%", 212500],
            "80261001": ["Kamera Canon EOS M50 Kit 15-45mm", 8000000, "10%", 7200000],
            "80261002": ["Kamera Sony Alpha a6400", 12000000, "15%", 10200000],
            "81262001": ["TV LED Samsung 43 Inch 4K UHD", 6000000, "20%", 4800000],
            "81262002": ["TV LED LG 55 Inch OLED", 15000000, "15%", 12750000],
            "82263001": ["Laptop ASUS VivoBook 14", 7500000, "10%", 6750000],
            "82263002": ["Laptop Lenovo IdeaPad 3", 8500000, "15%", 7225000],
        }
        self.transactions = {
            # note tambahkan metode pembayaran
            '1': {'date': '01/12/24',
                'kasir': 'andris',
                'items': {'79260002': 1, '82263001': 1, '78259002': 3},
                'total_qty': 5,
                'total_value': 7312500,
                'pay' : 'tunai'},
            '2': {'date': '15/12/24',
                'kasir': 'tomo',
                'items': {'82263002': 2, '80261002': 3, '73252002': 2, '79260002': 2},
                'total_qty': 9,
                'total_value': 46600000,
                'pay' : 'tunai'},
            '3': {'date': '19/12/24',
                'kasir': 'tomo',
                'items': {'82263002': 2, '76257001': 2, '71254001': 2},
                'total_qty': 6,
                'total_value': 18330000,
                'pay' : 'tunai'},
            '4': {'date': '20/12/24',
                'kasir': 'aqil',
                'items': {'75256001': 1, '71253003': 2, '76257001': 1, '77258002': 3, '71254001': 2},
                'total_qty': 9,
                'total_value': 5098750,
                'pay' : 'tunai'},
            '5': {'date': '21/12/24',
                'kasir': 'aqil',
                'items': {'72251003': 2},
                'total_qty': 2,
                'total_value': 1650000,
                'pay' : 'tunai'},
            '6': {'date': '28/12/24',
                'kasir': 'aqil',
                'items': {'82263002': 3, '76257001': 1, '80261001': 3, '81262001': 3, '80261002': 2},
                'total_qty': 12,
                'total_value': 79775000,
                'pay' : 'tunai'},
        }
    
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
        while True:
            print("0 -> Batal")
            qeury = input("Cari Produk: ").lower()

            # Cari berdasarkan ID
            for product_id, value in self.products.items():
                if qeury in product_id or qeury in value[0].lower():
                    results.append(product_id)
            
            if results == []:
                input("Produk Tidak ditemukan...")
                self.clear_screen()
            else:
                return results

            # lagi membuat fitur tambah barang, baru selesai validasi barang yang dicari ada atau tidak, tugas selanjutnya uji coba sampai berhasil

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

        new_item = self.search_product()
        
        if new_item == []:
            pass


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