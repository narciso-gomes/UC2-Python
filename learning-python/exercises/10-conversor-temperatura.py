from models.temperatura import Temperatura

temperatura = float(input("Informe a temperatura em °C: "))
temperatura = Temperatura(temperatura)
temperatura.imprimir_temperaturas()
temperatura.imprimir_classificacao()

