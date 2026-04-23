from flask import Flask
import psutil
import os

app = Flask(__name__)

@app.route("/")
def home():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent

    if cpu > 80 or memory > 80:
        status = "ALERT 🚨"
        color = "red"
    else:
        status = "SAFE ✅"
        color = "green"

    return f"""
    <h1>Cloud Monitoring System</h1>
    <h2>CPU Usage: {cpu}%</h2>
    <h2>Memory Usage: {memory}%</h2>
    <h2 style='color: {color}'>Status: {status}</h2>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
