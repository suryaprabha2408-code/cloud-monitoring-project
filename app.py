from flask import Flask
import psutil
from datetime import datetime
import requests

app = Flask(__name__)
def send_email(cpu, memory, status):
    url = "https://api.emailjs.com/api/v1.0/email/send"

    data = {
        "service_id": "service_l02zigf",
        "template_id": "template_k6hdfcm",
        "user_id": "Hu5lYNGCkePdHkQ0n",
        "template_params": {
            "cpu": cpu,
            "memory": memory,
            "status": status
        }
    }

    requests.post(url, json=data)

@app.route('/')
def home():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent

    status = "SAFE ✅"
    alert = ""

    # 🔥 ALERT CONDITION
    if cpu > 50 or memory > 50:
        status = "DANGER ⚠️"
        alert = "🚨 ALERT: High Resource Usage!"
        send_email(cpu, memory, status)

    # 📝 LOG WRITE
    log = f"{datetime.now()} | CPU: {cpu}% | Memory: {memory}% | Status: {status}\n"
    with open("logs.txt", "a") as f:
        f.write(log)

    # 🌐 OUTPUT
    return f"""
    <h1>Cloud Monitoring System</h1>
    <p>CPU Usage: {cpu}%</p>
    <p>Memory Usage: {memory}%</p>
    <p>Status: {status}</p>
    <h2 style='color:red;'>{alert}</h2>
    """
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
