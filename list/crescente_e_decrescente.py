myList = []
count = 0
while count < 5:
    value = int(input("Digite um número: "))
    myList.append(value)
    count = count +1

myList.sort()

print(myList)

print("\n")

myList.sort(reverse=True)

print(myList)