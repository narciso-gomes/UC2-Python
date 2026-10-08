def media(*notas):
    total_notas = len(notas)
    soma = sum(notas)
    media = soma / total_notas

    if media >= 7:
        resultado = "Aprovado"
    elif media >= 5:
        resultado = "Recuperação"
    else:
        resultado = "Reprovado"

    return {"Média": media, "Resultado": resultado}


print(media(1, 2))
print(media(10,8,5,8))
print(media(5,5,5,10))