from flask import Flask, jsonify
from flask_cors import CORS
import os
from api.devices import devices_bp

backend_host = os.getenv("BACKEND_HOST")
backend_port = os.getenv("BACKEND_PORT")

frontend_host = os.getenv("FRONTEND_HOST")
frontend_port = os.getenv("FRONTEND_PORT")

app = Flask(__name__)
CORS(
    app,
    resources={r"/*": {"origins": f"http://{frontend_host}:{frontend_port}"}},
    methods=["GET","POST","PUT","DELETE"],
    allow_headers=["Content-Type","Authirization"]
)

app.register_blueprint(devices_bp, url_prefix="/devices")

@app.route("/status", methods=['GET'])
def get_status():
    return jsonify({
        "message": "Backend funcionando correctamente",
        "HOST": backend_host,
        "PORT": backend_port
    }), 200

if __name__ == '__main__':
    app.run(debug=True, host=backend_host, port=backend_port)