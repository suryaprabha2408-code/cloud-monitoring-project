from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    usage = 85   # sample value

    if usage > 100:
        status = "ALERT 🚨"
    else:
        status = "SAFE ✅"

    return f"""
    <h1>Cloud Monitoring System</h1>
    <h2>Current Usage: {usage}</h2>
    <h2>Status: {status}</h2>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)