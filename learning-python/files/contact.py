import os

print("Informe os dados de cada contato para gravação")
print("Deixe em branco para parar")

if not os.path.isfile("contatos.txt"):
    arq = open("contatos.txt", "w")
else:
    arq = open("contatos.txt", "a+")

while True:
    contato = input("Contato: ")
    if contato == "":
        break

    arq.write(contato + "\n")
arq.close()

print("-" * 50)
print("Contatos cadastrados:")
arq = open("contatos.txt")
linhas = arq.readlines()

for contato in linhas:
    print(contato.strip())
arq.close()
print("-" * 50)
