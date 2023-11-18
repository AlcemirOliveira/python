import numpy as np

altura=[1.7,1.5,1.8,1.65,1.6]
peso=[45.0,85.0,67.0,80.0,58.0]
imc = peso[1] / altura[1]**2
print(round(imc,2))
#calculo IMC por interação nas listas ALTURA e PESO
tl = len(altura)
print('='*50)
print('imc:',end=" ")
for i in range(tl):
    imc = round(peso[i] / altura[i]**2,2)
    print(imc,end=' - ')
print()
print('='*50)
# calculo IMC  usando NUMPY array
nAltura = np.array(altura)
nPeso=np.array(peso)
imc = nPeso / nAltura**2
print('peso:',peso)
print('altura:',altura)
print('imc:',imc)
print('='*50)
