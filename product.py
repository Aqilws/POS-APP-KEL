from reports import Reports

class Products(Reports):
    def __init__(self):
        super().__init__()
        # Format ID 3 Pertama brand 3 berikutnya kategori 3 berikunya lagi nomor urut
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

