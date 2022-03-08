count = 2
resultt = 0

num = int(input("Digite um número: "))

while count <= (num/2):
    if num % count == 0:
        resultt = resultt + 1
        break;
    else:
        break
count = count + 1 
    
if resultt == 0:
    print("é um npumero primo ")
else:
    print("Não é um número primo")