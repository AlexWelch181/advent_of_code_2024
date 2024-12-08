from collections import defaultdict
import time

with open('day_eight_in.txt') as file:
    data = [list(row.strip('\n')) for row in file.readlines()]

ROWS, COLS = len(data), len(data[0])
dictionary = defaultdict(list)
for r in range(ROWS):
    for c in range(COLS):
        if data[r][c] != '.':
            dictionary[data[r][c]].append([r, c])

# Time for first attempt is approx 2s
special = set()
special2 = set()
start = time.time()
for r in range(ROWS):
    for c in range(COLS):
        for _, vals in dictionary.items():
            for r1, c1 in vals:
                for r2, c2 in vals:
                    if (r1, c1) != (r2, c2):
                        d1 = abs(r-r1)+abs(c-c1)
                        d2 = abs(r-r2)+abs(c-c2)
                        dr1 = r-r1
                        dc1 = c-c1
                        dr2 = r-r2
                        dc2 = c-c2
                        if (d1*2==d2 or d2*2==d1) and (dr1*dc2 == dr2*dc1):
                            special.add((r,c))
                        if (dr1*dc2 == dr2*dc1):
                            special2.add((r,c))
print(len(special))
print(len(special2))
print(time.time() - start)


# Time for improved version approx 0.08
special = set()
special2 = set()
start = time.time()
for _, vals in dictionary.items():
    for r1, c1 in vals:
        for r2, c2 in vals:
            if (r1, c1) != (r2, c2):
                    dx = abs(r1-r2)
                    dy = abs(c1-c2)
                    for mul in range(1, ROWS):
                        for rd in [-1, 1]:
                            for rc in [-1, 1]:
                                r = r1 + dx*rd*mul
                                c = c1 + dy*rc*mul
                                if 0<=r<ROWS and 0<=c<COLS:
                                    d1 = abs(r-r1)+abs(c-c1)
                                    d2 = abs(r-r2)+abs(c-c2)
                                    dr1 = r-r1
                                    dc1 = c-c1
                                    dr2 = r-r2
                                    dc2 = c-c2
                                    if (d1*2==d2 or d2*2==d1) and (dr1*dc2 == dr2*dc1):
                                        special.add((r,c))
                                    if (dr1*dc2 == dr2*dc1):
                                        special2.add((r,c))

print(len(special))
print(len(special2))
print(time.time() - start)
