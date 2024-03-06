# Usa la imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY agify.py .
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 5001
EXPOSE 5001

# Comando para ejecutar el servicio Agify
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5001", "agify:app"]