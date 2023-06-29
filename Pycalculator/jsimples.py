import os

def jsimples():
    os.system('clear')
    print(' ×------- JUROS SIMPLES -------×\n')
    c = float(input('\nCapital investido = '))
    i = float(input('Taxa de juros = '))
    t = float(input('Tempo = ')) 
    j = c*i*t
    m = j + c
    print(f'\n<( Montante a receber: {m})>')
    print(f'\n<( apartir do Juros de: {j})>')
    
    