horas_assistadas = float(input("Digite a quantidade de horas assistidas por semana: "))
valor_mensal = float(input("Digite o valor mensal da assinatura: "))

total = (valor_mensal / (horas_assistadas) * 4)

print(f"O custo por hora de entreterimento é de: {total:.2f}")

