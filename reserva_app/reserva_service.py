from dicionario_csv import Dicionario_Csv

# Objeto padrão
def reserva(codigo, usuario, sala, data_hora_inicio, data_hora_fim):
    return {
        "codigo": codigo,
        "usuario": usuario,
        "sala": sala,
        "data e hora de inicio": data_hora_inicio,
        "data e hora do fim": data_hora_fim,
        "ativa": True
    }

# -------------------------------------------------------

ARQUIVO_LISTA_RESERVAS = "lista_reservas.csv"

def criar_reserva(reserva: dict) -> None:
    reservas = obter_reservas()

    chaves_dicionario = [key for key in reservas]

    # Verifica se uma reserva com esse código já foi criada
    codigo_ja_existe = reserva['codigo'] in chaves_dicionario
    
    if codigo_ja_existe:
        raise ValueError("Uma reserva com esse código já existe!")

    Dicionario_Csv.salvar_dicionario_em_arquivo(reserva, ARQUIVO_LISTA_RESERVAS)


def obter_reservas() -> list[dict]:
    return Dicionario_Csv.obter_lista_dicionarios_em_csv(ARQUIVO_LISTA_RESERVAS)


def obter_reserva(id: int) -> dict:
    return Dicionario_Csv.obter_dicionario_por_numero_linha_csv(id, ARQUIVO_LISTA_RESERVAS)


def atualizar_reserva(id: int, nova_reserva: dict) -> None:
    pass


def deletar_reserva(id: int) -> None:
    Dicionario_Csv.excluir_linha_arquivo_por_padrao(f'id:{id}', ARQUIVO_LISTA_RESERVAS)
