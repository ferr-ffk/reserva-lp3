from banco.banco import abrir_conexao, fechar_conexao
from banco.mysql_utils import executar_sql

def usuario_modelo(nome, email, senha):
    return {
        "nome":nome,
        "email": email,
        "senha": senha,
        "admin": False
    }

def criar_usuario(nome: str, email: str, senha: str, admin: bool = False) -> None:
    """Cria um usuário a partir das informações fornecidas

    Args:
        nome (str): O nome do usuário
        email (str): O email (único) do usuário
        senha (str): A senha do usuário
        admin (bool, optional): Se o usuário possui capacidades de administrador. Defaults to False.
    """

    conexao = abrir_conexao("localhost", "estudante1", "123", "teste_python")

    admin = str(admin).lower()

    sql = f"INSERT INTO `usuario` (`nome`, `email`, `senha`, `admin`) VALUES (\"{nome}\", \"{email}\", \"{senha}\", {admin})"

    executar_sql(conexao, sql)

    fechar_conexao(conexao)


def obter_usuarios() -> list[dict]:
    """Lista os usuários cadastrados no banco

    Returns:
        list: A lista de usuários cadastrados
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