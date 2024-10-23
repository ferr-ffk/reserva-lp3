from banco.banco import abrir_conexao, fechar_conexao
from banco.mysql_utils import executar_sql

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

def criar_sala(codigo: str, capacidade: int, tipo: str, descricao: str) -> None:
    """Armazena uma sala criada no arquivo .csv

    Args:
        codigo (int): O id de número inteiro
        capacidade (int): A capacidade total da sala
        tipo (str): O tipo por extenso
        descricao (str): A descrição geral da sala
    """

    conexao = abrir_conexao("localhost", "estudante1", "123", "teste_python")

    sql = f"INSERT INTO `sala` (`codigo`, `capacidade`, `tipo`, `descricao`) VALUES (\"{codigo}\", {capacidade}, \"{tipo}\", {descricao})"

    executar_sql(conexao, sql)

    fechar_conexao(conexao)


def obter_salas() -> list:
    """Obtém todas as salas persistidas

    Returns:
        list: A lista de todas as salas
    """

    conexao = abrir_conexao("localhost", "estudante1", "123", "teste_python")

    sql = f"SELECT * FROM `sala`"

    return executar_sql(conexao, sql)


def obter_sala(id: int) -> dict:
    pass


def atualizar_sala(id: int, nova_sala: dict) -> None:
    pass


def deletar_sala(id: int) -> None:
    pass


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
