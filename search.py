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

        # konfigurasi grid kepada window
        window.grid_columnconfigure(0, weight=1)
        window.grid_rowconfigure(0, weight=1)
        
        # Membuat frame sebagai element utama
        # frame = tk.Frame(window, bg="red")
        # frame.grid(row=0, column=0, sticky="nswe")
        # frame.grid_rowconfigure(0, weight=1)
        # frame.grid_columnconfigure(0, weight=1)


        # Function add
        def add_qty():
            try: 
                qty = int(input_qty.get()) + 1
            except:
                qty = 1
            input_qty.delete(0,tk.END)
            input_qty.insert(0, qty)
        
        # Function reduce
        def reduce_qty():
            try: 
                qty = int(input_qty.get()) - 1
            except:
                qty = 0
            input_qty.delete(0,tk.END)
            input_qty.insert(0, qty)

        # Frame table
        frame_table = tk.Frame(window, padx=10, background="blue")
        frame_table.grid(row=0, column=0, sticky="wn")

        # frame search
        frame_search = tk.Frame(frame_table)
        frame_search.grid(row=0, column=0, sticky="w")
        # Label search
        label_search = tk.Label(frame_search, text="Cari Barang:")
        label_search.grid(row=0, column=0, pady=5, sticky="w")
        # Input search
        input_search = tk.Entry(frame_search)
        input_search.grid(row=1, column=0)
        # Button search
        button_search = tk.Button(frame_search, text="Cari")
        button_search.grid(row=1, column=1, padx=10)

        # Frame add to chart
        frame_add_chart = tk.Frame(frame_table)
        frame_add_chart.grid(row=0, column=0, sticky="se")
        # button reduce
        button_del = tk.Button(frame_add_chart, text="-", width=3, command=reduce_qty)
        button_del.grid(row=0, column=0, padx=10)
        # Input QTY
        input_qty = tk.Entry(frame_add_chart, width=2)
        input_qty.grid(row=0, column=1)
        # button add
        button_add = tk.Button(frame_add_chart, text="+", width=3, command=add_qty)
        button_add.grid(row=0, column=2, padx=10)
        # button add to chart
        button_add_to_chart = tk.Button(frame_add_chart, text="Tambahkan")
        button_add_to_chart.grid(row=0, column=3)

        # Table Search
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
        # Menempatkan Treeview/table di layout
        table.grid(row=2, column=0, pady=10)

        # frame chart
        frame_chart = tk.Frame(window, padx=15, background="red")
        frame_chart.grid(row=0, column=1, sticky="en")
        # Frame Label chart
        frame_label_chart = tk.Frame(frame_chart)
        frame_label_chart.grid(row=0, column=0, sticky="we")
        # Label Chart
        label_chart = tk.Label(frame_label_chart, text="Daftar Tambahan Barang")
        label_chart.grid(row=0, column=0)

        # Frame edit chart
        frame_edit_chart = tk.Frame(frame_chart, padx=0, pady=0)
        frame_edit_chart.grid(row=0, column=0, sticky="e")
        # Edit
        button_edit = tk.Button(frame_edit_chart, text="Edit")
        button_edit.grid(row=0, column=0, padx=10)
        # Hapus
        button_delete = tk.Button(frame_edit_chart, text="Hapus")
        button_delete.grid(row=0, column=1)

        # Tabel chart
        columns_chart = ("No", "Nama_Produk", "Harga_Promo", "Jumlah")
        table_chat = ttk.Treeview(frame_chart, columns=columns_chart, show="headings")
        table_chat.grid(row=1, column=0, pady=5)
        # Set heading
        table_chat.heading("No", text="No")
        table_chat.heading("Nama_Produk", text="Nama Produk")
        table_chat.heading("Harga_Promo", text="Harga Promo")
        table_chat.heading("Jumlah", text="Jumlah")
        # Set ukuran lebar kolom
        table_chat.column("No", width=50)
        table_chat.column("Nama_Produk", width=150)
        table_chat.column("Harga_Promo", width=100)
        table_chat.column("Jumlah", width=50)

        # Frame end / selesai
        frame_end = tk.Frame(frame_chart, bg="light blue")
        frame_end.grid(row=2, column=0, sticky="se")
        # Label end
        label_end = tk.Button(frame_end, text="Selesai")
        label_end.grid(row=0, column=0)






        window.mainloop()

apk = Search()
apk.window()