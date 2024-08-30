from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import tempfile
import os
import uuid
import sys

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas las rutas

@app.route('/compile', methods=['POST'])
def analyze_code():
    data = request.get_json()
    if 'code' not in data:
        return jsonify({"error": "No code provided"}), 400

    code = data['code']

    # Crear un archivo temporal
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as tmp_file:
        tmp_file.write(code.encode())
        tmp_filename = tmp_file.name

    try:
        # Ejecutar tu script con el archivo guardado
        result = subprocess.run([sys.executable, 'Driver.py', tmp_filename], capture_output=True, text=True, encoding='utf-8')
        if result.returncode != 0:
            return jsonify({"error": result.stderr}), 500

        return jsonify({"output": result.stdout}), 200

    finally:
        # Eliminar el archivo temporal
        os.remove(tmp_filename)

if __name__ == '__main__':
    app.run(debug=True)
