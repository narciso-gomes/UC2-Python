# A empresa paga por hora. Até 220 horas no mês, a hora vale o valor normal. As horas que passarem de 220
# valem 50% a mais. Sobre o salário bruto incide o desconto do INSS: 7,5% para bruto de até R$ 1.500,00; 9%
# para bruto acima disso até R$ 2.800,00; e 12% para bruto acima de R$ 2.800,00. Use a alíquota única sobre
# o valor total, sem cálculo progressivo

# ▸ O programa recebe o nome, o valor da hora e as horas trabalhadas no mês.
# ▸ Mostre o salário bruto, o valor do INSS e o salário líquido, todos com duas casas decimais.
# ▸ Testes: R$ 12,00 a hora com 240 horas; depois R$ 12,00 a hora com 200 horas.

from models.colaborador import Colaborador

nome = input("Nome: ")
valor_hora = float(input("Valor hora (R$): "))
horas_trabalhadas = int(input("Horas trabalhadas: "))

colaborador = Colaborador(nome, horas_trabalhadas, valor_hora)

print("-" * 30)
print("Contracheque do Colaborador")
print("-" * 30)

print(f"Salário bruto..: R${colaborador.valor_salario_bruto():.2f}")
print(f"Valor INSS.....: R${colaborador.valor_inss():.2f}")
print(f"Salário líquido: R${colaborador.valor_salario_liquido():.2f}")
