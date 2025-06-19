from flask import Flask, request
from prometheus_client import Counter, Histogram, generate_latest
import time
import random

app = Flask(__name__)

# Métricas SRE
REQUEST_COUNT = Counter('request_count', 'Número de peticiones', ['method', 'endpoint']) #Total de peticiones hechas a cualquier endpoint
ERROR_COUNT = Counter('error_count', 'Número de errores', ['endpoint']) #Total de errores simulados (HTTP 500)
REQUEST_LATENCY = Histogram('request_latency_seconds', 'Tiempo de respuesta', ['endpoint']) #Latencia (tiempo de respuesta) de /login

@app.route("/")
def home():
    REQUEST_COUNT.labels(method="GET", endpoint="/").inc()
    return "DEMO SRE con Flask + Prometheus."

#Latencia de los endpoints
@app.route("/login")
def login():
    REQUEST_COUNT.labels(method="GET", endpoint="/login").inc() #Incremento de 1
    start_time = time.time()

    # Simulamos latencia entre 0.1 y 1.2 segundos
    simulated_latency = random.uniform(0.1, 1.2)
    time.sleep(simulated_latency)

    REQUEST_LATENCY.labels(endpoint="/login").observe(time.time() - start_time)
    return "Login exitoso (simulado)"

# Errores simulados
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
