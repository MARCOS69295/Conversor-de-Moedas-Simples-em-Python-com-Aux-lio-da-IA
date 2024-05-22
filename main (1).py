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
