import random
import emoji
num = random.random()
print(num)
num = random.randint(1,100)
print('randomico entre 1 e 100 : ',num)
print(emoji.emojize('ola mundo :earth_americas:',use_aliases=True))
print(emoji.emojize('ola mundo :heart:',use_aliases=True))
print(emoji.demojize('nome do simbolo ❤ '))
