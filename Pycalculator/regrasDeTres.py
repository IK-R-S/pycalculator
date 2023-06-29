import os

def regradetres():
	os.system('clear')

	print(' ×------- REGRA DE TRÊS SIMPLES -------×\n')
	a = float(input(' VALOR (A): '))
	print('\n<< Está para >>\n')
	b = float(input(' VALOR (B): '))
	print('\n<( assim como )>\n')
	c = float(input(' VALOR (C): '))
	print('\n<< Está para >>\n')

	d = (b*c)/a
	d = round(d, 2)

	print(' +------> {}'.format(d))
