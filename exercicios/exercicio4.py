def calcular_moeda(dolar, euro):
    valor_reais = float(input("Digite o valor em reais: "))
    calc_dolar = valor_reais / dolar
    calc_euro = valor_reais / euro

    print(f"{valor_reais} em dólar é de: {calc_dolar:.2f}. E em euros é de: {calc_euro:.2f}")
    
calcular_moeda(dolar=5.32, euro=6.16)
