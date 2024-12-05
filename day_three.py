import re

with open('day_three_in.txt') as file:
    data = file.read().replace('\n', '')
    
muls = re.findall(r'mul\(?\d+,?\d+\)', data)
out = 0
for mul in muls:
    num1, num2 = mul.strip(')').replace('mul(','').split(',')
    out += int(num1) * int(num2)

muls = re.findall(r'(?:mul\(?\d+,?\d+\))|do\(\)|don\'t\(\)', data)

out2 = 0
cmds = ('do()','don\'t()')
do = True
for mul in muls:
    if mul in cmds:
        if mul == cmds[0]:
            do = True
        else:
            do = False
    else:
        if do:
            num1, num2 = mul.strip(')').replace('mul(','').split(',')
            out2 += int(num1) * int(num2)

print(out)
print(out2)