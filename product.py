import tkinter as tk
from tkinter import ttk

class Product:
    def __init__(self, id, name, price, discount, final_price):
        self.id = id
        self.name = name
        self.price = price
        self.discount = discount
        self.final_price = final_price

class Brand:
    def __init__(self):
        self.__brands = {
            "Lojel": "071",
            "Nike": "072",
            "Adidas": "073",
            "Levi's": "074",
            "Casio": "075",
            "Chanel": "076",
            "Terry Palmer": "077",
            "Generic Home Items": "078",
            "Supra": "079",
            "Canon": "080",
            "Sony": "080",
            "Samsung": "081",
            "LG": "081",
            "ASUS": "082",
            "Lenovo": "082",
        }

class Category:
    def __init__(self):
        self.__categories = {
            "Koper": "253",
            "Tas": "254",
            "Pakaian": "255",
            "Jam Tangan": "256",
            "Parfum": "257",
            "Handuk": "258",
            "Peralatan Rumah Tangga": "259",
            "Elektronik Dapur": "260",
            "Kamera": "261",
            "Televisi": "262",
            "Laptop": "263",
        }

class ProductList:
    def __init__(self):
        self.__list_products = {
            "071253001": ["Koper Lojel Lineo Salmon S", 500000, "50%", 250000],
            "071253002": ["Koper Lojel Lineo Salmon M", 750000, "40%", 450000],
            "071253003": ["Koper Lojel Lineo Salmon L", 1000000, "30%", 700000],
            "071254001": ["Tas Selempang Eiger 18L", 300000, "20%", 240000],
            "071254002": ["Tas Backpack Eiger 25L", 400000, "15%", 340000],
            "072251001": ["Sepatu Nike Running Air Zoom", 1200000, "30%", 840000],
            "072251002": ["Sepatu Nike Basketball Lebron 19", 2000000, "20%", 1600000],
            "072251003": ["Sepatu Nike Casual Air Force 1", 1100000, "25%", 825000],
            "073252001": ["Jaket Adidas Essentials", 600000, "20%", 480000],
            "073252002": ["Jaket Adidas Performance", 750000, "25%", 562500],
            "073252003": ["Jaket Adidas Climaproof", 850000, "30%", 595000],
            "074255001": ["Kemeja Formal Levi's", 500000, "15%", 425000],
            "074255002": ["Jeans Slim Fit Levi's 501", 900000, "20%", 720000],
            "074255003": ["Jaket Denim Levi's Original", 1000000, "25%", 750000],
            "075256001": ["Jam Tangan Casio G-Shock GA-2100", 1500000, "10%", 1350000],
            "075256002": ["Jam Tangan Casio Vintage Gold", 700000, "20%", 560000],
            "076257001": ["Parfum Chanel Bleu de Chanel 100ml", 2000000, "15%", 1700000],
            "076257002": ["Parfum Chanel Coco Mademoiselle 50ml", 1800000, "10%", 1620000],
            "077258001": ["Handuk Terry Palmer Bath Towel", 150000, "30%", 105000],
            "077258002": ["Handuk Terry Palmer Face Towel", 75000, "25%", 56250],
            "078259001": ["Bantal Dakron King Size", 120000, "20%", 96000],
            "078259002": ["Guling Dakron Medium", 100000, "15%", 85000],
            "079260001": ["Panci Supra Chef's Pan 24cm", 300000, "20%", 240000],
            "079260002": ["Wajan Supra Teflon 28cm", 250000, "15%", 212500],
            "080261001": ["Kamera Canon EOS M50 Kit 15-45mm", 8000000, "10%", 7200000],
            "080261002": ["Kamera Sony Alpha a6400", 12000000, "15%", 10200000],
            "081262001": ["TV LED Samsung 43 Inch 4K UHD", 6000000, "20%", 4800000],
            "081262002": ["TV LED LG 55 Inch OLED", 15000000, "15%", 12750000],
            "082263001": ["Laptop ASUS VivoBook 14", 7500000, "10%", 6750000],
            "082263002": ["Laptop Lenovo IdeaPad 3", 8500000, "15%", 7225000],
        }

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplikasi List Barang")
        self.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        self.tree = ttk.Treeview(self)
        self.tree["columns"] = ("ID", "Nama", "Harga", "Diskon", "Harga Setelah Diskon")
        self.tree.column("#0", width=0, stretch=tk.NO)
        self.tree.column("ID", anchor=tk.W, width=120)
        self.tree.column("Nama", anchor=tk.W, width=300)
        self.tree.column("Harga", anchor=tk.W, width=100)
        self.tree.column("Diskon", anchor=tk.W, width=100)
        self.tree.column("Harga Setelah Diskon", anchor=tk.W, width=150)

        self.tree.heading("#0", text="", anchor=tk.W)
        self.tree.heading("ID", text="ID", anchor=tk.W)
        self.tree.heading("Nama", text="Nama", anchor=tk.W)
        self.tree.heading("Harga", text="Harga", anchor=tk.W)
        self.tree.heading("Diskon", text="Diskon", anchor=tk.W)
        self.tree.heading("Harga Setelah Diskon", text="Harga Setelah Diskon", anchor=tk.W)

        self.tree.pack(pady=20)

        self.populate_tree()

    def populate_tree(self):
        product_list = ProductList()
        for id, details in product_list._ProductList__list_products.items():
            self.tree.insert("", tk.END, values=(id, details[0], details[1], details[2], details[3]))

if __name__ == "__main__":
    app = Application()
    app.mainloop()
