from flask import Flask, jsonify, request

app = Flask(__name__)

# Data produk
produk = [
    {"id": 1, "nama": "Tas Ransel", "harga": 150000, "stok": 10},
    {"id": 2, "nama": "Sepatu Olahraga", "harga": 300000, "stok": 15},
    {"id": 3, "nama": "Kemeja Pria", "harga": 120000, "stok": 20},
    {"id": 4, "nama": "Dress Wanita", "harga": 250000, "stok": 8},
    {"id": 5, "nama": "Jaket Kulit", "harga": 500000, "stok": 5},
]

# Endpoint untuk mendapatkan semua produk
@app.route('/api/produk', methods=['GET'])
def get_produk():
    return jsonify(produk)

# Endpoint untuk mendapatkan produk berdasarkan ID
@app.route('/api/produk/<int:id>', methods=['GET'])
def get_produk_by_id(id):
    item = next((p for p in produk if p['id'] == id), None)
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

if __name__ == '__main__':
    app.run(debug=True)
