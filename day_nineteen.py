from functools import cache

with open('day_nineteen_in.txt') as file:
    towels, combos = file.read().split('\n\n')
    towels = [towel.strip() for towel in towels.split(',')]
    combos = combos.split('\n')

@cache
def count(tcombo):
    if len(tcombo) == 0: return 1
    return sum(count(tcombo.removeprefix(towel)) for towel in towels if tcombo.startswith(towel))

out = out2 =  0
for combo in combos:
    summ = count(combo)
    out2 += summ
    if summ:
        out += 1
print(out)
print(out2)