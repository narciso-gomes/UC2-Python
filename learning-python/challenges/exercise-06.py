import random

numero_descobrir = random.randint(1, 10)

tentativas = 1
maximo_tentativas = 5

while tentativas <= maximo_tentativas:

    print(f"\nTentativa: {tentativas}/{maximo_tentativas}")

    numero = int(input("Qual o número? "))
    if numero == numero_descobrir:
        print(f"Parabéns! \nVocê acertou o número: {numero_descobrir}")
        print(numero_descobrir)
        break

    if numero > numero_descobrir:
        print("O número é MENOR")

    if numero < numero_descobrir:
        print("O número é MAIOR")

    tentativas += 1
else:
    print(f"Número de tentativas esgotadas\n O número era: {numero_descobrir}")
