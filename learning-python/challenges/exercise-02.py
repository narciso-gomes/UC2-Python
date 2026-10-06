print('Imprimir os números de 1 a 10:')
for numero in range(1, 11):
    print(numero)
    
print('\nImprimir apenas os números pares de 2 a 20:')
for numero in range(2, 21):
    if numero % 2 == 0:
        print(numero)

print('\nImprimir uma contagem regressiva de 10 até 1:')
for numero in range(10, 0, -1):
    print(numero)