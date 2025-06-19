# 🛠️ SRE_Demo – Monitoreo con Flask + Prometheus + Grafana + Docker

Este proyecto es una **prueba de concepto (POC)** basada en los principios de **Site Reliability Engineering (SRE)**.  
Simula un entorno de monitoreo para una aplicación web con Flask, incluyendo:

- Exposición de métricas personalizadas
- Recolección con Prometheus
- Visualización en tiempo real con Grafana
- Contenedores orquestados con Docker Compose

---

## 📌 Tecnologías Utilizadas

- [Flask](https://flask.palletsprojects.com/) – API web simple
- [Prometheus](https://prometheus.io/) – Recolección de métricas
- [Grafana](https://grafana.com/) – Dashboards de monitoreo
- [Docker Compose](https://docs.docker.com/compose/) – Orquestación de servicios

---

## ⚙️ Endpoints de la App

| Endpoint              | Descripción                       |
|-----------------------|-----------------------------------|
| `/`                   | Página de bienvenida              |
| `/login`              | Simula login con latencia         |
| `/error`              | Simula error HTTP 500             |
| `/metrics`            | Métricas en formato Prometheus    |

---

## 📊 Métricas expuestas

- `request_count_total` – Número total de peticiones por endpoint
- `error_count_total` – Número de errores simulados
- `request_latency_seconds` – Histograma de latencia para `/login`

---

## 🐳 Ejecuta el proyecto

1. Clona el repositorio:

```bash
git clone https://github.com/RosmeriCcF/SRE_Demo.git
cd SRE_Demo
