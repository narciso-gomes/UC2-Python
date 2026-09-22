class Colaborador:
    LIMITE_HORAS = 220
    _horas_extras = 0

    def __init__(self, nome, horas_trabalhadas, valor_hora):
        self._nome = nome
        self._horas_trabalhadas = horas_trabalhadas
        self._valor_hora = valor_hora
        if horas_trabalhadas > self.LIMITE_HORAS:
            self._horas_extras = horas_trabalhadas - self.LIMITE_HORAS
            self._horas_trabalhadas = self.LIMITE_HORAS

    def nome(self):
        return self._nome

    def horas_trabalhadas(self):
        return self._horas_trabalhadas

    def horas_extras(self):
        return self._horas_extras

    def total_horas(self):
        return self._horas_trabalhadas + self._horas_extras

    def valor_hora(self):
        return self._valor_hora

    def valor_hora_extra(self):
        return self.valor_hora() * 1.5

    def valor_salario(self):
        return self.horas_trabalhadas() * self.valor_hora()

    def valor_extras(self):
        return self.horas_extras() * self.valor_hora_extra()

    def valor_salario_bruto(self):
        return self.valor_salario() + self.valor_extras()

    def valor_inss(self):
        salario_bruto = self.valor_salario_bruto()
        if salario_bruto <= 1500:
            valor_inss = salario_bruto * 0.075
        elif salario_bruto <= 2800:
            valor_inss = salario_bruto * 0.09
        else:
            valor_inss = salario_bruto * 0.12
        return valor_inss
    
    def valor_salario_liquido(self):
        return self.valor_salario_bruto() - self.valor_inss()
    