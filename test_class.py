pi = 3.14
class Circulo:
    def __init__(self, raio=0):
        self.raio = raio
    def CalcArea(self):
        result1 = str(pi*(self.raio ** 2))
        return (result1)
    def calcPerimetro(self):
        result = str(2*pi*self.raio)
        return (result)

teste = Circulo(6)


# print(teste.CalcArea())
# print(teste.calcPerimetro())

class Disciplina:
    def __init__(self, nomeD, cargaHTotal, cargaHteorica, cargaHpratica):
        self.nomeD = nomeD
        self.cargaHTotal = cargaHTotal
        self.cargaHteorica = cargaHteorica
        self.cargaHpratica = cargaHpratica
    def imprime(self):
        print(f"{self.nomeD} - {self.cargaHTotal}")
        


class Estudante(Disciplina):
    def __init__(self, nome="default", numMatricula=None, curso="ads", disciplinas=None):
        #sempre que tem herança deve-se inicializar a classe pai
        super().__init__("default","default","default","default")
        self.nome = nome
        self.numMatricula = numMatricula
        self.curso = curso
        self.disciplinas = disciplinas
    def getAluno(self):
        print(f"o nome do aluno é: {self.nome}")
        print(f"numero de matricula {self.numMatricula}") 
        print(f"Curso {self.curso}")
        print(f"numero de matricula {self.disciplinas}")

    def imprimee(self):
        return f"{self.nome} - {self.numMatricula} ({self.curso}) {self.disciplinas.nomeD}"
        

d = Disciplina("matematica", 2, 3, 8)
guizaodozap = Estudante("guilherme", 123123, "ads", d)

print(guizaodozap.imprimee())
