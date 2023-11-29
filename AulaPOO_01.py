class Meu_Objeto :
    def __init__(self):
        self.nome="Paulo"
        self.idade = 30
        #print("construtor chamado com sucesso")

    def imprime(self):
        print("Meu nome é {} e tenho {} anos.". format(self.nome,self.idade))

Pedro = Meu_Objeto()
Pedro.imprime()
print("="*30)
#============== segundo caso ==========
class Meu_Objeto2 :
    def __init__(self,n,i):
        self.nome= n
        self.idade = i
        #print("construtor chamado com sucesso")

    def imprime(self,x):
        print("Meu nome é {} e tenho {} anos.". format(self.nome,self.idade))
        return x**2

anderson = Meu_Objeto2("Anderson",25)
anderson.imprime(5)

print("="*30)
#============== terceiro caso ==========
class Meu_Objeto3:
    def __init__(self, n, i=10):
        self.nome = n
        self.idade = i
        #print("construtor chamado com sucesso")

    def imprime(self, x, *args):
        print("Meu nome é {} e tenho {} anos.".format(self.nome, self.idade))
        return x**2

lucas = Meu_Objeto3("Lucas")
lucas.imprime(5,1,2,3,4,5)
print("="*30)
#============== Exercicio1 ==========
class Retangulo:
    def __init__(self, l=1, a=1):
        self.largura = l
        self.altura = a
        #print("construtor chamado com sucesso")

    def area(self):
        return self.altura * self.largura
        # print("Área do retângulo: ", self.altura * self.largura)
    def perimetro(self):
        return self.largura * 2 + self.altura *2

    def imprime(self):
        if self.largura == self.altura:
            tipo="Quadrado"
        else:
            tipo="Retangulo"

        print("{}: largura: {} m e altura: {} m .".format(tipo,self.largura, self.altura))
        print("           área: {} m2 ".format(Retangulo.area(self)))
        print("           perímetro: {} m ".format( Retangulo.perimetro(self)))


lg=float(input('informe a largura do retângulo : '))
alt=float(input('informe a altura do retângulo : '))

retangulo = Retangulo(lg,alt)
retangulo.imprime() # imprime valores defalt se não informado
print("area=",retangulo.area(), " m2")
print("="*30)

