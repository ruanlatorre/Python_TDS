import requests #Biblioteca para requisições HTTP

cep = input("Digite o CEP (somente numeros): ")
cep = cep.replace("-", "").replace(".", "") #Vai tirar o espaço que o usuario digitar

if len(cep) != 8 or not cep.isdigit():
    print("CEP inválido, digite até 8 números")
else:
    url = f"https://viacep.com.br/ws/{cep}/json"
    resposta = requests.get(url)
    dados = resposta.json()
    
if "erro" in dados:
    print("CEP não encontrado")

else:
    logradouro = dados.get("logradouro", "")
    complemento = dados.get("complemento", "")
    bairro = dados.get("bairro", "")
    cidade = dados.get("localidade", "")
    estado = dados.get("uf", "")

    print("\n ---- Endereço encontrado")
    print(f"Logradouro: {logradouro}")
    print(f"Complemento: {complemento}")
    print(f"Bairro: {bairro}")
    print(f"Cidade: {cidade}")
    print(f"Estado {estado}")