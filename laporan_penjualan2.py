from prettytable import PrettyTable
from api import get_produk, get_all_transaksi
from main import clear_screen
import os

class Laporan_Penjualan:
    def __init__(self):
        self.transaction_id = str
        self.product_id = str
        self.transactions = []
        # Konversi dari data api ke data yang dibutuhkan
        self.all_transaction = self.convert_transactions_from_api()
        self.all_products = self.convert_products_from_api()
        self.menu()
    
    def convert_transactions_from_api(self):
        return get_all_transaksi()
    
    def convert_products_from_api(self):
        return get_produk()


    def view_transactions(self):
        """Metode untuk menampilkan semua transaksi"""

        table = PrettyTable()
        table.title = ("TRANSAKSI")
        table.field_names = ["ID", "Tanggal", "Kasir", "Banyaknya", "Total Bayar", "Metode Pembayaran"]
        table.align["Kasir"] = 'l'
        table.align["Total Value"] = 'r'
        print(self.all_products)
        return

        if self.transactions == []:
            datas = get_all_transaksi 
        else:
            datas = self.transactions

        for transaction in datas:
            # table.add_row([
            #     transaction['id'],
            #     transaction['date'],
            #     transaction['kasir'],
            #     transaction['total_qty'],
            #     transaction['total_value'],
            #     transaction['pay'],
            # ])
            print(transaction)
        
        print(table)
    
    def search_transaction(self):
        """Metode untuk mencari transaksi"""

        while True:
            print("\nCari Transaksi Berdasarkan ")
            print("ID Transaksi/Nama kasir/Metode Pembayaran\n")
            print("0 -> Batal")
            query = input("Cari Transaksi: ").strip().lower()
            result = []

            if query == '0': # jika user memasukan angka 0 maka return angka '0' untuk menandakan. batal
                return result
            elif query == '':
                clear_screen()
                input("Input Tidak Boleh kosong...")
                clear_screen()
            else:
                # Cari berdasarkan ID Transaksi
                for transaction in get_all_transaksi:
                    if query == str(transaction["id"]):
                        result.append(transaction)
                
                # jika dengan id tidak ditemukan maka cari dengan opsi lain (Nama kasir/Tanggal/Metode Pembayaran)
                if result == []:
                    for transaction in get_all_transaksi: 
                        if  query in transaction['date'] or \
                            query in transaction['kasir'].lower() or \
                            query in transaction['pay'].lower():
                            result.append(transaction)  
                        
                        # note: Backslash (\) digunakan untuk menunjukkan bahwa baris tersebut dilanjutkan ke baris berikutnya.

                # Validasi hasil pencarian, jika tidak ditemukan akan diulang kembali
                # jika ada hasilnya/ditemukan akan me-return variable results
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