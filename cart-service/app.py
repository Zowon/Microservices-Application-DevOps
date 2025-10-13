from flask import Flask, jsonify
import os

app = Flask(__name__)
SERVICE_NAME = os.getenv("SERVICE_NAME", "cart-service")

@app.route("/")
def index():
    return jsonify({
        "service": SERVICE_NAME,
        "message": f"{SERVICE_NAME} is running"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)