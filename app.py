from flask import Flask, jsonify, abort

app = Flask(__name__)

PRODUCTS = [
    {"id": 1, "name": "keyboard", "price": 59000, "stock": 10},
    {"id": 2, "name": "mouse", "price": 29000, "stock": 5},
    {"id": 3, "name": "monitor", "price": 189000, "stock": 0},
    {"id": 4, "name": "game", "price": 20000, "stock": 1},
]


@app.route("/api/products")
def list_products():
    return jsonify(PRODUCTS)


@app.route("/api/products/<int:product_id>")
def get_product(product_id):
    for p in PRODUCTS:
        if p["id"] == product_id:
            return jsonify(p)
    abort(404)


@app.route("/healthz")
def healthz():
    return "ok"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)