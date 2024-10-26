import datetime


_FORMATO_DATA = '%Y-%m-%d %H:%M'


def converter_str_datetime(s: str) -> datetime:
    """Converte uma string no formato padrão do sql em um objeto datetime

    Args:
        s (str): A string a ser convertida

    Returns:
        datetime: O objeto datetime com os valores de data e horário vindos da string
    """
    
    return datetime.datetime.strptime(s, _FORMATO_DATA)


def converter_datetime_str_mysl(data: datetime.datetime) -> str:
    """Converte um objeto datetime em uma string para que possa ser inserida no MySQL

    Args:
        data (datetime): O objeto a ser transformado

    Returns:
        str: A string, já formatada no padrão de datetime do MySQL
    """

    return data.strftime(_FORMATO_DATA)


def obter_formato_data() -> str:
    """Obtém o formato que é utilizado para fazer a conversão

    Returns:
        str: A string do formato
    """
    
    return _FORMATO_DATA


def set_formato_data(novo_formato: str) -> None:
    """Define um novo valor para o formato a ser utilizado para fazer a conversão, seguindo a tabela:
    <table>
        <tr><td>%Y</td> <td>(Ano)</td></tr>
        <tr><td>%m</td> <td>(Mês)</td></tr>
        <tr><td>%d</td> <td>(Dia)</td></tr>
        <tr><td>%H</td> <td>(Hora)</td></tr>
        <tr><td>%M</td><td>(Minuto)</td></tr>
        <tr><td>%S</td><td> (Segundo)</td></tr>
    </table>

    Args:
        novo_formato (str): O novo formato 
    """
    
    _FORMATO_DATA = novo_formato