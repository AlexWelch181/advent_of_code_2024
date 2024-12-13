import numpy as np
import re

part2 = True

with open('day_thirteen_in.txt') as file:
    equation = dict()
    ax, ay, bx, by = range(4)
    varidx = 0
    out = 0
    for line in file.readlines():
        if line == '\n':
            continue
        else:
            if varidx < 4:
                a, b = [int(s) for s in re.findall(r'\b\d+\b', line)]
                equation[varidx] = a
                varidx += 1
                equation[varidx] = b
                varidx += 1
            else:
                varidx %= 4
                x, y = [int(s) for s in re.findall(r'\b\d+\b', line)]
                if part2:
                    x += 10000000000000
                    y += 10000000000000
                bnumerator = y*equation[ax]-x*equation[ay]
                bdenom = equation[by]*equation[ax] - equation[bx]*equation[ay]
                if bnumerator % bdenom == 0:
                    b = bnumerator / bdenom
                    anumerator = (x-b*equation[bx])
                    adenom = equation[ax]
                    if  anumerator % adenom == 0:
                        a = anumerator / adenom
                        out += 3*a + b
print(int(out))


            
            
        




