# 1 - programa que leia numero inteiro e mostre na tela seu antecessor e seu sucessor
n=int(input('digite o numero : '))
print('o numero é {}, seu antecessor é {} e seu sucessor é {}'.format(n,n-1,n+1))

# 2- ler um numero e mostrar seu DOBRO, seu TRIPLO, e RAIZ QUADRADA
n2=int(input('digite o numero : '))
print('o dobro de {} é {} ,o triplo é {} e a raiz quadrada é {:.3f}'.format(n2,2*n2,3*n2,n2**(1/2)))
# 3 - mostrar 2 notas do aluno e calcular média
n1=int(input('nota1 : '))
n2=int(input('nota2 : '))
media=(n1+n2)/2
print('nota1 = {}, nota2 = {} ,média = {}'.format(n1,n2,media))
# 4 - ler valor em metros e converter para centimetros e milimetros
c=int(input('medida em metros : '))
cm=c*100
mm=c*1000
print('medida em metro={},em centimetros={}, em milimetros={}'.format(c,cm,mm))
# 5 - ler um numero e mostrar sua tabuada de multiplicação
n=int(input('numero para tabuada : '))
print('='*25)
print('tabuada de {}'.format(n))
print('{} x {:>2} = {:>2}'.format(n,1,n*1))
print('{} x {:>2} = {:>2}'.format(n,2,n*2))
print('{} x {:>2} = {:>2}'.format(n,3,n*3))
print('{} x {:>2} = {:>2}'.format(n,4,n*4))
print('{} x {:>2} = {:>2}'.format(n,5,n*5))
print('{} x {:>2} = {:>2}'.format(n,6,n*6))
print('{} x {:>2} = {:>2}'.format(n,7,n*7))
print('{} x {:>2} = {:>2}'.format(n,8,n*8))
print('{} x {:>2} = {:>2}'.format(n,9,n*9))
print('{} x {:>2} = {:>2}'.format(n,10,n*10))
print('='*25)

# calculo da tabuada por Iteração
print('tabuada de {} - por Iteração'.format(n))
for num in range(1,11):
    print('{} x {:>2} = {:>2}'.format(n,num,n*num))
print('='*13)
