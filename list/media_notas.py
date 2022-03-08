nota1 = float(input("Digite a nota: "))
nota2 = float(input("Digite a nota: "))
nota3 = float(input("Digite a nota: "))
nota4 = float(input("Digite a nota: "))
nota5 = float(input("Digite a nota: "))
nota6 = float(input("Digite a nota: "))
nota7 = float(input("Digite a nota: "))
nota8 = float(input("Digite a nota: "))
nota9 = float(input("Digite a nota: "))
nota10 = float(input("Digite a nota: "))

mylist = [nota1,nota2,nota3,nota4,nota5,nota6,nota7,nota8,nota9,nota10]
aculm = 0

for x in mylist:
    aculm = aculm + x

resulttt = aculm/10
print(f"A média da sala é: {resulttt}")