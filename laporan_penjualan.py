class Laporan_Penjualan:
    def __init__(self):
        self.__products = {
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
        self.__transactions = {
            # Format tahun bulan tanggal urutan
            1 : {
                "tgl" : "01/12/24",
                "kasir" : "andris",
                "items" : {
                    "079260002" : 1,
                    "082263001" : 1,
                    "078259002" : 3
                }
            }
        }

    def menu(self):
        print("\n===== Menu Laporan Penjualan ======")
        print("[1] Tambah Pesanan")
        print("[2] Tampilkan Pesanan")
        print("[0] Kembali ke Menu Utama")
        self.select() = input("Pilih menu: ")

    def select(self):
        pass

lp = Laporan_Penjualan()
lp.menu()