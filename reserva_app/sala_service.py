from dicionario_csv import Dicionario_Csv

# Objeto padrão
def sala(codigo, capacidade, tipo, descricao):
    return {
        "codigo": codigo,
        "capacidade":capacidade,
        "ativa": True,
        "tipo": tipo,
        "descricao": descricao
    }
# -------------------------------------------------------

ARQUIVO_LISTA_SALAS = "lista_salas.csv"

def criar_salas(codigo, capacidade, tipo, descricao: dict) -> None:
    """Armazena uma sala criada no arquivo .csv

    Args:
        codigo (int): O id de número inteiro
        capacidade (int): A capacidade total da sala
        tipo (str): O tipo por extenso
        descricao (str): A descrição geral da sala

    Raises:
        ValueError: Se já possui uma sala com o código fornecido
    """

    salas = obter_salas()

    sala_dic = sala(codigo, capacidade, tipo, descricao)

    chaves_dicionario = [key for key in salas]

    # Verifica se uma reserva com esse código já foi criada
    codigo_ja_existe = sala_dic['codigo'] in chaves_dicionario
    
    if codigo_ja_existe:
        raise ValueError("Uma sala com esse código já existe!")

    Dicionario_Csv.salvar_dicionario_em_arquivo(sala_dic, ARQUIVO_LISTA_SALAS)


def obter_salas() -> list[dict]:
    return Dicionario_Csv.obter_lista_dicionarios_em_csv(ARQUIVO_LISTA_SALAS)


def obter_sala(id: int) -> dict:
    return Dicionario_Csv.obter_dicionario_por_numero_linha_csv(id, ARQUIVO_LISTA_SALAS)


def atualizar_sala(id: int, nova_sala: dict) -> None:
    pass


def deletar_sala(id: int) -> None:
    Dicionario_Csv.excluir_linha_arquivo_por_padrao(f'id:{id}', ARQUIVO_LISTA_SALAS)
