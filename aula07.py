a=4
b=10
c=21
d=64
print('='*30)
print('a soma de {} + {} + {} = {} '.format(a,b,c,a+b+c))
soma=a+b+c
print('soma de {} + {} + {} = {}'.format(a,b,c,soma))
subt=c-b-a
print('subtração de {} - {} - {} = {}'.format(c,b,a,subt))
pot=a**b
print('potencia de {} elevado a {} = {}'.format(a,b,pot))
inteiro=c//a
print('parte inteira de {} / {} = {}'.format(c,a,inteiro))
resto=c%a
print('resto da divisão de {} por {} = {}'.format(c,a,resto))
raiz=d**(1/2)
print('raiz quadrada de {} é igual a {:.2f}'.format(d,raiz),end=" e " )
raiz_cub=d**(1/3)
print('raiz cubica de {} é {:.3f}'.format(d,raiz_cub))
cubo=a**3
print('o cubo de {} é {}'.format(a,cubo))
print('='*30)
animal = input('nome do animal : ')
print('o animal é o {}!'.format(animal.upper()))
print('o animal é o {:20}!'.format(animal.upper()))
print('o animal é o {:>20}!'.format(animal.upper()))
print('o animal é o {:<20}!'.format(animal.upper()))
print('o animal é o {:^20}!'.format(animal.upper()))
print('o animal é o {:=^20}!'.format(animal.upper()))


