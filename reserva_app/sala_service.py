from dicionario_csv import obter_lista_dicionarios_em_csv

# Objeto padrão

# -------------------------------------------------------

def criar_salas(sala: dict) -> None:
    pass


def obter_salas() -> list[dict]:
    return obter_lista_dicionarios_em_csv("lista_salas.csv")


def atualizar_sala(id: int, nova_sala: dict) -> None:
    pass


def deletar_sala(id: int) -> None:
    pass
