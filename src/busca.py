from time import perf_counter

from src.models.medicamento import Medicamento


def preparar_busca_binaria(
    medicamentos: list[Medicamento],
) -> list[Medicamento]:
    medicamentos_com_registro = [
        medicamento
        for medicamento in medicamentos
        if medicamento.numero_registro_produto.strip()
    ]

    return sorted(
    medicamentos_com_registro,
    key=lambda medicamento: int(medicamento.numero_registro_produto.strip()),
)


def busca_binaria(
    medicamentos_ordenados: list[Medicamento],
    termo: str,
) -> tuple[Medicamento | None, int, float]:
    alvo = termo.strip()

    if not alvo.isdigit():
        return None, 0, 0.0

    alvo_numero = int(alvo)

    inicio = 0
    fim = len(medicamentos_ordenados) - 1
    comparacoes = 0
    encontrado = None

    tempo_inicio = perf_counter()

    while inicio <= fim:
        meio = (inicio + fim) // 2
        medicamento = medicamentos_ordenados[meio]
        registro = int(medicamento.numero_registro_produto.strip())

        comparacoes += 1

        if registro == alvo_numero:
            encontrado = medicamento
            break

        if alvo_numero < registro:
            fim = meio - 1
        else:
            inicio = meio + 1

    tempo_ms = (perf_counter() - tempo_inicio) * 1000

    return encontrado, comparacoes, tempo_ms


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
