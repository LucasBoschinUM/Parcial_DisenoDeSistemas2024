# Parcial de Diseño de Sistemas
Este repositorio contiene un proyecto de verificación de secuencias de ADN, donde podrás identificar mutantes y obtener estadísticas de las secuencias evaluadas.

## 🌟 Guía rápida para ejecutar el proyecto
Sigue estos sencillos pasos para configurar y poner en marcha la aplicación:

### Paso 1: Instalar dependencias
Asegúrate de tener todas las dependencias necesarias ejecutando el siguiente comando en la terminal:

pip install -r requirements.txt

### Paso 2: Iniciar el programa
Ejecuta el archivo principal para iniciar el programa:

python3 app_inicio.py

### Paso 3: Configurar Postman
Abre Postman y carga la colección de solicitudes que encontrarás en la carpeta collection.

### Paso 4: Verificación de ADN (POST)
En Postman, selecciona la solicitud POST para enviar una secuencia de ADN y verificar si es mutante. Ingresa la secuencia en el cuerpo de la solicitud y envíala.
La aplicación estará disponible en:


### Paso 5: Consultar estadísticas (GET)
Para obtener estadísticas de mutantes y no mutantes registrados en la base de datos, selecciona la solicitud GET en Postman. La URL para esta solicitud es:


🌐 Ejecutar en modo Docker y Hosting en Render
Si prefieres usar la versión desplegada en la nube, simplemente abre Postman y usa las siguientes URLs:

POST para verificar mutantes:


GET para consultar estadísticas: