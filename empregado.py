
#para importar um arquivo em py deve-se fazer no arquivo que será importado
# a seguinte linha
# if __name__ == '__main__':
    #main()

class Empregado:
    def __init__(self, idx, name):
        self.idx = idx
        self.name = name


#assalariado herda de empregado
class Assalariado(Empregado):
    def __init__(self, idx, name, salario):
        super().__init__(idx, name) #método construtor da super classe(Empregado)
        self.salario = salario
    
    def calcula_salario(self):
        return self.salario


class Freelancer(Empregado):
    def __init__(self, idx, name, horas_trabalhadas, valor_por_hora):
        super().__init__(idx, name)
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_por_hora = valor_por_hora

    def calcula_salario(self):
        return self.horas_trabalhadas * self.valor_por_hora

class Comissionado(Assalariado):
    def __init__(self, idx, name, salario, comissao):
        super().__init__(idx, name, salario)
        self.comissao = comissao

    def calcula_salario(self):
        #usando um método da classe pai
        return self.comissao + super().calcula_salario()


# usando interface
# CalculadoraDeSalario é uma interface
# Quando uma classe implementa uma interface, se compromete a fornecer o comportamento publicado por esta interface.
class CalculadoraDeSalario:
    def calcula(self, empregados):
        print('calculado salario')
        for e in empregados:
            print(f'O empregado {e.name} ({e.idx}) tem o salário: {e.calcula_salario()}')

#interface
class Regua:
    def __init__(self, tam):
        self.tamanho = tam

    def __gt__(self, outraRegua):
        return self.tamanho > outraRegua.tamanho

regua1 = Regua(15)
regua2 = Regua(25)
print(regua2 > regua1)

A = Assalariado(1, 'Assalariado', 1200)
print(A.calcula_salario())

F = Freelancer(2, 'fREELANCER', 40, 100)
print(F.calcula_salario())

C = Comissionado(3, 'comissionado', 1300, 200)
print(C.calcula_salario())

calculadora = CalculadoraDeSalario()
calculadora.calcula([A, F, C])

