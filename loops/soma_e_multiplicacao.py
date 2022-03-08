start = int(input("Digite o início: "))
last = int(input("Digite o ultimo: "))
rangeee = range(start, last+1)
par = 0
impar = 0

for x in rangeee:
    if x % 2 == 0:
        par = par + x
    else:
        impar = impar + x

print(f"A soma dos pares do range é: {par}")
print(f"A soma dos impares do range é: {impar}")