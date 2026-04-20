import requests
### CRIANDO FUNÇÃO DE CONVERSÃO ###

def converter_moeda(valor, moeda_origem, moeda_destino):

    endpoint_url = f"https://api.exchangerate-api.com/v4/latest/{moeda_origem}"

    try:
        resposta = requests.get(endpoint_url, timeout=5)
        resposta.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise Exception(f"Erro na Requisição API: {e}")

    resposta_dict = resposta.json()

    if moeda_destino not in resposta_dict['rates']:
        raise ValueError("Moeda de destino inválida")
    
    moeda_dest = float(resposta_dict["rates"][moeda_destino])

    conversao = valor * moeda_dest    
    
    return conversao
    
resultado = converter_moeda(15,"BRL","USD")

print(f'Valor Convertido: {resultado:.2f}')