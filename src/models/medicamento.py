from dataclasses import dataclass


@dataclass
class Medicamento:
    tipo_produto: str
    nome_produto: str
    data_finalizacao_processo: str
    categoria_regulatoria: str
    numero_registro_produto: str
    data_vencimento_registro: str
    numero_processo: str
    classe_terapeutica: str
    empresa_detentora_registro: str
    situacao_registro: str
    principio_ativo: str