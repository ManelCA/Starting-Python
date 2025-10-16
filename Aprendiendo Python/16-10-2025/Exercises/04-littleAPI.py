# archivo: app.py
from flask import Flask, jsonify, request

# Crear la app
app = Flask(__name__)

# Datos simulados (como si fuera una base de datos)
productos = [
    {"id": 1, "nombre": "Silla", "precio": 49.99},
    {"id": 2, "nombre": "Mesa", "precio": 120.00},
    {"id": 3, "nombre": "Lámpara", "precio": 25.50}
]

# Ruta raíz


@app.route('/')
def home():
    return jsonify({"mensaje": "Bienvenido a la API de ejemplo con Flask"}), 200

# Obtener todos los productos


@app.route('/productos', methods=['GET'])
def get_productos():
    return jsonify(productos), 200

# Obtener un producto por ID


@app.route('/productos/<int:id>', methods=['GET'])
def get_producto(id):
    producto = next((p for p in productos if p["id"] == id), None)
    if producto:
        return jsonify(producto), 200
    return jsonify({"error": "Producto no encontrado"}), 404

# Agregar un nuevo producto


@app.route('/productos', methods=['POST'])
def add_producto():
    nuevo = request.get_json()
    nuevo["id"] = len(productos) + 1
    productos.append(nuevo)
    return jsonify(nuevo), 201

# Eliminar un producto


@app.route('/productos/<int:id>', methods=['DELETE'])
def delete_producto(id):
    global productos
    productos = [p for p in productos if p["id"] != id]
    return jsonify({"mensaje": "Producto eliminado"}), 200


# Ejecutar la app
if __name__ == '__main__':
    app.run(debug=True)
