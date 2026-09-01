from html import unescape
from time import perf_counter
import unicodedata

from src.models.medicamento import Medicamento


def normalizar_texto(valor: str) -> str:
    texto = unescape(valor)

    texto = texto.replace("’", "'").replace("‘", "'")

    texto = " ".join(texto.strip().casefold().split())

    texto = unicodedata.normalize("NFKD", texto)

    return "".join(
        caractere
        for caractere in texto
        if not unicodedata.combining(caractere)
    )


def preparar_busca_binaria(
    medicamentos: list[Medicamento],
) -> list[Medicamento]:
    return sorted(
        medicamentos,
        key=lambda medicamento: normalizar_texto(
            medicamento.nome_produto
        ),
    )


def busca_binaria(
    medicamentos_ordenados: list[Medicamento],
    termo: str,
) -> tuple[Medicamento | None, int, float]:
    alvo = normalizar_texto(termo)

    inicio = 0
    fim = len(medicamentos_ordenados) - 1
    comparacoes = 0
    encontrado = None

    tempo_inicio = perf_counter()

    while inicio <= fim:
        meio = (inicio + fim) // 2
        medicamento = medicamentos_ordenados[meio]
        nome = normalizar_texto(medicamento.nome_produto)

        comparacoes += 1

        if nome == alvo:
            encontrado = medicamento
            fim = meio - 1
        elif alvo < nome:
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
    alvo = normalizar_texto(termo)
    encontrado = None
    comparacoes = 0

    inicio = perf_counter()
    for medicamento in medicamentos:
        comparacoes += 1
        if alvo == normalizar_texto(getattr(medicamento, campo)):
            encontrado = medicamento
            break
    tempo_ms = (perf_counter() - inicio) * 1000

    return encontrado, comparacoes, tempo_ms
