
def valida_senha(senha):
    totalCaracteres = 0
    totalDigitos = 0

    for c in senha:
        if(c.isdigit()):
            totalDigitos += 1
        else:
            totalCaracteres += 1
    return totalCaracteres >= 8 and totalDigitos >= 1

print(valida_senha('senha123'))
print(valida_senha('abc123'))
print(valida_senha('senhaforte'))
print(valida_senha('12345678'))
print(valida_senha('senhaBoa1'))


