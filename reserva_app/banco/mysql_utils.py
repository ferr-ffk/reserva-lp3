from mysql.connector import *
from banco import *


def executar_sql(conexao: MySQLConnection, sql: str) -> None:
    """Executa um sql em uma conexão estabelecida.

    Args:
        conexao (MySQLConnection): A conexão que será utilizada
        sql (str): A string do SQL a ser executado
    """

    cursor = conexao.cursor(dictionary=True)
    cursor.execute(sql)

    resultado = []

    for registro in cursor:
        resultado.append(registro)

    conexao.commit()

    return resultado
