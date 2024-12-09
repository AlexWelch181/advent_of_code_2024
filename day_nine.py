with open('day_nine_in.txt') as file:
    input = file.readline().strip()

inbetween = []
id = 0
for i in range(len(input)):
    if i % 2 == 1:
        for _ in range(int(input[i])):
            inbetween.append('.')
    else:
        for _ in range(int(input[i])):
            inbetween.append(str(id))
        id += 1

back = len(inbetween)-1
front = 0
inbetween = list(inbetween)
while front < back:
    while inbetween[front] != '.':
        front += 1
    while inbetween[back] == '.': 
        inbetween.pop()
        back -= 1
    if front > back:
        break
    inbetween[front] = inbetween[back]
    inbetween[back] = '.'

out = 0
for idx in range(len(inbetween)):
    if inbetween[idx] == '.':
        continue
    out += idx * int(inbetween[idx])

print(out)

from collections import defaultdict

files = defaultdict()
freespace = []
pos = 0
id = 0
for i, char in enumerate(input):
    x = int(char)
    if i % 2 == 0:
        files[id] = (pos, x)
        id += 1
    else:
        if x != 0:
            freespace.append((pos, x))
    pos += x

while id > 0:
    id -= 1
    pos, length = files[id]
    for i, (start, size) in enumerate(freespace):
        if start >= pos:
            freespace = freespace[:i]
            break
        if length <= size:
            files[id] = (start, length)
            if length == size:
                freespace.pop(i)
            else:
                freespace[i] = (start+length, size-length)
            break

out = 0
for id, (pos, size) in files.items():
    for x in range(pos, pos+size):
        out += x * id
print(out)