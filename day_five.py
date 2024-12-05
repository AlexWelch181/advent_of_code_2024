from collections import defaultdict, Counter

lookup = defaultdict(list)

def is_valid(pages):
    seen = set()
    for page in pages:
        if len(seen.intersection(set(lookup[page]))) > 0:
            return False
        seen.add(page)
    return True

def get_middle(pages):
    parents = Counter()
    children = Counter()
    for page in pages:
        for child in lookup[page]:
            if child in pages:
                children[page] += 1
                parents[child] += 1
    for page in pages:
        if parents[page] == children[page]:
            return int(page)

    


with open('day_five_in.txt') as file:
    printing = False
    pagelist = []
    for line in file.readlines():
        line = line.strip('\n')
        if not line:
            printing = True
            continue
        if not printing:
            before, after = line.split('|')
            lookup[before].append(after)
        else:
            pagelist.append(line.split(','))


out = out2 = 0
for pages in pagelist:
    if is_valid(pages):
        out += int(pages[len(pages) // 2])
    else:
        out2 += get_middle(pages)

print(out)
print(out2)