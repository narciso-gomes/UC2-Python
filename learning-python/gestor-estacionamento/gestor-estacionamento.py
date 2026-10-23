import os
import subprocess

TIPOS = ("carro", "moto")
VAGAS = {"carro": 5, "moto": 3}
PRECO_HORA = {"carro": 6.00, "moto": 3.50}
MENSALISTAS = ("ABC1D23", "MOT0R99")

patio = [
    {"placa": "QWE4R56", "tipo": "carro", "entrada": 8},
    {"placa": "MOT0R99", "tipo": "moto", "entrada": 9},
    {"placa": "ZXC7V89", "tipo": "carro", "entrada": 10},
]

saidas = []


def menu():
    print("-" * 50)
    print("Gestor de estacionamento")
    print("-" * 50)
    print("01 - Pátio")


def lista():
    titulos = ["Placa", "Tipo", "Entrada"]
    print("-" * 30)
    print(f"| {titulos[0]:<7} | {titulos[1]:<6} | {titulos[2]:<7} |")
    print("-" * 30)
    for veiculo in patio:
        print(
            f"| {veiculo['placa']:<7} | {veiculo['tipo']:<6} | {veiculo['entrada']:<7} |"
        )
    print("-" * 30)


while True:
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
    try:
        menu()
        opcao = int(input("Opção: "))

        if opcao == 1:
            lista()
        
        input("Precione ENTER para continuar...")

    except ValueError as erro:
        print(f"Erro: {erro}")
        input("Precione ENTER para voltar para o menu...")
