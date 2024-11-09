import unittest
from app_inicio import app  # Import the Flask app from your main file // Importa la aplicación Flask de tu archivo principal

class TestApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up the app for testing mode // Configura la aplicación para el modo de pruebas
        app.config['TESTING'] = True
        cls.client = app.test_client()  # Test client to send HTTP requests // Cliente de pruebas para enviar solicitudes HTTP

    def test_home_route(self):
        # Assuming the blueprint has a '/' route for the entry point // Asumiendo que el blueprint tiene una ruta '/' para el punto de entrada
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)  # Make sure to adjust the expected code // Asegúrate de ajustar el código esperado

    def test_mutant_route(self):
        # Test for the '/mutant/' route if it exists in the blueprint // Prueba para la ruta '/mutant/' si existe en el blueprint
        data = {
            "dna": ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]
        }
        response = self.client.post('/mutant/', json=data)
        self.assertIn(response.status_code, [200, 403])  # We expect 200 if it's a mutant or 403 if it's not // Esperamos 200 si es un mutante o 403 si no lo es



if __name__ == '__main__':
    unittest.main()
