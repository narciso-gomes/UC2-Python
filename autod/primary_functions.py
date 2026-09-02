print("Teste de funções padrões do Python")
print("Funções disponíveis: ")
print("01: abs(n) - Retorna o valor absoluto de n")
print("02: chr(n) - Retorna o caractere representado pelo número n")
print("03: ord(c) - Retorna o código correspondente ao caractere c")
print("04: round(n,d) - Arredonda n considerando d casas decimais")
print("05: type(o) - retorna o tipo de o")

numero_funcao = int(input("Escolha o número da função que deseja testar: "))

match numero_funcao:
    case 1:
        valor = int(input("Informe o número que deseja o valor absoluto: "))
        valor_absoluto = abs(valor)
        print("O valor absoluto de", valor, "é", valor_absoluto)
    case 2:
        valor = int(input("Informe a número que deseja saber a representação em caractere usando a tabela Unicode: "))
        caractere_numero = chr(valor)
        print("O valor que representa o caractere do número", valor, "é", repr(caractere_numero))
    case 3:
        caractere = str(input("Informe o caractere: "))
        codigo_caractere = ord(caractere)
        print("O código correspondente para o caractere", caractere, "é", repr(codigo_caractere))
    case 4:
        valor = float(input("Informe o valor que deseja arredondar: "))
        total_casas_decimais = int(input("Informe o total de casas decimais: "))
        valor_arredondado = round(valor, total_casas_decimais)
        print("O valor", valor, "arredondado usando", total_casas_decimais, "casas decimais é", valor_arredondado)
    case 5:
        valor = input("Informe um valor: ")
        tipo_valor = type(valor)
        print("O tipo do valor", valor, "é",tipo_valor)
        