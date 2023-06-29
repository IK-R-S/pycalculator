import os

def jcomposto():
    os.system('clear')
    print(' ×------- JUROS COMPOSTOS -------×\n')
    c = float(input('\nCapital investido = '))
    i = float(input('Taxa de juros = '))
    n = float(input('N° de Períodos = ')) 
    m = c*(1+i)**n
    j = m - c
    print(f'\n<( Montante a receber: {m})>')
    print(f'\n<( apartir do Juros de: {j})>')
    
    