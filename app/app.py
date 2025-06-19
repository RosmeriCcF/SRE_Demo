from flask import Flask, request
from prometheus_client import Counter, Histogram, generate_latest
import time
import random

app = Flask(__name__)

# Métricas SRE
REQUEST_COUNT = Counter('request_count', 'Número de peticiones', ['method', 'endpoint'])
ERROR_COUNT = Counter('error_count', 'Número de errores', ['endpoint'])
REQUEST_LATENCY = Histogram('request_latency_seconds', 'Tiempo de respuesta', ['endpoint'])

@app.route("/")
def home():
    REQUEST_COUNT.labels(method="GET", endpoint="/").inc()
    return "¡Hola! Esta es una demo SRE con Flask + Prometheus."

@app.route("/login")
def login():
    REQUEST_COUNT.labels(method="GET", endpoint="/login").inc()
    start_time = time.time()

    # Simulamos latencia entre 0.1 y 1.2 segundos
    simulated_latency = random.uniform(0.1, 1.2)
    time.sleep(simulated_latency)

    REQUEST_LATENCY.labels(endpoint="/login").observe(time.time() - start_time)
    return "Login exitoso (simulado)"

@app.route("/error")
def error():
    REQUEST_COUNT.labels(method="GET", endpoint="/error").inc()
    ERROR_COUNT.labels(endpoint="/error").inc()
    return "Error simulado", 500

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain; version=0.0.4'}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
