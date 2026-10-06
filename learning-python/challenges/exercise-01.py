temperatura = float(input("Temperatura °C: "))

if temperatura >= 30:
    print("Calor intenso! Beba bastante água.")
elif temperatura >= 20:
    print("Temperatura agradável!")
elif temperatura >= 10:
    print("Tempo fresco. Um agasalho ajuda.")
else:
    print("Frio intenso! Vista um casaco.")
