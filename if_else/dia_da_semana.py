num = int(input("Digite um número correspondente da semana: "))

if num >= 1 and num <= 7:
    print("\nParabéns tu digitou um numero certo: ")
    if num == 1:
        print("Domingo")
    elif num == 2:
        print("segunda")
    elif num == 3:
        print("terça")
    elif num == 4:
        print("quarta")
    elif num == 5:
        print("quinta")
    elif num == 6:
        print("sexta")
    else:
        print("sabado")
else:
    print("Digite um numero correto")

print("\n")