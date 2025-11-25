from flask import Flask, jsonify, request
import os
import random
import datetime

app = Flask(__name__)

# Usamos el puerto 8080 si está definido en las variables de entorno, o 80 por defecto
port = int(os.environ.get("PORT", 80))

# Simulador de IA - Respuestas predefinidas
AI_RESPONSES = [
    "¡Hola! Soy una IA simple creada por Jimmy Espinoza. ¿En qué puedo ayudarte?",
    "Como IA, puedo decirte que hoy es un gran día para aprender Docker y CI/CD.",
    "Mi función principal es demostrar un pipeline de CI/CD funcional.",
    "¡Excelente! El despliegue automático está funcionando correctamente.",
    "Soy parte del proyecto de Jimmy Espinoza para el examen de CI/CD."
]

@app.route('/')
def hello_world():
    return '''
    <h1>¡este es mi examen final </h1>
    <p>Aplicación Flask con IA - Versión 1.0.5</p>
    <p>Endpoints disponibles:</p>
    <ul>
        <li><a href="/ai">/ai</a> - Consulta a la IA</li>
        <li><a href="/health">/health</a> - Estado de la aplicación</li>
        <li><a href="/info">/info</a> - Información del sistema</li>
    </ul>
    '''

@app.route('/ai')
def ai_endpoint():
    """Endpoint que simula una respuesta de IA"""
    response = random.choice(AI_RESPONSES)
    return jsonify({
        "ai_response": response,
        "timestamp": datetime.datetime.now().isoformat(),
        "version": "1.0.5",
        "author": "Jimmy Espinoza"
    })

@app.route('/health')
def health_check():
    """Endpoint para verificar el estado de la aplicación"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.datetime.now().isoformat(),
        "version": "1.0.5"
    })

@app.route('/info')
def info():
    """Endpoint con información del sistema"""
    return jsonify({
        "app_name": "Flask AI App - Jimmy Espinoza",
        "version": "1.0.5",
        "python_version": "3.10",
        "framework": "Flask 3.1.2",
        "deployment": "Docker + CI/CD",
        "author": "Jimmy Espinoza"
    })

if __name__ == '__main__':
    # Escuchar en 0.0.0.0 para aceptar conexiones externas
    app.run(host='0.0.0.0', port=port, debug=False)