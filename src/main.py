from src.busca import busca_sequencial
from src.data.loader import carregar_medicamentos
from src.tabela import console, tabela_medicamento, tabela_metricas

def main() -> None:
    medicamentos = carregar_medicamentos()
    console.print(f"BASE CARREGADA: {len(medicamentos)} REGISTROS.\n")

    while True:
        termo = console.input("NOME DO MEDICAMENTO: ").strip()
        encontrado, comparacoes, tempo_ms = busca_sequencial(medicamentos, termo)

        if encontrado:
            console.print(tabela_medicamento(encontrado))
        else:
            console.print(f"NENHUM REGISTRO COM '{termo.upper()}'.\n")

        console.print(tabela_metricas(comparacoes, tempo_ms))

        resposta = console.input("\nBUSCAR OUTRO? [S/N]: ").strip().upper()
        console.print()
        if resposta != "S":
            break


if __name__ == "__main__":
    main()
