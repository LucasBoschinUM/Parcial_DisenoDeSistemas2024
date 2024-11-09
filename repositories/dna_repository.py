from database.db_connection import *
from models.dna_model import Dna

class DnaStorage:
    def store_sequence(self, sequence, mutant_status):
        db_session_session = get_db()
        sequence_str = ",".join(sequence)

        # Check if the sequence is already registered // Verificar si la secuencia ya está registrada
        existing_entry = db_session_session.query(Dna).filter(Dna.dna == sequence_str).first()
        
        if existing_entry:
            return False  # Duplicated sequence, do not save // Secuencia duplicada, no guardar

        # Insert the new sequence in the database // Insertar la nueva secuencia en la base de datos
        dna = Dna(dna=sequence_str, mutant_status=mutant_status)
        db_session_session.add(dna)
        db_session_session.commit()
        return True

    def get_mutant_dna_count(self):
        db_session_session = get_db()
        # Count mutant sequences // Contar secuencias mutantes
        return db_session_session.query(Dna).filter(Dna.mutant_status.is_(True)).count()

    def get_human_dna_count(self):
        db_session_session = get_db()
        # Count human sequences // Contar secuencias humanas
        return db_session_session.query(Dna).filter(Dna.mutant_status.is_(False)).count()
