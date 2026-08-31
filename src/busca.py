from time import perf_counter

from src.models.medicamento import Medicamento


def busca_sequencial(
    medicamentos: list[Medicamento],
    termo: str,
    campo: str = "nome_produto",
) -> tuple[Medicamento | None, int, float]:
    alvo = termo.strip().casefold()
    encontrado = None
    comparacoes = 0

    inicio = perf_counter()
    for medicamento in medicamentos:
        comparacoes += 1
        if alvo in getattr(medicamento, campo).casefold():
            encontrado = medicamento
            break
    tempo_ms = (perf_counter() - inicio) * 1000

    return encontrado, comparacoes, tempo_ms
