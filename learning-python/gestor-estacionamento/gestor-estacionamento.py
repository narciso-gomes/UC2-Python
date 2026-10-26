import os
import subprocess
import sys

TIPOS = ("carro", "moto")
VAGAS = {"carro": 5, "moto": 3}
PRECO_HORA = {"carro": 6.00, "moto": 3.50}
MENSALISTAS = ("ABC1D23", "MOT0R99")

patio = [
    {"placa": "QWE4R56", "tipo": "carro", "entrada": 8},
    {"placa": "MOT0R99", "tipo": "moto", "entrada": 9},
    {"placa": "ZXC7V89", "tipo": "carro", "entrada": 10},
    {"placa": "ABC1D23", "tipo": "carro", "entrada": 11},
    {"placa": "NMI9999", "tipo": "moto", "entrada": 12},
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
    print(
        f"Gestor de estacionamento VC={total_vagas_disponiveis_carro} | VM={total_vagas_disponiveis_moto}"
    )
    print("-" * 50)
    print("1 - Pátio")
    print("2 - Entrada")
    print("3 - Saída")
    print("4 - Consultar")
    print("5 - Vagas")
    print("6 - Relatório")
    print("7 - Cancelar")
    print("0 - Sair")


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

    placa = input("Placa: ").upper().strip()
    hora_entrada = int(input("Hora: (H) "))

    veiculo = {"placa": placa, "tipo": TIPOS[tipo - 1], "entrada": hora_entrada}
    patio.append(veiculo)
    print("Veículo adicionado ao pátio com sucesso!")


def consultar():
    veiculo = busca_veiculo_placa()
    print(f"Placa..........: {veiculo["placa"]}")
    print(f"Tipo...........: {veiculo["tipo"].capitalize()}")
    print(f"Hora de entrada: {veiculo["entrada"]}")
    print(f"Mensalista.....: {'Sim' if veiculo["mensalista"] else 'Não'}")


def saida():
    veiculo = busca_veiculo_placa()
    hora_saida = int(input("Hora de saída: "))

    if hora_saida < veiculo["entrada"]:
        raise ValueError("Hora de saída não pode ser menor que a hora de entrada.")

    if veiculo["mensalista"]:
        valor = 0
    else:
        total_horas = hora_saida - veiculo["entrada"]

        if total_horas == 0:
            total_horas += 1

        if veiculo["tipo"] == "carro":
            valor = PRECO_HORA["carro"] * total_horas
        elif veiculo["tipo"] == "moto":
            valor = PRECO_HORA["moto"] * total_horas

        print(f"Valor total (R$): {valor:.2f}")

    patio.pop(veiculo["index"])
    veiculo["valor"] = valor
    veiculo["saida"] = hora_saida
    saidas.append(veiculo)


def busca_veiculo_placa():
    placa = input("Placa: ").upper().strip()
    index, veiculo = next(
        ((i, v) for i, v in enumerate(patio) if v["placa"] == placa),
        (None, None),
    )

    if not veiculo:
        raise ValueError(f"Veículo com placa {placa}, não encontrado")

    mensalista = veiculo["placa"] in MENSALISTAS
    veiculo["mensalista"] = mensalista
    veiculo["index"] = index

    return veiculo


def vagas():
    print("Vagas de carros: ", total_vagas_disponiveis_carro)
    print("Vagas de motos.: ", total_vagas_disponiveis_moto)


def relatorio():
    total_veiculos_patio = len(patio)
    total_veiculos_saida = len(saidas)
    total_faturamento = 0
    total_mensalistas = 0
    maior_valor = 0

    for veiculo_saida in saidas:
        total_faturamento += veiculo_saida["valor"]
        if veiculo_saida["mensalista"]:
            total_mensalistas += 1

        if maior_valor < veiculo_saida["valor"]:
            maior_valor = veiculo_saida["valor"]

    print("-" * 30)
    print("Relatório de Movimentações")
    print("-" * 30)
    print(f"Total de veículos no pátio: {total_veiculos_patio}")
    print(f"Total de saídas...........: {total_veiculos_saida}")
    print(f"Saídas de mensalistas.....: {total_mensalistas}")
    print(f"Faturamento do dia........: R$ {total_faturamento:.2f}")
    print(f"Maior valor do dia........: R$ {maior_valor:.2f}")


def cancelar():
    veiculo = busca_veiculo_placa()
    acao = (
        input(
            f"Tem certeza que deseja remover o veículo: {veiculo["placa"]} - {veiculo["tipo"]}? (S/N) "
        )
        .strip()
        .upper()
    )
    if acao == "S":
        patio.pop(veiculo["index"])
        print("Entrada cancelada com sucesso!")
    else:
        print("Ação cancelada!")


def sair():
    acao = input("Tem certeza que deseja sair? (S/N) ").strip().upper()
    if acao == "S":
        print("Até a próxima!")
        sys.exit()


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

        if opcao == 3:
            saida()

        if opcao == 4:
            consultar()

        if opcao == 5:
            vagas()

        if opcao == 6:
            relatorio()

        if opcao == 7:
            cancelar()

        if opcao == 0:
            sair()

        input("Precione ENTER para continuar...")

    except ValueError as erro:
        print(f"Erro: {erro}")
        input("Precione ENTER para voltar para o menu...")
