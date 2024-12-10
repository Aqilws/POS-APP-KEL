from product import Products
from induk import Induk
import tkinter as tk
from tkinter import ttk

class Search(Products):
    def __init__(self):
        super().__init__()
        self.__product_id = str
        self.__qty = 0
    
    def window(self):
        window = tk.Tk()
        window.title(self.get_aplication_name())
        window.geometry(self.get_screen_size())
        window.resizable(False, False)

        # konfigurasi grid kepada window
        window.grid_columnconfigure(0, weight=1)
        window.grid_rowconfigure(0, weight=1)

        def back_to_transaction():
            idk = Induk()
            idk.window()

        # Function add
        def add_qty():
            try: 
                self.__qty = int(input_qty.get()) + 1
            except:
                self.__qty = 1
            input_qty.delete(0,tk.END)
            input_qty.insert(0, self.__qty)
            button_add_to_chart.config(state="normal")
        
        # Function reduce
        def reduce_qty():
            if self.__qty > 0:
                self.__qty = self.__qty - 1
            
            input_qty.delete(0,tk.END)
            input_qty.insert(0, self.__qty)
            if self.__qty < 1:
                button_add_to_chart.config(state="disabled")
        
        def on_table_selected(event):
            selected_item = table.selection()
            input_qty.delete(0, tk.END)
            self.__qty = 1
            input_qty.insert(0, self.__qty)
            button_add_to_chart.config(state="normal")
            if selected_item:
                self.__product_id = table.item(selected_item[0], "values")[0]
                frame_add_chart.grid(row=0, column=0, sticky="se")
            else:
                frame_add_chart.grid_forget()

        def add_to_chart():
            self.set_chart(product_id=self.__product_id, qty=self.__qty)
            # bersihkan treeview
            for product in table_chat.get_children():
                table_chat.delete(product)
            
            # Tampilkan data ke chart/keranjang    
            no = 0
            chart = self.get_chart()
            for transaction_id in chart[self.get_transaction_id()]:
                table_chat.insert("", "end", values=transaction_id)


        # ---------------------------------- Frame table ----------------------------------
        frame_table = tk.Frame(window, padx=10)
        frame_table.grid(row=0, column=0, sticky="wn")

        # frame search
        frame_search = tk.Frame(frame_table)
        frame_search.grid(row=0, column=0, sticky="w")
        label_search = tk.Label(frame_search, text="Cari Barang:")
        label_search.grid(row=0, column=0, pady=5, sticky="w")
        input_search = tk.Entry(frame_search)
        input_search.grid(row=1, column=0)
        button_search = tk.Button(frame_search, text="Cari")
        button_search.grid(row=1, column=1, padx=10)

        # Frame add to chart
        frame_add_chart = tk.Frame(frame_table)
        frame_add_chart.grid(row=0, column=0, sticky="se")
        frame_add_chart.grid_forget() # Sembunyikan ketia pertama kali
        button_del = tk.Button(frame_add_chart, text="-", width=3, command=reduce_qty)
        button_del.grid(row=0, column=0, padx=10)
        input_qty = tk.Entry(frame_add_chart, width=2)
        input_qty.grid(row=0, column=1)
        button_add = tk.Button(frame_add_chart, text="+", width=3, command=add_qty)
        button_add.grid(row=0, column=2, padx=10)
        button_add_to_chart = tk.Button(frame_add_chart, text="Tambahkan", command=add_to_chart)
        button_add_to_chart.grid(row=0, column=3)
        button_add_to_chart.config(state="disabled")

        # Table Search
        columns = ("ID", "Nama_Poduk", "Harga_Normal", "Diskon", "Harga_Promo")
        table = ttk.Treeview(frame_table, columns=columns, show="headings", height=18)
        table.grid(row=2, column=0, pady=10)
        # Manambahkan colom dan menepatkan heading
        table.heading("ID", text="ID")
        table.heading("Nama_Poduk", text="Nama Produk")
        table.heading("Harga_Normal", text="Harga Normal")
        table.heading("Diskon", text="Diskon")
        table.heading("Harga_Promo", text="Harga Promo")
        # Menyesuaikan lebar kolom
        for i in columns:
            if i == "Nama_Poduk":
                table.column(i, width=200)
            elif i == "Diskon" or i == "ID":
                table.column(i, width=100, anchor="center")
            else:
                table.column(i, width=100, anchor="e")
        # Menambahkan data ke tabel/Treeveiw
        for product_id in self.get_list_products():
            product = self.get_list_products()[product_id]
            product[1] = self.price_format(price=product[1])
            product[len(product) - 1] = self.price_format(product[len(product) - 1]) # ubah format angka
            product.insert(0, product_id) # Tambahkan id
            table.insert("", "end", values=product)
        # Event ketika item yang ada di table di klik
        table.bind("<ButtonRelease-1>", on_table_selected)

        # ---------------------------------- frame chart ----------------------------------
        frame_chart = tk.Frame(window, padx=15)
        frame_chart.grid(row=0, column=1, sticky="en")
        frame_label_chart = tk.Frame(frame_chart)
        frame_label_chart.grid(row=0, column=0, sticky="we")
        label_chart = tk.Label(frame_label_chart, text="Daftar Tambahan Barang")
        label_chart.grid(row=0, column=0)

        # Frame edit chart
        frame_edit_chart = tk.Frame(frame_chart, padx=0, pady=0)
        frame_edit_chart.grid(row=0, column=0, sticky="e")
        button_edit = tk.Button(frame_edit_chart, text="Edit")
        button_edit.grid(row=0, column=0, padx=10)
        button_delete = tk.Button(frame_edit_chart, text="Hapus")
        button_delete.grid(row=0, column=1)

        # Tabel chart
        columns_chart = ("No", "Nama_Produk", "Harga_Promo", "Jumlah")
        table_chat = ttk.Treeview(frame_chart, columns=columns_chart, show="headings", height=20)
        table_chat.grid(row=1, column=0, pady=5)
        # Set heading
        table_chat.heading("No", text="No")
        table_chat.heading("Nama_Produk", text="Nama Produk")
        table_chat.heading("Harga_Promo", text="Harga Promo")
        table_chat.heading("Jumlah", text="Jumlah")
        # Set ukuran lebar kolom
        table_chat.column("No", width=50, anchor="center")
        table_chat.column("Nama_Produk", width=150)
        table_chat.column("Harga_Promo", width=100, anchor="e")
        table_chat.column("Jumlah", width=50, anchor="center")

        # Frame end / selesai
        label_total_tambahan = tk.Label(frame_chart, text=f"Total Tambahan Rp. ")
        label_total_tambahan.grid(row=2, column=0, sticky="w")
        button_end = tk.Button(frame_chart, text="Selesai", command=back_to_transaction)
        button_end.grid(row=2, column=0, sticky="E")

        # Tampilkan
        window.mainloop()

apk = Search()
apk.window()