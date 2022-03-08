from random import randint
from collections import Counter

count = 0 
mylist = []
while count < 100:
    randomm = randint(1, 6)
    mylist.append(randomm)
    count = count + 1

counter = Counter(mylist)

print(counter)