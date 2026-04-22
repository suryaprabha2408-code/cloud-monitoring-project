from flask import Flask
import random
import os

app = Flask(__name__)

@app.route("/")
def home():
    usage = random.randint(50, 150)

    if usage > 100:
        status = "ALERT 🚨"
    else:
        status = "SAFE ✅"

    return f"""
    <h1>Cloud Monitoring System</h1>
    <h2>Current Usage: {usage}</h2>
    <h2 style='color: {"red" if usage > 100 else "green"}'>
    Status: {status}
    </h2>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)