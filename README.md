Estruturação do Código:

Utilizaremos as funções necessárias para a conversão de moedas.
Utilizaremos também uma API para obter as taxas de câmbio atuais.


Interface de Linha de Comando necessária para aplicação da conversão de moedas:

Permitiremos que o usuário insira a moeda de origem, a moeda de destino e o valor a ser convertido.

Na Utilização da Inteligência Artificial:

Utilizaremos a IA para sugestões de estrutura de código e funções específicas necessária para aplicação do conversor de moedas.


Passo a Passo do Desenvolvimento do conversor de moedas:

1. Configuração Inicial e Obtenção de Dados da aplicação:

Primeiramente, precisamos de uma API para obter as taxas de câmbio. Uma das opções gratuitas é a ExchangeRate-API. Vamos configurar apropriada de uma função para obter essas taxas.



import requests

def get_exchange_rat
(api_key, base_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        return data['conversion_rates'][target_currency]
    else:
        raise Exception("Erro ao obter as taxas de câmbio.")


2. Função de Conversão de Moedas:

Com a taxa de câmbio obtida, podemos criar uma função para realizar a conversão para falicitar a aplicação.



def convert_currency(amount, rate):
    return amount * rate


3. Interface de Linha de Comando:

Vamos criar uma interface simples onde o usuário pode inserir a moeda de origem, a moeda de destino e o valor a ser convertido.




def main():
    api_key = "sua_api_key_aqui"  # Substitua pela sua chave da API
    base_currency = input("Digite a moeda de origem (ex: USD): ").upper()
    target_currency = input("Digite a moeda de destino (ex: EUR): ").upper()
    amount = float(input("Digite o valor a ser convertido: "))
    
    try:
        rate = get_exchange_rate(api_key, base_currency, target_currency)
        converted_amount = convert_currency(amount, rate)
        print(f"{amount} {base_currency} é igual a {converted_amount:.2f} {target_currency}")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()


4. Relatório de Utilização da IA:

A seguir está um resumo de como a IA foi utilizada no desenvolvimento deste código:



5. Sugestão de Estrutura do Código:

A IA sugeriu a criação de funções modulares (get_exchange_rate, convert_currency) para manter o código organizado e reutilizável.


6. Implementação das Funções:


A IA ajudou a definir a estrutura da função get_exchange_rate para fazer uma solicitação HTTP e processar a resposta JSON.
A IA sugeriu a função convert_currency para realizar a multiplicação simples necessária para a conversão de moeda.


7. Interface de Linha de Comando:

A IA orientou na criação de uma interface simples e amigável, utilizando input para coletar dados do usuário e print para exibir os resultados.


8. Tratamento de Erros:

A IA sugeriu a implementação de um bloco try-except para capturar e tratar possíveis erros durante a execução de obtenção das taxas de câmbio.



Código Completo na integra:


import requests

def get_exchange_rate(api_key, base_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        return data['conversion_rates'][target_currency]
    else:
        raise Exception("Erro ao obter as taxas de câmbio.")

def convert_currency(amount, rate):
    return amount * rate

def main():
    api_key = "sua_api_key_aqui"  # Substitua pela sua chave da API
    base_currency = input("Digite a moeda de origem (ex: USD): ").upper()
    target_currency = input("Digite a moeda de destino (ex: EUR): ").upper()
    amount = float(input("Digite o valor a ser convertido: "))
    
    try:
        rate = get_exchange_rate(api_key, base_currency, target_currency)
        converted_amount = convert_currency(amount, rate)
        print(f"{amount} {base_currency} é igual a {converted_amount:.2f} {target_currency}")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
