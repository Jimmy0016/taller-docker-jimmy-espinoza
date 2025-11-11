FROM python:3.10-slim


WORKDIR /app


COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt


COPY . .

# -----------------------------------------------------------------
# 5. EXPONE EL PUERTO (si es necesario)
# Informa a Docker que el contenedor escuchará en el puerto 8080.
# Esto es más bien "documentación" para el usuario y para Docker.
EXPOSE 8080

# -----------------------------------------------------------------
# 6. EJECUTA LA APLICACIÓN
# El comando para iniciar la aplicación cuando se lance el contenedor.
CMD ["python", "app.py"]