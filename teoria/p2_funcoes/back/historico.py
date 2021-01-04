# salvar
caminho = 'teoria/p2_funcoes/logs/historico.txt'

def salvar_historico(linha:str) -> None:
    arquivo = open(caminho,'a')
    arquivo.write(f'{linha}\n')
    arquivo.close()

# listar
def ler_historico() -> list:
    lista_linhas_arquivo = []
    arquivo = open(caminho, 'r')
    for linha in arquivo:
        linha_limpa = linha.strip() # retira caracteres de escape e espacos branco (\n \t \r ' ')
        lista_dados_linha = linha_limpa.split(';') # transforma a string em uma lista de acordo com o caracter passado como argumento
        linha_formatada = f'{lista_dados_linha[0]} {lista_dados_linha[1]} {lista_dados_linha[2]} = {lista_dados_linha[3]}'
        lista_linhas_arquivo.append(linha_formatada)
    arquivo.close()
    return lista_linhas_arquivo
