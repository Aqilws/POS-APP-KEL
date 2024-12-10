from induk import Induk

class Reports(Induk):
    def __init__(self):
        super().__init__()
        self.__transaction_id = "241210001"
        self.__list_products = {
            # Format ID product: Nama barang, Harga Normal, Diskon, Harga setelah diskon
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

        self.__list_transactions = {
            # Format Id 2 angka pertama tahun, dilanjutkan 2 lagi bulan, 2 lagi tanggal dan 3 angka nomor urut perhari
            "241210001" : [
                # id product, qty/jumlah yang dibeli
                ["071253002", 3],
                ["082263001", 1]
            ],
            "241210001" : [
                ["080261002", 1],
                ["081262002", 2],
            ]
        }

        self.__chart = {
            self.__transaction_id : {
                '112' : 1,
                '132' : 1,
                '321' : 1,
                '222' : 1,
            }
        }

    # Get list products
    def get_list_products(self):
        return self.__list_products
    
    # Get chart
    def get_chart(self):
        return self.__chart
    
    # Get transaction id
    def get_transaction_id(self):
        return self.__transaction_id

    def set_chart(self, product_id, qty):
        if product_id in self.__chart[self.__transaction_id]:
            self.__chart[self.__transaction_id][product_id] += qty
        else:
            self.__chart[self.__transaction_id][product_id] = qty
    
    # format harga
    def price_format(self, price):
        return f"{price:,}".replace(",", ".")
    
# rpt = Reports()
# rpt.set_chart(qty=3, product_id="222")
# print(rpt.get_chart())