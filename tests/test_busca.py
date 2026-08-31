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
    encontrados, comparacoes, _ = busca_sequencial(BASE, "fluoxetina")
    assert len(encontrados) == 1
    assert comparacoes == 3


def test_nao_encontra():
    encontrados, _, _ = busca_sequencial(BASE, "ASPIRINA")
    assert encontrados == []


def test_base_vazia():
    encontrados, comparacoes, _ = busca_sequencial([], "dipirona")
    assert encontrados == [] and comparacoes == 0
