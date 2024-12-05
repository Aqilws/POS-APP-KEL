from product import Products
import tkinter as tk




class Search(Products):
    def __init__(self):
        super().__init__()
    
    def window(self):
        window = tk.Tk()
        window.title(apk.get_aplication_name())
        window.geometry(apk.get_screen_size())
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
        frame_table.grid(row=1, column=0)

        # Label table
        label_table = tk.Label(frame_table, text="Hasil Pencarian:")
        label_table.grid(row=0, column=0, padx=10)

        window.mainloop()

apk = Search()
apk.window()