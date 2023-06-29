import os

def porcentagem():
    os.system('clear')
    print('×--------- PORCENTAGEM ---------×')
    print('|                               |')
    print('|     [a] Quantos % X é de Y    |')
    print('|     [b] X% de um total Y      |')
    print('|                               |')
    print('×-------------------------------×\n')
    op = ' '
    while op not in 'ab':
        op = input('opção: ')
    if op == 'a':
        x = float(input('\nX = '))
        y = float(input('Y = '))
        z = (x*100)/y
        z = round(z, 2)
        print(f'\n<( {x} equivale a {z}% de {y})> ')
    elif op == 'b':
        x = float(input('\nX = '))
        y = float(input('Y = '))
        z = (x/100)*y
        z = round(z, 2)
        print(f'\n<( {x}% de {y} é igual a {z} )>')
    else:
        print('\nOpção a ou b!\n')
