# Usa la imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY genderize.py .
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 7000
EXPOSE 7000

# Comando para ejecutar el servicio Genderize
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:7000", "genderize:app"]