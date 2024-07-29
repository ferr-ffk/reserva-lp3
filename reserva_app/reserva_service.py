from dicionario_csv import Dicionario_Csv

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

ARQUIVO_LISTA_RESERVAS = "lista_reservas.csv"

def criar_reserva(codigo, usuario, sala, data_hora_inicio, data_hora_fim) -> None:
    """Cria uma reserva e armazena no arquivo .csv

    Args:
        codigo (int): O código da sala em um número inteiro
        usuario (str): O nome do usuário responsável pela reserva
        sala (int): O código da sala
        data_hora_inicio (str): O horário de início da reserva
        data_hora_fim (str): O horário de término da reserva

    Raises:
        ValueError: Se uma reserva já possuir esse código
    """

    reserva = reserva_modelo(codigo, usuario, sala, data_hora_inicio, data_hora_fim)
    
    if codigo_existe(codigo):
        raise ValueError("Uma reserva com esse código já existe!")

    Dicionario_Csv.salvar_dicionario_em_arquivo(reserva, ARQUIVO_LISTA_RESERVAS)


def obter_reservas() -> list[dict]:
    return Dicionario_Csv.obter_lista_dicionarios_em_csv(ARQUIVO_LISTA_RESERVAS)


def obter_reserva(id: int) -> dict:
    return Dicionario_Csv.obter_dicionario_por_padrao(f'id:{id}', ARQUIVO_LISTA_RESERVAS)


def atualizar_reserva(id: int, nova_reserva: dict) -> None:
    pass


def deletar_reserva(id: int) -> None:
    Dicionario_Csv.excluir_linha_arquivo_por_padrao(f'id:{id}', ARQUIVO_LISTA_RESERVAS)


def codigo_existe(codigo: str) -> bool:
    """Checa se um código existe na lista de reservas

    Args:
        codigo (str): O código, em formato de string. Se o valor não for passado como uma string não funciona

    Returns:
        bool: True se o código existe, False do contrário
    """

    reservas = obter_reservas()

    for reserva in reservas:
        if codigo == reserva['codigo']:
            return True

    return False