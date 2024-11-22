import os
from flask import Flask
from controller.controller import mutant_blueprint
from database.db_connection import init_db

app = Flask(__name__)

# Initialize the database // Inicializar la base de datos
init_db()

# Register the controller blueprint // Registrar el blueprint del controlador
app.register_blueprint(mutant_blueprint)

# Add a route for the root URL // Agrega una ruta para la URL raíz
@app.route('/')
def home():
    return "¡Bienvenido a la API de Mutantes! Consulta los endpoints /mutant/, /stats y /health para más información.", 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000)) 
    app.run(host='0.0.0.0', port=port)