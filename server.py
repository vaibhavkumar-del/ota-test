from flask import Flask

app = Flask(__name__)

@app.route("/update_flag.txt")
def update():
    return "0"   # change to 1 to trigger OTA

@app.route("/")
def home():
    return "OTA SERVER RUNNING"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)