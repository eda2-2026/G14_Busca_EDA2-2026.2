from src.busca import busca_binaria, preparar_busca_binaria
from src.models.medicamento import Medicamento


def fabricar(nome: str, registro: str = "100") -> Medicamento:
    return Medicamento(
        tipo_produto="MEDICAMENTO",
        nome_produto=nome,
        data_finalizacao_processo="01/01/2020",
        categoria_regulatoria="Generico",
        numero_registro_produto=registro,
        data_vencimento_registro="01/01/2030",
        numero_processo="123",
        classe_terapeutica="CLASSE TESTE",
        empresa_detentora_registro="EMPRESA X",
        situacao_registro="Ativo",
        principio_ativo=nome.lower(),
    )


BASE_BINARIA = [
    fabricar("AMOXICILINA"),
    fabricar("DIPIRONA"),
    fabricar("FLUOXETINA"),
    fabricar("IBUPROFENO"),
    fabricar("PARACETAMOL"),
    fabricar("PREDNISONA"),
    fabricar("SERTRALINA"),
]


def test_prepara_base_em_ordem_alfabetica():
    base = [
        fabricar("PARACETAMOL"),
        fabricar("AMOXICILINA"),
        fabricar("IBUPROFENO"),
    ]

    ordenados = preparar_busca_binaria(base)

    assert [m.nome_produto for m in ordenados] == [
        "AMOXICILINA",
        "IBUPROFENO",
        "PARACETAMOL",
    ]


def test_encontra_elemento_do_meio():
    encontrado, comparacoes, _ = busca_binaria(BASE_BINARIA, "ibuprofeno")

    assert encontrado is not None
    assert encontrado.nome_produto == "IBUPROFENO"
    assert comparacoes == 3


def test_encontra_primeiro_elemento():
    encontrado, comparacoes, _ = busca_binaria(BASE_BINARIA, "AMOXICILINA")

    assert encontrado is not None
    assert encontrado.nome_produto == "AMOXICILINA"
    assert comparacoes <= 3


def test_encontra_ultimo_elemento():
    encontrado, comparacoes, _ = busca_binaria(BASE_BINARIA, "SERTRALINA")

    assert encontrado is not None
    assert encontrado.nome_produto == "SERTRALINA"
    assert comparacoes <= 3


def test_nao_encontra():
    encontrado, comparacoes, _ = busca_binaria(BASE_BINARIA, "ASPIRINA")

    assert encontrado is None
    assert comparacoes <= 3


def test_base_vazia():
    encontrado, comparacoes, _ = busca_binaria([], "IBUPROFENO")

    assert encontrado is None
    assert comparacoes == 0


def test_ignora_acentos_e_entidades_html():
    base = preparar_busca_binaria(
        [
            fabricar("&#211;LEO MINERAL"),
            fabricar("PARACETAMOL"),
        ]
    )

    encontrado, _, _ = busca_binaria(base, "oleo mineral")

    assert encontrado is not None
    assert encontrado.nome_produto == "&#211;LEO MINERAL"