import json
import os

ARQUIVO = os.path.join(os.path.dirname(__file__), "equipamentos.json")
TIPOS = ("notebook", "tablet", "kit arduino", "fone")
RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"


def carregar_dados():
    global equipamentos
    equipamentos = []

    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            equipamentos = json.load(arquivo)


def salvar_dados():
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(equipamentos, arquivo, ensure_ascii=False, indent=4)


carregar_dados()


def menu():
    print()
    print("-" * 50)
    print("Menu de Ações:")
    print("-" * 50)
    print("📋 1. Listar...: Tabela dos equipamentos")
    print("➕ 2. Cadastrar: Adicionar novo equipamento")
    print("📤 3. Emprestar: Registrar empréstimo de equipamento")
    print("📥 4. Devolver.: Registrar devolução de equipamento")
    print("🔎 5. Consultar: Consultar detalhes do equipamento por código")
    print("📊 6. Relatório: Relatório de todos os equipamentos")
    print("🗑️  7. Remover..: Apagar um registro de equipamento")
    print("🚪 0. Sair.....: Sair da aplicação")


def listar():
    print()
    print("LISTA DE EQUIPAMENTOS")
    print("-" * 55)
    titulos = ["Código", "Tipo", "Disponível", "Nome"]
    print(f"{titulos[0]:<6} | {titulos[1]:<12} | {titulos[3]:<15} | {titulos[2]:<11} |")
    print("-" * 55)

    for equipamento in equipamentos:
        disponivel = (
            f"{GREEN}Sim{RESET}" if equipamento["disponivel"] else f"{RED}Não{RESET}"
        )
        escape = ""

        print(
            f"{equipamento['codigo']:<6} | {equipamento['tipo']:<12} | {equipamento['com']:<15} | {disponivel}{escape:<8} |"
        )
    print("-" * 55)
    input("Precione ENTER para voltar para o menu...")


def cadastrar():
    print("Cadastro de novo equipamento")
    print("-" * 50)
    codigo_equipamento = input("Código: ").upper()
    equipamentos_filtrados = [
        equipamento
        for equipamento in equipamentos
        if equipamento["codigo"] == codigo_equipamento
    ]
    if len(equipamentos_filtrados) > 0:
        raise ValueError(f"Código {codigo_equipamento} já utilizado.")

    tipo_equipamento = input("Tipo: ")
    if tipo_equipamento not in TIPOS:
        raise ValueError(f"O tipo {tipo_equipamento} não é válido.")

    equipamento = {
        "codigo": codigo_equipamento,
        "tipo": tipo_equipamento,
        "disponivel": True,
        "com": "",
        "emprestimos": 0,
    }
    equipamentos.append(equipamento)
    print("Equipamento cadastrado com sucesso!")
    salvar_dados()

    input("Precione ENTER para voltar para o menu...")


def emprestar():
    print("Empréstimo de equipamento")
    print("-" * 50)
    nome_responsavel = input("Nome: ").strip()
    if len(nome_responsavel) < 3:
        raise ValueError("Nome deve ter no mínimo 3 caracteres")

    equipamentos_pessoa = [
        equipamento
        for equipamento in equipamentos
        if equipamento["com"].lower() == nome_responsavel.lower()
    ]
    if len(equipamentos_pessoa) >= 2:
        raise ValueError(
            f"{nome_responsavel} atingiu o limite de empréstimo. (Máximo 02 equipamentos)"
        )

    codigo_equipamento = input("Código: ").upper()
    equipamento_encontrado = next(
        (
            equipamento
            for equipamento in equipamentos
            if equipamento["codigo"] == codigo_equipamento
        ),
        None,
    )
    if equipamento_encontrado is None:
        raise ValueError(f"Equipamento com código {codigo_equipamento} não encontrado")
    if not equipamento_encontrado["disponivel"]:
        raise ValueError("Equipamento indisponível")

    equipamento_encontrado["com"] = nome_responsavel
    equipamento_encontrado["disponivel"] = False
    equipamento_encontrado["emprestimos"] += 1
    print("Equipamento emprestado com sucesso!")
    salvar_dados()

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
            raise ValueError(f"{nome_responsavel} não possui equipamentos emprestados.")

        print(f"Equipamentos emprestados para {nome_responsavel}:")
        print("-" * 50)
        for equipamento in equipamentos_pessoa:
            print(f"Codigo: {equipamento['codigo']} Tipo: {equipamento['tipo']}")
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
            salvar_dados()

            if len(equipamentos_pessoa) > 1:
                proximo_equipamento = input(
                    "Deseja registra a próxima devolução? (S ou N): "
                )
                if proximo_equipamento == "N":
                    break
            else:
                break
        else:
            raise ValueError("Equipamento não encontrado")

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
        print(f"Código: {equipamento_encontrado['codigo']}")
        print(f"Tipo: {equipamento_encontrado['tipo']}")
        print(f"Disponível: {'Sim' if equipamento_encontrado['disponivel'] else 'Não'}")
        print(f"Responsável: {equipamento_encontrado['com']}")
        print(f"Total de empréstimos: {equipamento_encontrado['emprestimos']}")
    else:
        raise ValueError(f"Equipamento {codigo_equipamento} não encontrado")

    input("Precione ENTER para voltar para o menu...")


