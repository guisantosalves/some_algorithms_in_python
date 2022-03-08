verify = 0
arrr = []
bigger = 0

while verify < 10:
    enter = int(input("Digite um número: "))
    arrr.append(enter)
    verify = verify + 1


bigger = max(arrr)
lower = min(arrr)

print(f"seu menor numero é: {lower}")
print(f"Seu maior numero é: {bigger}")

