from flask import Flask
import os

app = Flask(__name__)

# Usamos el puerto 8080 si está definido en las variables de entorno, o 8080 por defecto
port = int(os.environ.get("PORT", 8080))

@app.route('/')
def hello_world():
    return '¡Hola, jimmy espinoza!'

if __name__ == '__main__':
    # Escuchar en 0.0.0.0 para aceptar conexiones externas
    app.run(host='0.0.0.0', port=port)