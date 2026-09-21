class Temperatura:

    def __init__(self, temperatura_celsius):
        self._temperatura_celsius = temperatura_celsius

    def temperatura_celsius(self):
        return self._temperatura_celsius

    def temperatura_kelvin(self):
        temperatura_K = self.temperatura_celsius() + 273.15
        return temperatura_K

    def temperatura_fahrenheit(self):
        temperatura_F = (self.temperatura_celsius() * 1.8) + 32
        return temperatura_F

    def classificacao(self):
        if self.temperatura_celsius() < 15:
            classificacao = "Frio"
        elif self.temperatura_celsius() >= 15 and self.temperatura_celsius() <= 28:
            classificacao = "Agradável"
        else:
            classificacao = "Quente"

        return classificacao

    def imprimir_temperaturas(self):
        print("-" * 60)
        print(f"Temperatura em Celsius: {self.temperatura_celsius()} °C")
        print(f"Temperatura em Kelvin: {self.temperatura_kelvin()} K")
        print(f"Temperatura em Fahrenheit: {self.temperatura_fahrenheit()} °F")

    def imprimir_classificacao(self):
        print("-" * 60)
        print(f"O clima está: {self.classificacao()}")
