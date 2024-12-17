import re
from collections import deque

with open('day_seventeen_in.txt') as file:
    registers, instructions = file.read().split('\n\n')
    oa, ob, oc = [int(num) for num in re.findall(r'-*\b\d+\b', registers)]
    instructions = [int(num) for num in re.findall(r'-*\b\d+\b', instructions)]

def combo(num, a, b, c):
    if num < 4:
        return num
    if num == 4:
        return a
    if num == 5:
        return b
    if num == 6:
        return c
    else:
        raise Exception

def adv(operand, a, b, c, ipointer, step):
    a = a >> combo(operand, a, b, c)
    return a, b, c, ipointer, step

def bxl(operand, a, b, c, ipointer, step):
    b = b^operand
    return a, b, c, ipointer, step

def bst(operand, a, b, c, ipointer, step):
    b = combo(operand, a, b, c) % 8
    return a, b, c, ipointer, step


def jnz(operand, a, b, c, ipointer, step):
    if a:
        ipointer = operand
        step = 0
    return a, b, c, ipointer, step

def bxc(operand, a, b, c, ipointer, step):
    b = b^c
    return a, b, c, ipointer, step

def out(operand, a, b, c, ipointer, step):
    res.append(combo(operand, a, b, c)%8)
    return a, b, c, ipointer, step

def bdv(operand, a, b, c, ipointer, step):
    b = a >> combo(operand, a, b, c)
    return a, b, c, ipointer, step

def cdv(operand, a, b, c, ipointer, step):
    c = a >> combo(operand, a, b, c)
    return a, b, c, ipointer, step
        

def run(a, b, c, instructions, ipointer):
    functions = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]
    while ipointer < len(instructions):
        step = 2
        opcode = instructions[ipointer]
        operand = instructions[ipointer+1]
        a,b,c,ipointer,step = functions[opcode](operand, a, b, c, ipointer, step)
        ipointer += step
    return res

res = []
run(oa,ob,oc,instructions,0)
print(','.join([str(num) for num in res]))

res = []
valid = ['000','001','010','011','100','101','110','111']
target = ''.join(str(i) for i in instructions)
q = deque([''])
for digit in range(len(target)-1, -1, -1):
    tmpq = []
    while q:
        num = q.popleft()
        for bidx in range(len(valid)):
            res = []
            tmp = num + valid[bidx]
            run(int(tmp, 2), 0, 0, instructions, 0)
            if ''.join(str(i) for i in res) == target[digit:]:
                tmpq.append(tmp)
    for tmp in tmpq:
        q.append(tmp)


possible = [int(num, 2) for num in q]
print(min(possible))