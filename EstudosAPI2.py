import pandas as pd
import requests as rq

#####-----------LENDO CSV---------#####
def lerCSV(caminho):
    print("Lendo CSV...")
    File_csv = pd.read_csv(caminho)

    return File_csv
#####------CONSUMO DE API-----#####

def converterMoedas(valor, moedaOrigem):

# CHAMADA DE API E JSON
 
    endpoint_url = f'https://api.exchangerate-api.com/v4/latest/{moedaOrigem}'
    response = rq.get(endpoint_url, timeout=5)
    print("-"*10)
    print(f'O status da requisição foi - {response.status_code}')
    print("-"*10)

#TRATAMENTO DE ERRO NA REQUISIÇÃO
    try:
        response.raise_for_status()
    except rq.exceptions.HTTPError:
        raise ValueError(f"Moeda Inválida - {moedaOrigem}")
    
    dados = response.json()

# CAPTURA DA COTAÇÃO DO REAL PARA A MOEDA EM EXECUÇÃO
    
    moedaBRl = float(dados['rates']['BRL'])
# CALCULO DA CONVERSÃO PARA REAL
    conversao = valor * moedaBRl

    return conversao

def processarPedidos(caminho):

# PROCESSAMENTO DE ITEM A ITEM DO CSV
    csv = lerCSV(caminho)
    for _, linha in csv.iterrows():
        
        pessoa = linha['Cliente']
        valor = linha['Valor']
        moedaOrigem = linha['Moeda'] 
        try:
            result = converterMoedas(valor, moedaOrigem)
        except ValueError as v:
            print(v)
            continue

        print(f'A conversão de {pessoa} do valor {valor} {moedaOrigem} convertido para BRL foi de: {result:.2f}')

processarPedidos("C:/Users/jonha/Desktop/Teste.csv")
print("-"*10)