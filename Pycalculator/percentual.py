import os

def percentual():
	os.system('clear')
	print(' ×------- DIFERENÇA PERCENTUAL -------×\n')
	vi = float(input('\nValor inicial = '))
	vf = float(input('\nValor final = '))

	pct = ((vf - vi) / vi) * 100
	percentual = round(pct, 2)

	if percentual < 0:
    		print(f'\n<( Diminuição percentual de {percentual}% )>')

	elif percentual > 0:
    		print(f'\n<( Aumento percentual de {percentual}% )>')

	else:
    		print('\n<( O Valor inicial não sofreu alteração (0%) )>')
