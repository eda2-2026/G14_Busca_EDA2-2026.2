from src.busca import (
    busca_binaria,
    busca_sequencial,
    preparar_busca_binaria,
)
from src.data.loader import carregar_medicamentos
from src.tabela import console, tabela_medicamento, tabela_metricas


def main() -> None:
    medicamentos = carregar_medicamentos()
    medicamentos_ordenados = preparar_busca_binaria(medicamentos)

    console.print(f"BASE CARREGADA: {len(medicamentos)} REGISTROS.\n")

    while True:
        termo = console.input("NOME DO MEDICAMENTO: ").strip()

        encontrado_sequencial, comparacoes_sequencial, tempo_sequencial = (
            busca_sequencial(medicamentos, termo)
        )

        encontrado_binaria, comparacoes_binaria, tempo_binaria = busca_binaria(
            medicamentos_ordenados,
            termo,
        )

        encontrado = encontrado_sequencial or encontrado_binaria

        if encontrado:
            console.print(tabela_medicamento(encontrado))
        else:
            console.print(f"NENHUM REGISTRO COM '{termo.upper()}'.\n")

        console.print(
            tabela_metricas(
                comparacoes_sequencial,
                tempo_sequencial,
                comparacoes_binaria,
                tempo_binaria,
            )
        )

        resposta = console.input("\nBUSCAR OUTRO? [S/N]: ").strip().upper()
        console.print()

        if resposta != "S":
            break


if __name__ == "__main__":
    main()