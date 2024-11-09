import unittest
from repositories.dna_repository import DnaStorage
from database.db_connection import get_db
from models.dna_model import Dna

class TestDnaStorage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Initialize the database session only once for all tests // Inicializa la sesión de la base de datos solo una vez para todas las pruebas
        cls.db_session = get_db()
        cls.repo = DnaStorage()

    def setUp(self):
        # Clean and add data before each test // Limpiar y agregar datos antes de cada prueba
        self.db_session.query(Dna).delete()
        self.db_session.commit()

        # Insert test records // Insertar registros de prueba
        sample_data = [
            Dna(dna="ATGCGA,CAGTGC,TTATGT,AGAAGG,CCCCTA,TCACTG", mutant_status=True),
            Dna(dna="GCTGTA,CAGTGC,TTGTAT,AGAGTG,CCTTTA,TCACTG", mutant_status=False),
            Dna(dna="TTTTTT,GGGGGG,CCCCCC,AAAAAA,TTTTTT,GGGGGG", mutant_status=True)
        ]
        self.db_session.bulk_save_objects(sample_data)
        self.db_session.commit()

    @classmethod
    def tearDownClass(cls):
        # Clean up test data at the end and close the session // Limpiar los datos de prueba al final y cerrar la sesión
        cls.db_session.query(Dna).delete()
        cls.db_session.commit()
        cls.db_session.close()

    def test_count_mutant_dna(self):
        self.assertEqual(self.repo.get_mutant_dna_count(), 2)  # We expect 2 mutant sequences // Esperamos 2 secuencias mutantes

    def test_count_human_dna(self):
        self.assertEqual(self.repo.get_human_dna_count(), 1)  # We expect 1 human sequence // Esperamos 1 secuencia humana

if __name__ == "__main__":
    unittest.main()
