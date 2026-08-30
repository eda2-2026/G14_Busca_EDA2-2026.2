from pathlib import Path

import pandas as pd

from src.models.medicamento import Medicamento


CAMINHO_PADRAO = Path("data/DADOS_ABERTOS_MEDICAMENTOS.csv")


def carregar_medicamentos(
    caminho: str | Path = CAMINHO_PADRAO,
) -> list[Medicamento]:
    df = pd.read_csv(
        caminho,
        sep=";",
        encoding="cp1252",
        dtype=str,
        keep_default_na=False,
    )

    medicamentos = []

    for _, linha in df.iterrows():
        medicamento = Medicamento(
            tipo_produto=linha["TIPO_PRODUTO"],
            nome_produto=linha["NOME_PRODUTO"],
            data_finalizacao_processo=linha["DATA_FINALIZACAO_PROCESSO"],
            categoria_regulatoria=linha["CATEGORIA_REGULATORIA"],
            numero_registro_produto=linha["NUMERO_REGISTRO_PRODUTO"],
            data_vencimento_registro=linha["DATA_VENCIMENTO_REGISTRO"],
            numero_processo=linha["NUMERO_PROCESSO"],
            classe_terapeutica=linha["CLASSE_TERAPEUTICA"],
            empresa_detentora_registro=linha["EMPRESA_DETENTORA_REGISTRO"],
            situacao_registro=linha["SITUACAO_REGISTRO"],
            principio_ativo=linha["PRINCIPIO_ATIVO"],
        )

        medicamentos.append(medicamento)

    return medicamentos