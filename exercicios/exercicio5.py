valor_camisa = 12.50
calcular = 0
quantidade_camisa = int(input("Digite a quantidade de camisas a ser comprada: "))

if quantidade_camisa < 6:
    calcular = (valor_camisa * quantidade_camisa) - ((valor_camisa * quantidade_camisa) * 3 / 100)
    print(f"O valor total deu: {calcular:.2f}")
elif quantidade_camisa > 5 and quantidade_camisa <= 10:
    calcular = (valor_camisa * quantidade_camisa) - ((valor_camisa * quantidade_camisa) * 5 / 100)
    print(f"O valor total deu: {calcular:.2f}")
else:
    calcular = (valor_camisa * quantidade_camisa) - ((valor_camisa * quantidade_camisa) * 7 / 100)
    print(f"O valor total deu: {calcular:.2f}")


