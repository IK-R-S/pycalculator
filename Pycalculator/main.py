from regrasDeTres import *
from percentual import *
from porcentagem import *
from jsimples import *
from jcomposto import *
from os import system as sy
from time import sleep as s

def ok():
    ok = input('\nDigite ENTER para limpar o resultado. ')

while True:
	sy('clear')
	print('+---- SISTEMA DE CONTABILIDADES E ESTATÍSTICAS ----+')
	print('|                                                  |')
	print('|           [1] REGRA DE TRÊS SIMPLES              |')
	print('|           [2] DIFERENÇA PERCENTUAL               |')
	print('|           [3] PORCENTAGEM                        |')
	print('|           [4] JUROS SIMPLES                      |')
	print('|           [5] JUROS COMPOSTOS                    |')
	print('|           [1] MÉDIA ARITMÉTICA SIMPLES           |')
	print('|           [0] SAIR                               |')
	print('|                                                  |')
	print('+--------------------------------------------------+')
	print('√ Atualização 1 (Porcentagem)')
	print('√ Atualização 2 (Juros simples e compostos)')
	print('• Atualização 3 (Média)\n')

	m = int(input('Selecione um módulo: '))

	if m == 1:
		regradetres()
		ok()
	elif m == 2:
		percentual()
		ok()
	elif m == 3:
		porcentagem()
		ok()
	elif m == 4:
		jsimples()
		ok()
	elif m == 5:
		jcomposto()
		ok()
	elif m == 0:
		print('\nPrograma encerrado. Até mais!')
		s(0.7)
		sy('clear')
		break
	else:
		print('\ncomando desconhecido ou ainda não atualizado :(\n')
		s(1)

