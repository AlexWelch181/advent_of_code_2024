from collections import Counter

secrets = [int(x) for x in open('day_twentytwo_in.txt').readlines()]
seqCount = Counter()


def gen_next(num, epochs, target=None):
    digit = num  % 10
    last = digit
    tmp = []
    tried = set()
    profit = 0
    found = False
    for i in range(epochs):
        num = ((num << 6) ^ num) % 16777216
        num = ((num >> 5) ^ num) % 16777216
        num = ((num << 11) ^ num) % 16777216
        new = num % 10
        tmp.append(new - last)
        last = new
        if len(tmp) == 4:
            if target:
                if not found and tuple(tmp) == target:
                    profit = new
                    found = True
            else:
                if tuple(tmp) not in tried:
                    seqCount[tuple(tmp)] += last
                    tried.add(tuple(tmp))
            tmp.pop(0)
    return num, profit

out = 0
out2 = 0
for secret in secrets:
    n, profit =  gen_next(secret, 2000)
    out += n
    out2 += profit
print(out)
for secret in secrets:
    n, profit =  gen_next(secret, 2000, max(seqCount, key=lambda x: seqCount[x]))
    out += n
    out2 += profit
print(out2)