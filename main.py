from flask import Flask, request, send_file
import datetime

app = Flask(__name__)

@app.route("/track_open")
def track_open():
    email_id = request.args.get("id", "unknown")
    with open("open_logs.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} - Opened by: {email_id}\n")
    return send_file("pixel.png", mimetype="image/png")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
