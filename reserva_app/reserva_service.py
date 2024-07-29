from dicionario_csv import Dicionario_Csv

# Objeto padrão

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
    pass
