nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

result = (nota1 + nota2 + nota3 + nota4) / 4

if result >= 6:
    print("Você foi aprovado")
else:
    print("Você foi reprovado")