TIPOS = ("notebook", "tablet", "kit arduino", "fone")

equipamentos = [
    {
        "codigo": "NB01",
        "tipo": "notebook",
        "disponivel": True,
        "com": "",
        "emprestimos": 4,
    },
    {
        "codigo": "NB02",
        "tipo": "notebook",
        "disponivel": False,
        "com": "Ana",
        "emprestimos": 7,
    },
    {
        "codigo": "TB01",
        "tipo": "tablet",
        "disponivel": True,
        "com": "",
        "emprestimos": 2,
    },
    {
        "codigo": "AR01",
        "tipo": "kit arduino",
        "disponivel": False,
        "com": "Bruno",
        "emprestimos": 5,
    },
    {"codigo": "FN01", "tipo": "fone", "disponivel": True, "com": "", "emprestimos": 0},
]


def menu():
    print("Menu de Ações:")
    print("-" * 50)
    print("01. Listar")
    print("02. Cadastrar")
    print("03. Emprestar")
    print("04. Devolver")
    print("05. Consultar")
    print("06. Relatório")
    print("07. Remover")
    print("0.. Sair")


def listar():
    print()
    print("Lista equipamentos:")
    print("-" * 50)
    for equipamento in equipamentos:
        print(f"Codigo: {equipamento["codigo"]}")
        print(f"Tipo: {equipamento["tipo"]}")
        print(f"Dispível: {"Sim" if equipamento["disponivel"] else "Não"}")
        if not equipamento["disponivel"]:
            print(f"Portador: {equipamento["com"]}")
        print("-" * 50)
    input("Precione ENTER para voltar para o menu")


while True:
    menu()
    acao = int(input("Escolha uma ação: "))

    if acao == 1:
        listar()

    if acao == 0:
        print("Fim do programa!")
        break
