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
        
        
if __name__ == "__main__":
    # salvar_dicionario_em_arquivo({
    #     "nome": "Davi Gomes",
    #     "idade": 82741,
    #     "apelidoss": "davi, david, gomes, mr. david"
    # }, "teste.csv")
    
    print(obter_lista_dicionarios_em_csv("teste.csv"))