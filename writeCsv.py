import csv

#lendo arquiv
f = open('output.csv', 'r')
csvReader = csv.reader(f)

for row in csvReader:
    print(row)

#writing
juliano = ['lucas', 22, 'mt']
s = open('output.csv','w')
write = s.write(f'{juliano}')