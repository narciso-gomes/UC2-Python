from Account import Conta, ContaInvestimento
from Client import ClientePF, ClientePJ

clientePF = ClientePF(
    nome="Mário Arruda dos Santos",
    endereco="Paraná/BR",
    cpf="00000000000",
    nascimento="1991-03-03",
)
contaPF = ContaInvestimento(numero=11111, cliente=clientePF)

clientePJ = ClientePJ(nome="NG Tech", endereco="Pará/BR", cnpj="0020300003000")
contaPJ = Conta(numero=22222, cliente=clientePJ)

contaPJ.depositar(500)

contaPF.imprimir()
contaPJ.imprimir()

contaPJ.transferir(contaPF, 200)

contaPF.imprimir()
contaPJ.imprimir()

Conta.imprimir_quantidade()
