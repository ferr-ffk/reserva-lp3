from dicionario_csv import Dicionario_Csv

# Objeto padrão

# -------------------------------------------------------

ARQUIVO_LISTA_SALAS = "lista_salas.csv"

def criar_salas(sala: dict) -> None:
    pass


def obter_salas() -> list[dict]:
    return Dicionario_Csv.obter_lista_dicionarios_em_csv(ARQUIVO_LISTA_SALAS)


def obter_sala(id: int) -> dict:
    return Dicionario_Csv.obter_dicionario_por_numero_linha_csv(id, ARQUIVO_LISTA_SALAS)


def atualizar_sala(id: int, nova_sala: dict) -> None:
    pass


def deletar_sala(id: int) -> None:
    pass
