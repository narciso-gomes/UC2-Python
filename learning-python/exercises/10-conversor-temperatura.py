# Temperatura para quem viaja
# Um site de viagens informa a temperatura em três escalas e diz o que esperar do dia.
# Fahrenheit => F = C * 1.8 + 32
# Kelvin => K = C + 273.15
# -> O programa recebe a temperatura em Celsius e mostra as três escalas
# -> Mostre também a classificação: abaixo de 15 graus é frio, de 15 a 28 é agradável, acima de 28 é quente
# -> Testes: 30 graus e 15 graus

from models.temperatura import Temperatura

temperatura = float(input("Informe a temperatura em °C: "))
temperatura = Temperatura(temperatura)
temperatura.imprimir_temperaturas()
temperatura.imprimir_classificacao()

