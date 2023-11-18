from random import uniform
from random import randint

texto=[]
"""
def obterTexto():
    for i in range(1,100):
        texto.append(str(uniform(1.50,2.20)) + ";" +
                     str(uniform(50, 120)) + ";" +
                    str(randint(1,10)) + "\n")
"""
def obterTexto():
    for i in range(1,100):
        texto.append(str(round(uniform(1.50,2.20),2)) + ";" +
                     str(round(uniform(50, 120),2)) + ";" +
                    str(randint(1,10)) + "\n")

def gerarArquivo():
    arq ='G:\desenvolvimento\Python\peso.csv'
    entrada=open(arq,'w+',encoding='UTF-8')
    obterTexto()
    entrada.writelines(texto)
    entrada.close()


if __name__ == '__main__':
    gerarArquivo()
