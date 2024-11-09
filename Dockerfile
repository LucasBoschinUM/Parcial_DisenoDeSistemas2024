# Use a Python base image // Usar una imagen base de Python
FROM python:3.12-slim

# Set the working directory inside the container // Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copy the archive of dependencies to the container // Copia el archivo de dependencias al contenedor
COPY requirements.txt .

# Install the project dependencies // Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the project content to the container // Copia todo el contenido del proyecto al contenedor
COPY . .

# Expose the port where the application will run // Expone el puerto donde se ejecutará la aplicación
EXPOSE 5000

# Set the environment variable to run Flask in production mode // Establece la variable de entorno para ejecutar Flask en modo de producción
ENV FLASK_ENV=production

# Define the command to run the application // Define el comando para ejecutar la aplicación
CMD ["python", "app_inicio.py"]