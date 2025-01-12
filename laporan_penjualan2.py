from prettytable import PrettyTable
from api import get_produk, get_all_transaksi
from main import clear_screen

class Laporan_Penjualan:
    def __init__(self):
        self.transaction_id = str
        self.product_id = str
        self.display_data = []                          # untuk menmpung data transaksi yang ingin ditampilkan
        self.all_transactions = get_all_transaksi()     # untuk menmpung semua data transaksi yang ada di api
        
        # Jalankan metode menu
        self.menu()


    def view_transactions(self):
        """Metode untuk menampilkan transaksi"""

        table = PrettyTable()
        table.title = ("TRANSAKSI")
        table.field_names = ["ID", "Tanggal", "Kasir", "Banyaknya", "Total Bayar", "Metode Pembayaran"]
        table.align["Kasir"] = 'l'
        table.align["Total Value"] = 'r'

        # jika data transaksi kosong maka akan menampilkan semua transaksi yang ada di api.py
        if self.display_data == []: self.display_data = self.all_transactions

        for trs_id in self.display_data:
            table.add_row([
                trs_id,                                          # ID Transaksi
                self.display_data[trs_id]['date'],          # Tanggal transaksi
                self.display_data[trs_id]['kasir'],         # Nama Kasir
                self.display_data[trs_id]['total_qty'],     # Total Banyaknya produk (pcs/qty)
                self.display_data[trs_id]['total_value'],   # Total Bayar
                self.display_data[trs_id]['pay'],           # Metode pembayaran
            ])

        print(table)
    
    def search_transaction(self):
        """Metode untuk mencari transaksi"""

        while True:
            print("\nCari Transaksi Berdasarkan ")
            print("ID Transaksi/Nama kasir/Metode Pembayaran\n")
            print("0 -> Batal")
            query = input("Cari Transaksi: ").strip().lower()
            result = [] # untuk menmpung hasil pencarian

            if query == '0': # jika user memasukan angka 0 maka return angka '0' untuk menandakan. batal
                return result
            elif query == '':
                clear_screen()
                input("Input Tidak Boleh kosong...")
                clear_screen()
            else:
                # Cari berdasarkan ID Transaksi
                for trs_id in self.all_transactions:
                    if query == trs_id: result.append({trs_id: self.all_transactions[trs_id]})
                
                # jika dengan id tidak ditemukan maka cari dengan opsi lain (Nama kasir/Tanggal/Metode Pembayaran)
                if result == []:
                    for trs_id in self.all_transactions: 
                        if  (query in self.all_transactions[trs_id]['date'] or          # cari berdasarkan tanggal
                            query in self.all_transactions[trs_id]['kasir'].lower() or  # cari berdasarkan nama kasir
                            query in self.all_transactions[trs_id]['pay'].lower()):     # cari berdasarkan metode pambayaran
                            result.append({trs_id: self.all_transactions[trs_id]})      # simpan hasil pencarian

                # Validasi hasil pencarian, jika tidak ditemukan akan diulang kembali
                if result == []:
                    clear_screen()
                    input("Transaksi tidak ditemukan, harap coba lagi!...")
                    clear_screen()
                else:
                    return result

    def detail_transaction(self):
        table = PrettyTable()
        table.title = "DETAIL INFORMASI"
        table.field_names = ["No", "Product ID", "Nama Produk", "Harga Normal", "Diskon", "Harga Jual", "Banyaknya", "Jumlah`"]
        table.align["Nama Produk"] = 'l'
        table.align["Harga Normal"] = 'r'
        table.align["Harga Jual"] = 'r'
        table.align["Sub-Total"] = 'r'
        no = 1

        for i in self.transactions:
            print(i)

    def menu(self):
        clear_screen()
        self.view_transactions()

        results = self.search_transaction()

        if results == []:
            return
        elif len(results) > 1:
            self.detail_transaction()
            
        else:
            self.transactions = results
            self.menu()        


Laporan_Penjualan()