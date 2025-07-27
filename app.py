from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hola desde Railway"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # ⬅️ Railway define esta variable
    app.run(host="0.0.0.0", port=port)         # ⬅️ host debe ser 0.0.0.0
