from collections import Counter

a = []
b = []

with open('day_one_in.txt') as file:
    for line in file.readlines():
        x, y = line.split()
        a.append(int(x))
        b.append(int(y))

a.sort()
b.sort()
freq = Counter(b)
summ = 0
product = 0
for x,y in zip(a,b):
    summ += abs(x - y)
    product += x * freq[x]
print(summ, product)

