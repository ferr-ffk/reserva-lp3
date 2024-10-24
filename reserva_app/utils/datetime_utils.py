import datetime


def converter_datetime_str_mysl(data: datetime) -> str:
    """Converte um objeto datetime em uma string para que possa ser inserida no MySQL

    Args:
        data (datetime): O objeto a ser transformado

    Returns:
        str: A string, já formatada no padrão de datetime do MySQL
    """

    return data.strftime('%Y-%m-%d %H:%M:%S')

