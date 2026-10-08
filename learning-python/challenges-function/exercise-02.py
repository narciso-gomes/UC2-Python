def maior_numero(lista_numeros):
    maior = 0
    for numero in lista_numeros:
        if(maior < numero):
            maior = numero

    return maior

print(maior_numero([5, 2,3,4, -1]))