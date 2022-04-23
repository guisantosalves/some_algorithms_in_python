class Pai:
    def __init__(self):
        self.nomeFather = 'Marcos'
    def quemSouEuOne(self):
        print(f'sou o pai, meu nome é: Marcos')

class Mae: 
    def __init__(self):
        self.nomeMom = 'Martha'
    def quemSouEuTwo(self):
        print(f'sou a mae, meu nome é: Martha')
        
class Filho(Pai, Mae):
    def __init__(self, nomeSon, idade):
        self.nomeSon = nomeSon
        self.idade = idade
        super().__init__()
    def PrintName(self):
        print(f'meu nome é: {self.nomeSon}')
    

son = Filho('guilherme', 20)

son.PrintName()
son.quemSouEuOne()
son.quemSouEuTwo()