def remover():
    global equipamentos

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
        if equipamento_encontrado["disponivel"]:
            equipamentos = [
                equipamento
                for equipamento in equipamentos
                if equipamento["codigo"] != codigo_equipamento
            ]
            salvar_dados()
            print(f"Equipamento {codigo_equipamento} removido com sucesso!")
        else:
            raise ValueError("Equipamento está emprestado, não pode ser apagado.")
    else:
        raise ValueError(f"Equipamento {codigo_equipamento} não encontrado")

    input("Precione ENTER para voltar para o menu...")


def relatorio():
    total_equipamentos = len(equipamentos)
    total_equipamentos_disponiveis = 0
    total_equipamentos_emprestados = 0
    total_notebook = 0
    total_tablet = 0
    total_arduino = 0
    total_fone = 0
    equipamento_mais_emprestado = None

    if not equipamentos:
        raise ValueError("Não há equipamentos cadastrados.")

    for equipamento in equipamentos:
        if equipamento["disponivel"]:
            total_equipamentos_disponiveis += 1
        else:
            total_equipamentos_emprestados += 1

        if equipamento["tipo"] == "notebook":
            total_notebook += 1

        if equipamento["tipo"] == "tablet":
            total_tablet += 1

        if equipamento["tipo"] == "kit arduino":
            total_arduino += 1

        if equipamento["tipo"] == "fone":
            total_fone += 1

        if not equipamento_mais_emprestado:
            equipamento_mais_emprestado = equipamento
        else:
            if equipamento_mais_emprestado["emprestimos"] < equipamento["emprestimos"]:
                equipamento_mais_emprestado = equipamento

    print("-" * 50)
    print("Relatório de Equipamentos")
    print("-" * 50)
    print(f"Total de equipamentos............: {total_equipamentos}")
    print(f"Total de equipamentos disponíveis: {total_equipamentos_disponiveis}")
    print(f"Total de equipamentos emprestados: {total_equipamentos_emprestados}")
    print(
        f"Equipamento mais emprestado......: {equipamento_mais_emprestado['codigo']} - {equipamento_mais_emprestado['tipo']} ({equipamento_mais_emprestado['emprestimos']} empréstimos)"
    )
    print(f"Total de notebooks...............: {total_notebook}")
    print(f"Total de tablets.................: {total_tablet}")
    print(f"Total de arduinos................: {total_arduino}")
    print(f"Total de fones...................: {total_fone}")

    input("Precione ENTER para voltar para o menu...")


while True:
    try:
        menu()
        acao = int(input("Escolha uma ação: "))

        if acao not in range(8):
            raise ValueError("Opção inválida")

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

        if acao == 6:
            relatorio()

        if acao == 7:
            remover()

        if acao == 0:
            print("Fim do programa!")
            break

    except KeyboardInterrupt:
        print("\nOperação interrompida pelo usuário")
        break
    except ValueError as erro:
        print(f"Erro: {erro}")
        input("Precione ENTER para voltar para o menu...")
