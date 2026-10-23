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


def vagas_disponiveis():
    global total_vagas_disponiveis_carro
    global total_vagas_disponiveis_moto

    total_vagas_carro = 0
    total_vagas_moto = 0

    for veiculo in patio:
        if veiculo["tipo"] == "carro":
            total_vagas_carro += 1
        elif veiculo["tipo"] == "moto":
            total_vagas_moto += 1

    total_vagas_disponiveis_carro = VAGAS["carro"] - total_vagas_carro
    total_vagas_disponiveis_moto = VAGAS["moto"] - total_vagas_moto


def menu():
    print("-" * 50)
    print("Gestor de estacionamento")
    print("-" * 50)
    print("01 - Pátio")
    print("02 - Entrada")


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


def entrada():
    tipo = int(input("Tipo: (1 - Carro | 2 - Moto) "))

    if tipo == 1 and total_vagas_disponiveis_carro <= 0:
        raise ValueError("Não há mais vagas para Carros.")
    elif tipo == 2 and total_vagas_disponiveis_moto <= 0:
        raise ValueError("Não há mais vagas para Motos.")

    placa = input("Placa: ")
    hora_entrada = int(input("Hora: (H) "))

    veiculo = {"placa": placa, "tipo": TIPOS[tipo - 1], "entrada": hora_entrada}
    patio.append(veiculo)
    print("Veículo adicionado ao pátio com sucesso!")


while True:
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
    vagas_disponiveis()
    try:
        menu()
        opcao = int(input("Opção: "))

        if opcao == 1:
            lista()

        if opcao == 2:
            entrada()

        input("Precione ENTER para continuar...")

    except ValueError as erro:
        print(f"Erro: {erro}")
        input("Precione ENTER para voltar para o menu...")
