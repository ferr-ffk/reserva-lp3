from dicionario_csv import Dicionario_Csv

def usuario_modelo(nome, email, senha):
    return {
        "nome":nome,
        "email": email,
        "senha": senha,
        "admin": False
    }

CAMINHO_ARQUIVO_USUARIOS = "lista_usuarios.csv"

def criar_usuario(nome, email, senha) -> None:
    usuario = usuario_modelo(nome, email, senha)

    Dicionario_Csv.salvar_dicionario_em_arquivo(usuario, CAMINHO_ARQUIVO_USUARIOS)


def obter_usuarios() -> list[dict]:
    return Dicionario_Csv.obter_lista_dicionarios_em_csv(CAMINHO_ARQUIVO_USUARIOS)