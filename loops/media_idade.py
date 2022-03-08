verify = True
count = 0
ageCount = 0

while verify:

    idades = int(input("Digite sua idade: "))
    if idades == 0:
        break
    ageCount = ageCount + idades
    count = count + 1
    

resultt = ageCount / count

print(f"A média é: {resultt}")