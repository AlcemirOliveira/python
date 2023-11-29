frase='Curso em Video Python'
print('frase: ',frase)
print('frase [0 a 5]: ',frase[0:5])
print('frase [0 a 9]: ',frase[:9])
print('frase [9 a 14]: ',frase[9:14])
print('frase [9 ao fim]: ',frase[9:])
print('frase saltando letras: ',frase[::2])
print('frase maiuscula:',frase.upper())
print('frase minuscula:',frase.lower())
print('frase capitalizada: ',frase.capitalize())
print('{:-^40}'.format(frase))
print('Imprimindo letras individualmente')
print('-'*45)
for letra in frase:
    print(letra,end='-')
print()
print('='*45)
dividido = frase.split()
print('array de palavras: ',dividido)
print('primeira palavra: ',dividido[0])
tam = len(dividido)
print('ultima palavra: ',dividido[tam-1])
print('ultima palavra: ',dividido[-1])em
print('qtd palavras na frase: ',tam)
print('='*40)
print('Quantidade de letras "o" na frase: ',frase.count('o'))
print('='*40)
find1=input('procurar palavra na frase: ')
find2=frase.find(find1)
print('palavra "{}" encontrada na posição: {} '.format(find1,find2))
print(find1 in frase)
if find2 >=0 :
    print('encontrada palavra:{} '.format(find1))
else:
    print('não encontrada palavra: {}'.format(find1))

# OUTRA FORM DE TESTAR SE PALAVRA FOI ENCONTRADA
if (find1 in frase):
    print('encontrada palavra:{} '.format(find1))
else:
    print('não encontrada palavra: {}'.format(find1))
print('='*40)
