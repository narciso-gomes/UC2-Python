from mathematical_functions import *

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
print("09: Resolver MDC")
print("10: Calcular juros")
print("11: Calcular fatorial")

sair = False

while not sair:
    try:
        numero_funcao = int(input("Número função: "))

        match numero_funcao:
            case 0:
                sair = True
            case 8:
                funcao_segundo_grau()
            case 9:
                mdc()
            case 10:
                calcular_juros()
            case 11:
                calcula_fatorial()

    except Exception as e:
        print(e)
        print("Ocorreu um erro")
    except ValueError as e:
        print(e)
        print("Número inválido")
