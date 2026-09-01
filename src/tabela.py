from html import unescape
from rich import box
from rich.console import Console
from rich.table import Table

from src.models.medicamento import Medicamento

console = Console()

def tabela_medicamento(medicamento: Medicamento) -> Table:
    tabela = Table(box=box.SQUARE)
    tabela.add_column("CAMPO")
    tabela.add_column("VALOR")

    tabela.add_row("PRODUTO", unescape(medicamento.nome_produto).upper())
    tabela.add_row("REGISTRO", medicamento.numero_registro_produto.upper())
    tabela.add_row("SITUACAO", medicamento.situacao_registro.upper())
    tabela.add_row("CATEGORIA", medicamento.categoria_regulatoria.upper())
    tabela.add_row("CLASSE", medicamento.classe_terapeutica.upper())
    tabela.add_row("EMPRESA", medicamento.empresa_detentora_registro.upper())
    return tabela


def tabela_metricas(
    comparacoes_sequencial: int,
    tempo_sequencial: float,
    comparacoes_binaria: int,
    tempo_binaria: float,
) -> Table:
    tabela = Table(box=box.SQUARE)
    tabela.add_column("ALGORITMO")
    tabela.add_column("COMPARACOES", justify="right")
    tabela.add_column("TEMPO", justify="right")

    tabela.add_row(
        "SEQUENCIAL",
        str(comparacoes_sequencial),
        f"{tempo_sequencial:.4f} MS",
    )

    tabela.add_row(
        "BINARIA",
        str(comparacoes_binaria),
        f"{tempo_binaria:.4f} MS",
    )

    return tabela
