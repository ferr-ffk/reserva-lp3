from datetime import datetime
from banco.banco import abrir_conexao, fechar_conexao
from utils.mysql_utils import executar_sql
from utils.datetime_utils import *

# Objeto padrão
def reserva_modelo(codigo, usuario, sala, data_hora_inicio, data_hora_fim):
    return {
        "codigo": codigo,
        "usuario": usuario,
        "sala": sala,
        "data_e_hora_de_inicio": data_hora_inicio,
        "data_e_hora_do_fim": data_hora_fim,
        "ativa": True
    }

# -------------------------------------------------------

def criar_reserva(id_usuario, codigo_sala, data_hora_inicio, data_hora_fim) -> None:
    """Persiste uma reserva no banco de dados

    Args:
        usuario (str): O id do usuário responsável pela reserva
        codigo_sala (int): O código da sala
        data_hora_inicio (str): O horário de início da reserva
        data_hora_fim (str): O horário de término da reserva

    Raises:
        ValueError: Se uma reserva já possuir esse código
    """
    
    conexao = abrir_conexao("localhost", "root", "123456", "teste_python")

    data_inicio_format = converter_datetime_str_mysl(data_hora_inicio)
    data_fim_format = converter_datetime_str_mysl(data_hora_fim)

    sql = f"INSERT INTO `reserva` (`id_usuario`, `codigo_sala`, `data_hora_inicio`, `data_hora_fim`) VALUES (\"{id_usuario}\", \"{codigo_sala}\", \"{data_inicio_format}\", \"{data_fim_format}\")"

    executar_sql(conexao, sql)

    fechar_conexao(conexao)


def obter_reservas() -> list[dict]:
    conexao = abrir_conexao("localhost", "root", "123456", "teste_python")

    resultado = executar_sql(conexao, "SELECT * FROM reserva")

    fechar_conexao(conexao)

    return resultado


def obter_reserva(id: int) -> dict:
    pass


def atualizar_reserva(id: int, nova_reserva: dict) -> None:
    pass


def deletar_reserva(id: int) -> None:
    pass


def codigo_existe(codigo: str) -> bool:
    """Checa se um código existe na lista de reservas

    Args:
        codigo (str): O código, em formato de string. Se o valor não for passado como uma string não funciona

    Returns:
        bool: True se o código existe, False do contrário
    """

    # É necessário converter o código para se ter certeza que a comparação seja entre duas strings
    codigo = str(codigo)

    reservas = obter_reservas()

    for reserva in reservas:
        if codigo == reserva['codigo']:
            return True

    return False

if __name__ == "__main__":
    agora = datetime.datetime.now()

    # criar_reserva(1, 1, agora, agora)

    reservas = obter_reservas()

    print(reservas)