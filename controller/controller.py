from flask import Blueprint, request, jsonify
from services.mutant_service import MutantService

# Create the Blueprint for the mutant routes // Crear el Blueprint para las rutas de mutantes
mutant_blueprint = Blueprint('mutant', __name__)
service = MutantService()

@mutant_blueprint.route('/mutant/', methods=['POST'])
def analyze_dna():
    # Get the JSON data from the request // Obtener los datos JSON de la solicitud
    request_data = request.get_json()
    sequence = request_data.get("dna")

    # Validate the DNA sequence // Validar la secuencia de ADN
    if not sequence:
        return jsonify({"error": "Se requiere una secuencia de ADN"}), 400

    # Check if the DNA belongs to a mutant // Verificar si el ADN pertenece a un mutante
    mutant_status = service.mutant_status(sequence)
    saved_successfully = service.store_sequence(sequence, mutant_status=mutant_status)

    # Respond according to the result // Responder de acuerdo al resultado
    if not saved_successfully:
        return jsonify({"message": "La secuencia de ADN ya existe"}), 409
    
    response_message = "Mutante detectado" if mutant_status else "No es un mutante"
    response_code = 200 if mutant_status else 403
    return jsonify({"message": response_message}), response_code

@mutant_blueprint.route('/stats', methods=['GET'])
def retrieve_stats():
    # Get and return the statistics // Obtener y devolver las estadísticas
    statistics = service.retrieve_stats()
    return jsonify(statistics)

@mutant_blueprint.route('/health', methods=['GET'])
def check_health():
    # Check the health status of the service // Verificar el estado de salud del servicio
    return jsonify({"status": "saludable"}), 200
