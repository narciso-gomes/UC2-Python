dias_semandas = {
    "Segunda": None,
    "Terça": None,
    "Quarta": None,
    "Quinta": None,
    "Sexta": None,
    "Sábado": None,
    "Domingo": None,
}

print("Informe a temperatura de cada dia da semana: ")

for chave in dias_semandas.keys():
    temperatura = float(input(f"{chave}: "))
    dias_semandas[chave] = temperatura

maior_temperatura = max(dias_semandas.values())
menor_temperatura = min(dias_semandas.values())
media_temperatura = sum(dias_semandas.values()) / len(dias_semandas)
temperaturas_acima_media = {key: value for key, value in dias_semandas.items() if value > media_temperatura}

print(f"A maior temperatura da semana foi: {maior_temperatura}°C")
print(f"A menor temperatura da semana foi: {menor_temperatura}°C")
print(f"A média da temperatura semanal foi: {round(media_temperatura, 2)}°C")

if(len(temperaturas_acima_media.keys()) > 0):
    print("As temperaturas acima da média foram: ")
    for chave, valor in temperaturas_acima_media.items():
        print(f" - {chave}: {valor}°C")
else:
    print("A temperatura se manteve a mesma durante toda a semana")