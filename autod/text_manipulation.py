print("Manipulação de dados textuais")
print("------------------")
print("01 - find(subtexto, inicio, fim)")
print("02 - format(X1, ..., Xn)")
print("03 - lower()")
print("04 - replace(str_procurar, str_substituir, numero_ocorrencias)")
print("------------------")

numero_funcao = int(input("Informe a função: "))

match numero_funcao:
    case 1:
        texto = str(input("Informe o texto: "))
        pesquisa = str(input("Informe a pesquisa: "))
        posicao_inicial = int(input("Informe a posição inicial: "))
        posicao_final = int(input("Informe a posição final: "))
        achou = texto.find(pesquisa, posicao_inicial, posicao_final)
        print(achou)

    case 2:
        texto = str(input("Informe o texto: "))
        posicao1 = str(input("Posição 01: "))
        posicao2 = str(input("Posição 02: "))
        resultado = texto.format(posicao1, posicao2)
        print(resultado)

    case 3:
        texto = str(input("Informe o texto: "))
        texto_caixa_baixa = texto.lower()
        print(texto_caixa_baixa)

    case 4:
        texto = str(input("Informe o texto: "))
        str_busca = str(input("Informe o texto de busca: "))
        str_substituir = str(input("Informe o texto que vai substituir a busca: "))
        numero_ocorrencias = int(input("Número de ocorrências (-1 para todas): "))
        resultado = texto.replace(str_busca, str_substituir, numero_ocorrencias)
        print(resultado)
