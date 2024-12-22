from collections import deque
from itertools import product
from functools import cache

codes = open('day_twentyone_in.txt').read().split('\n')

num_pad = [['7','8','9'],
           ['4','5','6'],
           ['1','2','3'],
           [-1,'0','A']]

dir_pad = [[-1,'^','A'],
           ['<','v','>']]


dpad_dic = {}
for r in range(len(dir_pad)):
    for c in range(len(dir_pad[0])):
        if dir_pad[r][c] != -1:
            q = deque([(r,c,'')])
            seen = {(r,c)}
            dpad_dic[dir_pad[r][c], dir_pad[r][c]] = 'A'
            while q:
                rr, cc, moves = q.popleft()
                for nr, nc, nm in [(rr-1,cc,'^'),(rr,cc+1,'>'),(rr+1,cc,'v'),(rr,cc-1,'<')]:
                    if nr < 0 or nc < 0 or nr >= len(dir_pad) or nc >= len(dir_pad[0]): continue
                    if (nr, nc) in seen: continue
                    if dir_pad[nr][nc] == -1: continue
                    seen.add((nr,nc))
                    dpad_dic[(dir_pad[r][c],dir_pad[nr][nc])] = moves + nm + 'A'
                    if moves and moves[-1] == nm: q.appendleft((nr,nc,moves+nm))
                    else: q.append((nr,nc,moves+nm))

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

res = 0
for code in codes:
    r, c = 3, 2
    string_choice = []
    for alphanum in code:
        (r,c), p = solve(r, c, alphanum)
        string_choice.append(p)
    combinations = [''.join(combo) for combo in product(*string_choice)]
    options = []
    for combo in combinations:
        for i in range(2):
            out = ''
            combo = 'A' + combo
            for idx in range(1, len(combo)):
                out += dpad_dic[(combo[idx-1], combo[idx])]
            combo = out
        options.append(len(combo))
    res += min(options) * int(''.join(x for x in code if x.isdigit()))

print(res)
        
        