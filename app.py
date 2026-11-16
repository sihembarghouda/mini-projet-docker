from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Bienvenue dans mon application Docker - Version 2 !",
        "environment": os.getenv("ENV", "development"),
        "hostname": socket.gethostname()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
