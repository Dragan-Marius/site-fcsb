
from flask import Flask, render_template, jsonify 
import json

app = Flask(__name__)

@app.route("/")

def home():
    with open("players.json") as f1:
        players= json.load(f1)
    with open("transfers.json") as f2:
        transfers = json.load(f2)
    return render_template("index.html", players=players, transfers=transfers)

if __name__ == "__main__":
    app.run(debug=True)
