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
    "1": {
        "date": "2024-03-20",
        "kasir": "John",
        "total_qty": 3,
        "total_value": 1500000,
        "pay": "cash",
        "items": {
            "71253001": 2,
            "71253002": 1
        }
    }
}
last_transaction_id = 1
_pesanan_items = [
    
]

# Fungsi internal untuk mengakses data (tidak menggunakan Flask)
def get_produk_data():
    """Fungsi internal untuk mengakses data produk"""
    return produk

def get_produk_by_id_data(id):
    """Fungsi internal untuk mengakses data produk berdasarkan ID"""
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

# Flask routes (endpoint API)
@app.route('/api/produk', methods=['GET'])
def get_produk():
    return jsonify(produk)

@app.route('/api/produk/<int:id>', methods=['GET'])
def get_produk_by_id(id):
    item = get_produk_by_id_data(id)
    if item:
        return jsonify(item)
    return jsonify({"error": "Produk tidak ditemukan"}), 404

# Endpoint untuk menambah produk baru
@app.route('/api/produk', methods=['POST'])
def tambah_produk():
    data = request.json
    if "nama" in data and "harga" in data and "stok" in data:
        new_id = max([p["id"] for p in produk]) + 1 if produk else 1
        new_produk = {
            "id": new_id,
            "nama": data["nama"],
            "harga": data["harga"],
            "stok": data["stok"]
        }
        produk.append(new_produk)
        return jsonify(new_produk), 201
    return jsonify({"error": "Data produk tidak lengkap"}), 400

# Endpoint untuk memperbarui data produk
@app.route('/api/produk/<int:id>', methods=['PUT'])
def update_produk(id):
    data = request.json
    item = next((p for p in produk if p['id'] == id), None)
    if item:
        item.update({
            "nama": data.get("nama", item["nama"]),
            "harga": data.get("harga", item["harga"]),
            "stok": data.get("stok", item["stok"]),
        })
        return jsonify(item)
    return jsonify({"error": "Produk tidak ditemukan"}), 404

# Endpoint untuk menghapus produk
@app.route('/api/produk/<int:id>', methods=['DELETE'])
def delete_produk(id):
    global produk
    produk = [p for p in produk if p['id'] != id]
    return jsonify({"message": "Produk berhasil dihapus"}), 200

# Tambahkan endpoint baru untuk melihat pesanan items
@app.route('/api/pesanan-items', methods=['GET'])
def view_pesanan_items():
    items = get_pesanan_items()
    return jsonify(items)

@app.route('/api/transaksi', methods=['GET'])
def view_all_transaksi():
    return jsonify(get_all_transaksi())

if __name__ == '__main__':
    app.run(debug=True)