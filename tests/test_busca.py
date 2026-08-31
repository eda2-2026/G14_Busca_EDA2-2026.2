from src.busca import busca_sequencial
from src.models.medicamento import Medicamento


def fabricar(nome: str) -> Medicamento:
    return Medicamento(
        tipo_produto="MEDICAMENTO",
        nome_produto=nome,
        data_finalizacao_processo="01/01/2020",
        categoria_regulatoria="Generico",
        numero_registro_produto="100",
        data_vencimento_registro="01/01/2030",
        numero_processo="123",
        classe_terapeutica="ANTIDEPRESSIVOS",
        empresa_detentora_registro="EMPRESA X",
        situacao_registro="Ativo",
        principio_ativo=nome.lower(),
    )


BASE = [fabricar("DIPIRONA"), fabricar("FLUOXETINA"), fabricar("PARACETAMOL")]


def test_encontra_ignorando_caixa():
    encontrado, comparacoes, _ = busca_sequencial(BASE, "fluoxetina")
    assert encontrado.nome_produto == "FLUOXETINA"
    assert comparacoes == 2


def test_para_no_primeiro_encontrado():
    _, comparacoes, _ = busca_sequencial(BASE, "dipirona")
    assert comparacoes == 1


def test_nao_encontra():
    encontrado, comparacoes, _ = busca_sequencial(BASE, "ASPIRINA")
    assert encontrado is None
    assert comparacoes == 3


def test_base_vazia():
    encontrado, comparacoes, _ = busca_sequencial([], "dipirona")
    assert encontrado is None and comparacoes == 0
