from flask import Flask, render_template, jsonify
from flask_cors import CORS
from model import dados

app = Flask(__name__)
CORS(app)

@app.route("/grafico")
def index():
  return render_template('grafico.html')

@app.route("/dado")
def busca():
    return jsonify(dados)


if __name__ == "__main__":
 app.run()