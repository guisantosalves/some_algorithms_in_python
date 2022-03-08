from tokenize import String


a = float(input("Digite um número: "))
b = float(input("Digite um número: "))

op = int(input("Qual operação deseja realiza\n1 - somar\n2 - subtrair\n3 - dividir\n4 - multiplicar\n"))

if op == 1:
    result = a + b
elif op == 2:
    result = a - b
elif op == 3: 
    result = a / b
elif op == 4:
    result = a * b
else:
    print('Digite números válidos')

print(f"Seu número é: {result}\n")

if result % 2 == 0:
    print("Seu numero é par")
    if result > 0:
        print("Seu numero é positivo")
        vv = str(result)
        if "." in vv:
            print("Seu número é decimal")
        else:
            print("Seu numero nao é decimal")
    else:
        print("Seu número é menor que zero")
else:
    print("Seu numero é impar")