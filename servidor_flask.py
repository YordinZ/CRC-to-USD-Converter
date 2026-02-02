from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Carga variables del archivo .env

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def index():
    return send_from_directory('.', 'conversor.html')

@app.route('/api/exchange-rate', methods=['GET'])
def get_exchange_rate():
    api_url = os.getenv("EXCHANGE_API_URL", "https://open.er-api.com/v6/latest/USD")

    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()

        data = response.json()

        if data.get("result") != "success":
            return jsonify({"error": "Error en la respuesta de la API"}), 500

        rates = data.get("rates", {})
        usd_crc = rates.get("CRC")

        if usd_crc is None:
            return jsonify({"error": "No se pudo obtener CRC"}), 500

        return jsonify({
            "success": True,
            "rate": usd_crc,
            "base": "USD",
            "target": "CRC"
        })

    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Error de conexión: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
