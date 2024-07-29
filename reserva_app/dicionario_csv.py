def salvar_dicionario_em_arquivo(dic: dict, caminho_arquivo: str) -> None:
    """Salva um dicionário comum em um dado arquivo .csv, de forma que cada campo corresponda à chave e ao valor. Exemplo: 'chave:valor' é um campo válido. 'chave:valor,chave:valor,chave:valor' é um exemplo de uma linha válida de um arquivo .csv dado

    Args:
        dic (dict): O dicionário a ser salvo
        caminho_arquivo (str): O caminho relativo do arquivo
    """    
    
    with open(caminho_arquivo, "a") as arquivo:
        lista_valores: list[str] = []
                
        for key in dic:
            value = dic[key]
            
            if type(value) == str:
                value = value.replace(',', ';')
                
            lista_valores.append(f'"{key}:{value}"')
            
        linha_produto = ','.join(lista_valores) + '\n'
        
        arquivo.write(linha_produto)
        
        
def obter_lista_dicionarios_em_csv(caminho_arquivo: str) -> list[dict]:
    """Obtém a lista dos objetos de dicionário de um arquivo a partir de arquivo dado

    Args:
        caminho_arquivo (str): O caminho relativo do arquivo

    Returns:
        list[dict]: A lista de dicionários
    """
    lista: list[dict] = []
    
    with open(caminho_arquivo, "r") as arquivo:
        for linha in arquivo:
            if linha == "": break
            
            lista.append(obter_dicionario_por_linha_csv(linha))
    
    return lista
        
        
def obter_dicionario_por_linha_csv(linha: str) -> dict:
    """Retorna um dicionário com base numa string formatada para arquivos .csv É necessário que a linha esteja formatada de modo que cada campo corresponda à chave e ao valor. Exemplo: 'chave:valor,chave:valor,chave:valor' é uma linha válida

    Args:
        linha (str): A linha a ser extraída o dicionário

    Returns:
        dict: O dicionário com base na linha
    """    
    
    pares: list[str] = linha.strip().split(",")
    
    dic: dict[str, int | float | str] = {}
    
    for par in pares:
        chave_valor: list[str] = par.split(":")
        
        # Remove as aspas
        chave = chave_valor[0].replace('"', '')
        valor = chave_valor[1].replace('"', '').replace(';', ',')
        
        # Obtém a chave por meio da f string para que consiga inserir no comando
        comando = f"dic.update({chave}='{valor}')"
        
        # Executa a linha de código criada
        eval(comando)
    
    return dic
        
        
def obter_dicionario_por_numero_linha_csv(n: int, caminho_arquivo: str) -> dict:
    """Obtém um dicionário com base em um arquivo dado e um número de linha

    Args:
        n (int): O índice da linha (começa em 0)
        caminho_arquivo (str): O caminho relativo do arquivo

    Raises:
        ValueError: Se n for fora do alcance das linhas do arquivo

    Returns:
        dict: O dicionário na linha 'n' 
    """
    
    with open(caminho_arquivo, "r") as arquivo:
        i: int = 0
        
        for linha in arquivo:
            if i == n: 
                return obter_dicionario_por_linha_csv(linha)
            
            i += 1
        
        raise ValueError("O número da linha não é válido!")
        

def excluir_linha_arquivo(n: int, caminho_arquivo: str) -> None:
    """Exclui uma linha de um arquivo qualquer

    Args:
        n (int): O índice da linha (começa em zero)
        caminho_arquivo (str): A string do caminho relativo do arquivo
    """
    linhas: list[str] = []

    # Armazena as linhas previamente
    with open(caminho_arquivo, "r") as arquivo:
        linhas = arquivo.readlines()
    
    with open(caminho_arquivo, "w") as arquivo:
        # A cada linha verifica se o número dela é igual ao parâmetro, se for, não adiciona no arquivo novamente
        i = 0

        for linha in linhas:

            if i == n:
                i += 1
                continue

            i += 1
            arquivo.write(linha)


def excluir_linha_arquivo_por_padrao(padrao: str, caminho_arquivo: str) -> None:
    """Exclui a linha de um arquivo por verificar se ela começa com o padrão fornecido

    Args:
        padrao (str): _description_
        caminho_arquivo (str): _description_
    """

    # Armazena as linhas previamente
    with open(caminho_arquivo, "r") as arquivo:
        linhas = arquivo.readlines()
    
    with open(caminho_arquivo, "w") as arquivo:
        # A cada linha verifica se o número dela é igual ao parâmetro, se for, não adiciona no arquivo novamente
        for linha in linhas:
            # Remove o caracter de nova linha e verifica se o padrão é o mesmo que o da linha
            if not linha.strip("\n").startswith(padrao):
                arquivo.write(linha)

if __name__ == "__main__":

    salvar_dicionario_em_arquivo({
        "nome": "Davi Gomes",
        "idade": 82741,
        "apelidoss": "davi, david, gomes, mr. david"
    }, "teste.csv")

    # salvar_dicionario_em_arquivo({
    #     "nome": "Mister",
    #     "idade": 198284,
    #     "apelidoss": "mister, master"
    # }, "teste.csv")

    # salvar_dicionario_em_arquivo({
    #     "nome": "Fernando",
    #     "idade": 19825,
    #     "apelidoss": "sei lá"
    # }, "teste.csv")

    # salvar_dicionario_em_arquivo({
    #     "nome": "Leonardo",
    #     "idade": 294836,
    #     "apelidoss": "leleo, leo"
    # }, "teste.csv")
    
    print(obter_lista_dicionarios_em_csv("teste.csv"))
    
    # print(obter_dicionario_por_numero_linha_csv(0, "teste.csv"))

    # excluir_linha_arquivo(0, "teste.csv")

    # excluir_linha_arquivo_por_padrao("\"nome:Davi Gomes\"", "teste.csv")

    print(obter_lista_dicionarios_em_csv("teste.csv"))

