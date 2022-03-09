mylist = []
count = 0
newListPar = []
newListImpar = []

while count < 5:
    value = int(input("Digite um numero inteiro: "))
    mylist.append(value)
    count = count + 1

for x in mylist:
    if(x % 2 == 0):
        newListPar.append(x)
    else:
        newListImpar.append(x)

print(f"somente os pares: {newListPar}")
print(f"somente os impares: {newListImpar}")