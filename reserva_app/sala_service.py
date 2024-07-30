from random import randint
from dicionario_csv import Dicionario_Csv

# Objeto padrão
def sala_modelo(codigo, capacidade, tipo, descricao):
    return {
        "codigo": codigo,
        "capacidade":capacidade,
        "ativa": True,
        "tipo": tipo,
        "descricao": descricao
    }
# -------------------------------------------------------

ARQUIVO_LISTA_SALAS = "lista_salas.csv"

def criar_sala(codigo, capacidade, tipo, descricao: dict) -> None:
    """Armazena uma sala criada no arquivo .csv

    Args:
        codigo (int): O id de número inteiro
        capacidade (int): A capacidade total da sala
        tipo (str): O tipo por extenso
        descricao (str): A descrição geral da sala

    Raises:
        ValueError: Se já possui uma sala com o código fornecido
    """

    sala = sala_modelo(codigo, capacidade, tipo, descricao)
    
    if codigo_existe(codigo):
        raise ValueError("Uma sala com esse código já existe!")

    Dicionario_Csv.salvar_dicionario_em_arquivo(sala, ARQUIVO_LISTA_SALAS)


def obter_salas() -> list[dict]:
    return Dicionario_Csv.obter_lista_dicionarios_em_csv(ARQUIVO_LISTA_SALAS)


def obter_sala(id: int) -> dict:
    return Dicionario_Csv.obter_dicionario_por_numero_linha_csv(id, ARQUIVO_LISTA_SALAS)


def atualizar_sala(id: int, nova_sala: dict) -> None:
    pass


def deletar_sala(id: int) -> None:
    Dicionario_Csv.excluir_linha_arquivo_por_padrao(f'id:{id}', ARQUIVO_LISTA_SALAS)


def codigo_existe(codigo: str) -> bool:
    """Checa se um código existe na lista de salas

    Args:
        codigo (str): O código, em formato de string. Se o valor não for passado como uma string não funciona

    Returns:
        bool: True se o código existe, False do contrário
    """

    # É necessário converter o código para se ter certeza que a comparação seja entre duas strings
    codigo = str(codigo)

    salas = obter_salas()

    for sala in salas:
        if codigo == sala['codigo']:
            return True

    return False


def criar_codigo_sala() -> str:
    """Gera um código de sala aleatório

    Returns:
        str: A string do código, sendo ele um número aleatório entre 0 e 10000
    """
    
    return randint(0, 10000)