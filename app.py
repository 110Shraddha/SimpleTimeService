cat <<EOF > app.py
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_time():
    timestamp = datetime.utcnow().isoformat() + "Z"
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    return jsonify({
        "timestamp": timestamp,
        "ip": ip
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
EOF
echo "flask==2.3.3" > requirements.txt
