from repositories.dna_repository import DnaStorage


class MutantService:
    def __init__(self):
        self.repository = DnaStorage()

    def mutant_status(self, dna):
        n = len(dna)
        sequences_found = 0

        # Check rows // Verificar filas
        for row in dna:
            if self._has_sequence(row):
                sequences_found += 1
            if sequences_found > 1:
                return True

        # Check columns // Verificar columnas
        for col in range(n):
            column = ''.join([dna[row][col] for row in range(n)])  # Column as string // Columna como cadena
            if self._has_sequence(column):
                sequences_found += 1
            if sequences_found > 1:
                return True

        # Check diagonals from left to right and right to left // Verificar diagonales de izquierda a derecha y de derecha a izquierda
        for i in range(n - 3):
            for j in range(n - 3):
                # Diagonal from left to right // Diagonal de izquierda a derecha
                if dna[i][j] == dna[i + 1][j + 1] == dna[i + 2][j + 2] == dna[i + 3][j + 3]:
                    sequences_found += 1
                # Diagonal from right to left // Diagonal de derecha a izquierda
                if dna[i][j + 3] == dna[i + 1][j + 2] == dna[i + 2][j + 1] == dna[i + 3][j]:
                    sequences_found += 1
                if sequences_found > 1:
                    return True

        return False  # If more than one sequence was not found, it is not a mutant // Si no se encontró más de una secuencia, no es un mutante

    def _has_sequence(self, sequence):
        """Verifica si hay una secuencia de cuatro letras iguales consecutivas en una fila o columna.  // Check if there is a sequence of four consecutive equal letters in a row or column."""
        count = 1
        for i in range(1, len(sequence)):
            if sequence[i] == sequence[i - 1]:
                count += 1
                if count == 4:
                    return True
            else:
                count = 1
        return False

    def store_sequence(self, dna, mutant_status):
        return self.repository.store_sequence(dna, mutant_status)

    def retrieve_stats(self):
        get_mutant_dna_count = self.repository.get_mutant_dna_count()
        get_human_dna_count = self.repository.get_human_dna_count()
        ratio = get_mutant_dna_count / get_human_dna_count if get_human_dna_count > 0 else 0
        return {
            "get_mutant_dna_count": get_mutant_dna_count,
            "get_human_dna_count": get_human_dna_count,
            "ratio": ratio
        }
