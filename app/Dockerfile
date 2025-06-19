# Construcción del contenedor para app Flask:
# Imagen base oficial de Python
FROM python:3.11-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos los archivos de la app
COPY . .

# Instalamos las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt #Flask y prometheus_client

# Exponemos el puerto 5000 (donde corre Flask)
EXPOSE 5000

# Comando para ejecutar la app
CMD ["python", "app.py"]
