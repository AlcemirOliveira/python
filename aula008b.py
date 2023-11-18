# usando from lib import função
from math import sqrt,ceil,floor,trunc
n=float(input('digite um numero : '))
raiz=sqrt(n)
print('raiz de {} = {}'.format(n,raiz))
print('raiz ceil de {} = {}'.format(n,ceil(raiz)))
print('raiz floor de {} = {}'.format(n,floor(raiz)))
print('raiz trunc de {} = {}'.format(n,trunc(raiz)))
print('raiz arredondada  de {} = {}'.format(n,round(raiz,3)))
print('raiz arredondada  de {} = {:.3f}'.format(n,raiz))
