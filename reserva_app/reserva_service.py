from dicionario_csv import Dicionario_Csv

# Objeto padrão
def reserva(codigo, usuario, sala, data_hora_inicio, data_hora_fim):
    reserva = dict()
    {
        "codigo": codigo,
        "usuario": usuario,
        "sala": sala,
        "data e hora de inicio": data_hora_inicio,
        "data e hora do fim": data_hora_fim,
        "ativa": True
    }
# -------------------------------------------------------

ARQUIVO_LISTA_RESERVAS = "lista_reservas.csv"

def criar_reservas(reserva: dict) -> None:
    pass


def obter_reservas() -> list[dict]:
    return Dicionario_Csv.obter_lista_dicionarios_em_csv(ARQUIVO_LISTA_RESERVAS)


def obter_reserva(id: int) -> dict:
    return Dicionario_Csv.obter_dicionario_por_numero_linha_csv(id, ARQUIVO_LISTA_RESERVAS)


def atualizar_reserva(id: int, nova_reserva: dict) -> None:
    pass


def deletar_reserva(id: int) -> None:
    Dicionario_Csv.excluir_linha_arquivo_por_padrao(f'id:{id}', ARQUIVO_LISTA_RESERVAS)
