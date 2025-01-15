from flask import Flask, jsonify, request

app = Flask(__name__)

produk = [
    {"id": 71253001, "nama": "Koper Lojel Lineo Salmon N", "harga": 500000, "stok": 10},
    {"id": 71253002, "nama": "Koper Lojel Lineo Salmon M", "harga": 750000, "stok": 15},
    {"id": 71253003, "nama": "Koper Lojel Lineo Salmon L", "harga": 1000000, "stok": 20},
    {"id": 71254001, "nama": "Tas Selempang Eiger 18L", "harga": 300000, "stok": 8},
    {"id": 71254002, "nama": "Tas Backpack Eiger 25L", "harga": 400000, "stok": 5},
    {"id": 72251001, "nama": "Sepatu Nike Running Air Zoom", "harga": 1200000, "stok": 10},
    {"id": 72251002, "nama": "Sepatu Nike Basketball Lebron 19", "harga": 2000000, "stok": 15},
    {"id": 72251003, "nama": "Sepatu Nike Casual Air Force 1", "harga": 1100000, "stok": 20},
    {"id": 73252001, "nama": "Jaket Adidas Essentials", "harga": 600000, "stok": 8},
    {"id": 73252002, "nama": "Jaket Adidas Performance", "harga": 750000, "stok": 5},
    {"id": 73252003, "nama": "Jaket Adidas Climaproof", "harga": 850000, "stok": 10},
    {"id": 74255001, "nama": "Kemeja Formal Levi's", "harga": 500000, "stok": 10},
    {"id": 74255002, "nama": "Jeans Slim Fit Levi's 501", "harga": 900000, "stok": 15},
    {"id": 74255003, "nama": "Jaket Denim Levi's Original", "harga": 1000000, "stok": 5},
    {"id": 75256001, "nama": "Jam Tangan Casio G-Shock GA-2100", "harga": 1500000, "stok": 10},
    {"id": 75256002, "nama": "Jam Tangan Casio Vintage Gold", "harga": 700000, "stok": 15},
    {"id": 76257001, "nama": "Parfum Chanel Bleu de Chanel 100ml", "harga": 2000000, "stok": 8},
    {"id": 76257002, "nama": "Parfum Chanel Coco Mademoiselle 50ml", "harga": 1800000, "stok": 10},
    {"id": 77258001, "nama": "Handuk Terry Palmer Bath Towel", "harga": 150000, "stok": 20},
    {"id": 77258002, "nama": "Handuk Terry Palmer Face Towel", "harga": 75000, "stok": 15},
    {"id": 78259001, "nama": "Bantal Dakron King Size", "harga": 120000, "stok": 10},
    {"id": 78259002, "nama": "Guling Dakron Medium", "harga": 100000, "stok": 5},
    {"id": 79260001, "nama": "Panci Supra Chef's Pan 24cm", "harga": 300000, "stok": 10},
    {"id": 79260002, "nama": "Wajan Supra Teflon 28cm", "harga": 250000, "stok": 15},
    {"id": 80261001, "nama": "Kamera Canon EOS M50 Kit 15-45mm", "harga": 8000000, "stok": 5},
    {"id": 80261002, "nama": "Kamera Sony Alpha a6400", "harga": 12000000, "stok": 5},
    {"id": 81262001, "nama": "TV LED Samsung 43 Inch 4K UHD", "harga": 6000000, "stok": 10},
    {"id": 81262002, "nama": "TV LED LG 55 Inch OLED", "harga": 15000000, "stok": 5},
    {"id": 82263001, "nama": "Laptop ASUS VivoBook 14", "harga": 7500000, "stok": 10},
    {"id": 82263002, "nama": "Laptop Lenovo IdeaPad 3", "harga": 8500000, "stok": 15},
]

# Dictionary untuk menyimpan transaksi
transactions = {
    
}
last_transaction_id = 1
_pesanan_items = [
    
]

def get_produk_data():
    return produk

def get_produk_by_id_data(id):
    return next((p for p in produk if p['id'] == id), None)

def simpan_transaksi(transaksi):
    global last_transaction_id
    last_transaction_id += 1
    transactions[str(last_transaction_id)] = transaksi
    return {
        "message": "Transaksi berhasil disimpan", 
        "transaction_id": str(last_transaction_id)
    }

def get_all_transaksi():
    return transactions

def simpan_pesanan_item(items):
    global _pesanan_items
    _pesanan_items = items
    return {"message": "Pesanan berhasil disimpan"}

def get_pesanan_items():
    print("Isi _pesanan_items:", _pesanan_items)
    return _pesanan_items

karyawan = [
    {
        "Nama_Karyawan": "Muhamad Andris",
        "Tanggal_Lahir": "29 Desember 2000",
        "Posisi_Jabatan": "Manager toko",
        "Username": "Muhammadandris",
        "Password": "Andris20"
    },
    {
        "Nama_Karyawan": "Aqil Wira Saputra",
        "Tanggal_Lahir": "15 Juni 2004",
        "Posisi_Jabatan": "Kasir",
        "Username": "Aqil",
        "Password": "Aqil24"
    },
    {
        "Nama_Karyawan": "M Fatkhul Rozi",
        "Tanggal_Lahir": "21 Januari 2002",
        "Posisi_Jabatan": "Staf Gudang",
        "Username": "Mfatkhulrozi",
        "Password": "Rozi22"
    },
    {
        "Nama_Karyawan": "Triam Tomo",
        "Tanggal_Lahir": "29 Juli 2003",
        "Posisi_Jabatan": "Pramuniaga",
        "Username": "Triamtomo",
        "Password": "Tomo23"
    },
    {
        "Nama_Karyawan": "Nevi Afyanthi Sangadj",
        "Tanggal_Lahir": "11 Oktober 2005",
        "Posisi_Jabatan": "Admin Toko",
        "Username": "Nefiafyanthisangadj",
        "Password": "Nefi25"
    }
]

def get_karyawan_data():
    return karyawan

def verify_karyawan_login(username, password):
    for k in karyawan:
        if k["Username"] == username and k["Password"] == password:
            return k
    return None



if __name__ == '__main__':
    app.run(debug=True)

