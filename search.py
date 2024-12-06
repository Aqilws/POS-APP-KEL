from product import Products
import tkinter as tk
from tkinter import ttk

class Search(Products):
    def __init__(self):
        super().__init__()
    
    def window(self):
        window = tk.Tk()
        window.title(self.get_aplication_name())
        window.geometry(self.get_screen_size())
        window.resizable(False, False)

        # frame search
        frame_search = tk.Frame(window)
        frame_search.grid(row=0, column=0, padx=10, pady=10)
        # label search
        label_search = tk.Label(frame_search, text="Masukan Kata Kunci:")
        label_search.grid(row=0, column=0, sticky="w")
        # Input Search
        entry_key = tk.Entry(frame_search)
        entry_key.grid(row=1, column=0, pady=5)
        # buttuon search
        button_search = tk.Button(frame_search, text="Cari")
        button_search.grid(row=1, column=1, padx=10)

        # Frame table
        frame_table = tk.Frame(window, bg="light blue")
        frame_table.grid(row=1, column=0, padx=10, pady=10)
        # Label table
        label_table = tk.Label(frame_table, text="Hasil Pencarian:")
        label_table.grid(row=0, column=0, padx=10)
        # Table
        columns = ("ID", "Nama_Poduk", "Harga_Normal", "Diskon", "Harga_Promo")
        table = ttk.Treeview(frame_table, columns=columns, show="headings")
        
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
            elif i == "Diskon":
                table.column(i, width=100, anchor="center")
            else:
                table.column(i, width=100, anchor="e")

        
        # Menambahkan data ke tabel/Treeveiw
        for product_id in self.get_list_products():
            product = self.get_list_products()[product_id]
            product[len(product) - 1] = self.price_format(product[len(product) - 1])
            product.insert(0, product_id)
            table.insert("", "end", values=product)
        # Menempatkan Treeview/table di layout
        table.grid(row=1, column=0)





        window.mainloop()

apk = Search()
apk.window()