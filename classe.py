#herança -> reutilização de código


class Usuario:
    def __init__(self, username, email):
        self.username = username
        self.email = email
    
    def auth(self):
        print("Acesso autorizado")


# sempre quando faço uma herança preciso chamar o método construtor da minha classe pai
class Pessoa (Usuario):
    #atributos da classe
    genero = "homo"

    #construtor
    def __init__(self, nome, idade, profissao):
        #contrutor super classe
        super().__init__("defaultUsername", "default@default.com")
        self.nome = "default"
        self.idade = -1
        self.profissao = "default"

    def fala(self):
        print(f"meu nome é: {self.nome}")

p = Pessoa('guilherme', 23, 'eestudante')

class runner:
    def __init__(self, pessoa):
        self.pessoa = pessoa
    def run(self):
        self.pessoa.fala()

r = runner(p)

class PessoaJuridiaca(Usuario):
    def __init__(self):
        super().__init__("default", "default")
        self.cnpj = "cnpj"
        self.responsavel = None

empresa = PessoaJuridiaca()

print(p.auth())
print(empresa.responsavel)
print(empresa.username)


print(Pessoa.genero)
print(p.fala())
print(r.run())

#atributo herdado da classe pai
print(p.username)
print(p.email)
print(p.auth())

# print(isinstance(p, Pessoa)) -> serve para verificar a confidencialidade da herança


