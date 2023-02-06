#Entendendo um Algoritmo e um Programa
    #Um algoritmo é uma sequência finita de passos. Podendo produzir uma entrada e uma saída.
    #O programa é algo que possui um algoritmo e é executado pela máquina.
#Aritmética básica; Tipos de Dados e Operadores.

#Desvios Condicionais
def desv_condi():
    a = int(input('Entre com um número:'))
    if a == 1:
        print('É um binário')
    elif a == 0:
        print('É um binário')
    else:
        print('Não é um binário')

def desv_condi2():
    y = 1 + 2
    x = input('Tente advinhar qual o número que irá aparecer:')
    if y == x:
        print("Parabéns, você advinhou!")
    else:
        print("Você não acertou, que tal tentar mais uma vez?")

def desv_condi3():
    while True:
        a = int(input('Entre com um número:'))
        if a == 0:
            print('Você ganhou 4x', 'Ganhou:', 4*a)
            break
        elif a >= 3:
            print('Você ganhou 2x', 'Ganhou:', 2*a)
            break
        elif a == 1:
            print('Você ganhou 3x', 'Ganhou:', 3*a)
            break
        else:
            print('Você não obtêve nenhum ganhou.')

def desv_condi4():
    listacao_alimentos = ['Biscoito Negresco', 'Carne Bovina', 'Pães', 'Feijão Branco']
    listei = [listacao_alimentos, 'Hello World!', 5, True, 4.6, False]
    for i in range(5):
        print(listacao_alimentos)
    for i in range(4, 9):
        print(listacao_alimentos)
    for i in range(10, 3, -1):
        print(listacao_alimentos)
    for i, item in enumerate(listacao_alimentos):
        print(i, item)
desv_condi4()