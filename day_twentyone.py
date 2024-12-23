from collections import deque, defaultdict
from itertools import product
from functools import cache

codes = open('day_twentyone_in.txt').read().split('\n')

num_pad = [['7','8','9'],
           ['4','5','6'],
           ['1','2','3'],
           [-1,'0','A']]

dpad = [[-1,'^','A'],
           ['<','v','>']]

def create_dict(grid):
    dic = defaultdict(list)
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] != -1:
                q = deque([(r,c,'',{(r,c)})])
                dic[grid[r][c], grid[r][c]] = ['A']
                while q:
                    rr, cc, moves, seen = q.popleft()
                    for nr, nc, nm in [(rr-1,cc,'^'),(rr,cc+1,'>'),(rr+1,cc,'v'),(rr,cc-1,'<')]:
                        if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]): continue
                        if (nr, nc) in seen: continue
                        if grid[nr][nc] == -1: continue
                        nseen = seen.copy()
                        nseen.add((nr,nc)) 
                        if dic[(grid[r][c],grid[nr][nc])] and len(moves + nm + 'A') > len(list(dic[(grid[r][c],grid[nr][nc])])[0]): continue
                        if dic[(grid[r][c],grid[nr][nc])] and len(moves + nm + 'A') < len(list(dic[(grid[r][c],grid[nr][nc])])[0]):
                            dic[(grid[r][c],grid[nr][nc])] = []
                        dic[(grid[r][c],grid[nr][nc])].append(moves + nm + 'A')
                        if moves and moves[-1] == nm: q.appendleft((nr,nc,moves+nm,nseen))
                        else: q.append((nr,nc,moves+nm,nseen))
    return dic

def solve(r, c, target):
    q = deque([(r,c,'',{(r,c)})])
    possible = []
    shortest = float('inf')
    while q:
        rr, cc, moves, seen = q.popleft()
        if len(moves) > shortest: continue
        for nr, nc, nm in [(rr-1,cc,'^'),(rr,cc+1,'>'),(rr+1,cc,'v'),(rr,cc-1,'<')]:
            if nr < 0 or nc < 0 or nr >= len(num_pad) or nc >= len(num_pad[0]): continue
            if (nr, nc) in seen: continue
            if num_pad[nr][nc] == -1: continue
            if nm in moves and nm != moves[-1]: continue
            if num_pad[nr][nc] == target:
                tr, tc = nr ,nc 
                if len(moves+nm+'A') <= shortest:
                    shortest = len(moves+nm+'A')
                    possible.append(moves+nm+'A')
                    break
            else:
                nseen = seen.copy()
                nseen.add((nr,nc))
                if moves and moves[-1] == nm: q.appendleft((nr,nc,moves+nm,nseen))
                else: q.append((nr,nc,moves+nm,nseen))
    return (tr,tc), possible


dpad_dic = create_dict(dpad)
numpad_dic = create_dict(num_pad)
dpad_lengths = {key: len(val[0]) for key, val in dpad_dic.items()}

@cache
def compute(x, y, depth=2):
    if depth == 1:
        return dpad_lengths[(x,y)]
    optimal = float('inf')
    for seq in dpad_dic[(x,y)]:
        length = 0
        for a, b in zip('A' + seq, seq):
            length += compute(a, b, depth-1)
        optimal = min(optimal, length)
    return optimal

res = 0
for code in codes:
    r, c = 3, 2
    string_choice = []
    for alphanum in code:
        (r,c), p = solve(r, c, alphanum)
        string_choice.append(p)
    combinations = [''.join(combo) for combo in product(*string_choice)]
    options = []
    optimal = float('inf')
    for combo in combinations:
        length = 0
        for x, y in zip('A' + combo, combo):
            length += compute(x, y, 25)
        optimal = min(optimal, length)
    res += optimal * int(''.join(x for x in code if x.isdigit()))
print(res)
        
        