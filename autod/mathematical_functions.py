import math

print("Teste de funções matemáticas do Python")
print("Funções disponíveis: ")
print("00: Sair do programa")
print("01: ceil(x) - Retorna o teto de x")
print("02: floor(x) - Retorna o piso de x")
print("03: trunc(x) - Retorna a parte inteira de x")
print("04: exp(x) - Retorna e×")
print("05: log(x, b) - Logaritmo de x em uma base b. Sem b = logaritmo natura de x")
print("06: sqrt(x) - Retorna a raiz quadrada de x")
print("07: pi - retorna o valor de π")
print("08: Resolver função do segundo grau")

sair = False

while not sair:

    numero_funcao = int(input("Número função: "))

    match numero_funcao:
        case 0:
            sair = True

        case 8:
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
