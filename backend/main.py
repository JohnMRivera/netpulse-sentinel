from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}},
methods=["GET","POST"],
allow_headers=["Content-Type","Authirization"]
)

@app.route("/status", methods=['GET'])
def get_status():
    return jsonify({
        "message": "Backend funcionando correctamente",
        "status": 200
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    # app.run(host='0.0.0.0', port=5000)