from dicionario_csv import obter_lista_dicionarios_em_csv

# Objeto padrão

# -------------------------------------------------------

def criar_reservas(reserva: dict) -> None:
    pass


def obter_reservas() -> list[dict]:
    return obter_lista_dicionarios_em_csv("lista_reservas.csv")


def atualizar_reserva(id: int, nova_reserva: dict) -> None:
    pass


def deletar_reserva(id: int) -> None:
    pass
