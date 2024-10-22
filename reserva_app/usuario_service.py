from banco.banco import abrir_conexao, fechar_conexao
from banco.mysql_utils import executar_sql

def usuario_modelo(nome, email, senha):
    return {
        "nome":nome,
        "email": email,
        "senha": senha,
        "admin": False
    }

CAMINHO_ARQUIVO_USUARIOS = "lista_usuarios.csv"

def criar_usuario(nome: str, email: str, senha: str, admin: bool) -> None:
    conexao = abrir_conexao("localhost", "estudante1", "123", "teste_python")

    admin = str(admin).lower()

    sql = f"INSERT INTO `usuario` (`nome`, `email`, `senha`, `admin`) VALUES (\"{nome}\", \"{email}\", \"{senha}\", {admin})"

    executar_sql(conexao, sql)


def obter_usuarios() -> list[dict]:
    """Lista os usuários cadastrados no banco

    Args:
        conexao (MySQLConnection): _description_

    Returns:
        list: _description_
    """

    conexao = abrir_conexao("localhost", "estudante1", "123", "teste_python")

    resultado = executar_sql(conexao, "SELECT * FROM usuario")

    fechar_conexao(conexao)

    return resultado


if __name__ == "__main__":
    criar_usuario("Fernando", "freitas@gmail", "123456", True)

    usuarios = obter_usuarios()

    for usuario in usuarios:
        print(usuario)