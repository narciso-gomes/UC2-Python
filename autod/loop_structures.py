print("Estruturas de repetições em python")

print("1: Lista de números com intervalos até limite")
print("2: Soma de números")
print("0: Sair")

sair = False


def lista_numeros():
    numero_limite = int(input("Número limite: "))
    intervalo = int(input("Intervalo: "))
    total = 0
    while total <= numero_limite:
        print(total)
        total += intervalo


def soma_valores():
    soma = 0
    total_somas = int(input("Total de somas: "))
    for cont in range(total_somas):
        n = float(input("Informe um número: "))
        soma += n
    print(soma)


while not sair:
    opcao = int(input("Opção: "))

    match opcao:
        case 0:
            sair = True
        case 1:
            lista_numeros()
        case 2:
            soma_valores()
