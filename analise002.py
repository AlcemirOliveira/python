import numpy as np

"""
def tabela(valIMC):
    if valIMC<16:
        return str(valIMC) + ': Magreza grave'
    elif valIMC < 17:
        return str(valIMC) + ': Magreza moderada'
    elif valIMC < 18.5:
        return str(valIMC) + ': Magreza leve'
    elif valIMC < 25:
        return str(valIMC) + ': Saudável'
    elif valIMC < 30:
        return str(valIMC) + ': Sobrepeso'
    elif valIMC < 35:
        return str(valIMC) + ': Obesidade Grau I'
    elif valIMC < 40:
        return str(valIMC) + ': Obesidade Grau II (severe)'
    else:
        return str(valIMC) + ': Obesidade Grau III (mórbida)'
"""

def tabela(valIMC):
    if valIMC<16:
        return  '- Magreza grave'
    elif valIMC < 17:
        return  '- Magreza moderada'
    elif valIMC < 18.5:
        return  '- Magreza leve'
    elif valIMC < 25:
        return  '- Saudável'
    elif valIMC < 30:
        return  '- Sobrepeso'
    elif valIMC < 35:
        return  '- Obesidade Grau I'
    elif valIMC < 40:
        return  '- Obesidade Grau II (severe)'
    else:
        return  '- Obesidade Grau III (mórbida)'

altura,peso,forca = np.loadtxt('G:\desenvolvimento\Python\peso.csv',
                               delimiter=';',
                               unpack=True,
                               dtype='float')
# print('altura:',altura)
# print('peso:',peso)
# print('forca:',forca)
imc = peso / altura ** 2
"""
print('Mínimo: ',tabela(np.amin(imc)))
print('Máximo: ', tabela(np.amax(imc)))
print('Máx - Mín: ', tabela(np.ptp(imc)))
print('Média: ', tabela(np.median(imc)))
print('Média por força: ', tabela(np.average(imc)))
print('Média aritmética: ', tabela(np.mean(imc)))
print('Média aritmética: {:.2f}'.format(np.mean(imc)))
print('Desvio padrão: {:.2f}'.format(np.std(imc)))
print('Variância: {:.2f}'.format(np.var(imc)))
"""
print('Mínimo          : {:.2f} {} '.format(np.amin(imc),tabela(np.amin(imc))))
print('Máximo          : {:.2f} {} '.format(np.amax(imc),tabela(np.amax(imc))))
print('Máx-Mín         : {:.2f} {} '.format(np.ptp(imc),tabela(np.ptp(imc))))
print('Média           : {:.2f} {} '.format(np.median(imc),tabela(np.median(imc))))
print('Média por força : {:.2f} {} '.format(np.average(imc),tabela(np.average(imc))))
print('Média Aritmética: {:.2f} {} '.format(np.mean(imc),tabela(np.mean(imc))))
print('Desvio Padrão   :  {:.2f}   '.format(np.std(imc)))
print('Variância       : {:.2f}    '.format(np.var(imc)))