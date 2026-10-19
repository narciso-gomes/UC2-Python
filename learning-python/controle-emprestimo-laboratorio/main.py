TIPOS = ("notebook", "tablet", "kit arduino", "fone")

equipamentos = [
    {
        "codigo": "NB01",
        "tipo": "notebook",
        "disponivel": False,
        "com": "Ana",
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
    print("Lista equipamentos:")
    print("-" * 50)
    titulos = ["Código", "Tipo", "Disponível"]
    print(f"{titulos[0]:<6} | {titulos[1]:<12} | {titulos[2]:<11}")
    print("-" * 39)
    for equipamento in equipamentos:
        disponivel = "Sim" if equipamento["disponivel"] else "Não"

        print(
            f"{equipamento['codigo']:<6} | {equipamento['tipo']:<12} | {disponivel:<11}"
        )
    input("Precione ENTER para voltar para o menu...")


def cadastrar():
    print("Cadastro de novo equipamento")
    print("-" * 50)
    codigo_equipamento = input("Código: ")
    tipo_equipamento = input("Tipo: ")
    equipamento = {
        "codigo": codigo_equipamento,
        "tipo": tipo_equipamento,
        "disponivel": True,
        "com": "",
        "emprestimos": 0,
    }
    equipamentos.append(equipamento)
    print("Equipamento cadastrado com sucesso!")
    input("Precione ENTER para voltar para o menu...")


def emprestar():
    print("Empréstimo de equipamento")
    print("-" * 50)
    nome_responsavel = input("Nome: ")

    equipamentos_pessoa = [
        equipamento
        for equipamento in equipamentos
        if equipamento["com"] == nome_responsavel
    ]

    if len(equipamentos_pessoa) >= 2:
        print(
            f"{nome_responsavel} atingiu o limite de empréstimo. (Máximo 02 equipamentos)"
        )
    else:
        codigo_equipamento = input("Código: ")

        encontrou_equipamento = False
        for equipamento in equipamentos:
            if equipamento["codigo"] == codigo_equipamento:
                encontrou_equipamento = True
                if equipamento["disponivel"]:
                    equipamento["com"] = nome_responsavel
                    equipamento["disponivel"] = False
                    equipamento["emprestimos"] = equipamento["emprestimos"] + 1
                    print("Equipamento emprestado com sucesso!")
                else:
                    print("Equipamento indisponível")
                break

        if not encontrou_equipamento:
            print(f"Equipamento com código {codigo_equipamento} não encontrado")

    input("Precione ENTER para voltar para o menu...")


def devolver():
    print("Devolução de equipamento")
    print("-" * 50)
    nome_responsavel = input("Nome: ")

    while True:
        equipamentos_pessoa = [
            equipamento
            for equipamento in equipamentos
            if equipamento["com"] == nome_responsavel
        ]

        if len(equipamentos_pessoa) == 0:
            print(f"{nome_responsavel} não possui equipamentos emprestados.")
            break

        print(f"Equipamentos emprestados para {nome_responsavel}:")
        print("-" * 50)
        for equipamento in equipamentos_pessoa:
            print(f"Codigo: {equipamento["codigo"]} Tipo: {equipamento["tipo"]}")
        codigo_produto_devolucao = input("Código produto: ")
        equipamento_encontrado = next(
            (
                equipamento
                for equipamento in equipamentos_pessoa
                if equipamento["codigo"] == codigo_produto_devolucao
            ),
            None,
        )
        if equipamento_encontrado:
            equipamento_encontrado["com"] = ""
            equipamento_encontrado["disponivel"] = True
            print("Equipamento devolvido com sucesso!")

            if len(equipamentos_pessoa) > 1:
                proximo_equipamento = input(
                    "Deseja registra a próxima devolução? (S ou N): "
                )
                if proximo_equipamento == "N":
                    break
            else:
                break
        else:
            print("Equipamento não encontrado")

    input("Precione ENTER para voltar para o menu...")


def consultar():
    codigo_equipamento = input("Código equipamento: ")
    equipamento_encontrado = next(
        (
            equipamento
            for equipamento in equipamentos
            if equipamento["codigo"] == codigo_equipamento
        ),
        None,
    )

    if equipamento_encontrado:
        print(f"Código: {equipamento_encontrado["codigo"]}")
        print(f"Tipo: {equipamento_encontrado["tipo"]}")
        print(f"Disponível: {"Sim" if equipamento_encontrado["disponivel"] else "Não"}")
        print(f"Responsável: {equipamento_encontrado["com"]}")
        print(f"Total de empréstimos: {equipamento_encontrado["emprestimos"]}")
    else:
        print(f"Equipamento {codigo_equipamento} não encontrado")

    input("Precione ENTER para voltar para o menu...")


def remover():
    global equipamentos

    codigo = input("Código: ")
    equipamentos = [
        equipamento for equipamento in equipamentos if equipamento["codigo"] != codigo
    ]
    print(f"Equipamento {codigo} removido com sucesso!")
    input("Precione ENTER para voltar para o menu...")


while True:
    menu()
    acao = int(input("Escolha uma ação: "))

    if acao == 1:
        listar()

    if acao == 2:
        cadastrar()

    if acao == 3:
        emprestar()

    if acao == 4:
        devolver()

    if acao == 5:
        consultar()

    if acao == 7:
        remover()

    if acao == 0:
        print("Fim do programa!")
        break
