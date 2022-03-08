p1 = float(input("Digite a nota da prova 1: "))
p2 = float(input("Digite a nota da prova 2: "))
p3 = float(input("Digite a nota da prova 3: "))

result = ((p1 * 1) + (p2 * 1) + (p3 * 2)) / (1 + 1 + 2)

if result >= 60:
    print("você passou")
else:
    print("Reprovou")