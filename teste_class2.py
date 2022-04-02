import math


class Tempo:
    def __init__(self, horas, minutos, segundos):
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos
    def proxSegundo(self):
        return self.segundos + 1
    def ant_segundo(self):
        return self.segundos - 1


T = Tempo(14,21,51)

# print(T.proxSegundo())
# print(T.ant_segundo())

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def calcularDistancia(self, x, y):
        express = (x - self.x)**2 + (y - self.y)**2
        return math.sqrt(express)

    def __str__(self):
        # SOBRESCRITA DE MÉTODOS
        return f"({self.x},{self.y})"

class Reta:
    def __init__(self, ponto_inicialX, ponto_inicialY, ponto_finalX, ponto_finalY):
        self.ponto_inicial = [ponto_inicialX, ponto_inicialY]
        self.ponto_final = [ponto_finalX, ponto_finalY]
    def getAll(self):
        return [self.ponto_inicial, self.ponto_final]

p = Ponto(7,5)
print(p.calcularDistancia(2,2))

R = Reta(p.x, p.y, 2, 3)
print(R.getAll())

