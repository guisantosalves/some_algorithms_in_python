
mylist = []
mySecondlist = []
count1 = 0
count2 = 0

while count1 < 5:
    value = int(input("Digite um numero: "))
    mylist.append(value)
    count1 = count1 + 1

print("\n")
print("Lista 2")
while count2 < 5:
    value1 = int(input("Digite um numero: "))
    mySecondlist.append(value1)
    count2 = count2 + 1

print(mylist)
print(mySecondlist)

intersection = set.intersection(set(mylist), set(mySecondlist))
intersecitonList = list(intersection)

for x in mySecondlist:
    mylist.append(x)


print(f"Junção das listas: {mylist}")
print(f"A intersecção entre a lista é: {intersecitonList}")