# from datetime import datetime

# ano_atual = datetime.now().year
# clube = "SPFC"
# campeonato_mundial = 3
# ano_fundacao = 1930

# print(f"{clube} possui {campeonato_mundial} títulos mundiais. São {ano_atual - ano_fundacao} anos de existência")

# escola = "SENAI"
# curso = "Técnico em Desenvolvimento de Sistema"
# unidade_curricular = "Lógica de Programação e Algoritmos"

# print(f"Escola: {escola} \n Curso: {curso} \n Unidade Curricular: {unidade_curricular}")

# print(f"Matrícula do Junior é {25:06d}. ")
# print(f"Matrícula do Alice é {14785:06d}. ")
# print(f"Matrícula do José é {100258:06d}. ")

print(f"Programa de empréstimos. "
      f"Responda: (0-Não ou 1-Sim)")

nome_negativo = int(input("Possui nome negativado? "))

if nome_negativo == 1:
    print("Você não pode realizar empréstimo: ")
else:
    carteira_assinada = int(input("Possui carteira assinada? "))
    if carteira_assinada == 0:
        print("Não pode realizar empréstimo ")
    else:
        possui_casa_propria = int(input("Possui casa própria? "))
        if possui_casa_propria == 0:
            print("Não pode realizar empréstimo")
        else:
            print("Conceder empréstimo")
