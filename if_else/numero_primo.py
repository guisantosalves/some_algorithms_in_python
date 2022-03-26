num = int(input("Verificar se é primo: "))
multi = 0

for i in range(2, num):
    if num % i == 0:
        print("Multiplo de: ",i)
        multi+=1
    
if multi == 0:
    print("é primo garai")
else: 
    print("Não é primo")