# create a simple flask app
from flask import Flask, render_template
import os
import requests

app = Flask(__name__)

PORT = os.environ.get("PORT", 9000)
BACKEND_URL = os.environ.get("BACKEND_URL", "http://localhost:8000")

@app.route("/")
def index():
    response = requests.get(f"{BACKEND_URL}/api/get")
    
    data = None
    if response.status_code == 200:
        data = response.json()
    else:
        raise Exception(f"Failed to fetch data from backend. Status code: {response.status_code}")

    print(data, type(data))

    env = dict(os.environ)

    return render_template("index.html", env = env, data=data["data"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=True)