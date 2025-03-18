from flask import Flask, jsonify
from flask_cors import CORS
import os

backend_host = os.getenv("BACKEND_HOST")
backend_port = os.getenv("BACKEND_PORT")

frontend_host = os.getenv("FRONTEND_HOST")
frontend_port = os.getenv("FRONTEND_PORT")

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": f"http://{frontend_host}:{frontend_port}"}},
methods=["GET","POST"],
allow_headers=["Content-Type","Authirization"]
)

@app.route("/status", methods=['GET'])
def get_status():
    return jsonify({
        "message": "Backend funcionando correctamente",
        "status": 200,
        "HOST": backend_host,
        "PORT": backend_port
    })

if __name__ == '__main__':
    app.run(debug=True, host=backend_host, port=backend_port)
    # app.run(host='0.0.0.0', port=5000)