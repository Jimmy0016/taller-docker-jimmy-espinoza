from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hola mundo"})

@app.route('/suma/<int:a>/<int:b>')
def suma(a, b):
    return jsonify({"resultado": a + b})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
