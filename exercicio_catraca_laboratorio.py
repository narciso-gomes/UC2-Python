str_matricula_ativa = input("Matricula ativa? (S ou N): ")

if str_matricula_ativa != "S" or str_matricula_ativa != "N":
    print("Você informou um valor inválido")
    exit()

matricula_ativa = str_matricula_ativa == "S"

horario_entrada = int(input("Horário da entrada (HH): "))

pode_entrar = horario_entrada < 18

if matricula_ativa and pode_entrar:
    print("Bem vindo!")
else:
    if matricula_ativa:
        print("Laboratório fechado, volte amanhã antes das 18h")
    else:
        print("Sua matrícula não está ativa!")
