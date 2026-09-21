dias_semana = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")
temperaturas = []


print("Informe a temperatura de cada dia da semana (°C)")

for i in range(len(dias_semana)):
    temperatura = float(input(dias_semana[i] + ": "))
    temperaturas.insert(i, temperatura)

maior_temperatura = max(temperaturas)
menor_temperatura = min(temperaturas)
temperatura_media_semana = sum(temperaturas) / len(dias_semana)

print(f"A maior temperatura registrada foi {maior_temperatura}°C")
print("A menor temperatura registrada foi", str(menor_temperatura) + "°C")
print("A temperatura média da semana é", str(temperatura_media_semana) + "°C")
