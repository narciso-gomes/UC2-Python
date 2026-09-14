import math

def valor_fatorial(num):
    if num <= 1:
        return 1
    return num * valor_fatorial(num - 1)


def calcula_fatorial():
    numero = int(input("Informe um número: "))
    print(f"O fatorial de {numero} é {valor_fatorial(num=numero)}")


def valor_juros(capital, taxa, tempo=12):
    return capital * taxa * tempo / 100


def calcular_juros():
    print("Cálculo de juros")
    capital = float(input("Capital: "))
    taxa = float(input("Taxa: "))
    tempo = input("Tempo (12 meses padrão): ")
    if tempo == "":
        juros = valor_juros(capital, taxa)
    else:
        tempo = float(tempo)
        juros = valor_juros(capital, taxa, tempo)
    print("O valor de juros é:", juros)


def mdc():
    print("Informe dois números")

    n1 = int(input("N1: "))
    n2 = int(input("N2: "))

    if n1 < 1 or n2 < 1:
        print("Números inválidos para MDC")
    else:
        while True:
            resto = n1 % n2
            print(n1, "/", n2, "-> resto:", resto)
            if resto == 0:
                break
            n1 = n2
            n2 = resto
        print("O MDC é ", n2)


def funcao_segundo_grau():
    print("Informe os termos da equação Ax² + Bx + C")
    A = float(input("A: "))
    B = float(input("B: "))
    C = float(input("C: "))

    if A == 0:
        print("Não é uma função de segundo grau")
    else:
        delta = B**2 - 4 * A * C
        if delta < 0:
            print("A equação não tem raízes")
        elif delta == 0:
            x1 = B * (-1) / 2 * A
            print("A equação possui a raiz: ", x1)
        else:
            raiz_delta = math.sqrt(delta)
            x1 = (B * (-1) + raiz_delta) / 2 * A
            x2 = (B * (-1) - raiz_delta) / 2 * A
            print("A equação possui duas raízes: ")
            print("x1=", x1)
            print("x2=", x2)


