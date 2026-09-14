HISTORICO = ''

def calcula(expressao):
    try:
        return eval(expressao)
    except:
        print("Expressão inválida!")
        return None
    
def historico(expressao, resultado):
    global HISTORICO
    if resultado is not None:
        HISTORICO += '\n\n' + expressao
        HISTORICO += '\n' + str(resultado)

def principal():
    while True:
        print("Informe a expressão matemática")
        print("h para histórico, s para sair")
        expressao = input()
        if(expressao.lower() == 's'):
            break
        if(expressao.lower() == 'h'):
            print(HISTORICO, '\n')
        else:
            resultado = calcula(expressao)
            historico(expressao, resultado)
            print(resultado, '\n')

if __name__ == '__main__':
    principal()