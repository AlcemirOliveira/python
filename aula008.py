import math
n=float(input('digite um numero : '))
raiz=math.sqrt(n)
print('raiz de {} = {}'.format(n,raiz))
print('raiz ceil de {} = {}'.format(n,math.ceil(raiz)))
print('raiz floor de {} = {}'.format(n,math.floor(raiz)))
print('raiz trunc de {} = {}'.format(n,math.trunc(raiz)))
print('raiz arredondada  de {} = {}'.format(n,round(raiz,3)))
print('raiz arredondada  de {} = {:.3f}'.format(n,raiz))
